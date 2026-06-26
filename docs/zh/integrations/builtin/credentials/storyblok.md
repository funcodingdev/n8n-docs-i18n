---
title: Storyblok credentials
description: >-
  Storyblok credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Storyblok 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Storyblok credentials
originalFilePath: integrations/builtin/credentials/storyblok.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/storyblok'
url: 'https://docs.n8n.io/integrations/builtin/credentials/storyblok'
layout:
  description:
    visible: false
---

# Storyblok credentials <a href="#storyblok-credentials" id="storyblok-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Storyblok](../app-nodes/n8n-nodes-base.storyblok.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Storyblok](https://www.storyblok.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Content API key：用于 read-only access
- Management API key：用于完整 CRUD operations

{% hint style="info" %}
**Content API support**

n8n 仅支持 Content API v1。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些服务的更多信息，请参考 Storyblok 的 [Content v1 API documentation](https://www.storyblok.com/docs/api/content-delivery/v1) 和 [Management API documentation](https://www.storyblok.com/docs/api/management/getting-started/introduction)。

## 使用 Content API key <a href="#using-content-api-key" id="using-content-api-key"></a>

要配置此 credential，你需要：

- 一个 Content **API Key**：前往你的 Storyblok workspace 的 **Settings > Access Tokens** 获取 API key。选择 **Public** (`version=published`) 或 **Preview** (`version-published` 和 `version=draft`) 作为 **Access Level**。将此 access token 作为你的 **API Key** 输入。更详细的说明请参考 [How to retrieve and generate access tokens](https://www.storyblok.com/faq/retrieve-and-generate-access-tokens)。

有关每种 Access Level 支持的 operations 的更多信息，请参考 [Content v1 API Authentication](https://www.storyblok.com/docs/api/content-delivery/v1#topics/authentication)。

## 使用 Management API key <a href="#using-management-api-key" id="using-management-api-key"></a>

要配置此 credential，你需要：

- 一个 **Personal Access Token**：前往 [**My Account**](https://app.storyblok.com/#!/me/account) **> Personal access tokens** 生成新的 access token。将此 access token 作为你的 **Personal Access Token** 输入。
