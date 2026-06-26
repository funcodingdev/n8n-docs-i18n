---
title: TheHive 5 credentials
description: >-
  TheHive 5 credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 TheHive 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: TheHive 5 credentials
originalFilePath: integrations/builtin/credentials/thehive5.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/thehive5'
url: 'https://docs.n8n.io/integrations/builtin/credentials/thehive5'
layout:
  description:
    visible: false
---

# TheHive 5 credentials <a href="#thehive-5-credentials" id="thehive-5-credentials"></a>

你可以使用这些 credentials 通过 TheHive 5 对以下 nodes 进行身份验证。

- [TheHive 5](../app-nodes/n8n-nodes-base.thehive5.md)

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个 nodes。将这些 credentials 与 TheHive 5 node 配合使用。如果你使用 TheHive node 连接 TheHive 3 或 TheHive 4，请使用 [TheHive credentials](thehive.md)。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在你的 server 上安装 [TheHive 5](https://docs.strangebee.com/thehive/download/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [TheHive's API documentation](https://docs.strangebee.com/thehive/api-docs/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：拥有 `orgAdmin` 和 `superAdmin` 账号的 users 可以生成 API keys：
    - `orgAdmin` account：前往 **Organization > Create API Key**，为你希望生成 key 的 user 创建。
    - `superAdmin` account：前往 **Users > Create API Key**，为你希望生成 key 的 user 创建。
    - 更多信息请参考 [API Authentication](https://docs.strangebee.com/cortex/api/api-guide/?h=api+key#authentication)。
- 一个 **URL**：你的 TheHive server 的 URL。
- **Ignore SSL Issues**：打开后，即使 SSL certificate validation 失败，n8n 也会继续连接。
