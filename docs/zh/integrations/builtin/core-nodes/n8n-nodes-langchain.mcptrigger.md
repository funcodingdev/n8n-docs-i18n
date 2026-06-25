---
title: MCP Server Trigger node documentation
description: >-
  了解如何在 n8n 中使用 MCP Server Trigger node。按照技术文档将 MCP Server Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: MCP Server Trigger node documentation
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
layout:
  description:
    visible: false
---

# MCP Server Trigger node <a href="#mcp-server-trigger-node" id="mcp-server-trigger-node"></a>

使用 MCP Server Trigger node 让 n8n 充当 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server，从而让 MCP client 可以使用 n8n tool 和 workflow。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/httprequest.md)找到此 node 的身份验证信息。
{% endhint %}

## MCP Server Trigger node 如何工作 <a href="#how-the-mcp-server-trigger-node-works" id="how-the-mcp-server-trigger-node-works"></a>

MCP Server Trigger node 充当 MCP client 进入 n8n 的入口点。它通过暴露一个 URL 来工作，MCP client 可以与该 URL 交互，以访问 n8n tool。

与传统 [trigger node](#user-content-fn-1)[^1] 不同，传统 trigger node 响应事件并将输出传递给下一个[连接的 node](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/workflow-components/connect-nodes-together)，而 MCP Server Trigger node 只连接并执行 [tool](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/understand-ai-components/how-tools-work) node。Client 可以列出可用 tool，并调用单个 tool 来执行工作。

你可以通过附加 [Custom n8n Workflow Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) node，将 n8n workflow 暴露给 client。

{% hint style="info" %}
**支持 Server-Sent Events（SSE）和 streamable HTTP**

MCP Server Trigger node 同时支持 [Server-Sent Events (SSE)](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) 以及 [streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)，前者是构建在 HTTP 之上的长连接 transport，用于 client 与 server 之间的连接。它当前不支持 [standard input/output (stdio)](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio) transport。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用这些参数配置 node。

### MCP URL <a href="#mcp-url" id="mcp-url"></a>

MCP Server Trigger node 有两个 **MCP URLs**：test 和 production。n8n 会在 node 面板顶部显示这些 URL。

选择 **Test URL** 或 **Production URL** 来切换 n8n 显示的 URL。

* **Test**：当你选择 **Listen for Test Event** 或 **Execute workflow** 且 workflow 未激活时，n8n 会注册 test MCP URL。调用 MCP URL 时，n8n 会在 workflow 中显示数据。
* **Production**：发布 workflow 时，n8n 会注册 production MCP URL。使用 production URL 时，n8n 不会在 workflow 中显示数据。你仍然可以查看 production execution 的 workflow 数据：选择 workflow 中的 **Executions** 标签页，然后选择要查看的 workflow execution。

### Authentication <a href="#authentication" id="authentication"></a>

你可以要求连接 MCP URL 的 client 进行身份验证。可从这些身份验证方法中选择：

- Bearer auth
- Header auth

有关设置每种 credential type 的更多信息，请参阅 [HTTP request credentials](../credentials/httprequest.md)。

### Path <a href="#path" id="path"></a>

默认情况下，此字段包含随机生成的 MCP URL path，以避免与其他 MCP Server Trigger node 冲突。

你可以手动指定 URL path，包括添加 route parameter。例如，如果你使用 n8n 原型化 API，并希望 endpoint URL 保持一致，可能需要这样做。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MCP Server Trigger node 文档集成模板](https://n8n.io/integrations/mcp-server-trigger)或[搜索所有模板](https://n8n.io/workflows/)

### 与 Claude Desktop 集成 <a href="#integrating-with-claude-desktop" id="integrating-with-claude-desktop"></a>

你可以通过运行 gateway 将 SSE 消息代理到基于 stdio 的 server，从 [Claude Desktop](https://claude.ai/download) 连接到 MCP Server Trigger node。

为此，请将以下内容添加到 Claude Desktop 配置中：

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "<MCP_URL>",
        "--header",
        "Authorization: Bearer ${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "<MCP_BEARER_TOKEN>"
      }
    }
  }
}
```

请务必将 `<MCP_URL>` 和 `<MCP_BEARER_TOKEN>` placeholder 替换为你的 MCP Server Trigger node 参数和 credential 中的值。

## 限制 <a href="#limitations" id="limitations"></a>

### 使用 webhook replica 配置 MCP Server Trigger node <a href="#configuring-the-mcp-server-trigger-node-with-webhook-replicas" id="configuring-the-mcp-server-trigger-node-with-webhook-replicas"></a>

MCP Server Trigger node 依赖 Server-Sent Events（SSE）或 streamable HTTP，它们要求同一个 server instance 处理持久连接。在 [queue mode](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/enable-queue-mode) 下运行 n8n 时，取决于你的 [webhook processor](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/enable-queue-mode#webhook-processors) 配置，这可能导致问题：

* 如果你使用 queue mode 且只有 **single webhook replica**，MCP Server Trigger node 会按预期工作。
* 如果运行 **multiple webhook replicas**，你需要将所有 `/mcp*` 请求路由到单个专用 webhook replica。为 MCP 请求创建一个单独的 replica set，其中包含一个 webhook container。然后更新 ingress 或 load balancer 配置，将所有 `/mcp*` 流量定向到该 instance。

{% hint style="warning" %}
**使用多个 webhook replica 运行时请谨慎**

如果运行 MCP Server Trigger node 时使用多个 webhook replica，却没有将所有 `/mcp*` 请求路由到单个专用 webhook replica，你的 SSE 和 streamable HTTP 连接会频繁中断，或无法可靠地传递事件。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 还提供 [MCP Client Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) node，可将 n8n AI agent 连接到外部 tool。

有关 protocol、server 和 client 的更多详细信息，请参阅 [MCP documentation](https://modelcontextprotocol.io/introduction) 和 [MCP specification](https://modelcontextprotocol.io/specification/)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 MCP Server Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### 在 reverse proxy 后运行 MCP Server Trigger node <a href="#running-the-mcp-server-trigger-node-with-a-reverse-proxy" id="running-the-mcp-server-trigger-node-with-a-reverse-proxy"></a>

在 nginx 等 reverse proxy 后运行 n8n 时，如果 MCP endpoint 未配置为适配 SSE 或 streamable HTTP，可能会遇到问题。

具体来说，你需要为该 endpoint 禁用 proxy buffering。可能还需要调整的其他项目包括禁用 gzip compression（n8n 会自行处理）、禁用 chunked transfer encoding，并将 `Connection` 设置为空字符串，以便从转发的 header 中移除它。在 MCP endpoint 中显式禁用这些项，可确保它们不会从 nginx 配置中的其他位置继承。

用于提供 MCP 流量并启用这些设置的 nginx location block 示例可能如下：

```
location /mcp/ {
    proxy_http_version          1.1;
    proxy_buffering             off;
    gzip                        off;
    chunked_transfer_encoding   off;

    proxy_set_header            Connection '';

    # The rest of your proxy headers and settings
    # . . .
}
```

[^1]: Trigger node 是一种特殊 node，负责响应特定条件执行 workflow。所有 production workflow 都至少需要一个 trigger 来决定 workflow 何时运行。
