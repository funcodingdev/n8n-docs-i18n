---
title: Bubble credentials
description: >-
  Bubble credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Bubble。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Bubble credentials
originalFilePath: integrations/builtin/credentials/bubble.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/bubble'
url: 'https://docs.n8n.io/integrations/builtin/credentials/bubble'
layout:
  description:
    visible: false
---

# Bubble credentials <a href="#bubble-credentials" id="bubble-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Bubble](../app-nodes/n8n-nodes-base.bubble.md)

{% hint style="info" %}
**API access**

你需要付费 plan 才能访问 Bubble APIs。
{% endhint %}

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bubble 的 API 文档](https://manual.bubble.io/help-guides/integrations/api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个付费 [Bubble](https://bubble.io) 账号，以及：

- 一个 **API Token**
- 一个 **App Name**
- 你的 **Domain**，如果你使用 custom domain

要进行设置，你需要创建一个 app：

1. 前往 Bubble 中的 [**Apps**](https://bubble.io/home/apps) 页面。
1. 选择 **Create an app**。
1. 为你的 app 输入 **Name**，例如 `n8n-integration`。
1. 选择 **Get started**。app 详情会打开。
1. 在左侧导航中，选择 **Settings**（齿轮图标）。
1. 选择 **API** 选项卡。
1. 在 **Public API Endpoints** 区域中，勾选 **Enable Data API**。
1. 页面会显示 **Data API root URL**，例如：`https://n8n-integration.bubbleapps.io/version-test/api/1.1/obj`。
1. 复制 URL 中 `https://` 之后、`.bubbleapps.io` 之前的部分，并在 n8n 中将其输入为 **App Name**。在上面的示例中，你应输入 `n8n-integration`。
1. 选择 **Generate a new API token**。
8. 输入 **API Token Label**，例如 `n8n integration`。
1. 复制 **Private key**，并在 n8n credential 中将其输入为 **API Token**。
    - 有关生成 API tokens 的更多信息，请参阅 [Data API | Authentication](https://manual.bubble.io/core-resources/api/the-bubble-api/the-data-api/authentication)。
1. 在 n8n 中，选择最符合你的 app 的 **Environment**：
    - 对于尚未部署的 app，选择 **Development**，访问地址为 `https://appname.bubbleapps.io/version-test` 或 `https://www.mydomain.com/version-test`。
    - 对于已经[部署](https://manual.bubble.io/help-guides/getting-started/navigating-the-bubble-editor/deploying-your-app)的 app，选择 **Live**，访问地址为 `https://appname.bubbleapps.io` 或 `https://www.mydomain.com`。
1. 在 n8n 中，选择你的 **Hosting**：
    - 如果你尚未设置 custom domain，选择 **Bubble Hosting**。
    - 如果你已经设置 [custom domain](https://manual.bubble.io/help-guides/getting-started/navigating-the-bubble-editor/tabs-and-sections/settings-tab/web-app/custom-domain-and-dns)，选择 **Self Hosted** 并输入你的 custom **Domain**。

有关更多信息，请参阅 Bubble 的 [Creating and managing apps](https://manual.bubble.io/help-guides/getting-started/creating-and-managing-apps) 文档。
