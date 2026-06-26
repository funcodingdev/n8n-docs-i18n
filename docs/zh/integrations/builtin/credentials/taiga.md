---
title: Taiga credentials
description: >-
  Taiga credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Taiga 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Taiga credentials
originalFilePath: integrations/builtin/credentials/taiga.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/taiga'
url: 'https://docs.n8n.io/integrations/builtin/credentials/taiga'
layout:
  description:
    visible: false
---

# Taiga credentials <a href="#taiga-credentials" id="taiga-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Taiga](../app-nodes/n8n-nodes-base.taiga.md)
- [Taiga Trigger](../trigger-nodes/n8n-nodes-base.taigatrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Taiga](https://taiga.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Taiga's API documentation](https://docs.taiga.io/api.html)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **Username**：输入你的 username 或 user email address。更多信息请参考 [Normal login](https://docs.taiga.io/api.html#auth-normal-login)。
- 一个 **Password**：输入你的 password。
- **Environment**：在 **Cloud** 或 **Self-Hosted** 之间选择。对于 **Self-Hosted** instances，你还需要添加：
    - **URL**：输入你的 Taiga URL。
