---
title: Cloudflare credentials
description: >-
  Cloudflare credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Cloudflare。
contentType:
  - integration
  - reference
nodeTitle: Cloudflare credentials
originalFilePath: integrations/builtin/credentials/cloudflare.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cloudflare'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cloudflare'
layout:
  description:
    visible: false
---

# Cloudflare credentials <a href="#cloudflare-credentials" id="cloudflare-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Cloudflare node](../app-nodes/n8n-nodes-base.cloudflare.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cloudflare account](https://developers.cloudflare.com/fundamentals/setup/account/)。
- [添加一个 domain](https://developers.cloudflare.com/fundamentals/setup/manage-domains/add-site/)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cloudflare 的 API 文档](https://developers.cloudflare.com/fundamentals/api/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **API token**：按照 [Cloudflare 文档创建 API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)。
