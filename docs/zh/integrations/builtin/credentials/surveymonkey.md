---
title: SurveyMonkey credentials
description: >-
  SurveyMonkey credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SurveyMonkey 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: SurveyMonkey credentials
originalFilePath: integrations/builtin/credentials/surveymonkey.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/surveymonkey'
url: 'https://docs.n8n.io/integrations/builtin/credentials/surveymonkey'
layout:
  description:
    visible: false
---

# SurveyMonkey credentials <a href="#surveymonkey-credentials" id="surveymonkey-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SurveyMonkey Trigger](../trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md)


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [SurveyMonkey](https://www.surveymonkey.com) 账号。
- 从你的 [**Developer dashboard > My apps**](https://developer.surveymonkey.com/apps/) [注册一个 app](https://api.surveymonkey.com/v3/docs?api_key=3yr7n6m8sjwvm48x8nhxej52#registering-an-app)。
    - 有关必须使用的 scopes，请参考 [所需 app scopes](#required-app-scopes)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SurveyMonkey's API documentation](https://developer.surveymonkey.com/api/v3/#SurveyMonkey-Api)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 **Access Token**：创建 app 后生成。
- 一个 **Client ID**：创建 app 后生成。
- 一个 **Client Secret**：创建 app 后生成。

创建 app 并分配适当 scopes 后，前往 **Settings > Credentials**。复制 **Access Token**、**Client ID** 和 **Secret**，并将它们添加到 n8n。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：创建 app 后生成。
- 一个 **Client Secret**：创建 app 后生成。

创建 app 并分配适当 scopes 后：

1. 前往 app 的 **Settings > Settings**。
2. 从 n8n 复制 **OAuth Redirect URL**。
3. 用该 URL 覆盖 app 现有的 **OAuth Redirect URL**。
4. 选择 **Submit Changes**。
5. 确认 **Scopes** 部分包含 [所需 app scopes](#required-app-scopes)。

从 app 的 **Settings > Credentials** 中复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential。现在你可以从 n8n 选择 **Connect my account**。

{% hint style="info" %}
**SurveyMonkey Test OAuth Flow**

只有保留默认 SurveyMonkey **OAuth Redirect URL**，并将 n8n OAuth Redirect URL 添加为 **Additional Redirect URL** 时，此选项才有效。
{% endhint %}

## 所需 app scopes <a href="#required-app-scopes" id="required-app-scopes"></a>

创建 app 后，前往 **Settings > Scopes**。为你的 n8n credential 选择以下 scopes 才能正常工作：

- **View Surveys**
- **View Collectors**
- **View Responses**
- **View Response Details**
- **Create/Modify Webhooks**
- **View Webhooks**

选择 **Update Scopes** 保存。
