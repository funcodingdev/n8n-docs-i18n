---
title: Twake credentials
description: >-
  Twake credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Twake 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Twake credentials
originalFilePath: integrations/builtin/credentials/twake.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/twake'
url: 'https://docs.n8n.io/integrations/builtin/credentials/twake'
layout:
  description:
    visible: false
---

# Twake credentials <a href="#twake-credentials" id="twake-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Twake](../app-nodes/n8n-nodes-base.twake.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Twake](https://twake.app/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Cloud API key
- Server API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Twake's documentation](https://doc.twake.app/developers-api/api-reference)。

## 使用 Cloud API key <a href="#using-cloud-api-key" id="using-cloud-api-key"></a>

要配置此 credential，你需要：

- 一个 **Workspace Key**：当你将 **n8n** application 安装到 Twake Cloud environment 并选择 **Configure** 时生成。更详细的说明请参考 [How to connect n8n to Twake](https://help.twake.app/en/latest/applications/connectors/index.html#how-to-connect-n8n-to-twake)。

## 使用 Server API key <a href="#using-server-api-key" id="using-server-api-key"></a>

要配置此 credential，你需要：

- 一个 **Host URL**：你的 Twake self-hosted instance 的 URL。
- 一个 **Public ID**：创建 app 时生成。
- 一个 **Private API Key**：创建 app 时生成。

要生成你的 **Public ID** 和 **Private API Key**，请[创建 Twake application](https://doc.twake.app/developers-api/get-started/create-your-first-application)：

1. 前往 **Workspace Settings > Applications and connectors > Access your applications and connectors > Create an application**。
2. 输入适当 details。
3. 创建 app 后，查看其 **API Details**。
4. 复制 **Public identifier**，并将其添加为 n8n **Public ID**。
5. 复制 **Private key**，并将其添加为 n8n **Private API Key**。

更多信息请参考 [API settings](https://doc.twake.app/developers-api/get-started/create-your-first-application#id-3.-api-settings)。
