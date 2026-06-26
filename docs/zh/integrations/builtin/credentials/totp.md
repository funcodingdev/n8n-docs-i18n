---
title: TOTP credentials
description: >-
  TOTP credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 TOTP 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: TOTP credentials
originalFilePath: integrations/builtin/credentials/totp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/totp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/totp'
layout:
  description:
    visible: false
---

# TOTP credentials <a href="#totp-credentials" id="totp-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [TOTP](../core-nodes/n8n-nodes-base.totp.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

生成 TOTP **Secret** 和 **Label**。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Secret and label

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Time-based One-time Password (TOTP) 是一种使用当前时间生成 one-time password (OTP) 的算法。更多信息请参考 [Google Authenticator | Key URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format)。

## 使用 secret and label <a href="#using-secret-and-label" id="using-secret-and-label"></a>

要配置此 credential，你需要：

- 一个 **Secret**：authenticator setup 期间编码在 QR code 中的 secret key。它是以 Base32 编码的任意 key value，例如：`BVDRSBXQB2ZEL5HE`。更多信息请参考 [Google Authenticator Secret](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#secret)。
- 一个 **Label**：account 的标识符。它包含以 URI-encoded string 表示的 account name。你可以包含 prefixes，用于标识管理该 account 的 provider 或 service。如果使用 prefixes，请使用 literal 或 url-encoded colon 分隔 issuer prefix 和 account name，例如：`GitHub:john-doe`。更多信息请参考 [Google Authenticator Label](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#label)。
