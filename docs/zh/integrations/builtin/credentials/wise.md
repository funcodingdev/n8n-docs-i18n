---
title: Wise credentials
description: >-
  Wise credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Wise 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Wise credentials
originalFilePath: integrations/builtin/credentials/wise.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/wise'
url: 'https://docs.n8n.io/integrations/builtin/credentials/wise'
layout:
  description:
    visible: false
---

# Wise credentials <a href="#wise-credentials" id="wise-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Wise](../app-nodes/n8n-nodes-base.wise.md)
- [Wise Trigger](../trigger-nodes/n8n-nodes-base.wisetrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Wise](https://wise.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Wise's API documentation](https://docs.wise.com/api-docs/api-reference)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **API Token**：前往你的 **user menu > Settings > API tokens** 生成 API token。将生成的 API key 输入到你的 n8n credential。更多信息请参考 [Getting started with the API](https://wise.com/help/articles/2958107/getting-started-with-the-api)。
- 你的 **Environment**：选择最匹配 Wise account environment 的环境。
    - 如果你使用 Wise test sandbox account，请选择 **Test**。
    - 否则请选择 **Live**。
- **Private Key (Optional)**：对于需要 Strong Customer Authentication (SCA) 的 live endpoints，请生成 public 和 private key。将 private key 输入到这里。更多信息请参考 [添加 private key](#add-a-private-key)。
    - 如果你使用 **Test** environment，只有在 [public keys management page](https://sandbox.transferwise.tech/public-keys) 上启用了 Strong Customer Authentication 时，才需要输入 Private Key。

## 添加 private key <a href="#add-a-private-key" id="add-a-private-key"></a>

Wise 使用 Strong Customer Authentication (SCA) 保护部分 live endpoints 和 operations。细节请参考 [Strong Customer Authentication & 2FA](https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa)。

如果你向需要 SCA 的 endpoint 发出 request，Wise 会返回 403 Forbidden HTTP status code。返回的 error 类似如下：

> This request requires Strong Customer Authentication (SCA). Please add a key pair to your account and n8n credentials. See https://api-docs.transferwise.com/#strong-customer-authentication-personal-token

要使用需要 SCA 的 endpoints，请生成 RSA key pair，并将相关 key information 同时添加到 Wise 和 n8n：

1. 生成 RSA key pair：

    ```sh
    $ openssl genrsa -out private.pem 2048
    $ openssl rsa -pubout -in private.pem -out public.pem
    ```

2. 将 public key `public.pem` 的内容添加到 Wise 的 **user menu > Settings > API tokens > Manage public keys**。
3. 在 n8n 中，将 private key `private.pem` 的内容添加到 **Private Key (Optional)**。

更多信息请参考 [Personal Token SCA](https://docs.wise.com/api-docs/guides/strong-customer-authentication-2fa/personal-token-sca)。
