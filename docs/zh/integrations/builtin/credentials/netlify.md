---
title: Netlify credentials
description: >-
  Netlify credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Netlify 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Netlify credentials
originalFilePath: integrations/builtin/credentials/netlify.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/netlify'
url: 'https://docs.n8n.io/integrations/builtin/credentials/netlify'
layout:
  description:
    visible: false
---

# Netlify credentials <a href="#netlify-credentials" id="netlify-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Netlify](../app-nodes/n8n-nodes-base.netlify.md)
- [Netlify Trigger](../trigger-nodes/n8n-nodes-base.netlifytrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Netlify](https://netlify.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Netlify's API documentation](https://docs.netlify.com/api/get-started/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 **Access Token**：在 **Applications > Personal Access Tokens** 中生成 Access Token。更详细的说明请参考 [Netlify API Authentication](https://docs.netlify.com/api/get-started/#authentication)。
