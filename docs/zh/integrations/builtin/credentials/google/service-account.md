---
title: Google Service Account
contentType:
  - integration
  - reference
nodeTitle: Google Service Account
originalFilePath: integrations/builtin/credentials/google/service-account.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google/service-account
url: https://docs.n8n.io/integrations/builtin/credentials/google/service-account
description: >-
  service account Google credentials 文档。使用这些 credentials 在 n8n 这个
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

# Google Service Account

使用 service accounts 比 OAuth2 更复杂。开始之前：

* 检查你的 node 是否与 Service Account [兼容](./#compatible-nodes)。
* 确认你确实需要使用 Service Account。对大多数用例来说，[OAuth2](oauth-single-service.md) 是更好的选择。
* 阅读 Google 关于[创建和管理 service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) 的文档。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Google Cloud](https://cloud.google.com/) 账号。

## 设置 Service Account <a href="#set-up-service-account" id="set-up-service-account"></a>

将 n8n credential 连接到 Google Service Account 有四个步骤：

1. [创建 Google Cloud Console 项目](service-account.md#create-a-google-cloud-console-project)。
2. [启用 APIs](service-account.md#enable-apis)。
3. [设置 Google Cloud Service Account](service-account.md#set-up-google-cloud-service-account)。
4. [完成 n8n credential](service-account.md#finish-your-n8n-credential)。

### 创建 Google Cloud Console 项目 <a href="#create-a-google-cloud-console-project" id="create-a-google-cloud-console-project"></a>

首先，创建一个 Google Cloud Console 项目。如果你已经有项目，请跳到下一节：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/n3k6ZZ7BRnKZ6enSxeVQ/" %}

### 启用 APIs <a href="#enable-apis" id="enable-apis"></a>

创建项目后，启用你需要访问的 APIs：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Xs1r022aU39nYSgCg3At/" %}

### 设置 Google Cloud Service Account <a href="#set-up-google-cloud-service-account" id="set-up-google-cloud-service-account"></a>

1.  打开 [Google Cloud Console - Library](https://console.cloud.google.com/apis/library)。确保你位于正确的项目中。

    <figure><img src="../../../.gitbook/assets/google-cloud-project-dropdown (1).png" alt=""><figcaption><p>检查 Google Cloud 顶部导航中的项目下拉菜单</p></figcaption></figure>
2. 打开左侧导航菜单，进入 **APIs & Services > Credentials**。Google 会带你进入 **Credentials** 页面。
3. 选择 **+ Create credentials > Service account**。
4. 在 **Service account name** 中输入名称，在 **Service account ID** 中输入 ID。更多信息请参考[创建 service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=en#creating)。
5. 选择 **Create and continue**。
6. 根据你的用例，你可能需要使用对应区域 **Select a role**，并 **Grant users access to this service account**。
7. 选择 **Done**。
8. 在 **Service Accounts** 区域选择刚创建的 service account。打开 **Keys** 标签页。
9. 选择 **Add key > Create new key**。
10. 在弹出的窗口中选择 **JSON**，然后选择 **CREATE**。Google 会将文件保存到你的电脑。

### 完成 n8n credential <a href="#finish-your-n8n-credential" id="finish-your-n8n-credential"></a>

Google 项目和 credentials 完成配置后，继续完成 n8n credential：

1. 打开下载的 JSON 文件。
2. 复制 `client_email`，并在 n8n credential 中将其填为 **Service Account Email**。
3.  复制 `private_key`。不要包含外层的 `"` 标记。将其作为 **Private Key** 填入 n8n credential。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>较旧版本的 n8n</strong></p><p>如果你运行的 n8n 版本早于 0.156.0，请将 JSON 文件中所有 <code>\n</code> 替换为换行。</p></div>
4. **可选**：选择是否要[**Impersonate a User**](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority)（开启）。
   1. 要使用此选项，你必须以 Google Workspace super admin 身份为 service account [Enable domain-wide delegation](service-account.md#enable-domain-wide-delegation)。
   2. 输入你要 impersonate 的用户 **Email**。
5. 如果你计划将此 credential 与 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/) node 配合使用，请开启 **Set up for use in HTTP Request node**。
   1. 开启此设置后，你需要为 node 添加 **Scope(s)**。n8n 会预填充一些 scopes。更多信息请参考 [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes)。
6. **Save** credentials。

## 视频 <a href="#video" id="video"></a>

{% embed url="https://www.youtube.com/embed/FzQzGODb5Gk?si=YR9vDaTet8vsj-y2" %}

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Service Account 无法访问 Google Drive 文件 <a href="#service-account-cant-access-google-drive-files" id="service-account-cant-access-google-drive-files"></a>

{% hint style="danger" %}
**无法访问 my drive**

Google 不再允许 2025 年 4 月 15 日之后创建的 Service Accounts 访问 `my drive`。Service Accounts 现在只能访问 shared drives。

虽然不推荐这样做，但如果你需要使用 Service Account 访问 `my drive`，可以通过[启用 domain-wide delegation](service-account.md#enable-domain-wide-delegation) 实现。你可以在[社区中的这篇帖子](https://community.n8n.io/t/please-please-help-upload-file-google-drive-node-with-service-account-not-working/147750/15)了解更多。
{% endhint %}

Service Account 无法访问未与其关联用户 email 共享的 Google Drive 文件和文件夹。

1. 打开 [Google Cloud Console](https://console.cloud.google.com)，复制你的 Service Account email。
2. 打开 [Google Drive](https://drive.google.com)，进入指定的文件或文件夹。
3. 右键点击文件或文件夹，然后选择 **Share**。
4. 将你的 Service Account email 粘贴到 **Add People and groups**。
5. 选择 **Editor** 以授予读写访问权限，或选择 **Viewer** 以授予只读访问权限。

### 启用 domain-wide delegation <a href="#enable-domain-wide-delegation" id="enable-domain-wide-delegation"></a>

要使用 service account impersonate 用户，你必须为 service account 启用 domain-wide delegation。

{% hint style="warning" %}
**不推荐**

Google 建议你[避免使用 domain-wide delegation](https://cloud.google.com/iam/docs/best-practices-service-accounts#domain-wide-delegation)，因为它允许 impersonate 任意用户（包括 super admins），可能带来安全风险。
{% endhint %}

要向 service account 授予 domain-wide authority，你必须是 Google Workspace domain 的 super administrator。然后：

1. 从你的 Google Workspace domain 的 [Admin console](https://admin.google.com/) 中选择汉堡菜单，然后选择 **Security > Access and data control > API Controls**。
2. 在 **Domain wide delegation** 面板中，选择 **Manage Domain Wide Delegation**。
3. 选择 **Add new**。
4. 在 **Client ID** 字段中，输入 service account 的 **Client ID**。获取 Client ID：
   * 打开你的 Google Cloud Console 项目，然后打开 [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) 页面。
   * 复制 **OAuth 2 Client ID**，并将其作为 **Domain Wide Delegation** 的 **Client ID**。
5. 在 **OAuth scopes** 字段中，输入以逗号分隔的 scopes 列表，以授予你的应用访问权限。例如，如果应用需要对 Google Drive API 和 Google Calendar API 拥有 domain-wide full access，请输入：`https://www.googleapis.com/auth/drive, https://www.googleapis.com/auth/calendar`。
6. 选择 **Authorize**。

在你可以 impersonate Workspace 中的所有用户之前，可能需要等待 5 分钟到 24 小时。
