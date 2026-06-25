---
title: DFIR-IRIS credentials
description: >-
  DFIR-IRIS credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 DFIR-IRIS。
contentType:
  - integration
  - reference
nodeTitle: DFIR-IRIS credentials
originalFilePath: integrations/builtin/credentials/dfiriris.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/dfiriris'
url: 'https://docs.n8n.io/integrations/builtin/credentials/dfiriris'
layout:
  description:
    visible: false
---
# DFIR-IRIS credentials <a href="#dfir-iris-credentials" id="dfir-iris-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

一个可访问的 [DFIR-IRIS](https://docs.dfir-iris.org/latest/getting_started/) instance。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务进行身份验证的更多信息，请参阅 [DFIR-IRIS 的 API 文档](https://docs.dfir-iris.org/operations/api/)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/iris-dfir/)。

## 使用 API Key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关获取 API key 的说明，请参阅 [DFIR-IRIS 的 API 文档](https://docs.dfir-iris.org/operations/api/)。
- 你的 DFIR-IRIS instance 的 **Base URL**。
