---
title: Cockpit credentials
description: >-
  Cockpit credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Cockpit。
contentType:
  - integration
  - reference
nodeTitle: Cockpit credentials
originalFilePath: integrations/builtin/credentials/cockpit.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cockpit'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cockpit'
layout:
  description:
    visible: false
---

# Cockpit credentials <a href="#cockpit-credentials" id="cockpit-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Cockpit](../app-nodes/n8n-nodes-base.cockpit.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cockpit](https://getcockpit.com/) 账号。
- 设置一个 [self-hosted Cockpit instance](https://getcockpit.com/documentation/core/quickstart/installation)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cockpit 的 API 文档](https://getcockpit.com/documentation/core/api/introduction)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 你的 **Cockpit URL**：你用于访问 Cockpit instance 的 URL
- 一个 **Access Token**：有关创建 API token 的说明，请参阅 [Cockpit Managing tokens 文档](https://getcockpit.com/documentation/core/api/authentication/#managing-tokens)。在 n8n 中使用 **API token** 作为 **Access Token**。
