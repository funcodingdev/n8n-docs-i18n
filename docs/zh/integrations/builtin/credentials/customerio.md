---
title: Customer.io credentials
description: >-
  Customer.io credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Customer.io。
contentType:
  - integration
  - reference
nodeTitle: Customer.io credentials
originalFilePath: integrations/builtin/credentials/customerio.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/customerio'
url: 'https://docs.n8n.io/integrations/builtin/credentials/customerio'
layout:
  description:
    visible: false
---

# Customer.io credentials <a href="#customerio-credentials" id="customerio-credentials"></a>

你可以使用这些 credentials 通过 Customer.io 验证以下 nodes。

- [Customer.io](../app-nodes/n8n-nodes-base.customerio.md)
- [Customer.io Trigger](../trigger-nodes/n8n-nodes-base.customeriotrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Customer.io](https://customer.io/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API Key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Customer.io summary API 文档](https://customer.io/docs/api/?api=journeys)。

有关每个 API 的详细 API reference 文档，请参阅 [Track API 文档](https://customer.io/docs/api/track/) 和 [App API 文档](https://customer.io/docs/api/app/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Tracking API Key**：用于 `https://track.customer.io/api/v1/` 的 [Track API](https://customer.io/docs/api/track/)。更多细节请参阅下面的 FAQs。
- 你的 **Region**：Customer.io 会根据你选择的 region 使用不同的 API subdomains。选项包括：
    - **Global region**：保留两个 APIs 的默认 URLs；用于所有非 EU 国家/地区。
    - **EU region**：将 Track API subdomain 调整为 `track-eu`，将 App API subdomain 调整为 `api-eu`；仅当你在 EU 时使用。
- 一个 **Tracking Site ID**：与你的 **Tracking API Key** 搭配使用时必需
- 一个 **App API Key**：用于 `https://api.customer.io/v1/api/` 的 [App API](https://customer.io/docs/api/app/)。更多细节请参阅下面的 FAQs。

有关创建 Tracking API 和 App API keys 的说明，请参阅 [Customer.io Finding and managing your API credentials 文档](https://customer.io/docs/accounts-and-workspaces/managing-credentials/)。

## 为什么需要 Tracking API Key 和 App API Key <a href="#why-you-need-a-tracking-api-key-and-an-app-api-key" id="why-you-need-a-tracking-api-key-and-an-app-api-key"></a>

Customer.io 有两个不同的 API endpoints，并且每个 endpoint 的 keys 生成和存储方式略有不同：

- [Track API](https://customer.io/docs/api/track/) 位于 `https://track.customer.io/api/v1/`
- [App API](https://customer.io/docs/api/app/) 位于 `https://api.customer.io/v1/api/`

Track API 需要 Tracking Site ID；App API 不需要。

根据你想执行的 operation，n8n 会使用正确的 API key 及其对应 endpoint。
