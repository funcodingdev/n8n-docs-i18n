---
title: Segment credentials
description: >-
  Segment credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Segment 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Segment credentials
originalFilePath: integrations/builtin/credentials/segment.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/segment'
url: 'https://docs.n8n.io/integrations/builtin/credentials/segment'
layout:
  description:
    visible: false
---

# Segment credentials <a href="#segment-credentials" id="segment-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Segment](../app-nodes/n8n-nodes-base.segment.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Segment](https://segment.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Segment's Sources documentation](https://segment.com/docs/connections/sources/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Write Key**：要获取 Write Key，请前往 **Sources > Add Source**。添加一个 **Node.js** source，并复制该 write key 到你的 n8n credential 中。

更多信息请参考 [Locate your Write Key](https://segment.com/docs/connections/find-writekey/)。
