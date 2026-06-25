---
title: Discourse credentials
description: >-
  Discourse credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Discourse。
contentType:
  - integration
  - reference
nodeTitle: Discourse credentials
originalFilePath: integrations/builtin/credentials/discourse.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/discourse'
url: 'https://docs.n8n.io/integrations/builtin/credentials/discourse'
layout:
  description:
    visible: false
---

# Discourse credentials <a href="#discourse-credentials" id="discourse-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Discourse](../app-nodes/n8n-nodes-base.discourse.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 托管一个 [Discourse](https://discourse.org/) instance
- 在托管 instance 上创建账号，并确保你是 admin

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Discourse 的 API 文档](https://docs.discourse.org/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 你的 Discourse instance 的 **URL**，例如 `https://community.n8n.io`
- 一个 **API Key**：通过 Discourse admin panel 创建 API key。有关创建 API key 和指定 username 的说明，请参阅 [Discourse create and configure an API key 文档](https://meta.discourse.org/t/create-and-configure-an-api-key/230124)。
- 一个 **Username**：使用你自己的名称、`system` 或其他用户。

有关示例，请参阅 [Discourse API 文档](https://docs.discourse.org/)的 Authentication 部分。
