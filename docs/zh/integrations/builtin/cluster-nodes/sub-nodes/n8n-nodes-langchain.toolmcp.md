---
title: MCP Client Tool node 文档
description: >-
  了解如何在 n8n 中使用 MCP Client Tool node。按照技术文档将 MCP Client Tool node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: MCP Client Tool node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp
layout:
  description:
    visible: false
---

# MCP Client Tool node <a href="#mcp-client-tool-node" id="mcp-client-tool-node"></a>

MCP Client Tool node 是 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) client，允许你使用 external MCP server 暴露的 tools。你可以将 MCP Client Tool node 连接到 models，以便通过 n8n agents 调用 external tools。

{% hint style="info" %}
**Credentials**

MCP Client Tool node 支持 [Bearer](../../credentials/httprequest.md#using-bearer-auth)、通用 [header](../../credentials/httprequest.md#using-header-auth)、multiple headers 和 [OAuth2](../../credentials/httprequest.md#using-oauth2) authentication methods。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置此 node。

* **SSE Endpoint**：要连接的 MCP server 的 SSE endpoint。
* **Authentication**：向 MCP server 认证时使用的 authentication method。MCP tool 支持 [bearer](../../credentials/httprequest.md#using-bearer-auth)、通用 [header](../../credentials/httprequest.md#using-header-auth)、multiple headers 和 [OAuth2](../../credentials/httprequest.md#using-oauth2) authentication。选择 **None** 表示尝试不使用 authentication 连接。
	* **Multiple Headers Auth**：当你的 MCP server 需要多个 header 时使用，例如 API key 和 username。在 credential 中将每个 header 添加为 **Name** 和 **Value** pair。你可以添加所需数量的 headers。
* **Tools to Include**：选择要暴露给 AI Agent 的 tools：
	* **All**：暴露 MCP server 提供的所有 tools。
	* **Selected**：激活 **Tools to Include** 参数，你可以在其中选择要暴露给 AI Agent 的 tools。
	* **All Except**：激活 **Tools to Exclude** 参数，你可以在其中选择要避免分享给 AI Agent 的 tools。AI Agent 将可以访问所有未被选中的 MCP server tools。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MCP Client Tool node 文档集成模板](https://n8n.io/integrations/mcp-client-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 还提供 [MCP Server Trigger](../../core-nodes/n8n-nodes-langchain.mcptrigger.md) node，允许你向 external AI Agents 暴露 n8n tools。

有关 protocol、servers 和 clients 的更多 details，请参阅 [MCP documentation](https://modelcontextprotocol.io/introduction) 和 [MCP specification](https://modelcontextprotocol.io/specification/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}
