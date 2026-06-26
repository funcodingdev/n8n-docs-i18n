---
title: QRadar credentials
description: >-
  QRadar credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  QRadar 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: QRadar credentials
originalFilePath: integrations/builtin/credentials/qradar.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/qradar'
url: 'https://docs.n8n.io/integrations/builtin/credentials/qradar'
layout:
  description:
    visible: false
---

# QRadar credentials <a href="#qradar-credentials" id="qradar-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Qradar](https://www.ibm.com/qradar) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [QRadar's documentation](https://ibmsecuritydocs.github.io/qradar_api_overview/)。

这是一个 credential-only node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/qradar/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：也称为 authorized service token。请使用 **Admin** tab 上的 **Manage Authorized Services** window 创建 authentication token。更多信息请参考 [Creating an authentication token](https://www.ibm.com/docs/en/qradar-common?topic=forwarding-creating-authentication-token)。
