---
title: OpenWeatherMap credentials
description: >-
  OpenWeatherMap credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 OpenWeatherMap 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: OpenWeatherMap credentials
originalFilePath: integrations/builtin/credentials/openweathermap.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/openweathermap'
url: 'https://docs.n8n.io/integrations/builtin/credentials/openweathermap'
layout:
  description:
    visible: false
---

# OpenWeatherMap credentials <a href="#openweathermap-credentials" id="openweathermap-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [OpenWeatherMap](../app-nodes/n8n-nodes-base.openweathermap.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [OpenWeatherMap's API documentation](https://openweathermap.org/api)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [OpenWeatherMap](https://openweathermap.org/) 账号，以及：

- 一个 **Access Token**

获取 **Access Token**：

1. 验证 email address 后，OpenWeatherMap 会在 welcome email 中包含一个 **API Key**。
2. 复制该 key，并将其输入到你的 n8n credential 中。

如果你更想创建一个新的 key：

1. 要创建新的 key，请前往 **Account >** [**API Keys**](https://home.openweathermap.org/api_keys)。
2. 在 **Create Key** section 中，输入 **API Key Name**，例如 `n8n integration`。
3. 选择 **Generate** 生成你的 key。
4. 复制生成的 key，并将其输入到你的 n8n credential 中。
