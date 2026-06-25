---
title: Facebook Graph API node documentation
description: >-
  了解如何在 n8n 中使用 Facebook Graph API node。按照技术文档将 Facebook Graph API
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Facebook Graph API node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi
layout:
  description:
    visible: false
---

# Facebook Graph API node <a href="#facebook-graph-api-node" id="facebook-graph-api-node"></a>

使用 Facebook Graph API node 自动化 Facebook Graph API 中的工作，并将 Facebook Graph API 与其他应用集成。n8n 内置支持大量 Facebook Graph API 功能，包括对 host URL、request method 等多个参数使用 GET、POST、DELETE query。

在本页中，你可以找到 Facebook Graph API node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Facebook Graph API credentials](../credentials/facebookgraph.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Default**
    * GET
    * POST
    * DELETE
* **Video Uploads**
    * GET
    * POST
    * DELETE

### 参数 <a href="#parameters" id="parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

* **Host URL**：请求的 host URL。可用选项如下：
    * **Default**：请求会发送到 `graph.facebook.com` host URL。用于大多数请求。
    * **Video**：请求会发送到 `graph-video.facebook.com` host URL。仅用于 video upload 请求。
* **HTTP Request Method**：此请求要使用的方法，可从以下选项中选择：
    * **GET**
    * **POST**
    * **DELETE**
* **Graph API Version**：此请求要使用的 [Facebook Graph API](https://developers.facebook.com/docs/graph-api/changelog) 版本。
* **Node**：要操作的 node，例如 `/<page-id>/feed`。请在 [Facebook Developer 官方文档](https://developers.facebook.com/docs/graph-api/using-graph-api)中阅读更多信息。
* **Edge**：要操作的 node 的 edge。Edge 表示附加到 node 的对象集合。
* **Ignore SSL Issues**：开启后，即使无法验证 SSL certificate，也仍会下载响应。
* **Send Binary File**：适用于 `POST` 操作。启用后，binary data 会作为正文发送。需要设置以下内容：
    * **Input Binary Field**：包含待上传文件数据的 binary property 名称。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Facebook Graph API node 文档集成模板](https://n8n.io/integrations/facebook-graph-api)或[搜索所有模板](https://n8n.io/workflows/)
