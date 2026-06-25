---
title: Google credentials
contentType: overview
nodeTitle: Google
originalFilePath: integrations/builtin/credentials/google/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google
url: https://docs.n8n.io/integrations/builtin/credentials/google
description: >-
  Google credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Google 进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Google

本节包含：

* [OAuth2 single service](oauth-single-service.md)：为特定服务 node 创建 OAuth2 credential，例如 Gmail node。有两个选项：
  * [Managed OAuth2](oauth-single-service.md#managed-oauth2)：直接在 n8n 中使用 Google 登录，无需在 Google Cloud Console 中设置。仅适用于 n8n Cloud 用户，并且只支持部分 Google nodes。
  * [Custom OAuth2](oauth-single-service.md#custom-oauth2)：在 Google Cloud Console 中配置 OAuth2 app，并将它连接到你的 n8n credential。
* [OAuth2 API (generic)](oauth-generic.md)：创建 OAuth2 credential，用于[自定义操作](../../custom-api-actions-for-existing-nodes.md)。
* [Service Account](service-account.md)：为部分特定服务 nodes 创建 [Service Account](https://cloud.google.com/iam/docs/service-account-overview) credential。
* [Google PaLM and Gemini](../googleai.md)：获取 Google Gemini/Google PaLM API key。

## OAuth2 和 Service Account <a href="#oauth2-and-service-account" id="oauth2-and-service-account"></a>

Google services nodes 有两种可用的身份验证方式：

* [OAuth2](https://developers.google.com/identity/protocols/oauth2)：推荐使用，因为它适用范围更广，也更容易设置。
* [Service Account](https://cloud.google.com/iam/docs/understanding-service-accounts)：如需判断何时需要 service account，请参考 [Google documentation: Understanding service accounts](https://cloud.google.com/iam/docs/understanding-service-accounts)。

### 面向 n8n Cloud 用户的 Managed OAuth2 <a href="#managed-oauth2-for-n8n-cloud-users" id="managed-oauth2-for-n8n-cloud-users"></a>

对于 n8n Cloud 用户，以下 Google nodes 支持 [Managed OAuth2](oauth-single-service.md#managed-oauth2)。这会简化 credential 创建流程：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/OI5s27oyRBdDvpwcuMQF/" %}

## 兼容 nodes <a href="#compatible-nodes" id="compatible-nodes"></a>

配置完成后，你可以使用 credentials 对以下 nodes 进行身份验证。大多数 nodes 兼容 OAuth2 身份验证。Service Account 身份验证的支持范围有限。

| Node                                                                                            | OAuth | Service Account |
| ----------------------------------------------------------------------------------------------- | :---: | :-------------: |
| [Google Ads](../../app-nodes/n8n-nodes-base.googleads.md)                                       |   ✅   |        ❌        |
| [Gmail](../../app-nodes/n8n-nodes-base.gmail/)                                                  |   ✅   |        ⚠️       |
| [Google Analytics](../../app-nodes/n8n-nodes-base.googleanalytics.md)                           |   ✅   |        ❌        |
| [Google BigQuery](../../app-nodes/n8n-nodes-base.googlebigquery.md)                             |   ✅   |        ✅        |
| [Google Books](../../app-nodes/n8n-nodes-base.googlebooks.md)                                   |   ✅   |        ✅        |
| [Google Calendar](../../app-nodes/n8n-nodes-base.googlecalendar/)                               |   ✅   |        ❌        |
| [Google Chat](../../app-nodes/n8n-nodes-base.googlechat.md)                                     |   ✅   |        ✅        |
| [Google Cloud Storage](../../app-nodes/n8n-nodes-base.googlecloudstorage.md)                    |   ✅   |        ✅        |
| [Google Contacts](../../app-nodes/n8n-nodes-base.googlecontacts.md)                             |   ✅   |        ❌        |
| [Google Cloud Firestore](../../app-nodes/n8n-nodes-base.googlecloudfirestore.md)                |   ✅   |        ✅        |
| [Google Cloud Natural Language](../../app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md)   |   ✅   |        ❌        |
| [Google Cloud Realtime Database](../../app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) |   ✅   |        ❌        |
| [Google Docs](../../app-nodes/n8n-nodes-base.googledocs.md)                                     |   ✅   |        ✅        |
| [Google Drive](../../app-nodes/n8n-nodes-base.googledrive/)                                     |   ✅   |        ✅        |
| [Google Drive Trigger](../../trigger-nodes/n8n-nodes-base.googledrivetrigger/)                  |   ✅   |        ✅        |
| [Google Perspective](../../app-nodes/n8n-nodes-base.googleperspective.md)                       |   ✅   |        ❌        |
| [Google Sheets](../../app-nodes/n8n-nodes-base.googlesheets/)                                   |   ✅   |        ✅        |
| [Google Slides](../../app-nodes/n8n-nodes-base.googleslides.md)                                 |   ✅   |        ✅        |
| [Google Tasks](../../app-nodes/n8n-nodes-base.googletasks.md)                                   |   ✅   |        ❌        |
| [Google Translate](../../app-nodes/n8n-nodes-base.googletranslate.md)                           |   ✅   |        ✅        |
| [Google Workspace Admin](../../app-nodes/n8n-nodes-base.gsuiteadmin.md)                         |   ✅   |        ❌        |
| [YouTube](../../app-nodes/n8n-nodes-base.youtube.md)                                            |   ✅   |        ❌        |

{% hint style="warning" %}
**Gmail 和 Service Accounts**

Google 从技术上支持在 Gmail 中使用 Service Accounts，但这需要启用 domain-wide delegation，而 Google 不建议这样做，并且其行为可能不稳定。

n8n 建议在 Gmail node 中使用 OAuth2。
{% endhint %}
