---
title: Elasticsearch credentials
description: >-
  Elasticsearch credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Elasticsearch。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Elasticsearch credentials
originalFilePath: integrations/builtin/credentials/elasticsearch.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/elasticsearch'
url: 'https://docs.n8n.io/integrations/builtin/credentials/elasticsearch'
layout:
  description:
    visible: false
---

# Elasticsearch credentials <a href="#elasticsearch-credentials" id="elasticsearch-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Elasticsearch](../app-nodes/n8n-nodes-base.elasticsearch.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Elasticsearch 的文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要一个拥有 [deployment](https://www.elastic.co/guide/en/cloud/current/ec-create-deployment.html) 的 [Elasticsearch](https://www.elastic.co/) 账号，以及：

- 一个 **Username**
- 一个 **Password**
- 你的 Elasticsearch application 的 **Base URL**（也称为 Elasticsearch application endpoint）

设置 credential：

1. 输入 Elasticsearch **Username**。
2. 输入 Elasticsearch **Password**。
3. 在 Elasticsearch 中，前往 **Deployments**。
4. 选择你的 deployment。
5. 选择 **Manage this deployment**。
6. 在 **Applications** 区域中，复制 **Elasticsearch** application 的 endpoint。
7. 在 n8n 中将其输入为 **Base URL**。
8. 默认情况下，n8n 只会在 SSL certificate validation 成功时连接。如果你想在 SSL certificate validation 失败时仍然连接，请打开 **Ignore SSL Issues**。

{% hint style="info" %}
**自定义 endpoint aliases**

如果你为 deployment 添加 [custom endpoint alias](https://www.elastic.co/guide/en/cloud/current/ec-regional-deployment-aliases.html)，请使用新的 endpoint 更新 n8n credential 的 **Base URL**。
{% endhint %}
