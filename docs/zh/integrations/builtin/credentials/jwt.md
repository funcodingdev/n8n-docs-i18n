---
title: JWT credentials
contentType:
  - integration
  - reference
priority: medium
nodeTitle: JWT credentials
originalFilePath: integrations/builtin/credentials/jwt.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jwt
url: https://docs.n8n.io/integrations/builtin/credentials/jwt
description: >-
  JWT credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对 JWT
  进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# JWT credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [JWT](../core-nodes/n8n-nodes-base.jwt.md)
* [Webhook](../core-nodes/n8n-nodes-base.webhook/)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Passphrase：使用 HMAC algorithm 和 secret 签名
* Private key (PEM key)：用于 [Private Key JWT](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authenticate-with-private-key-jwt)，支持 RSA 或 ECDSA algorithm

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多细节请参考 [JSON Web Token spec](https://datatracker.ietf.org/doc/html/rfc7519)。

如需更详细的介绍，请参考 [JWT website Introduction to JSON Web Tokens](https://jwt.io/introduction)。有关如何在两种类型以及相关 algorithms 之间选择的更多信息，请参考 [JSON Web Token (JWT) Signing Algorithms Overview](https://auth0.com/blog/json-web-token-signing-algorithms-overview/)。

## 使用 Passphrase <a href="#using-passphrase" id="using-passphrase"></a>

配置此 credential：

1. 选择 **Passphrase** 的 **Key Type**。
2. 输入 Passphrase **Secret**
3. 选择用于签名 assertion 的 **Algorithm**。支持的 algorithms 列表请参考下方[可用 algorithms](jwt.md#available-algorithms)。

## 使用 private key (PEM key) <a href="#using-private-key-pem-key" id="using-private-key-pem-key"></a>

配置此 credential：

1. 选择 **PEM Key** 的 **Key Type**。
2. **Private Key**：通过生成 Key Pair 获取。示例请参考 [Generate RSA Key Pair](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair)。
3. **Public Key**：通过生成 Key Pair 获取。示例请参考 [Generate RSA Key Pair](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair)。
4. 选择用于签名 assertion 的 **Algorithm**。支持的 algorithms 列表请参考下方[可用 algorithms](jwt.md#available-algorithms)。

## 可用 algorithms <a href="#available-algorithms" id="available-algorithms"></a>

此 n8n credential 支持以下 algorithms：

* `HS256`
* `HS384`
* `HS512`
* `RS256`
* `RS384`
* `RS512`
* `ES256`
* `ES384`
* `ES512`
* `PS256`
* `PS384`
* `PS512`
* `none`
