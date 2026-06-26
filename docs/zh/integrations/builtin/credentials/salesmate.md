---
title: Salesmate credentials
description: >-
  Salesmate credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Salesmate 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Salesmate credentials
originalFilePath: integrations/builtin/credentials/salesmate.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/salesmate'
url: 'https://docs.n8n.io/integrations/builtin/credentials/salesmate'
layout:
  description:
    visible: false
---

# Salesmate credentials <a href="#salesmate-credentials" id="salesmate-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Salesmate](../app-nodes/n8n-nodes-base.salesmate.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Salesmate](https://salesmate.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Salesmate's API documentation](https://apidocs.salesmate.io/?version=latest)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **Session Token**：即 **Access Key**。在 **My Account > Access Key** 中生成 access key。更多信息请参考 [Access Rights and Keys](https://apidocs.salesmate.io/?version=latest#ac8296ec-cb44-4937-a860-5ae032397ca0)。
- 一个 **URL**：你的 Salesmate domain name/base URL，例如 `n8n.salesmate.io`。
