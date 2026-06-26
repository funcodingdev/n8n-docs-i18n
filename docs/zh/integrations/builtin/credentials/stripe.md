---
title: Stripe credentials
description: >-
  Stripe credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Stripe 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Stripe credentials
originalFilePath: integrations/builtin/credentials/stripe.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/stripe'
url: 'https://docs.n8n.io/integrations/builtin/credentials/stripe'
layout:
  description:
    visible: false
---

# Stripe credentials <a href="#stripe-credentials" id="stripe-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Stripe Trigger](../trigger-nodes/n8n-nodes-base.stripetrigger.md)
- [Stripe](../app-nodes/n8n-nodes-base.stripe.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Secret key

你还需要 Stripe **Signature Secret** 或 endpoint secret，这是每个 webhook endpoint 的唯一 key，用于验证传入请求，确保它们确实来自 Stripe。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要配置此 credential，你需要一个 Stripe admin 或 developer account。有关该服务的更多信息，请参考 [Stripe's API documentation](https://docs.stripe.com/api)。

生成 API key 前，请决定是在 live mode 还是 test mode 中生成。有关这两种模式的更多信息，请参考 [Test mode and live mode](#test-mode-and-live-mode)。

### Live mode Secret key <a href="#live-mode-secret-key" id="live-mode-secret-key"></a>

要在 live mode 中生成 Secret key：

1. 打开 [Stripe developer dashboard](https://dashboard.stripe.com/developers)，并选择 [**API Keys**](https://dashboard.stripe.com/apikeys)。
2. 在 **Standard Keys** 部分，选择 **Create secret key**。
3. 输入 **Key name**，例如 `n8n integration`。
4. 选择 **Create**。新的 API key 会显示出来。
4. 复制 key，并在你的 n8n credential 中将其输入为 **Secret Key**。

更多信息请参考 Stripe 的 [Create a secret API key](https://docs.stripe.com/keys#create-api-secret-key)。

### Test mode Secret key <a href="#test-mode-secret-key" id="test-mode-secret-key"></a>

要在 test mode 中使用 Secret key，你必须复制现有 key：

1. 前往你的 [Stripe test mode developer dashboard](https://dashboard.stripe.com/test/developers)，并选择 [**API Keys**](https://dashboard.stripe.com/test/apikeys)。
2. 在 **Standard Keys** 部分，为 **Secret key** 选择 **Reveal test key**。
3. 复制 key，并在你的 n8n credential 中将其输入为 **Secret Key**。

更多信息请参考 Stripe 的 [Create a secret API key](https://docs.stripe.com/keys#create-api-secret-key)。

## Test mode and live mode <a href="#test-mode-and-live-mode" id="test-mode-and-live-mode"></a>

所有 Stripe API requests 都发生在 [test mode](https://docs.stripe.com/test-mode) 或 live mode 中。每种模式都有自己的 API key。

使用 test mode 访问模拟测试数据，使用 live mode 访问真实 account 数据。某个模式中的 objects 无法被另一个模式访问。

有关每种模式中可用内容以及何时使用它们的指导，请参考 [API keys | Test mode versus live mode](https://docs.stripe.com/keys#test-live-modes)。

{% hint style="info" %}
**两种模式的 n8n credentials**

如果你想同时使用 live mode 和 test mode keys，请将每种模式的 key 分别存储在单独的 n8n credential 中。
{% endhint %}

## Key prefixes <a href="#key-prefixes" id="key-prefixes"></a>

Stripe 的 Secret keys 始终以 `sk_` 开头：

- Live keys 以 `sk_live_` 开头。
- Test keys 以 `sk_test_` 开头。

n8n 尚未测试这些 credentials 与 Restricted keys（前缀为 `rk_`）配合使用。

{% hint style="warning" %}
**Publishable keys**

不要在你的 n8n credential 中使用 Publishable keys（前缀为 `pk_`）。
{% endhint %}
