"""Run with: python3 -m unittest discover -s _doctools -p 'test_*.py'"""

from contextlib import redirect_stderr, redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import os
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from _doctools import translate as translator


SOURCE = "---\ntitle: Example\n---\n# Hello\n\n```sh\necho hello\n```\n"
TRANSLATED = SOURCE.replace("# Hello", "# 你好")


def completion(content=TRANSLATED, finish_reason="stop"):
	return {"choices": [{"message": {"content": content}, "finish_reason": finish_reason}]}


class TranslateTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		class Handler(BaseHTTPRequestHandler):
			def do_POST(self):
				length = int(self.headers["Content-Length"])
				self.server.requests.append((self.path, dict(self.headers), json.loads(self.rfile.read(length))))
				status, data = self.server.responses.pop(0)
				self.send_response(status)
				self.send_header("Content-Type", "application/json")
				self.end_headers()
				self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

			def log_message(self, *args):
				pass

		cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
		cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
		cls.thread.start()
		cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

	@classmethod
	def tearDownClass(cls):
		cls.server.shutdown()
		cls.server.server_close()
		cls.thread.join()

	def setUp(self):
		self.directory = tempfile.TemporaryDirectory()
		self.addCleanup(self.directory.cleanup)
		self.root = Path(self.directory.name).resolve()
		self.docs = self.root / "docs"
		self.source = self.docs / "get-started" / "example.md"
		self.source.parent.mkdir(parents=True)
		self.source.write_text(SOURCE, encoding="utf-8")
		self.target = self.docs / "zh" / "get-started" / "example.md"
		self.server.requests = []
		self.server.responses = [(200, completion())]
		self.environment = patch.dict(os.environ, {}, clear=True)
		self.environment.start()
		self.addCleanup(self.environment.stop)
		self.root_patch = patch.object(translator, "ROOT", self.root)
		self.root_patch.start()
		self.addCleanup(self.root_patch.stop)

	def run_cli(self, *options, source=None):
		output = io.StringIO()
		with redirect_stdout(output), redirect_stderr(output):
			status = translator.main([
				str(source or self.source), "--base-url", self.base_url + "/openai",
				"--model", "anthropic/configured-model", *options,
			])
		return status, output.getvalue()

	def test_gateway_request_and_mirrored_output(self):
		os.environ["OPENAI_API_KEY"] = "test-bearer"
		status, _ = self.run_cli()
		self.assertEqual(status, 0)
		path, headers, body = self.server.requests[0]
		self.assertEqual(path, "/openai/chat/completions")
		self.assertEqual(headers["Authorization"], "Bearer test-bearer")
		self.assertNotIn("X-Bf-Vk", headers)
		self.assertEqual(body["model"], "anthropic/configured-model")
		self.assertEqual(body["messages"][1]["content"], SOURCE)
		self.assertFalse(body["stream"])
		self.assertEqual(self.target.read_text(), TRANSLATED)
		self.assertEqual(self.source.read_text(), SOURCE)

	def test_existing_translation_skipped_unless_overwrite(self):
		self.target.parent.mkdir(parents=True)
		self.target.write_text("existing translation\n")
		self.assertEqual(self.run_cli()[0], 0)
		self.assertEqual(self.server.requests, [])
		self.assertEqual(self.target.read_text(), "existing translation\n")
		self.assertEqual(self.run_cli("--overwrite")[0], 0)
		self.assertEqual(self.target.read_text(), TRANSLATED)

	def test_dry_run_limit_and_chinese_exclusion(self):
		self.source.with_name("second.md").write_text(SOURCE)
		self.target.parent.mkdir(parents=True)
		self.target.with_name("unrelated.md").write_text("中文")
		status, output = self.run_cli("--dry-run", "--limit", "1", source=self.docs)
		self.assertEqual(status, 0)
		self.assertEqual(output.count(" -> "), 1)
		self.assertFalse(self.target.exists())
		self.assertEqual(self.server.requests, [])

	def test_environment_configuration_and_no_auth(self):
		os.environ.update(OPENAI_BASE_URL=self.base_url + "/v1", OPENAI_MODEL="local/model")
		with redirect_stdout(io.StringIO()):
			self.assertEqual(translator.main([str(self.source)]), 0)
		path, headers, body = self.server.requests[0]
		self.assertEqual(path, "/v1/chat/completions")
		self.assertEqual(body["model"], "local/model")
		self.assertNotIn("Authorization", headers)
		self.assertNotIn("X-Bf-Vk", headers)

	def test_truncated_empty_or_changed_code_not_saved(self):
		for response in (
			completion(finish_reason="length"), completion(content=""),
			completion(content=TRANSLATED.replace("echo hello", "echo 你好")),
			completion(content=TRANSLATED.replace("title: Example", "title: 示例")),
			{"error": "bad response"},
		):
			with self.subTest(response=response):
				self.server.responses = [(200, response)]
				self.assertEqual(self.run_cli()[0], 1)
				self.assertFalse(self.target.exists())

	def test_failed_overwrite_preserves_existing_translation(self):
		self.target.parent.mkdir(parents=True)
		self.target.write_text("reviewed translation\n")
		self.server.responses = [(200, completion(finish_reason="length"))]
		self.assertEqual(self.run_cli("--overwrite")[0], 1)
		self.assertEqual(self.target.read_text(), "reviewed translation\n")

	def test_rate_limit_retry(self):
		self.server.responses = [(429, {"error": "limited"}), (200, completion())]
		with patch.object(translator.time, "sleep"):
			self.assertEqual(self.run_cli()[0], 0)
		self.assertEqual(len(self.server.requests), 2)

	def test_auth_failure_no_retry_or_error_body_leak_and_batch_continues(self):
		second = self.source.with_name("second.md")
		second.write_text(SOURCE)
		self.server.responses = [(401, {"error": "private-key-canary"}), (200, completion())]
		status, output = self.run_cli(source=self.source.parent)
		self.assertEqual(status, 1)
		self.assertIn("HTTP 401", output)
		self.assertNotIn("private-key-canary", output)
		self.assertEqual(len(self.server.requests), 2)
		self.assertFalse(self.target.exists())
		self.assertTrue(self.target.with_name("second.md").exists())

	def test_invalid_source_and_output_symlink_rejected(self):
		outside = self.root / "outside.md"
		outside.write_text(SOURCE)
		self.target.parent.mkdir(parents=True)
		self.target.symlink_to(self.source)
		for path in (outside, self.target, self.source):
			with self.subTest(path=path), self.assertRaises(SystemExit) as error:
				self.run_cli(source=path)
			self.assertEqual(error.exception.code, 2)
		self.assertEqual(self.server.requests, [])
		self.assertEqual(self.source.read_text(), SOURCE)

	def test_base_url_keeps_prefix(self):
		for prefix in ("/openai", "/openai/v1/", "/v1", "/custom/api/v1"):
			self.assertEqual(translator.completion_url(self.base_url + prefix),
				self.base_url + prefix.rstrip("/") + "/chat/completions")
		for url in ("", "file:///tmp/api", "https://key@example.com/v1", "https://example.com/v1?key=secret"):
			with self.subTest(url=url), self.assertRaises(ValueError):
				translator.completion_url(url)


if __name__ == "__main__":
	unittest.main()
