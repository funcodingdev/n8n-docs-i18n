---
title: ActiveCampaign credentials
description: >-
  ActiveCampaign credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 ActiveCampaign。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: ActiveCampaign credentials
originalFilePath: integrations/builtin/credentials/activecampaign.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/activecampaign'
url: 'https://docs.n8n.io/integrations/builtin/credentials/activecampaign'
layout:
  description:
    visible: false
---

# ActiveCampaign credentials <a href="#activecampaign-credentials" id="activecampaign-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [ActiveCampaign](../app-nodes/n8n-nodes-base.activecampaign.md)
- [Active Campaign Trigger](../trigger-nodes/n8n-nodes-base.activecampaigntrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [ActiveCampaign API 文档](https://help.activecampaign.com/hc/en-us/sections/360005740979-ActiveCampaign-API-Resources)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [ActiveCampaign](https://www.activecampaign.com/) 账号，以及：

- **API URL**
- **API Key**

获取二者并设置 credential：

1. 在 ActiveCampaign 中，从左侧菜单选择 **Settings**（齿轮图标）。
2. 选择 **Developer**。
3. 复制 **API URL** 并输入到你的 n8n credential 中。
4. 复制 **API Key** 并输入到你的 n8n credential 中。

有关更多信息或重置 API key 的说明，请参阅 [How to obtain your ActiveCampaign API URL and Key](https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#h_01HJ6REM2YQW19KYPB189726ST)。
