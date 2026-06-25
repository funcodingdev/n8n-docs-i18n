---
title: Google OAuth2 generic
contentType:
  - integration
  - reference
nodeTitle: Google OAuth2 generic
originalFilePath: integrations/builtin/credentials/google/oauth-generic.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic
url: https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic
description: >-
  通用 OAuth2 Google credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Google services 进行身份验证。
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

# Google OAuth2 generic

本文档说明如何创建通用 Google OAuth2 API credential，用于[自定义操作](../../custom-api-actions-for-existing-nodes.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/OI5s27oyRBdDvpwcuMQF/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Google Cloud](https://cloud.google.com/) 账号。

## 设置 OAuth <a href="#set-up-oauth" id="set-up-oauth"></a>

将 n8n credential 连接到 Google services 有五个步骤：

1. [创建 Google Cloud Console 项目](oauth-generic.md#create-a-google-cloud-console-project)。
2. [启用 APIs](oauth-generic.md#enable-apis)。
3. [配置 OAuth consent screen](oauth-generic.md#configure-your-oauth-consent-screen)。
4. [创建 Google OAuth client credentials](oauth-generic.md#create-your-google-oauth-client-credentials)。
5. [完成 n8n credential](oauth-generic.md#finish-your-n8n-credential)。

### 创建 Google Cloud Console 项目 <a href="#create-a-google-cloud-console-project" id="create-a-google-cloud-console-project"></a>

首先，创建一个 Google Cloud Console 项目。如果你已经有项目，请跳到[下一节](oauth-generic.md#enable-apis)：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/n3k6ZZ7BRnKZ6enSxeVQ/" %}

### 启用 APIs <a href="#enable-apis" id="enable-apis"></a>

创建项目后，启用你需要访问的 APIs：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Xs1r022aU39nYSgCg3At/" %}

### 配置 OAuth consent screen <a href="#configure-your-oauth-consent-screen" id="configure-your-oauth-consent-screen"></a>

如果你之前没有在 Google Cloud 项目中使用过 OAuth，需要先[配置 OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent)：

1.  打开 [Google Cloud Console - Library](https://console.cloud.google.com/apis/library)。确保你位于正确的项目中。

    <figure><img src="../../../.gitbook/assets/google-cloud-project-dropdown (1).png" alt=""><figcaption><p>检查 Google Cloud 顶部导航中的项目下拉菜单</p></figcaption></figure>
2. 打开左侧导航菜单，进入 **APIs & Services > OAuth consent screen**。Google 会将你重定向到 Google Auth Platform overview 页面。
3. 在 **Overview** 标签页选择 **Get started**，开始配置 OAuth consent。
4. 输入要显示在 OAuth 页面上的 **App name** 和 **User support email**。选择 **Next** 继续。
5. 对于 **Audience**，如果用户访问范围在你组织的 Google workspace 内，请选择 **Internal**；如果任何拥有 Google account 的用户都可以访问，请选择 **External**。更多用户类型信息，请参考 Google 的 [User type documentation](https://support.google.com/cloud/answer/15549945?sjid=17061891731152303663-EU#user-type)。选择 **Next** 继续。
6. 选择 Google 用来联系你了解项目变更的 **Email addresses**。选择 **Next** 继续。
7. 阅读并接受 Google 的 User Data Policy。选择 **Continue**，然后选择 **Create**。
8. 在左侧菜单中选择 **Branding**。
9. 在 **Authorized domains** 区域选择 **Add domain**：
   * 如果你使用 n8n 的 Cloud 服务，添加 `n8n.cloud`
   * 如果你是[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)，添加你的 n8n instance 域名。
10. 在页面底部选择 **Save**。

### 创建 Google OAuth client credentials <a href="#create-your-google-oauth-client-credentials" id="create-your-google-oauth-client-credentials"></a>

接下来，在 Google 中创建 OAuth client credentials：

1. 打开 [Google Cloud Console](https://console.cloud.google.com/)。确保你位于正确的项目中。
2. 在 **APIs & Services** 区域，选择 [**Credentials**](https://console.cloud.google.com/apis/credentials)。
3. 选择 **+ Create credentials** > **OAuth client ID**。
4. 在 **Application type** 下拉菜单中，选择 **Web application**。
5. Google 会自动生成一个 **Name**。将 **Name** 更新为你在控制台中容易识别的名称。
6. 从你的 n8n credential 中复制 **OAuth Redirect URL**。将它粘贴到 Google Console 的 **Authorized redirect URIs** 中。
7. 选择 **Create**。

### 完成 n8n credential <a href="#finish-your-n8n-credential" id="finish-your-n8n-credential"></a>

Google 项目和 credentials 完成配置后，继续完成 n8n credential：

1. 从 Google 的 **OAuth client created** 弹窗复制 **Client ID**。将其填入你的 n8n credential。
2. 从同一个 Google 弹窗复制 **Client Secret**。将其填入你的 n8n credential。
3.  你必须为此 credential 提供 scopes。更多信息请参考 [Scopes](oauth-generic.md#scopes)。多个 scopes 使用空格分隔输入，例如：

    ```
    https://www.googleapis.com/auth/gmail.labels https://www.googleapis.com/auth/gmail.addons.current.action.compose
    ```
4. 在 n8n 中，选择 **Sign in with Google** 完成 Google 身份验证。
5. **Save** 新 credentials。

## 视频 <a href="#video" id="video"></a>

下面的视频演示了上述步骤：

{% embed url="https://www.youtube.com/embed/FBGtpWMTppw" %}

## Scopes <a href="#scopes" id="scopes"></a>

Google services 有一个或多个可能的访问 scopes。scope 会限制用户可以执行的操作。所有服务的 scopes 列表请参考 [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes)。

n8n 不支持所有 scopes。创建通用 Google OAuth2 API credential 时，你可以输入下方 **Supported scopes** 列表中的 scopes。如果输入 n8n 尚不支持的 scope，它将无法工作。

<details>

<summary>Supported scopes</summary>

| Service                                     | Available scopes                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gmail                                       | <ul><li><code>https://www.googleapis.com/auth/gmail.labels</code></li><li><code>https://www.googleapis.com/auth/gmail.addons.current.action.compose</code></li><li><code>https://www.googleapis.com/auth/gmail.addons.current.message.action</code></li><li><code>https://mail.google.com/</code></li><li><code>https://www.googleapis.com/auth/gmail.modify</code></li><li><code>https://www.googleapis.com/auth/gmail.compose</code></li></ul> |
| Google Ads                                  | <ul><li><code>https://www.googleapis.com/auth/adwords</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                           |
| Google Analytics                            | <ul><li><code>https://www.googleapis.com/auth/analytics</code></li><li><code>https://www.googleapis.com/auth/analytics.readonly</code></li></ul>                                                                                                                                                                                                                                                                                                 |
| Google BigQuery                             | <ul><li><code>https://www.googleapis.com/auth/bigquery</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                          |
| Google Books                                | <ul><li><code>https://www.googleapis.com/auth/books</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                             |
| Google Calendar                             | <ul><li><code>https://www.googleapis.com/auth/calendar</code></li><li><code>https://www.googleapis.com/auth/calendar.events</code></li></ul>                                                                                                                                                                                                                                                                                                     |
| <p>Google Cloud<br>Natural Language</p>     | <ul><li><code>https://www.googleapis.com/auth/cloud-language</code></li><li><code>https://www.googleapis.com/auth/cloud-platform</code></li></ul>                                                                                                                                                                                                                                                                                                |
| <p>Google Cloud<br>Storage</p>              | <ul><li><code>https://www.googleapis.com/auth/cloud-platform</code></li><li><code>https://www.googleapis.com/auth/cloud-platform.read-only</code></li><li><code>https://www.googleapis.com/auth/devstorage.full_control</code></li><li><code>https://www.googleapis.com/auth/devstorage.read_only</code></li><li><code>https://www.googleapis.com/auth/devstorage.read_write</code></li></ul>                                                    |
| Google Contacts                             | <ul><li><code>https://www.googleapis.com/auth/contacts</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                          |
| Google Docs                                 | <ul><li><code>https://www.googleapis.com/auth/documents</code></li><li><code>https://www.googleapis.com/auth/drive</code></li><li><code>https://www.googleapis.com/auth/drive.file</code></li></ul>                                                                                                                                                                                                                                              |
| Google Drive                                | <ul><li><code>https://www.googleapis.com/auth/drive</code></li><li><code>https://www.googleapis.com/auth/drive.appdata</code></li><li><code>https://www.googleapis.com/auth/drive.photos.readonly</code></li></ul>                                                                                                                                                                                                                               |
| <p>Google Firebase<br>Cloud Firestore</p>   | <ul><li><code>https://www.googleapis.com/auth/datastore</code></li><li><code>https://www.googleapis.com/auth/firebase</code></li></ul>                                                                                                                                                                                                                                                                                                           |
| <p>Google Firebase<br>Realtime Database</p> | <ul><li><code>https://www.googleapis.com/auth/userinfo.email</code></li><li><code>https://www.googleapis.com/auth/firebase.database</code></li><li><code>https://www.googleapis.com/auth/firebase</code></li></ul>                                                                                                                                                                                                                               |
| Google Perspective                          | <ul><li><code>https://www.googleapis.com/auth/userinfo.email</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                    |
| Google Sheets                               | <ul><li><code>https://www.googleapis.com/auth/drive.file</code></li><li><code>https://www.googleapis.com/auth/spreadsheets</code></li></ul>                                                                                                                                                                                                                                                                                                      |
| Google Slide                                | <ul><li><code>https://www.googleapis.com/auth/drive.file</code></li><li><code>https://www.googleapis.com/auth/presentations</code></li></ul>                                                                                                                                                                                                                                                                                                     |
| Google Tasks                                | <ul><li><code>https://www.googleapis.com/auth/tasks</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                             |
| Google Translate                            | <ul><li><code>https://www.googleapis.com/auth/cloud-translation</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                 |
| GSuite Admin                                | <ul><li><code>https://www.googleapis.com/auth/admin.directory.group</code></li><li><code>https://www.googleapis.com/auth/admin.directory.user</code></li><li><code>https://www.googleapis.com/auth/admin.directory.domain.readonly</code></li><li><code>https://www.googleapis.com/auth/admin.directory.userschema.readonly</code></li></ul>                                                                                                     |

</details>

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Google 尚未验证此 app <a href="#google-hasnt-verified-this-app" id="google-hasnt-verified-this-app"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/uEYII1oKijzYurya61sf/" %}

### Google Cloud app 变为 unauthorized <a href="#google-cloud-app-becoming-unauthorized" id="google-cloud-app-becoming-unauthorized"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/PlbR0ntmBBE0DgjKiavq/" %}
