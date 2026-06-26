---
title: Kibana credentials
description: >-
  Kibana credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Kibana 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Kibana credentials
originalFilePath: integrations/builtin/credentials/kibana.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/kibana'
url: 'https://docs.n8n.io/integrations/builtin/credentials/kibana'
layout:
  description:
    visible: false
---

# Kibana credentials <a href="#kibana-credentials" id="kibana-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Elasticsearch](https://www.elastic.co/) 账号。
- 如果你要创建新账号进行测试，请在 Kibana 中加载一些 sample data。更多信息请参考 [Kibana quick start](https://www.elastic.co/guide/en/kibana/current/get-started.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Kibana's API documentation](https://www.elastic.co/guide/en/kibana/current/api.html)。

这是一个仅 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/kibana/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 你用于访问 Kibana 的 **URL**，例如 `http://localhost:5601`
- **Username**：使用你登录 Elastic 时使用的同一个 username。
- **Password**：使用你登录 Elastic 时使用的同一个 password。
