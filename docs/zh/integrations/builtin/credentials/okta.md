---
title: Okta credentials
description: >-
  Okta credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Okta 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Okta credentials
originalFilePath: integrations/builtin/credentials/okta.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/okta'
url: 'https://docs.n8n.io/integrations/builtin/credentials/okta'
layout:
  description:
    visible: false
---

# Okta credentials <a href="#okta-credentials" id="okta-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Okta](../app-nodes/n8n-nodes-base.okta.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Okta free trial](https://www.okta.com/free-trial/)，或在已有 Okta org 上创建一个 admin account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- SSWS API Access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Okta's documentation](https://developer.okta.com/docs/reference/)。

## 使用 SSWS API access token <a href="#using-ssws-api-access-token" id="using-ssws-api-access-token"></a>

要配置此 credential，你需要：

- **URL**：你的 Okta org 的 base URL，也称为你的唯一 subdomain。有两种快速获取方式：
    1. 在 Admin Console 中，选择你的 **Profile**，将鼠标悬停在 username 下方列出的 domain 上，然后选择 **Copy** icon。将其粘贴到 n8n 中，但务必在前面添加 `https://`。
    2. 复制 Admin Console URL 的 base URL，例如 `https://dev-123456-admin.okta.com`。将其粘贴到 n8n 中，并移除 `-admin`，例如：`https://dev-123456.okta.com`。
- 一个 **SSWS Access Token**：前往 **Security > API > Tokens > Create token** 创建 token。更多信息请参考 [Create Okta API tokens](https://help.okta.com/en-us/content/topics/security/api.htm?cshid=ext-create-api-token#create-okta-api-token)。
