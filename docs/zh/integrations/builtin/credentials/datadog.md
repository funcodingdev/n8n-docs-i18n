---
title: Datadog credentials
description: >-
  Datadog credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Datadog。
contentType:
  - integration
  - reference
nodeTitle: Datadog credentials
originalFilePath: integrations/builtin/credentials/datadog.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/datadog'
url: 'https://docs.n8n.io/integrations/builtin/credentials/datadog'
layout:
  description:
    visible: false
---
# Datadog credentials <a href="#datadog-credentials" id="datadog-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Datadog](https://app.datadoghq.eu/signup) 账号。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务进行身份验证的更多信息，请参阅 [Datadog 的 API 文档](https://docs.datadoghq.com/api/latest/)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/datadog/)。

## 使用 API Key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 你的 Datadog instance **Host**
- 一个 **API Key**
- 一个 **App Key**

有关更多信息，请参阅 Datadog 网站上的 [Authentication](https://docs.datadoghq.com/api/latest/authentication/)。
