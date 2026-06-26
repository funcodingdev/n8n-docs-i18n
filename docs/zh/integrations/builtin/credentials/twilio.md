---
title: Twilio credentials
description: >-
  Twilio credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Twilio 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Twilio credentials
originalFilePath: integrations/builtin/credentials/twilio.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/twilio'
url: 'https://docs.n8n.io/integrations/builtin/credentials/twilio'
layout:
  description:
    visible: false
---

# Twilio credentials <a href="#twilio-credentials" id="twilio-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Twilio](../app-nodes/n8n-nodes-base.twilio.md)
- [Twilio trigger](../trigger-nodes/n8n-nodes-base.twiliotrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **Auth token**：Twilio 建议仅将此方式用于 local testing。
- **API key**：Twilio 建议将此方式用于 production。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Twilio's API documentation](https://www.twilio.com/docs)。

## 使用 Auth Token <a href="#using-auth-token" id="using-auth-token"></a>

要配置此 credential，你需要一个 [Twilio](https://twilio.com/) 账号，以及：

- 你的 Twilio **Account SID**
- 你的 Twilio **Auth Token**

要设置 credential：

1. 在 n8n 中，选择 **Auth Token** 作为 **Auth Type**。
2. 在 Twilio 中，前往 **Console Dashboard > Account Info**。
3. 复制你的 **Account SID**，并将其输入到你的 n8n credential。这会作为 username。
4. 复制你的 **Auth Token**，并将其输入到你的 n8n credential。这会作为 password。

更多信息请参考 [Auth Tokens and How to Change Them](https://help.twilio.com/articles/223136027-Auth-Tokens-and-How-to-Change-Them)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Twilio](https://twilio.com/) 账号，以及：

- 你的 Twilio **Account SID**
- 一个 **API Key SID**：创建 API key 时生成。
- 一个 **API Key Secret**：创建 API key 时生成。

要设置 credential：

1. 在 n8n 中，选择 **API Key** 作为 **Auth Type**。
2. 在 Twilio 中，前往 **Console Dashboard > Account Info**。
3. 复制你的 **Account SID**，并将其输入到你的 n8n credential。
4. 在 Twilio 中，前往你账号的 [**API keys & tokens**](https://www.twilio.com/console/project/api-keys) 页面。
5. 选择 **Create API Key**。
6. 为你的 API key 输入 **Friendly name**，例如 `n8n integration`。
7. 选择你的 **Key type**。n8n 可配合 **Main** 或 **Standard** 使用。更多信息请参考 [选择 API key type](#selecting-an-api-key-type)。
8. 选择 **Create API Key** 完成 key 创建。
5. 在 **Copy secret key** 页面，复制随 key 显示的 **SID**，并将其输入到你的 n8n credential **API Key SID**。
6. 在 **Copy secret key** 页面，复制随 key 显示的 **Secret**，并将其输入到你的 n8n credential **API Key Secret**。

更详细的说明请参考 [Create an API key](https://www.twilio.com/docs/iam/api-keys#create-an-api-key)。

### 选择 API key type <a href="#selecting-an-api-key-type" id="selecting-an-api-key-type"></a>

创建 Twilio API key 时，你必须选择 key type。n8n credential 可配合 **Main** 和 **Standard** key types 使用。

以下是不同 API key types 的更多细节：

* **Main**：此 key type 为你提供与在 API requests 中使用 Account SID 和 Auth Token 相同级别的访问权限。
* **Standard**：此 key type 允许访问 Twilio APIs 中除 API key resources 和 Account resources 之外的所有功能。
* **Restricted**：此 key type 处于 beta。n8n 尚未针对此 key type 测试该 credential；如果你尝试使用并遇到问题，请告诉我们。

有关 key types 的更多信息，请参考 [Types of API keys](https://www.twilio.com/docs/iam/api-keys#types-of-api-keys)。
