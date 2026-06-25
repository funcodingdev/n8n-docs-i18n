---
title: Carbon Black credentials
description: >-
  Carbon Black credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Carbon Black。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Carbon Black credentials
originalFilePath: integrations/builtin/credentials/carbonblack.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/carbonblack'
url: 'https://docs.n8n.io/integrations/builtin/credentials/carbonblack'
layout:
  description:
    visible: false
---

# Carbon Black credentials <a href="#carbon-black-credentials" id="carbon-black-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Carbon Black subscription](https://www.broadcom.com/products/carbon-black/threat-prevention/carbon-black-cloud)。
- 创建一个 [Carbon Black developer account](https://developer.carbonblack.com/)。

## 身份验证方法 <a href="#authentication-methods" id="authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Carbon Black 的文档](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/carbon-black/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **URL**：此 URL 由你使用的 environment/product URL 决定。你可以通过查看 Carbon Black Cloud console 的网址找到它。有关更多信息，请参阅 [Carbon Black URL Parts 文档](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#the-url-parts)。
- 一个 **Access Token**：请参阅 [Carbon Black Create an API key 文档](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#carbon-black-cloud-manages-identities-and-roles) 创建 API key。在 n8n 中将 **API Secret Key** 添加为 **Access Token**。
