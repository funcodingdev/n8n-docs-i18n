---
title: Zammad credentials
description: >-
  Zammad credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zammad 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zammad credentials
originalFilePath: integrations/builtin/credentials/zammad.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zammad'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zammad'
layout:
  description:
    visible: false
---

# Zammad credentials <a href="#zammad-credentials" id="zammad-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Zammad](../app-nodes/n8n-nodes-base.zammad.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 hosted [Zammad](https://zammad.com/) 账号，或设置你自己的 Zammad instance。
- 对于 token authentication，请在 **Settings > System > API** 中启用 **API Token Access**。更多信息请参考 [Setting up a Zammad](https://admin-docs.zammad.org/en/latest/system/integrations/zabbix.html?#setting-up-a-zammad)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- Token auth：Zammad 推荐使用此身份验证方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关向该服务进行身份验证的更多信息，请参考 [Zammad's API Authentication documentation](https://docs.zammad.org/en/latest/api/intro.html?#authentication)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **Base URL**：输入你的 Zammad instance 的 URL。
- 一个 **Email** address：输入用于登录 Zammad 的 email address。
- 一个 **Password**：输入你的 Zammad password。
- **Ignore SSL Issues**：打开后，即使 SSL certificate validation 失败，n8n 也会继续连接。

## 使用 token auth <a href="#using-token-auth" id="using-token-auth"></a>

要配置此 credential，你需要：

- 一个 **Base URL**：输入你的 Zammad instance 的 URL。
- 一个 **Access Token**：为 Zammad instance 启用 **API Token Access** 后，任何拥有 `user_preferences.access_token` permission 的 user 都可以通过前往你的 **avatar > Profile > Token Access** 并 **Create** 新 token 来生成 **Access Token**。
    - access token permissions 取决于你希望用此 credential 完成哪些 actions。要使用 [Zammad](../app-nodes/n8n-nodes-base.zammad.md) node 的全部功能，请选择：
        - `admin.group`
        - `admin.organization`
        - `admin.user`
        - `ticket.agent`
        - `ticket.customer`
- **Ignore SSL Issues**：打开后，即使 SSL certificate validation 失败，n8n 也会继续连接。
