---
title: Vero credentials
description: >-
  Vero credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Vero 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Vero credentials
originalFilePath: integrations/builtin/credentials/vero.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/vero'
url: 'https://docs.n8n.io/integrations/builtin/credentials/vero'
layout:
  description:
    visible: false
---

# Vero credentials <a href="#vero-credentials" id="vero-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Vero](../app-nodes/n8n-nodes-base.vero.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Vero](https://getvero.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API auth token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Vero's API documentation](https://developers.getvero.com/track-api-reference/#/)。

## 使用 API auth token <a href="#using-api-auth-token" id="using-api-auth-token"></a>

要配置此 credential，你需要：

- 一个 **Auth Token**：从你的 Vero account [settings](https://app.getvero.com/settings/project) 获取 auth token。更多信息请参考 [API authentication](https://developers.getvero.com/track-api-reference/#/#authentication)。
