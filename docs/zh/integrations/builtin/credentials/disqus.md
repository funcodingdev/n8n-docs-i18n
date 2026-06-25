---
title: Disqus credentials
description: >-
  Disqus credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Disqus。
contentType:
  - integration
  - reference
nodeTitle: Disqus credentials
originalFilePath: integrations/builtin/credentials/disqus.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/disqus'
url: 'https://docs.n8n.io/integrations/builtin/credentials/disqus'
layout:
  description:
    visible: false
---

# Disqus credentials <a href="#disqus-credentials" id="disqus-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Disqus](../app-nodes/n8n-nodes-base.disqus.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Disqus](https://www.disqus.com/) 账号。
- 注册一个 [API application](https://help.disqus.com/en/articles/1717083-how-to-create-an-api-application)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Disqus 的 API 文档](https://disqus.com/api/docs/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 **Access Token**：注册 API application 后，复制 **API Key** 并在 n8n 中将其添加为 **Access Token**。
