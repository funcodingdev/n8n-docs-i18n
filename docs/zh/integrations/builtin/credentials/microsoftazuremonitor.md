---
title: Microsoft Azure Monitor credentials
description: >-
  Microsoft Azure Monitor credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Microsoft Azure Monitor 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Microsoft Azure Monitor credentials
originalFilePath: integrations/builtin/credentials/microsoftazuremonitor.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftazuremonitor'
url: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftazuremonitor'
layout:
  description:
    visible: false
---
# Microsoft Azure Monitor credentials <a href="#microsoft-azure-monitor-credentials" id="microsoft-azure-monitor-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 Microsoft Azure account 或 subscription
* 已在 Microsoft Entra ID 中注册 app

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Microsoft Azure Monitor's API documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/azure-monitor-rest-api-index)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要 Microsoft Azure account，并准备：

- **Client ID**
- **Client Secret**
- **Tenant ID**
- 你计划访问的 **Resource**

有关如何对该服务进行身份验证的更多信息，请参考 [Microsoft Azure Monitor's API documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api?tabs=rest#set-up-authentication)。
