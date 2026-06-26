---
title: TheHive credentials
description: >-
  TheHive credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 TheHive 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: TheHive credentials
originalFilePath: integrations/builtin/credentials/thehive.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/thehive'
url: 'https://docs.n8n.io/integrations/builtin/credentials/thehive'
layout:
  description:
    visible: false
---

# TheHive credentials <a href="#thehive-credentials" id="thehive-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [TheHive](../app-nodes/n8n-nodes-base.thehive.md)

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个 nodes。将这些 credentials 与 TheHive node 配合用于 TheHive 3 或 TheHive 4。如果你使用 TheHive5 node，请使用 [TheHive 5 credentials](thehive5.md)。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在你的 server 上安装 [TheHive](https://docs.strangebee.com/thehive/installation/installation-methods/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些服务的更多信息，请参考 [TheHive 3's API documentation](https://docs.thehive-project.org/thehive/legacy/thehive3/api/) 和 [TheHive 4's API documentation](https://docs.thehive-project.org/thehive/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：从 **Organization > Create API Key** 创建 API key。更多信息请参考 [API Authentication](https://docs.thehive-project.org/thehive/legacy/thehive3/api/authentication/)。
- 你的 **URL**：你的 TheHive server 的 URL。
- 一个 **API Version**：在以下选项之间选择：
    - **TheHive 3 (api v0)**
    - **TheHive 4 (api v1)**
    - 对于 TheHive 5，请改用 [TheHive 5 credentials](thehive5.md)。
- **Ignore SSL Issues**：打开后，即使 SSL certificate validation 失败，n8n 也会继续连接。
