---
title: Nextcloud credentials
description: >-
  Nextcloud credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Nextcloud 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Nextcloud credentials
originalFilePath: integrations/builtin/credentials/nextcloud.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/nextcloud'
url: 'https://docs.n8n.io/integrations/builtin/credentials/nextcloud'
layout:
  description:
    visible: false
---

# Nextcloud credentials <a href="#nextcloud-credentials" id="nextcloud-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Nextcloud](../app-nodes/n8n-nodes-base.nextcloud.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Nextcloud's API documentation](https://nextcloud-server.netlify.app/)。

有关安装和配置 Nextcloud 的更多信息，请参考 [Nextcloud's user manual](https://docs.nextcloud.com/server/stable/user_manual/en/contents.html)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要一个 [Nextcloud](https://nextcloud.com/) 账号，以及：

- 你的 **WebDAV URL**
- 你的 **User** name
- 你的 **Password** 或 app password

设置步骤：

1. 创建你的 **WebDAV URL**：如果 Nextcloud 位于 domain 的根目录，请输入你用于访问 Nextcloud 的 URL，并添加 `/remote.php/webdav/`。例如，如果你通过 `https://cloud.n8n.com` 访问 Nextcloud，则 WebDAV URL 是 `https://cloud.n8n.com/remote.php/webdav`。
    - 如果你将 Nextcloud 安装在 subdirectory 中，请输入你用于访问 Nextcloud 的 URL，并添加 `/<subdirectory>/remote.php/webdav/`。将 `<subdirectory>` 替换为 Nextcloud 安装所在的 subdirectory。
    - 有关构造 WebDAV URL 的更多信息，请参考 Nextcloud 的 [Third-party WebDAV clients](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients) 文档。
2. 输入你的 **User** name。
3. 对于 **Password**，Nextcloud 建议使用 app password，而不是你的 user password。创建 app password：
    1. 在 Nextcloud Web interface 中，选择右上角的 avatar，然后选择 **Personal settings**。
    2. 在左侧菜单中，选择 **Security**。
    3. 滚动到底部的 **App Password** section，并创建一个新的 app password。
    4. 复制该 app password，并在 n8n 中将其输入为你的 **Password**。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Nextcloud](https://nextcloud.com/) 账号，以及：

- **Authorization URL** 和 **Access Token URL**：它们取决于你用于访问 Nextcloud 的 URL。
- 一个 **Client ID**：在 **Administrator Security Settings** 中添加 OAuth2 client application 后生成。
- 一个 **Client Secret**：在 **Administrator Security Settings** 中添加 OAuth2 client application 后生成。
- 一个 **WebDAV URL**：它取决于你用于访问 Nextcloud 的 URL。

设置步骤：

1. 在 Nextcloud 中，打开你的 **Administrator Security Settings**。
2. 在 **OAuth 2.0 clients** 下找到 **Add client** section。
3. 为你的 client 输入一个 **Name**，例如 `n8n integration`。
4. 从 n8n 复制 **OAuth Callback URL**，并将其输入为 **Redirection URI**。
5. 然后在 Nextcloud 中选择 **Add**。
6. 在 n8n 中，更新 **Authorization URL**，将 `https://nextcloud.example.com` 替换为你用于访问 Nextcloud 的 URL。例如，如果你通过 `https://cloud.n8n.com` 访问 Nextcloud，则 Authorization URL 为 `https://cloud.n8n.com/apps/oauth2/authorize`。
7. 在 n8n 中，更新 **Access Token URL**，将 `https://nextcloud.example.com` 替换为你用于访问 Nextcloud 的 URL。例如，如果你通过 `https://cloud.n8n.com` 访问 Nextcloud，则 Access Token URL 为 `https://cloud.n8n.com/apps/oauth2/api/v1/token`。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Pretty URL 配置</strong></p><p><strong>Authorization URL</strong> 和 <strong>Access Token URL</strong> 假设你已经将 Nextcloud 配置为使用 <a href="https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#pretty-urls">Pretty URLs</a>。如果还没有，你必须在 Nextcloud URL 和 <code>/apps/oauth2</code> 部分之间添加 <code>/index.php/</code>，例如：<code>https://cloud.n8n.com/index.php/apps/oauth2/api/v1/token</code>。</p></div>

8. 复制 OAuth2 client 的 Nextcloud **Client Identifier**，并在 n8n 中将其输入为 **Client ID**。
9. 复制 Nextcloud **Secret**，并在 n8n 中将其输入为 **Client Secret**。
10. 在 n8n 中创建你的 **WebDAV URL**：如果 Nextcloud 位于 domain 的根目录，请输入你用于访问 Nextcloud 的 URL，并添加 `/remote.php/webdav/`。例如，如果你通过 `https://cloud.n8n.com` 访问 Nextcloud，则 WebDAV URL 是 `https://cloud.n8n.com/remote.php/webdav`。
    - 如果你将 Nextcloud 安装在 subdirectory 中，请输入你用于访问 Nextcloud 的 URL，并添加 `/<subdirectory>/remote.php/webdav/`。将 `<subdirectory>` 替换为 Nextcloud 安装所在的 subdirectory。
    - 有关构造 WebDAV URL 的更多信息，请参考 Nextcloud 的 [Third-party WebDAV clients](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients) 文档。

更详细的说明请参考 Nextcloud [OAuth2 Configuration documentation](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/oauth2.html)。
