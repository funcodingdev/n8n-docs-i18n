---
title: Metabase credentials
description: >-
  Metabase credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Metabase 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Metabase credentials
originalFilePath: integrations/builtin/credentials/metabase.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/metabase'
url: 'https://docs.n8n.io/integrations/builtin/credentials/metabase'
layout:
  description:
    visible: false
---

# Metabase credentials <a href="#metabase-credentials" id="metabase-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Metabase node](../app-nodes/n8n-nodes-base.metabase.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个可访问 Metabase instance 的 [Metabase](https://www.metabase.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Metabase's API documentation](https://www.metabase.com/docs/latest/api-documentation)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- **URL**：输入 Metabase instance 的 base URL。如果你使用自定义 domain，请使用该 URL。
- **Username**：输入 Metabase username。
- **Password**：输入 Metabase password。
