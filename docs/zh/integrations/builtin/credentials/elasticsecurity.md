---
title: Elastic Security credentials
description: >-
  Elastic Security credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Elastic Security。
contentType:
  - integration
  - reference
nodeTitle: Elastic Security credentials
originalFilePath: integrations/builtin/credentials/elasticsecurity.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity'
url: 'https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity'
layout:
  description:
    visible: false
---

# Elastic Security credentials <a href="#elastic-security-credentials" id="elastic-security-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Elastic Security](../app-nodes/n8n-nodes-base.elasticsecurity.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Elastic Security](https://www.elastic.co/security) 账号。
- [Deploy](https://www.elastic.co/guide/en/cloud/current/ec-create-deployment.html) 一个 application。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- API Key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Elastic Security 的文档](https://www.elastic.co/guide/en/security/current/es-overview.html)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- **Username**：用于登录 Elasticsearch 的 user account。
- **Password**：用于登录 Elasticsearch 的 user account。
- 你的 Elasticsearch application 的 **Base URL**（也称为 Elasticsearch application endpoint）：

    1. 在 Elasticsearch 中，选择 **Manage this deployment** 选项。
    2. 在 **Applications** 区域中，复制 **Elasticsearch** application 的 endpoint。
    3. 在 n8n 中将其添加为 **Base URL**。

{% hint style="info" %}
**自定义 endpoint aliases**

如果你为 deployment 添加 [custom endpoint alias](https://www.elastic.co/guide/en/cloud/current/ec-regional-deployment-aliases.html)，请使用新的 endpoint 更新 n8n credential 的 **Base URL**。
{% endhint %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：用于登录 Elasticsearch 的 user account。有关更多信息，请参阅 Elasticsearch 的 [Create API key 文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html)。
- 你的 Elasticsearch application 的 **Base URL**（也称为 Elasticsearch application endpoint）：

    1. 在 Elasticsearch 中，选择 **Manage this deployment** 选项。
    2. 在 **Applications** 区域中，复制 **Elasticsearch** application 的 endpoint。
    3. 在 n8n 中将其添加为 **Base URL**。
