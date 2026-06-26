---
title: WhatsApp Business Cloud credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: WhatsApp Business Cloud credentials
originalFilePath: integrations/builtin/credentials/whatsapp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/whatsapp
url: https://docs.n8n.io/integrations/builtin/credentials/whatsapp
description: >-
  WhatsApp Business Cloud credentials 文档。使用这些 credentials 在 n8n
  这个 workflow 自动化平台中对 WhatsApp Business Cloud 进行身份验证。
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

# WhatsApp Business Cloud credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/)
* [WhatsApp Trigger](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md)

## 要求 <a href="#requirements" id="requirements"></a>

要为 WhatsApp 创建 credentials，你需要以下 Meta assets：

* 一个 [Meta developer](https://developers.facebook.com/docs/development/register) account：developer account 允许你创建和管理 Meta apps，包括 WhatsApp integrations。

<details>

<summary>设置 Meta developer account</summary>

1. 访问 [Facebook Developers site](https://developers.facebook.com)。
2. 点击右上角的 **Getting Started**（如果链接显示为 **My Apps**，说明你已经设置了 developer account）。
3. 同意条款和条件。
4. 提供 phone number 进行验证。
5. 选择你的 occupation 或 role。

</details>

- 一个 Meta [business portfolio](https://www.facebook.com/business/help/1710077379203657?id=180505742745347)：WhatsApp messaging services 需要 Meta business portfolio，它以前称为 Business Manager account。UI 中可能仍显示任一选项。

<details>

<summary>设置 Meta business portfolio</summary>

1. 访问 [Facebook Business site](https://business.facebook.com)。
2. 选择 **Create an account**。
   * 如果你已经有 Facebook Business account 和 portfolio，但想创建新的 portfolio，请在左侧菜单中打开 business portfolio selector，并选择 **Create a business portfolio**。
3. 输入 **Business portfolio name**。
4. 输入你的 **name**。
5. 输入 **business email**。
6. 选择 **Submit** 或 **Create**。

</details>

- 一个配置了 WhatsApp 的 Meta [business app](https://developers.facebook.com/docs/development/create-an-app/)：拥有 developer account 后，你将创建 Meta business app。

<details>

<summary>设置带 WhatsApp 的 Meta business app</summary>

1. 访问 [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)
2. 选择 **Create app**。
3. 在 **Add products to your app** 中，选择 WhatsApp tile 中的 **Set up**。更多细节请参考 [Add the WhatsApp Product](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers#step-3--add-the-whatsapp-product)。
4. 这会打开 WhatsApp **Quickstart** 页面。选择你的 business portfolio。
5. 选择 **Continue**。
6. 在左侧菜单中，前往 **App settings** > **Basic**。
7. 为 app 设置 **Privacy Policy URL** 和 **Terms of Service URL**。
8. 将 **App Mode** 改为 **Live**。

</details>

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key：用于 [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/) node。
* OAuth2：用于 [WhatsApp Trigger](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md) node。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [WhatsApp's API documentation](https://developers.facebook.com/docs/whatsapp/#platform-apis)。

Meta 将创建 WhatsApp business apps 的 users 归类为 Tech Providers；更多信息请参考 Meta 的 [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

你需要 WhatsApp API key credentials 才能使用 [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/) node。

要配置此 credential，你需要：

* 一个 API **Access Token**
* 一个 **Business Account ID**

要生成 access token，请按以下步骤操作：

1. 访问 [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)。
2. 选择你的 Meta app。
3. 在左侧菜单中，选择 **WhatsApp** > **API Setup**。
4. 选择 **Generate access token** 并确认你要授予的访问权限。
5. 复制 **Access token**，并将其作为 **Access Token** 添加到 n8n。
6. 复制 **WhatsApp Business Account ID**，并将其作为 **Business Account ID** 添加到 n8n。

有关上述步骤的更多信息，请参考 [Test Business Messaging on WhatsApp](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-4--test-business-messaging-on-whatsapp)。

完全验证和发布你的 app 还需要更多配置。更多信息请参考 Meta 的 [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution) 第 5 步及后续步骤。有关 Meta App Review process 的更多信息，请参考 [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

你需要 WhatsApp OAuth2 credentials 才能使用 [WhatsApp Trigger](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md) node。

要配置此 credential，你需要：

* 一个 **Client ID**
* 一个 **Client Secret**

要检索这些项目，请按以下步骤操作：

1. 访问 [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)。
2. 选择你的 Meta app。
3. 在左侧菜单中，选择 **App settings** > **Basic**。
4. 复制 **App ID**，并在 n8n credential 中将其输入为 **Client ID**。
5. 复制 **App Secret**，并将其输入为 **Client Secret**。

完全验证和发布你的 app 还需要更多配置。更多信息请参考 Meta 的 [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution) 第 5 步及后续步骤。有关 Meta App Review process 的更多信息，请参考 [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)。
