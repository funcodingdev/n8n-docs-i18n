---
title: Acuity Scheduling credentials
description: >-
  Acuity Scheduling credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Acuity Scheduling。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Acuity Scheduling credentials
originalFilePath: integrations/builtin/credentials/acuityscheduling.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/acuityscheduling'
url: 'https://docs.n8n.io/integrations/builtin/credentials/acuityscheduling'
layout:
  description:
    visible: false
---

# Acuity Scheduling credentials <a href="#acuity-scheduling-credentials" id="acuity-scheduling-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Acuity Scheduling Trigger](../trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Acuity Scheduling](https://acuityscheduling.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [Acuity API 文档](https://developers.acuityscheduling.com/reference/quick-start)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 数字形式的 **User ID**
- **API Key**

请参阅 [Acuity API Quick Start authentication 说明](https://developers.acuityscheduling.com/reference/quick-start#authentication)，生成 API key 并查看你的 User ID。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果需要从头设置，请完成 [Acuity OAuth2 Account Registration 页面](https://acuityscheduling.com/oauth2/register)。使用该 registration 提供的 **Client ID** 和 **Client Secret**。
