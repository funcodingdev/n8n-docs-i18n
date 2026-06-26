---
title: uProc credentials
description: >-
  uProc credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 uProc 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: uProc credentials
originalFilePath: integrations/builtin/credentials/uproc.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/uproc'
url: 'https://docs.n8n.io/integrations/builtin/credentials/uproc'
layout:
  description:
    visible: false
---

# uProc credentials <a href="#uproc-credentials" id="uproc-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [uProc](../app-nodes/n8n-nodes-base.uproc.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [uProc](https://uproc.io) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [uProc's API documentation](https://docs.uproc.io/api/)。

## 使用 API Key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Email** address：输入用于登录 uProc 的 email address。它也显示在 **Settings > Integrations > API Credentials** 中。
- 一个 **API Key**：前往 **Settings > Integrations > API Credentials**。从 **API Credentials** 部分复制 **API Key (real)**，并将其输入到你的 n8n credential。
