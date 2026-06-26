---
title: Line credentials
description: >-
  Line credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对 Line
  node 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Line credentials
originalFilePath: integrations/builtin/credentials/line.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/line'
url: 'https://docs.n8n.io/integrations/builtin/credentials/line'
layout:
  description:
    visible: false
---

# Line credentials <a href="#line-credentials" id="line-credentials"></a>


{% hint style="warning" %}
**已弃用：服务终止**

LINE Notify 将于 2025 年 4 月 1 日停止服务，此 node 在该日期之后将不再工作。更多信息请查看 LINE Notify 的[服务终止公告](https://notify-bot.line.me/closing-announce)。
{% endhint %}


你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Line](../app-nodes/n8n-nodes-base.line.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Notify OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Line Notify's API documentation](https://notify-bot.line.me/doc/en/)。

## 使用 Notify OAuth2 <a href="#using-notify-oauth2" id="using-notify-oauth2"></a>

要配置此 credential，你需要一个 [Line](https://line.me/en/) 账号，并准备：

- **Client ID**
- **Client Secret**

要生成二者，请将 Line 与 [Line Notify](https://notify-bot.line.me/en/) 连接。然后：

1. 打开 Line Notify 页面以[添加新服务](https://notify-bot.line.me/my/services/new)。
1. 输入 **Service name**。当有人尝试连接到该服务时会显示此名称。
1. 输入 **Service description**。
1. 输入 **Service URL**
1. 输入你的 **Company/Enterprise**。
1. 选择你的 **Country/region**。
1. 输入你的姓名或团队名称作为 **Representative**。
1. 输入有效的 **Email address**。Line 会在服务完全注册前验证此 email address。请使用你可以立即访问的 email address。
1. 从你的 n8n credential 复制 **OAuth Redirect URL**，并在 Line Notify 中将它输入为 **Callback URL**。
1. 选择 **Agree and continue** 同意服务条款。
1. 确认输入的信息正确，然后选择 **Add**。
1. 检查你的 email，并打开 Line Notify Registration URL 以验证 email address。
1. 验证完成后，打开 [**My services**](https://notify-bot.line.me/my/services/)。
1. 选择刚添加的服务。
1. 复制 **Client ID**，并将它输入到你的 n8n credential。
1. 选择 **Display** **Client Secret** 的选项。复制 **Client Secret**，并将它输入到你的 n8n credential。
1. 在 n8n 中，选择 **Connect my account**，并按屏幕提示完成 credential。

更多信息请参考 [Line Notify's API documentation](https://notify-bot.line.me/doc/en/) 的 Authentication 部分。
