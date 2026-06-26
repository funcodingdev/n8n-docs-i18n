---
title: SIGNL4 credentials
description: >-
  SIGNL4 credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SIGNL4 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: SIGNL4 credentials
originalFilePath: integrations/builtin/credentials/signl4.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/signl4'
url: 'https://docs.n8n.io/integrations/builtin/credentials/signl4'
layout:
  description:
    visible: false
---

# SIGNL4 credentials <a href="#signl4-credentials" id="signl4-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SIGNL4](../app-nodes/n8n-nodes-base.signl4.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SIGNL4](https://www.signl4.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Webhook secret

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SIGNL4's Inbound Webhook documentation](https://connect.signl4.com/webhook/docs/index.html)。

## 使用 webhook secret <a href="#using-webhook-secret" id="using-webhook-secret"></a>

要配置此 credential，你需要：

- 一个 **Team Secret**：SIGNL4 会在 "Sign up complete" 邮件中包含此 secret，它是 webhook URL 的最后一部分。如果你的 webhook URL 是 `https://connect.signl4.com/webhook/helloworld`，你的 team secret 就是 `helloworld`。
