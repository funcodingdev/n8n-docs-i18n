---
title: Plivo credentials
description: >-
  Plivo credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Plivo 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Plivo credentials
originalFilePath: integrations/builtin/credentials/plivo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/plivo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/plivo'
layout:
  description:
    visible: false
---

# Plivo credentials <a href="#plivo-credentials" id="plivo-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Plivo](../app-nodes/n8n-nodes-base.plivo.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Plivo](https://www.plivo.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Plivo's API documentation](https://www.plivo.com/docs/voice/api/overview/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **Auth ID**：作用类似 username。从 Plivo [console](https://console.plivo.com/dashboard/) 的 **Overview** page 复制你的 Auth ID。
- 一个 **Auth Token**：作用类似 password。从 Plivo [console](https://console.plivo.com/dashboard/) 的 **Overview** page 复制你的 Auth Token。

更详细的说明请参考 [How can I change my Auth ID or Auth Token?](https://support.plivo.com/hc/en-us/articles/360041731231-How-can-I-change-my-Auth-ID-or-Auth-Token)。
