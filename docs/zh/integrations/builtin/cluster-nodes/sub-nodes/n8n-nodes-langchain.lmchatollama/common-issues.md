---
title: Ollama Chat Model node 常见问题
description: >-
  n8n workflow automation platform 中 Ollama Chat Model node 的常见问题与疑问文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Ollama Chat Model node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues
layout:
  description:
    visible: false
---

# Ollama Chat Model node 常见问题 <a href="#ollama-chat-model-node-common-issues" id="ollama-chat-model-node-common-issues"></a>

这里列出 [Ollama Chat Model node](README.md) 的一些常见错误和问题，以及解决或排查它们的步骤。

## 处理参数 <a href="#processing-parameters" id="processing-parameters"></a>

Ollama Chat Model node 是 sub-node[^1]。使用 expressions 处理多个 items 时，sub-nodes 的行为与其他 nodes 不同。

大多数 nodes，包括 [root nodes](#user-content-fn-2)[^2]，都会接收任意数量的 items 作为 input，处理这些 items，并输出结果。你可以使用 expressions 引用 input items，node 会依次为每个 item 解析 expression。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 会依次解析为每个 name。

在 sub-nodes 中，expression 始终解析为第一个 item。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 始终解析为第一个 name。

## 无法连接到远程 Ollama instance <a href="#cant-connect-to-a-remote-ollama-instance" id="cant-connect-to-a-remote-ollama-instance"></a>

Ollama Chat Model node 支持 Bearer token authentication，用于连接位于 authenticated proxies（例如 Open WebUI）之后的远程 Ollama instances。

对于远程认证连接，请在 Ollama credentials 中同时配置 remote URL 和 API key。

更多信息请参阅 [Ollama credentials 说明](../../../credentials/ollama.md)。

## 使用 Docker 时无法连接到本地 Ollama instance <a href="#cant-connect-to-a-local-ollama-instance-when-using-docker" id="cant-connect-to-a-local-ollama-instance-when-using-docker"></a>

Ollama Chat Model node 会使用 [Ollama credentials](../../../credentials/ollama.md) 中定义的 base URL 连接到本地托管的 Ollama instance。当你在 Docker 中运行 n8n 或 Ollama 时，需要配置网络，使 n8n 能连接到 Ollama。

Ollama 通常监听 `localhost`，也就是本地网络地址。在 Docker 中，默认情况下，每个 container 都有自己的 `localhost`，且只能从 container 内部访问。如果 n8n 或 Ollama 任一方运行在 containers 中，它们将无法通过 `localhost` 连接。

解决方案取决于你如何托管这两个组件。

### 如果只有 Ollama 在 Docker 中 <a href="#if-only-ollama-is-in-docker" id="if-only-ollama-is-in-docker"></a>

如果只有 Ollama 运行在 Docker 中，请配置 Ollama 监听所有 interfaces，即在 container 内绑定到 `0.0.0.0`（official images 已这样配置）。

运行 container 时，使用 `-p` flag [publish ports](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)。默认情况下，Ollama 运行在 11434 端口，因此你的 Docker command 应类似这样：

```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

配置 [Ollama credentials](../../../credentials/ollama.md) 时，`localhost` 地址应可正常工作（将 **base URL** 设为 `http://localhost:11434`）。

### 如果只有 n8n 在 Docker 中 <a href="#if-only-n8n-is-in-docker" id="if-only-n8n-is-in-docker"></a>

如果只有 n8n 运行在 Docker 中，请配置 Ollama 在 host 上绑定到 `0.0.0.0`，监听所有 interfaces。

如果你在 **Linux** 上用 Docker 运行 n8n，启动 container 时使用 `--add-host` flag，将 `host.docker.internal` 映射到 `host-gateway`。例如：

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

如果你使用 Docker Desktop，此配置会自动完成。

配置 [Ollama credentials](../../../credentials/ollama.md) 时，请使用 `host.docker.internal` 作为 host address，而不是 `localhost`。例如，要绑定到默认 11434 端口，可以将 base URL 设为 `http://host.docker.internal:11434`。

### 如果 Ollama 和 n8n 运行在不同 Docker containers 中 <a href="#if-ollama-and-n8n-are-running-in-separate-docker-containers" id="if-ollama-and-n8n-are-running-in-separate-docker-containers"></a>

如果 n8n 和 Ollama 都运行在 Docker 中但位于不同 containers，可以使用 Docker networking 连接它们。

配置 Ollama 监听所有 interfaces，即在 container 内绑定到 `0.0.0.0`（official images 已这样配置）。

配置 [Ollama credentials](../../../credentials/ollama.md) 时，请使用 Ollama container 的 name 作为 host address，而不是 `localhost`。例如，如果你将 Ollama container 命名为 `my-ollama`，且它监听默认 11434 端口，则可以将 base URL 设为 `http://my-ollama:11434`。

### 如果 Ollama 和 n8n 运行在同一个 Docker container 中 <a href="#if-ollama-and-n8n-are-running-in-the-same-docker-container" id="if-ollama-and-n8n-are-running-in-the-same-docker-container"></a>

如果 Ollama 和 n8n 运行在同一个 Docker container 中，`localhost` 地址不需要任何特殊配置。你可以配置 Ollama 监听 localhost，并在 [n8n 的 Ollama credentials](../../../credentials/ollama.md) 中配置 base URL 使用 localhost：`http://localhost:11434`。

## Error: connect ECONNREFUSED ::1:11434 <a href="#error-connect-econnrefused-111434" id="error-connect-econnrefused-111434"></a>

当你的计算机启用了 IPv6，但 Ollama 监听的是 IPv4 地址时，会出现此错误。

要修复此问题，请将 [Ollama credentials](../../../credentials/ollama.md) 中的 base URL 改为连接 `127.0.0.1`，这是 IPv4-specific local address，而不是可解析为 IPv4 或 IPv6 的 `localhost` alias：`http://127.0.0.1:11434`。

## Ollama 和 HTTP/HTTPS proxies <a href="#ollama-and-httphttps-proxies" id="ollama-and-httphttps-proxies"></a>

Ollama 的配置不支持 custom HTTP agents。这会让在 custom HTTP/HTTPS proxies 之后使用 Ollama 变得困难。取决于你的 proxy configuration，即使设置了 `HTTP_PROXY` 或 `HTTPS_PROXY` environment variables，也可能完全无法工作。

更多信息请参阅 [Ollama FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-do-i-use-ollama-behind-a-proxy)。

[^1]: n8n cluster nodes 由一个或多个连接到 root node 的 sub nodes 组成。Sub nodes 扩展 root node 的功能，提供对特定 services 或 resources 的访问，或提供特定类型的专用处理，例如 calculator functionality。
[^2]: 每个 n8n cluster node 都包含一个定义 cluster 主要功能的 root node。一个或多个 sub nodes 会附加到 root node，以扩展其功能。
