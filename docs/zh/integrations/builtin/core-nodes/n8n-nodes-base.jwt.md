---
title: JWT
description: >-
  n8n 中 JWT node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: JWT
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.jwt.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt'
layout:
  description:
    visible: false
---

# JWT <a href="#jwt" id="jwt"></a>

在 n8n workflow 中处理 JSON web token。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/jwt.md)找到该 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Decode
* Sign
* Verify

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

* **Credential to connect with**：选择或创建用于连接的 [JWT credential](../credentials/jwt.md)。
* **Token**：输入要 **Verify** 或 **Decode** 的 token。
* 如果选择 **Sign** 操作，还会有此参数：
    * **Use JSON to Build Payload**：开启后，该 node 会使用 JSON 构建 claims。这里的选择会影响 Payload Claims 部分显示的内容。

## Payload Claims <a href="#payload-claims" id="payload-claims"></a>

只有选择 **Sign** 操作时，该 node 才会显示 payload claims。你看到的内容取决于 **Use JSON to Build Payload** 的选择：

* 如果选择 **Use JSON to Build Payload**，此部分会显示 JSON editor，可用于构建 claims。
* 如果未选择 **Use JSON to Build Payload**，此部分会提示你 **Add Claim**。

你可以添加以下 claims。

### Audience <a href="#audience" id="audience"></a>

**Audience** 或 `aud` claim 标识 JWT 的预期接收方。

更多信息请参阅 ["aud" (Audience) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)。

### Expires In <a href="#expires-in" id="expires-in"></a>

**Expires In** 或 `exp` claim 标识 JWT 过期并且不得再被接受处理的时间。

更多信息请参阅 ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。

### Issuer <a href="#issuer" id="issuer"></a>

**Issuer** 或 `iss` claim 标识签发 JWT 的主体。

更多信息请参阅 ["iss" (Issuer) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1)。

### JWT ID <a href="#jwt-id" id="jwt-id"></a>

**JWT ID** 或 `jti` claim 为 JWT 提供唯一标识符。

更多信息请参阅 ["jti" (JWT ID) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7)。

### Not Before <a href="#not-before" id="not-before"></a>

**Not Before** 或 `nbf` claim 标识 JWT 在此时间之前不得被接受处理。

更多信息请参阅 ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)。

### Subject <a href="#subject" id="subject"></a>

**Subject** 或 `sub` claim 标识 JWT 的 subject 主体。

更多信息请参阅 ["sub" (Subject) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.2)。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Decode node 选项 <a href="#decode-node-options" id="decode-node-options"></a>

**Return Additional Info** 开关控制该 node 返回的信息量。

开启后，该 node 会返回完整的 decoded token，其中包含 header 和 signature 信息。关闭后，该 node 只返回 payload。

### Sign node 选项 <a href="#sign-node-options" id="sign-node-options"></a>

使用 **Override Algorithm** 控制项选择用于验证 token 的算法。此算法会覆盖 credentials 中选择的算法。

### Verify node 选项 <a href="#verify-node-options" id="verify-node-options"></a>

此操作包含多个 node 选项：

* **Return Additional Info**：此开关控制该 node 返回的信息量。开启后，该 node 会返回完整的 decoded token，其中包含 header 和 signature 信息。关闭后，该 node 只返回 payload。
* **Ignore Expiration**：此开关控制该 node 是否应忽略 token 的过期时间 claim（`exp`）。更多信息请参阅 ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。
* **Ignore Not Before Claim**：此开关控制是否忽略 token 的 not before claim（`nbf`）。更多信息请参阅 ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)。
* **Clock Tolerance**：输入检查 `nbf` 和 `exp` claim 时可容忍的秒数。这可以帮助你处理不同服务器之间的小幅时钟差异。更多信息请参阅 ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。
* **Override Algorithm**：用于验证 token 的算法。此算法会覆盖 credentials 中选择的算法。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 JWT 集成模板](https://n8n.io/integrations/jwt)或[搜索所有模板](https://n8n.io/workflows/)
