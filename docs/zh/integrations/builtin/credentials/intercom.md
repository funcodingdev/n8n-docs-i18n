---
title: Intercom credentials
description: >-
  Intercom credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Intercom 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Intercom credentials
originalFilePath: integrations/builtin/credentials/intercom.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/intercom'
url: 'https://docs.n8n.io/integrations/builtin/credentials/intercom'
layout:
  description:
    visible: false
---

# Intercom credentials <a href="#intercom-credentials" id="intercom-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Intercom](../app-nodes/n8n-nodes-base.intercom.md)


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Intercom](https://www.intercom.com/) developer account。
- 在你的 developer hub 中[创建 app](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Intercom's API documentation](https://developers.intercom.com/docs/references/introduction/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：当你[创建 app](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/) 时，Intercom 会自动生成 **Access Token**。将此 **Access Token** 用作你的 n8n **API Key**。更详细说明请参考[如何获取 Access Token](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/#how-to-get-your-access-token)。
