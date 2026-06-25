---
title: GraphQL
description: >-
  n8n 中 GraphQL node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: GraphQL
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.graphql.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.graphql'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.graphql'
layout:
  description:
    visible: false
---

# GraphQL <a href="#graphql" id="graphql"></a>

[GraphQL](https://graphql.org/) 是一种用于 API 的开源数据查询和操作语言，也是使用现有数据完成查询的 runtime。使用 GraphQL node 可以查询 GraphQL endpoint。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

### Authentication <a href="#authentication" id="authentication"></a>

选择要使用的身份验证类型。

如果选择 **None** 以外的任何选项，会出现 **Credential for <selected-auth-type>** 参数，你可以选择已有的身份验证 credential，或为该身份验证类型创建新的 credential。

### HTTP Request Method <a href="#http-request-method" id="http-request-method"></a>

选择该 node 应使用的底层 HTTP Request 方法。可选：

* **GET**
* **POST**：如果选择此方法，还需要选择该 node 应用于 query payload 的 **Request Format**。可选：
    * **GraphQL (Raw)**
    * **JSON**

### Endpoint <a href="#endpoint" id="endpoint"></a>

输入你想访问的 GraphQL Endpoint。

### Ignore SSL Issues <a href="#ignore-ssl-issues" id="ignore-ssl-issues"></a>

开启此控制项后，n8n 会忽略 SSL certificate validation failure。

### Query <a href="#query" id="query"></a>

输入要执行的 GraphQL query。

有关编写 query 的信息，请参阅[相关资源](#related-resources)。

### Response Format <a href="#response-format" id="response-format"></a>

选择希望接收 query 结果的格式。可选：

* **JSON**
* **String**：如果选择此格式，请输入 **Response Data Property Name**，用于定义写入该字符串的属性。

## Headers <a href="#headers" id="headers"></a>

以 **Name** / **Value** 对的形式输入要作为 query 一部分传递的任何 **Headers**。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 GraphQL 集成模板](https://n8n.io/integrations/graphql)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要使用 GraphQL node，你需要了解 GraphQL query language。GraphQL 有自己的 [Introduction to GraphQL](https://graphql.org/learn/) 教程。
