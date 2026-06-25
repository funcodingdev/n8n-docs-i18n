---
title: GetResponse credentials
description: >-
  GetResponse credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 GetResponse。
contentType:
  - integration
  - reference
nodeTitle: GetResponse credentials
originalFilePath: integrations/builtin/credentials/getresponse.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/getresponse'
url: 'https://docs.n8n.io/integrations/builtin/credentials/getresponse'
layout:
  description:
    visible: false
---

# GetResponse credentials <a href="#getresponse-credentials" id="getresponse-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [GetResponse](../app-nodes/n8n-nodes-base.getresponse.md)
- [GetResponse Trigger](../trigger-nodes/n8n-nodes-base.getresponsetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [GetResponse](https://www.getresponse.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GetResponse 的 API 文档](https://apidocs.getresponse.com/v3)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：要查看或生成 API key，请前往 **Integrations and API > API**。有关更详细的说明，请参阅 [GetResponse Help Center](https://www.getresponse.com/help/where-do-i-find-the-api-key.html)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：在你[注册 application](https://apidocs.getresponse.com/v3/authentication/oauth2) 时生成。
- 一个 **Client Secret**：在你[注册 application](https://apidocs.getresponse.com/v3/authentication/oauth2) 时作为 **Client Secret Key** 生成。

注册 application 时，从 n8n 复制 **OAuth Redirect URL**，并在 GetResponse 中将其添加为 **Redirect URL**。

{% hint style="info" %}
**使用 localhost 的 Redirect URL**

Redirect URL 应是你的 domain 中的 URL，例如：`https://mytemplatemaker.example.com/gr_callback`。GetResponse 不接受 localhost callback URL。请参阅 [FAQs](#configure-oauth2-credentials-for-a-local-environment)，为 local environment 配置 credentials。
{% endhint %}

## 为 local environment 配置 OAuth2 credentials <a href="#configure-oauth2-credentials-for-a-local-environment" id="configure-oauth2-credentials-for-a-local-environment"></a>

GetResponse 不接受 localhost callback URL。按照以下步骤为 local environment 配置 OAuth credentials：
1. 使用 [ngrok](https://ngrok.com/) 将运行在端口 `5678` 的 local server 暴露到互联网。在 terminal 中运行以下命令：
```sh
ngrok http 5678
```
2. 在新的 terminal 中运行以下命令。将 `<YOUR-NGROK-URL>` 替换为上一步获得的 URL。
```sh
export WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. 按照[使用 OAuth2](#using-oauth2) 说明配置 credentials，并将此 URL 用作 **Redirect URL**。
