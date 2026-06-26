---
title: LinkedIn credentials
description: >-
  LinkedIn credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  LinkedIn 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: LinkedIn credentials
originalFilePath: integrations/builtin/credentials/linkedin.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/linkedin'
url: 'https://docs.n8n.io/integrations/builtin/credentials/linkedin'
layout:
  description:
    visible: false
---

# LinkedIn credentials <a href="#linkedin-credentials" id="linkedin-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [LinkedIn](../app-nodes/n8n-nodes-base.linkedin.md)


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [LinkedIn](https://www.linkedin.com/) 账号。
* 创建一个 LinkedIn [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **Community Management OAuth2**：如果你是新的 LinkedIn 用户，或正在创建新的 LinkedIn app，请使用此方式。
- **OAuth2**：将此方式用于较旧的 LinkedIn apps 和 user accounts。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [LinkedIn's Community Management API documentation](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview?view=li-lms-2024-04)。

此 credential 适用于 API version `202404`。

## 使用 Community Management OAuth2 <a href="#using-community-management-oauth2" id="using-community-management-oauth2"></a>

如果你是新的 LinkedIn 用户，或正在创建新的 LinkedIn app，请使用此方式。

要配置此 credential，你需要一个 [LinkedIn](https://www.linkedin.com/) 账号、一个 LinkedIn [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852)，并准备：

- **Client ID**：创建新的 developer app 后生成。
- **Client Secret**：创建新的 developer app 后生成。

创建新的 developer app 并设置 credential：

1. 登录 LinkedIn，并选择此链接[创建新的 developer app](https://www.linkedin.com/developers/apps/new)。
2. 输入 app 的 **App name**，例如 `n8n integration`。
3. 对于 **LinkedIn Page**，输入 LinkedIn [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852)，或使用 **Create a new LinkedIn Page** 链接即时创建一个。更多信息请参考[将 App 关联到 LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360)。
4. 添加 **App logo**。
5. 勾选同意 **Legal agreement** 的复选框。
6. 选择 **Create app**。
7. 这应会打开 **Products** 标签页。选择你要为 app 启用的 products/APIs。要让 LinkedIn node 工作，必须包含并配置：
	- **Share on LinkedIn**
	- **Sign In with LinkedIn using OpenID Connect**
	- **Advertising API**（如果以 organization account 而不是 individual 身份使用）
8. 请求访问所需 products 后，打开 **Auth** 标签页。
9. 复制 **Client ID**，并将其输入到你的 n8n credential。
10. 选择图标以 **Copy** **Primary Client Secret**。在 n8n credential 中将其输入为 **Client Secret**。

{% hint style="info" %}
**从 organization accounts 发帖**

要以 organization 身份发帖，你需要让 app 通过 LinkedIn 的 [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review) 流程。
{% endhint %}

有关 scopes 和 permissions 的更多信息，请参考 [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)。

## 使用 Lead Sync API <a href="#using-lead-sync-api" id="using-lead-sync-api"></a>

LinkedIn 的 Lead Sync API 允许你使用 webhooks 将 LinkedIn ads 和 organic forms（company pages、events、products）的 lead form responses 同步到 n8n workflows。这需要更多设置以及 LinkedIn 审批。

### 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- LinkedIn developer app（使用上面的步骤创建）
- 你的 company LinkedIn account 已链接到 developer app
- 拥有 Lead Sync API product 的访问权限（需要单独申请）
- 公开可访问的 HTTPS webhook URL（你的 n8n workflow webhook URL）

### 设置流程 <a href="#setup-process" id="setup-process"></a>

1. **创建 LinkedIn developer app**：按照上方 Community Management OAuth2 或 OAuth2 部分中的步骤创建。
2. **链接 company account**：向 LinkedIn 提交请求，将你的 company LinkedIn account 链接到 developer app。此操作在 LinkedIn Developer Portal 中完成。
3. **请求 Lead Sync API access**：
   - 在你的 [LinkedIn developer app](https://www.linkedin.com/developers/apps/) 中，进入 **Products** 标签页。
   - 请求访问 **Lead Sync API** product。
4. **配置 permissions**：确保 app 拥有 `r_marketing_leadgen_automation` permission，它允许你：
   - 访问 authenticated member 的 ad forms 和 organic forms
   - 访问 form responses (leads)
   - 管理 lead notifications (webhooks)
5. **在 n8n 中设置 webhook**：
   - 在 n8n 中创建一个带 Webhook trigger node 的 workflow。
   - 从 n8n 复制 webhook URL（必须是 HTTPS）。
   - webhook URL 必须可公开访问，并且接受无需额外 authorization requirements 的 POST requests。
6. **处理 challenge request**：
   - 当你向 LinkedIn 注册 webhook 时，LinkedIn 会发送一个带有 `challengeCode` query parameter 的 GET request。
   - 你的 n8n workflow 必须在 3 秒内返回 JSON payload，其中包含：
     - `challengeCode`：LinkedIn 发送的 code
     - `challengeResponse`：使用 app 的 Client Secret 作为 key，对 challenge code 计算出的 HMAC-SHA256 hash
   - 示例 response 格式：
     ```json
     {
       "challengeCode": "890e4665-4dfe-4ab1-b689-ed553bceeed0",
       "challengeResponse": "27b1d19678542072a7f1d0ce845d0c78cec22567f413697e25648f44fa3d1514"
     }
     ```
7. **创建 lead notification subscription**：
   - 使用 `leadNotifications` API 创建 webhook subscription。
   - 你可以在不同级别创建 subscriptions：
     - **Owner level**：接收 organization 或 sponsored account 下所有 forms 的 notifications
     - **Form level**：仅接收特定 forms 的 notifications
     - **Associated entity level**：接收附加到特定 entities（ads、events 等）的 forms 的 notifications
   - 示例 API call：
     ```bash
     POST https://api.linkedin.com/rest/leadNotifications
     {
       "webhook": "https://your-n8n-instance.com/webhook/linkedin-leads",
       "owner": {"organization": "urn:li:organization:123456"},
       "leadType": "SPONSORED"
     }
     ```
8. **获取 lead form responses**：
   - 设置 webhook notifications 后，当有新 leads 提交时你会收到 notifications。
   - 使用 `leadFormResponses` API 获取实际 lead data：
     ```bash
     GET https://api.linkedin.com/rest/leadFormResponses?owner=(organization:urn%3Ali%3Aorganization%3A123456)&leadType=(leadType:SPONSORED)&q=owner
     ```

### Lead 类型 <a href="#lead-types" id="lead-types"></a>

LinkedIn 支持可同步的不同 leads 类型：

- **SPONSORED**：从 sponsored ads 收集的 leads
- **COMPANY**：从 company pages 收集的 leads
- **EVENT**：从 event pages 收集的 leads
- **ORGANIZATION_PRODUCT**：从 organization product pages 收集的 leads

### Webhook 验证 <a href="#webhook-validation" id="webhook-validation"></a>

LinkedIn 会每 2 小时定期重新验证 webhook endpoints。如果连续 3 次验证失败，endpoint 会被阻止，并且不再发送 events。确保你的 webhook：

- 在 3 秒内响应 challenge requests
- 对所有 notifications 返回 2xx HTTP status code
- 使用 HTTPS（不支持 HTTP URLs）
- 可公开访问且没有 authentication requirements

### 安全 <a href="#security" id="security"></a>

要验证 notifications 来自 LinkedIn：

1. 检查 POST request 中的 `X-LI-Signature` header
2. 此 header 包含 JSON-encoded POST body 的 HMAC-SHA256 hash，使用你的 app 的 Client Secret 计算得出
3. 在你这一侧计算相同 hash，并验证它是否匹配
4. 丢弃 signatures 不匹配的任何 events

更多信息请参考 LinkedIn 的 [Lead Sync API documentation](https://learn.microsoft.com/en-us/linkedin/marketing/lead-sync/leadsync) 和 [Webhook Validation guide](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

仅将此方式用于较旧的 LinkedIn apps 和 user accounts。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

所有用户都必须选择：

- **Organization Support**：如果开启，credential 会请求使用 `w_organization_social` scope 以 organization 身份发帖的 permission。
	- 要使用此选项，你必须让 app 通过 LinkedIn 的 [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review) 流程。
- **Legacy**：如果开启，credential 会使用 `r_liteprofile` 和 `r_emailaddress` 的 legacy scopes，而不是较新的 `profile` 和 `email` scopes。

如果你是[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要通过创建新的 developer app 从头配置 OAuth2：

1. 登录 LinkedIn，并选择此链接[创建新的 developer app](https://www.linkedin.com/developers/apps/new)。
2. 输入 app 的 **App name**，例如 `n8n integration`。
3. 对于 **LinkedIn Page**，输入 LinkedIn [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852)，或使用 **Create a new LinkedIn Page** 链接即时创建一个。更多信息请参考[将 App 关联到 LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360)。
4. 添加 **App logo**。
5. 勾选同意 **Legal agreement** 的复选框。
6. 选择 **Create app**。
7. 这应会打开 **Products** 标签页。选择你要为 app 启用的 products/APIs。要让 LinkedIn node 正常工作，必须包含：
	- **Share on LinkedIn**
	- **Sign In with LinkedIn using OpenID Connect**
8. 请求访问所需 products 后，打开 **Auth** 标签页。
9. 复制 **Client ID**，并将其输入到你的 n8n credential。
10. 选择图标以 **Copy** **Primary Client Secret**。在 n8n credential 中将其输入为 **Client Secret**。

{% hint style="info" %}
**从 organization accounts 发帖**

要以 organization 身份发帖，你需要让 app 通过 LinkedIn 的 [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review) 流程。
{% endhint %}

有关 scopes 和 permissions 的更多信息，请参考 [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)。
