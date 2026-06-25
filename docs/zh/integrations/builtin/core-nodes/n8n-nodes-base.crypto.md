---
title: Crypto
description: >-
  n8n 中 Crypto node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Crypto
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.crypto.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto'
layout:
  description:
    visible: false
---

# Crypto <a href="#crypto" id="crypto"></a>

使用 Crypto node 可以在 workflow 中执行加密相关操作。

{% hint style="info" %}
**Credentials**

你可以在[这里](/integrations/builtin/credentials/crypto.md)找到该 node 的身份验证信息。
{% endhint %}

## Action <a href="#actions" id="actions"></a>

* 使用口令或私钥[**Decrypt** 字符串](#decrypt-parameters)
* 使用口令或公钥[**Encrypt** 字符串](#encrypt-parameters)
* [**Generate** 随机字符串](#generate-parameters)
* 以指定格式[**Hash** 文本或文件](#hash-parameters)
* 以指定格式对文本或文件执行 [**Hmac**](#hmac-parameters)
* 使用私钥[**Sign** 字符串](#sign-parameters)

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

Node 参数取决于你选择的 action。

**Hmac**、**Sign**、**Encrypt** 和 **Decrypt** action 需要 [Crypto credentials](/integrations/builtin/credentials/crypto.md)。每个 action 会使用它需要的 credential 字段：

* **Hmac** 使用 **Hmac Secret**。
* **Sign** 使用 **Private Key**。
* **Encrypt** 和 **Decrypt** 在对称模式下使用 **Encryption Passphrase**，在非对称模式下使用 **Encryption Public Key** 和 **Encryption Private Key**。

### Decrypt 参数 <a href="#decrypt-parameters" id="decrypt-parameters"></a>

* **Mode**：选择要使用的模式。它必须与加密该值时使用的模式匹配。可选：
	* **Symmetric (Passphrase)**：使用口令和认证加密算法进行解密。
	* **Asymmetric (RSA)**：使用 RSA 私钥进行解密。
* **Cipher**：选择 **Symmetric (Passphrase)** 时，选择要使用的认证加密算法。它必须与加密该值时使用的 cipher 匹配。可选：
	* **AES-256-GCM**
	* **AES-192-GCM**
	* **AES-128-GCM**
	* **ChaCha20-Poly1305**
* **Value**：输入由 **Encrypt** action 生成的 base64 字符串。
* **Property Name**：输入要写入解密后值的属性名称。

### Encrypt 参数 <a href="#encrypt-parameters" id="encrypt-parameters"></a>

* **Mode**：选择要使用的模式。可选：
	* **Symmetric (Passphrase)**：使用口令和认证加密算法进行加密。
	* **Asymmetric (RSA)**：使用 RSA 公钥进行加密。
* **Cipher**：选择 **Symmetric (Passphrase)** 时，选择要使用的认证加密算法。解密该值时必须选择相同的 cipher。可选：
	* **AES-256-GCM**
	* **AES-192-GCM**
	* **AES-128-GCM**
	* **ChaCha20-Poly1305**
* **Value**：输入要加密的值。
* **Property Name**：输入要写入加密后值的属性名称。该 node 会将结果写为 base64 字符串。

{% hint style="info" %}
**RSA payload size**

Asymmetric (RSA) 模式只能加密较小的 payload，使用 2048-bit key 时大约为 190 bytes。较大的数据请使用对称模式。
{% endhint %}

### Generate 参数 <a href="#generate-parameters" id="generate-parameters"></a>

* **Property Name**：输入要写入随机字符串的属性名称。
* **Type**：选择用于生成字符串的编码类型。可选：
	* **ASCII**
	* **BASE64**
	* **HEX**
	* **UUID**
* **Length**：选择 **ASCII**、**BASE64** 或 **HEX** 时，输入生成字符串的长度。默认值为 `32`。

### Hash 参数 <a href="#hash-parameters" id="hash-parameters"></a>

* **Type**：选择要使用的 hash 类型。可选：
	* **MD5**
	* **SHA256**
	* **SHA3-256**
	* **SHA3-384**
	* **SHA3-512**
	* **SHA384**
	* **SHA512**
* **Binary File**：如果要 hash 的数据来自二进制文件，请开启此参数。
	* **Value**：如果关闭 **Binary File**，请输入要 hash 的值。
	* **Binary Property Name**：如果开启 **Binary File**，请输入包含要 hash 数据的二进制属性名称。
* **Property Name**：输入要写入 hash 的属性名称。
* **Encoding**：选择要使用的编码类型。可选：
	* **BASE64**
	* **HEX**

### Hmac 参数 <a href="#hmac-parameters" id="hmac-parameters"></a>

* **Binary File**：如果要创建 Hmac 的数据来自二进制文件，请开启此参数。
	* **Value**：如果关闭 **Binary File**，请输入要创建 Hmac 的值。
	* **Binary Property Name**：如果开启 **Binary File**，请输入包含要创建 Hmac 数据的二进制属性名称。
* **Type**：选择要使用的 hash 类型。可选：
	* **MD5**
	* **SHA256**
	* **SHA3-256**
	* **SHA3-384**
	* **SHA3-512**
	* **SHA384**
	* **SHA512**
* **Property Name**：输入要写入 Hmac 的属性名称。
* **Encoding**：选择要使用的编码类型。可选：
	* **BASE64**
	* **HEX**

此 action 使用你的 [Crypto credentials](/integrations/builtin/credentials/crypto.md) 中的 **Hmac Secret**。

### Sign 参数 <a href="#sign-parameters" id="sign-parameters"></a>

* **Value**：输入要签名的值。
* **Property Name**：输入要写入签名后值的属性名称。
* **Algorithm Name or ID**：从列表中选择算法名称，或使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
* **Encoding**：选择要使用的编码类型。可选：
	* **BASE64**
	* **HEX**

此 action 使用你的 [Crypto credentials](/integrations/builtin/credentials/crypto.md) 中的 **Private Key**。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Crypto 集成模板](https://n8n.io/integrations/crypto)或[搜索所有模板](https://n8n.io/workflows/)
