---
title: Yourls credentials
description: >-
  Yourls credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Yourls 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Yourls credentials
originalFilePath: integrations/builtin/credentials/yourls.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/yourls'
url: 'https://docs.n8n.io/integrations/builtin/credentials/yourls'
layout:
  description:
    visible: false
---

# Yourls credentials <a href="#yourls-credentials" id="yourls-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Yourls](../app-nodes/n8n-nodes-base.yourls.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在你的 server 上安装 [Yourls](https://github.com/YOURLS/YOURLS)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Yourl's documentation](https://yourls.org/docs)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Signature** token：前往 **Tools > Secure passwordless API call** 获取你的 **Signature** token。更多信息请参考 [Yourl's Passworldess API documentation](https://yourls.org/docs/guide/advanced/passwordless-api)。
- 一个 **URL**：输入你的 Yourls instance 的 URL。
