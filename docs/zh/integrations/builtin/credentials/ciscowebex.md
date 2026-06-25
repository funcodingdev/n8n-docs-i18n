---
title: Webex by Cisco credentials
description: >-
  Webex by Cisco credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Webex by Cisco。
contentType:
  - integration
  - reference
nodeTitle: Webex by Cisco credentials
originalFilePath: integrations/builtin/credentials/ciscowebex.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ciscowebex'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ciscowebex'
layout:
  description:
    visible: false
---

# Webex by Cisco credentials <a href="#webex-by-cisco-credentials" id="webex-by-cisco-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Webex by Cisco](../app-nodes/n8n-nodes-base.ciscowebex.md)
- [Webex by Cisco Trigger](../trigger-nodes/n8n-nodes-base.ciscowebextrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Webex by Cisco](https://www.webex.com/) 账号（这应会自动让你获得 [developer account access](https://developer.webex.com)）。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Webex 的 API 文档](https://developer.webex.com/docs/getting-started)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**n8n Cloud 用户注意事项**

你只需要在 OAuth credential 中输入 Credentials Name，并选择 **Connect my account** 按钮，即可将 Webex by Cisco 账号连接到 n8n。
{% endhint %}

如果你需要从零配置 OAuth2，需要创建一个 integration 才能使用此 credential。请参阅 [Webex Registering your Integration 文档](https://developer.webex.com/docs/integrations#registering-your-integration)中的说明开始操作。

n8n 建议为你的 integration 使用以下 **Scopes**：

* `spark:rooms_read`
* `spark:messages_write`
* `spark:messages_read`
* `spark:memberships_read`
* `spark:memberships_write`
* `meeting:recordings_write`
* `meeting:recordings_read`
* `meeting:preferences_read`
* `meeting:schedules_write`
* `meeting:schedules_read`
