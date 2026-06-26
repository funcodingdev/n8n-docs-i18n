---
title: OAuth 2.0 credentials 的 JWE token decryption
description: >-
  在 n8n 实例上启用 JWE-encrypted OAuth 2.0 tokens，让 identity provider 可以加密只有你的实例能解密的
  access 和 ID tokens。
contentType: howto
nodeTitle: Decrypt OAuth 2.0 tokens with JWE
originalFilePath: hosting/securing/oauth2-jwe-token-decryption.md
originalUrl: 'https://docs.n8n.io/hosting/securing/oauth2-jwe-token-decryption'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe
layout:
  description:
    visible: false
---

# OAuth 2.0 credentials 的 JWE token decryption <a href="#jwe-token-decryption-for-oauth-20-credentials" id="jwe-token-decryption-for-oauth-20-credentials"></a>

{% hint style="info" %}
**功能可用性**

* 从 n8n v2.21.0 起可用。
* 任何将 `N8N_ENV_FEAT_OAUTH2_JWE` 环境变量设为 `true` 的 n8n instance 都可使用。Self-hosted instances 可以直接设置。Cloud 上请联系 n8n support 申请启用。
* 需要支持将 tokens 加密为 JWE 的 identity provider (IdP)。
{% endhint %}

{% hint style="warning" %}
**预览功能**

JWE token decryption 处于 preview 阶段，并由环境 flag 控制。Field names、环境变量、JWKS endpoint path 和支持的 algorithms 在功能正式可用前可能会变化。请 pin 你的 n8n version，并在每次升级后重新测试 OAuth 2.0 credentials。
{% endhint %}

JWE token decryption 让你的 identity provider 能够返回加密为 [JWE](https://datatracker.ietf.org/doc/html/rfc7516) 的 OAuth 2.0 access 和 ID tokens。你的 n8n instance 会在 OAuth callback 上使用永不离开实例的 private key 解密 tokens。这可以保护 token contents，使其不被位于 IdP 和 n8n 之间的任何东西看到，包括 reverse proxies、browsers 和 logs。

## JWE token decryption 如何工作 <a href="#how-jwe-token-decryption-works" id="how-jwe-token-decryption-works"></a>

启用此功能后，n8n 会：

1. 启动时生成 RSA key pair，并用你的 instance encryption key 加密 private key 后存储在 database 中。
2. 在 instance-wide JWKS endpoint 发布匹配的 public key，让你的 IdP 可以获取它。
3. 在 OAuth callback 上使用与 JWE header 中 `kid` 匹配的 private key 解密 incoming JWE tokens。

IdP 会使用它从你的 JWKS endpoint 获取的 public key 加密每个 token。只有你的实例可以解密结果。

## 开始之前 <a href="#before-you-begin" id="before-you-begin"></a>

你需要：

* 在 n8n instance 上设置 `N8N_ENV_FEAT_OAUTH2_JWE=true`。Self-hosted instances 可以直接启用。Cloud 上请联系 n8n support 申请启用。
* 所有 n8n instances、main 和 workers 都共享相同的 `N8N_ENCRYPTION_KEY` 值。n8n 使用此 instance key 加密静态存储的 JWE private key。
* 支持使用 `RSA-OAEP-256` key encryption algorithm 的 JWE-encrypted tokens 的 IdP。

## 启用 JWE token decryption <a href="#enable-jwe-token-decryption" id="enable-jwe-token-decryption"></a>

1. 在**所有** n8n instances（main 和 workers）上设置以下环境变量：

    ```sh
    N8N_ENV_FEAT_OAUTH2_JWE=true
    ```

2. 重启所有 instances。启动时，n8n 会生成 RSA key pair，并在 JWKS endpoint 发布 public key。
3. 要确认功能已启用，请请求 JWKS endpoint，并检查其返回一个带有 `"alg": "RSA-OAEP-256"` 的 key：

    ```sh
    curl https://<your-n8n-host>/rest/.well-known/jwks.json
    ```

## 配置 identity provider <a href="#configure-your-identity-provider" id="configure-your-identity-provider"></a>

在 IdP 的 OAuth 2.0 client 或 application configuration 中：

1. 为 n8n 连接的 client 启用 encrypted tokens。
2. 将 client 的 JWKS URI 设置为你的 instance 的 JWKS endpoint。n8n 会在 credential 上显示此 URL，因此创建 credential 后可以直接从那里复制（见下一节）。
3. 选择 `RSA-OAEP-256` 作为 key encryption algorithm（`alg`）。将其与 IdP 支持的任意 content encryption algorithm（`enc`）配对，例如 `A128CBC-HS256` 或 `A256GCM`。

<details>

<summary>示例：Okta</summary>

1. 在 Okta admin console 中，打开 n8n 使用的 OAuth 2.0 application，或创建新的 web application。
2. 在 application 的 OpenID Connect settings 下启用 token encryption。
3. 将 **Key management algorithm** 设为 `RSA-OAEP-256`，并选择 content encryption algorithm（例如 `A256GCM`）。
4. 将 **JWKS URI** 设为 n8n 在 credential 的 **JWKS URI** field 中显示的值。

</details>

## 在 n8n 中配置 credential <a href="#configure-the-credential-in-n8n" id="configure-the-credential-in-n8n"></a>

1. 创建或编辑 [OAuth 2.0 API credential](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/httprequest#using-oauth2)。
2. 打开 **Encrypted Tokens (JWE)**。
3. 从 **JWKS URI** field 复制值，并将其粘贴到 IdP 的 JWKS URI 设置中（如果尚未这样做）。
4. 保存 credential 并连接。n8n 会解密 IdP 返回的 token，并存储解密后的形式供 workflows 使用。

来自 IdP 的 response 必须包含至少一个 JWE-encrypted token（access token、ID token 或两者）。如果 response 完全是 plaintext，n8n 会拒绝它，并报错 `Expected at least one JWE-encrypted token but received only plaintext`。

## JWKS endpoint 参考 <a href="#jwks-endpoint-reference" id="jwks-endpoint-reference"></a>

n8n 会在以下位置暴露 instance 的 public encryption keys：

```
<instance-base-url>/<rest-endpoint>/.well-known/jwks.json
```

| Property | Value |
| :------- | :---- |
| Default path | `/rest/.well-known/jwks.json` |
| Authentication | None（按设计公开可访问） |
| Rate limit | 每 IP 每分钟 `N8N_OAUTH_JWE_JWKS_PER_MINUTE` 次请求（默认 `60`） |
| Cache headers | `Cache-Control: public, max-age=3600, must-revalidate` |
| Response format | [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517#section-5)（RFC 7517 §5） |

如果你自定义了 `N8N_ENDPOINT_REST`，请在 path 中用你的值替换 `rest`。

## 支持的 algorithms <a href="#supported-algorithms" id="supported-algorithms"></a>

n8n 支持 `RSA-OAEP-256` 作为 key encryption。请配置 IdP 在加密 tokens 时使用此 `alg` 值。n8n 不限制 content encryption algorithms（`enc`）；可使用 IdP 支持的任意值。

JWKS schema 保留 elliptic-curve algorithms（`ECDH-ES` 及其 variants），但 n8n 尚未生成 EC keys。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

* **Credential 上没有出现 Encrypted Tokens (JWE) toggle。** 确认已在每个 n8n instance 上设置 `N8N_ENV_FEAT_OAUTH2_JWE=true`，且已重启所有 instances。
* **错误 `Expected at least one JWE-encrypted token but received only plaintext`。** IdP 返回了 plaintext token。确认你已为 IdP 中的 client 启用 token encryption，且 IdP 已从你的 JWKS endpoint 获取 key。
* **IdP 无法获取 JWKS URI。** 检查 IdP 是否可以访问 JWKS endpoint。Reverse proxies 和 authentication middleware 有时会阻止 `/rest/.well-known/jwks.json`。该 endpoint 必须可公开访问且无需 authentication。
* **IdP 过于频繁地获取 JWKS 并触发 rate limit。** 在 n8n instances 上增加 `N8N_OAUTH_JWE_JWKS_PER_MINUTE`，或配置 IdP 在完整 `max-age` window 内缓存 JWKS response。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [HTTP Request credentials: Using OAuth2](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/httprequest#using-oauth2)：设置通用 OAuth 2.0 credential。
* [Deployment environment variables](../basic-configuration/use-environment-variables/deployment.md)：`N8N_ENV_FEAT_OAUTH2_JWE` 和 `N8N_OAUTH_JWE_JWKS_PER_MINUTE` 参考。
* [Encryption key rotation](rotate-encryption-keys.md)：轮换保护静态 JWE private key 的 data encryption key。
* [JSON Web Encryption (RFC 7516)](https://datatracker.ietf.org/doc/html/rfc7516)：JWE specification。
