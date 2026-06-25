---
title: crowd.dev credentials
description: >-
  crowd.dev credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 crowd.dev。
contentType:
  - integration
  - reference
nodeTitle: crowd.dev credentials
originalFilePath: integrations/builtin/credentials/crowddev.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/crowddev'
url: 'https://docs.n8n.io/integrations/builtin/credentials/crowddev'
layout:
  description:
    visible: false
---

# crowd.dev credentials <a href="#crowddev-credentials" id="crowddev-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [crowd.dev](../app-nodes/n8n-nodes-base.crowddev.md)
* [crowd.dev Trigger](../trigger-nodes/n8n-nodes-base.crowddevtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个可用的 [crowd.dev](https://www.crowd.dev/) instance。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [crowd.dev 的文档](https://docs.crowd.dev/docs)，使用 API 时请参阅其 [API 文档](https://api.crowd.dev/api-reference)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **URL**：
    - 如果你的 crowd.dev instance 托管在 crowd.dev 上，请保留默认值 `https://app.crowd.dev`。
    - 如果你的 crowd.dev instance 是 [self-hosted](https://docs.crowd.dev/docs/technical-docs/self-hosting)，请使用你访问 crowd.dev instance 的 URL。
- 你的 crowd.dev **Tenant ID**：显示在 crowd.dev app 的 **Settings** 区域
- 一个 API **Token**：显示在 crowd.dev app 的 **Settings** 区域

有关更详细的说明，请参阅 [crowd.dev API 文档](https://api.crowd.dev/api-reference)。
