---
title: Mattermost credentials
description: >-
  Mattermost credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mattermost 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Mattermost credentials
originalFilePath: integrations/builtin/credentials/mattermost.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mattermost'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mattermost'
layout:
  description:
    visible: false
---

# Mattermost credentials <a href="#mattermost-credentials" id="mattermost-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mattermost](../app-nodes/n8n-nodes-base.mattermost.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mattermost's API documentation](https://api.mattermost.com/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [Mattermost](https://www.mattermost.com/) 账号，并准备：

- personal **Access Token**
- 你的 Mattermost **Base URL**。

设置步骤：

1. 在 Mattermost 中，前往 **Profile > Security > Personal Access Tokens**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>没有 Personal Access Tokens 选项</strong></p><p>如果你没有看到 Personal Access Tokens 选项，请参考下方 <a href="#enable-personal-access-tokens">启用 personal access tokens</a> 中的故障排查步骤。</p></div>

2. 选择 **Create Token**。
3. 输入 **Token description**，例如 `n8n integration`。
4. 选择 **Save**。
5. 复制 **Token ID**，并在 n8n credential 中将其输入为 **Access Token**。
6. 将 Mattermost URL 输入为 **Base URL**。
7. 默认情况下，n8n 仅在 SSL certificate validation 成功时连接。要在 SSL certificate validation 失败时仍然连接，请开启 **Ignore SSL Issues**。

更多信息请参考 Mattermost [Personal access tokens documentation](https://developers.mattermost.com/integrate/reference/personal-access-token/)。

## 启用 personal access tokens <a href="#enable-personal-access-tokens" id="enable-personal-access-tokens"></a>

看不到 **Personal Access Tokens** 选项可能有两个原因：

- Mattermost 未启用 personal access tokens integration。
- 你正在尝试以 non-admin user 身份生成 personal access token，而该用户没有生成 personal access tokens 的 permission。

要确定根本原因并解决：

1. 以 admin 身份登录 Mattermost。
2. 前往 **System Console > Integrations > Integration Management**。
3. 确认 **Enable personal access tokens** 设置为 **true**。如果不是，请修改。
4. 前往 **System Console > User Management > Users**。
5. 搜索你希望允许其生成 personal access tokens 的 user account。
6. 为该 user 选择 **Actions** dropdown，然后选择 **Manage roles**。
7. 勾选 **Allow this account to generate personal access tokens** 并 **Save**。

更多信息请参考 Mattermost [Personal access tokens documentation](https://developers.mattermost.com/integrate/reference/personal-access-token/)。
