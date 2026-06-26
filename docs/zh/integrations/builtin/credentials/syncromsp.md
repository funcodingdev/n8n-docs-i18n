---
title: SyncroMSP credentials
description: >-
  SyncroMSP credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SyncroMSP 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: SyncroMSP credentials
originalFilePath: integrations/builtin/credentials/syncromsp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/syncromsp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/syncromsp'
layout:
  description:
    visible: false
---

# SyncroMSP credentials <a href="#syncromsp-credentials" id="syncromsp-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SyncroMSP](../app-nodes/n8n-nodes-base.syncromsp.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SyncroMSP](https://syncromsp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SyncroMSP's API documentation](https://api-docs.syncromsp.com/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：在 SyncroMSP 中称为 **API token**。要创建 API token，请前往你的 **user menu > Profile/Password > API Tokens**，并选择 **Create New Token** 选项。选择 **Custom Permissions**，输入 token 名称并调整 permissions 以匹配你的需求。
- 你的 **Subdomain**：输入你的 SyncroMSP subdomain。它显示在 SyncroMSP 的 URL 中，位于 `https://` 和 `.syncromsp.com` 之间。如果完整 URL 是 `https://n8n-instance.syncromsp.com`，则应输入 `n8n-instance` 作为 subdomain。

有关创建新 tokens 的更多信息，请参考 [API Tokens](https://docs.syncromsp.com/imported/api-tokens)。
