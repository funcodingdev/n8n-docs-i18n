---
title: MCP Client node documentation
description: >-
  了解如何在 n8n 中使用 MCP Client node。按照技术文档将 MCP Client node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: MCP Client node documentation
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient
layout:
  description:
    visible: false
---

# MCP Client node <a href="#mcp-client-node" id="mcp-client-node"></a>

MCP Client node 是一个 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) client，允许你使用外部 MCP server 暴露的 tool。

你可以使用 MCP Client node 将 MCP tool 作为 workflow 中的常规 step 使用。

如果想将 MCP tool 作为 AI Agent 的 tool 使用，请改用 [MCP Client Tool node](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)。

{% hint style="info" %}
**Credentials**

MCP Client node 支持 [Bearer](../credentials/httprequest.md#using-bearer-auth)、通用 [header](../credentials/httprequest.md#using-header-auth)、multiple headers 和 [OAuth2](../credentials/httprequest.md#using-oauth2) 身份验证方式。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置此 node。

* **Server Transport**：要连接的 MCP Server endpoint 使用的 transport protocol。
* **MCP Endpoint URL**：外部 MCP Server 的 URL。例如 `https://mcp.notion.com/mcp`。
* **Authentication**：连接 MCP server 时使用的身份验证方法。MCP Client node 支持 [bearer](../credentials/httprequest.md#using-bearer-auth)、通用 [header](../credentials/httprequest.md#using-header-auth)、multiple headers 和 [OAuth2](../credentials/httprequest.md#using-oauth2) authentication。选择 **None** 可尝试不使用身份验证进行连接。
	* **Multiple Headers Auth**：当 MCP server 需要多个 header 时使用，例如 API key 和用户名。在 credential 中将每个 header 添加为 **Name** 和 **Value** 对。你可以按需添加任意数量的 header。
* **Tool**：选择此 node 要使用的 tool。tool 列表会自动从外部 MCP server 获取。
* **Input Mode**：
	* **Manual**：手动指定每个 tool 参数。
	* **JSON**：将 tool 参数指定为 JSON 对象。对于具有嵌套参数的 tool，请使用此 mode。

## 选项 <a href="#options" id="options"></a>

* **Convert to Binary**：是否将图片和音频转换为二进制数据。如果为 false，图片和音频会以 base64 编码字符串返回。
* **Timeout**：等待 tool call 完成的时间，单位为毫秒。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MCP Client node 文档集成模板](https://n8n.io/integrations/mcp-client)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要将 MCP tool 与 AI Agent 一起使用，n8n 提供了 [MCP Client Tool node](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)。

n8n 还提供了 [MCP Server Trigger](n8n-nodes-langchain.mcptrigger.md) node，允许你向外部 AI Agent 暴露 n8n tool。

有关 protocol、server 和 client 的更多详细信息，请参阅 [MCP documentation](https://modelcontextprotocol.io/introduction) 和 [MCP specification](https://modelcontextprotocol.io/specification/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}
