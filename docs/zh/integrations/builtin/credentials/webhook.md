---
title: Webhook credentials
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Webhook credentials
originalFilePath: integrations/builtin/credentials/webhook.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/webhook
url: https://docs.n8n.io/integrations/builtin/credentials/webhook
description: >-
  Webhook credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Webhook 进行身份验证。
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

# Webhook credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Webhook](../core-nodes/n8n-nodes-base.webhook/)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

你必须使用想要查询的 app 或 service 所要求的身份验证方式。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Basic auth
* Header auth
* JWT auth
* None

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/vIyn1XsEkjlolZzHTfTG/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fjWxEWe1g0CDvsx1igf6/" %}

## 使用 JWT auth <a href="#using-jwt-auth" id="using-jwt-auth"></a>

[**JWT Auth**](https://jwt.io/introduction/) 是一种使用 JSON Web Tokens (JWT) 对数据进行数字签名的身份验证方式。此身份验证方式使用 **JWT credential**，并可使用 **Passphrase** 或 **PEM Key** 作为 key type。更多信息请参考 [JWT credential](jwt.md)。
