---
title: WooCommerce credentials
description: >-
  WooCommerce credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 WooCommerce 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: WooCommerce credentials
originalFilePath: integrations/builtin/credentials/woocommerce.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/woocommerce'
url: 'https://docs.n8n.io/integrations/builtin/credentials/woocommerce'
layout:
  description:
    visible: false
---

# WooCommerce credentials <a href="#woocommerce-credentials" id="woocommerce-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [WooCommerce](../app-nodes/n8n-nodes-base.woocommerce.md)
- [WooCommerce Trigger](../trigger-nodes/n8n-nodes-base.woocommercetrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 在你的 WordPress website 上安装 [WooCommerce](https://woocommerce.com/) plugin。
- 在 WordPress 中，前往 **Settings > Permalinks**，并将 WordPress permalinks 设置为 **Plain** 以外的值。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [WooCommerce's REST API documentation](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Consumer Key**：生成 API key 时创建。
- 一个 **Consumer Secret**：生成 API key 时创建。
- 一个 **WooCommerce URL**

要生成 API key 并设置 credential：

1. 前往 **WooCommerce > Settings > Advanced > Rest API > Add key**。
2. 从 **Permissions** dropdown 中选择 **Read/Write**。
3. 复制生成的 **Consumer Key** 和 **Consumer Secret**，并将它们输入到你的 n8n credentials。
4. 将你的 WordPress site URL 输入为 **WooCommerce URL**。
5. 默认情况下，n8n 会在 Authorization header 中传递你的 credential details。如果你需要改为以 query string parameters 传递它们，请打开 **Include Credentials in Query**。

更多信息请参考 [Generate Keys](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/#3-generate-keys)。

## 解决 "Consumer key is missing" error <a href="#resolve-consumer-key-is-missing-error" id="resolve-consumer-key-is-missing-error"></a>

当你尝试连接 credentials 时，可能会收到这样的 error：`Consumer key is missing`。

当 server 在通过 SSL 进行身份验证时无法解析 Authorization header details，会发生此情况。

要解决此问题，请打开 **Include Credentials in Query** toggle，改为以 query string parameters 传递 consumer key/secret，然后重试 credential。
