---
title: Adalo credentials
description: >-
  Adalo credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation platform
  中验证 Adalo。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Adalo credentials
originalFilePath: integrations/builtin/credentials/adalo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/adalo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/adalo'
layout:
  description:
    visible: false
---

# Adalo credentials <a href="#adalo-credentials" id="adalo-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Adalo](../app-nodes/n8n-nodes-base.adalo.md)

{% hint style="info" %}
**API access**

你需要 Team 或 Business plan 才能使用 Adalo APIs。
{% endhint %}

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [Adalo API collections 文档](https://help.adalo.com/integrations/the-adalo-api/collections)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Adalo](https://www.adalo.com/) 账号，以及：

- **API Key**
- **App ID**

要获取这些信息，请创建一个 Adalo app：

1. 在顶部导航的 app dropdown 中，选择 **CREATE NEW APP**。
1. 选择适合你的 App Layout type，然后选择 **Next**。
    - 如果你是首次使用该产品，Adalo 推荐使用 **Mobile Only**。
1. 选择一个 template 开始，或选择 **Blank**，然后选择 **Next**。
1. 输入 **App Name**，例如 `n8n integration`。
1. 如果适用，为该 app 选择 **Team**。
1. 选择 branding colors。
1. 选择 **Create**。app editor 会打开。
1. 在左侧菜单中选择 **Settings**（齿轮图标）。
1. 选择 **App Access**。
1. 在 **API Key** section 中，选择 **Generate Key**。
    - 如果你的 plan level 不正确，你会看到升级提示。
1. 复制 key，并在 n8n credential 中作为 **API Key** 输入。
1. URL 在 `https://app.adalo.com/apps/` 后包含 **App ID**。例如，如果 app 的 URL 是 `https://app.adalo.com/apps/b78bdfcf-48dc-4550-a474-dd52c19fc371/app-settings`，则 `b78bdfcf-48dc-4550-a474-dd52c19fc371` 是 App ID。复制此值并输入到你的 n8n credential 中。

有关在 Adalo 中创建 apps 的更多信息，请参阅 [Creating an app](https://help.adalo.com/design/designing-your-app/creating-an-app)。有关生成 API keys 的更多信息，请参阅 [The Adalo API](https://help.adalo.com/integrations/the-adalo-api)。
