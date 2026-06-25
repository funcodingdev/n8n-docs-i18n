---
title: Invoice Ninja credentials
description: >-
  Invoice Ninja credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Invoice Ninja 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Invoice Ninja credentials
originalFilePath: integrations/builtin/credentials/invoiceninja.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/invoiceninja'
url: 'https://docs.n8n.io/integrations/builtin/credentials/invoiceninja'
layout:
  description:
    visible: false
---

# Invoice Ninja credentials <a href="#invoice-ninja-credentials" id="invoice-ninja-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Invoice Ninja](../app-nodes/n8n-nodes-base.invoiceninja.md)
- [Invoice Ninja Trigger](../trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Invoice Ninja](https://www.invoiceninja.com/) 账号。只有 Pro 和 Enterprise plans 支持 API integrations。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 APIs 的更多信息，请参考 Invoice Ninja 的 [v4 API documentation](https://invoice-ninja.readthedocs.io/en/latest/api.html) 和 [v5 API documentation](https://api-docs.invoicing.co/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **URL**：如果 Invoice Ninja 托管你的 installation，请使用提到的默认 URLs 之一。如果你是自托管 installation，请使用你的 Invoice Ninja instance URL。
- **API Token**：在 **Settings > Account Management > API Tokens** 中生成 API token。
- 可选的 **Secret**，仅适用于 v5 API users
