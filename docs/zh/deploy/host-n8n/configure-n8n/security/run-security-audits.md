---
title: 安全审计
description: 在你的 n8n 实例上运行 security audit。
contentType: howto
nodeTitle: Run security audits
originalFilePath: hosting/securing/security-audit.md
originalUrl: 'https://docs.n8n.io/hosting/securing/security-audit'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits'
layout:
  description:
    visible: false
---

# 安全审计 <a href="#security-audit" id="security-audit"></a>

你可以在 n8n 实例上运行 security audit，以检测常见安全问题。

## 运行 audit <a href="#run-an-audit" id="run-an-audit"></a>

你可以使用 CLI、public API 或 n8n node 运行 audit。

### CLI <a href="#cli" id="cli"></a>

运行 `n8n audit`。

### API <a href="#api" id="api"></a>

向 `/audit` endpoint 发起 `POST` 调用。你必须以 instance owner 身份认证。

### n8n node <a href="#n8n-node" id="n8n-node"></a>

将 [n8n node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.n8n) 添加到你的 workflow。选择 **Resource** > **Audit** 和 **Operation** > **Generate**。

## Report 内容 <a href="#report-contents" id="report-contents"></a>

audit 会生成五个 risk reports：

### Credentials <a href="#credentials" id="credentials"></a>

此 report 显示：

* 未在 workflow 中使用的 credentials。
* 未在 active workflow 中使用的 credentials。
* 未在最近 active workflow 中使用的 credentials。

### Database <a href="#database" id="database"></a>

此 report 显示：

* SQL nodes 的 **Execute Query** fields 中使用的 expressions。
* SQL nodes 的 **Query Parameters** fields 中使用的 expressions。
* SQL nodes 中未使用的 **Query Parameters** fields。

### File system <a href="#file-system" id="file-system"></a>

此 report 列出与 file system 交互的 nodes。

### Nodes <a href="#nodes" id="nodes"></a>

此 report 显示：

* 官方 risky nodes。这些是 n8n built in nodes。你可以用它们在 host system 上获取并运行任意代码，这会让实例暴露于 exploits。你可以在 [n8n code | Audit constants](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/security-audit/constants.ts#L51) 中的 `OFFICIAL_RISKY_NODE_TYPES` 下查看列表。
* Community nodes。
* Custom nodes。

### Instance <a href="#instance" id="instance"></a>

此 report 显示：

* 实例中未受保护的 webhooks。
* 缺少的 security settings。
* 你的实例是否过时。
