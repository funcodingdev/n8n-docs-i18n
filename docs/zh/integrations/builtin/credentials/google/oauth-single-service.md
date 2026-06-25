---
title: Google OAuth2 single service
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Google OAuth2 single service
originalFilePath: integrations/builtin/credentials/google/oauth-single-service.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service
url: >-
  https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service
description: >-
  single service OAuth2 Google credentials 文档。使用这些 credentials 在 n8n 这个
  workflow 自动化平台中对 Google 进行身份验证。
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

# Google OAuth2 single service

本文档说明如何为单个服务创建 Google credential。你也可以观看[视频](oauth-single-service.md#video)了解这些步骤。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Google Cloud](https://cloud.google.com/) 账号。

## Managed OAuth2 <a href="#managed-oauth2" id="managed-oauth2"></a>

n8n Cloud 用户可以在以下 nodes 中使用 **Managed OAuth2**：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/OI5s27oyRBdDvpwcuMQF/" %}

要使用 **Managed OAuth2**，只需在 credentials 页面点击 **Sign in with Google**。无需在 Google Cloud Console 或其他地方继续设置。

![Managed OAuth2 credentials screen](../../../.gitbook/assets/managed-oauth.png)

如果你更想使用 Custom OAuth2，可以使用下拉菜单更改身份验证类型。

## Custom OAuth2 <a href="#custom-oauth2" id="custom-oauth2"></a>

Managed OAuth2 不适用于自托管 n8n 用户，也不适用于上方[列出](oauth-single-service.md#managed-oauth2)范围之外的 Google nodes。你必须创建 custom OAuth2 single service credential。这意味着需要在 Google Cloud Console 中创建 app，并使用 Client ID 和 Client Secret 将它连接到 n8n。

本文档的其余部分介绍完整流程。

## 设置 Custom OAuth2 <a href="#set-up-custom-oauth2" id="set-up-custom-oauth2"></a>

将 n8n credential 连接到 Google services 有五个步骤：

1. [创建 Google Cloud Console 项目](oauth-single-service.md#create-a-google-cloud-console-project)。
2. [启用 APIs](oauth-single-service.md#enable-apis)。
3. [配置 OAuth consent screen](oauth-single-service.md#configure-your-oauth-consent-screen)。
4. [创建 Google OAuth client credentials](oauth-single-service.md#create-your-google-oauth-client-credentials)。
5. [完成 n8n credential](oauth-single-service.md#finish-your-n8n-credential)。

### 创建 Google Cloud Console 项目 <a href="#create-a-google-cloud-console-project" id="create-a-google-cloud-console-project"></a>

首先，创建一个 Google Cloud Console 项目。如果你已经有项目，请跳到[下一节](oauth-single-service.md#enable-apis)：

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
5.  对于 **Audience**，如果用户访问范围在你组织的 Google workspace 内，请选择 **Internal**；如果任何拥有 Google account 的用户都可以访问，请选择 **External**。更多用户类型信息，请参考 Google 的 [User type documentation](https://support.google.com/cloud/answer/15549945?sjid=17061891731152303663-EU#user-type)。选择 **Next** 继续。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Testing mode 和 test users</strong></p><p>如果选择 <strong>External</strong>，你的 app 默认会进入 Testing mode。在此模式下，只有你手动添加为 test users 的 Google accounts 可以完成 OAuth 流程，其他人会看到 "access denied" 页面。要了解如何添加用户，请参阅 <a href="oauth-single-service.md#google-hasnt-verified-this-app">Google 尚未验证此 app</a>。</p></div>
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
6.  从你的 n8n credential 中复制 **OAuth Redirect URL**。将它粘贴到 Google Console 的 **Authorized redirect URIs** 中。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>自托管的 OAuth redirect URL</strong></p><p>如果你在本机运行 n8n，使用 Google OAuth 不需要公共域名、SSL 证书或端口转发。Google 允许将 localhost 作为开发用途的有效 redirect URI。你的 n8n OAuth redirect URL 看起来可能类似：<code>http://localhost:5678/rest/oauth2-credential/callback</code>。关于可接受 redirect URIs 的更多详细信息，请参考 <a href="https://support.google.com/cloud/answer/15549257?hl=en#zippy=%2Cweb-applications">Google's redirect URI documentation</a>。</p></div>
7. 选择 **Create**。

### 完成 n8n credential <a href="#finish-your-n8n-credential" id="finish-your-n8n-credential"></a>

Google 项目和 credentials 完成配置后，继续完成 n8n credential：

1. 从 Google 的 **OAuth client created** 弹窗复制 **Client ID**。将其填入你的 n8n credential。
2. 从同一个 Google 弹窗复制 **Client Secret**。将其填入你的 n8n credential。
3. 在 n8n 中，选择 **Sign in with Google** 完成 Google 身份验证。
4. **Save** 新 credentials。

## 视频 <a href="#video" id="video"></a>

{% embed url="https://www.youtube.com/embed/FBGtpWMTppw" %}

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Google 尚未验证此 app <a href="#google-hasnt-verified-this-app" id="google-hasnt-verified-this-app"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/uEYII1oKijzYurya61sf/" %}

### Google Cloud app 变为 unauthorized <a href="#google-cloud-app-becoming-unauthorized" id="google-cloud-app-becoming-unauthorized"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/PlbR0ntmBBE0DgjKiavq/" %}

### redirect\_uri\_mismatch <a href="#redirecturimismatch" id="redirecturimismatch"></a>

此错误表示 n8n 发送的 redirect URI 与 Google Cloud Console OAuth client 中注册的任何 URI 都不匹配。

**修复：** 从 n8n credential 面板复制 **OAuth Redirect URL**，并将其完整粘贴到 Google OAuth client 的 **Authorized redirect URIs** 字段中，包括协议（`http` 或 `https`）和端口号。

### Access denied / "app not verified" <a href="#access-denied-app-not-verified" id="access-denied-app-not-verified"></a>

这通常是因为你的 app 仍处于 Testing mode，并且你尝试用于身份验证的 Google account 尚未添加为 test user。

**修复：** 前往 **APIs & Services** > **OAuth consent screen** > **Test users**，添加你要使用的账号。

### invalid\_client <a href="#invalidclient" id="invalidclient"></a>

此错误通常表示 n8n credential 中的 Client ID 或 Client Secret 与 Google Cloud Console 中的值不匹配。

**修复：** 回到 Google Cloud Console 中的 OAuth client，重新复制这两个值，然后重新输入到 n8n。复制时注意不要带入意外空格。
