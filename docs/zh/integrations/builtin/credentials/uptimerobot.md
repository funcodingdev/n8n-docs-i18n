---
title: UptimeRobot credentials
description: >-
  UptimeRobot credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 UptimeRobot 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: UptimeRobot credentials
originalFilePath: integrations/builtin/credentials/uptimerobot.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/uptimerobot'
url: 'https://docs.n8n.io/integrations/builtin/credentials/uptimerobot'
layout:
  description:
    visible: false
---

# UptimeRobot credentials <a href="#uptimerobot-credentials" id="uptimerobot-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [UptimeRobot](../app-nodes/n8n-nodes-base.uptimerobot.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [UptimeRobot](https://uptimerobot.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [UptimeRobot's API documentation](https://uptimerobot.com/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：从 **My Settings > API Settings** 获取你的 API Key。创建 **Main API Key**，并将此 key 输入到你的 n8n credential。

### API key 类型 <a href="#api-key-types" id="api-key-types"></a>

UptimeRobot 支持三种 API key 类型：

- **Account-specific**（也称为 **main**）：拉取多个 monitors 的数据。
- **Monitor-specific**：拉取单个 monitor 的数据。
- **Read-only**：只运行 `GET` API calls。

要完成 UptimeRobot node 中的所有 operations，请使用 **Main** 或 **Account-specific** API key type。更多信息请参考 [API authentication](https://uptimerobot.com/api/#auth)。
