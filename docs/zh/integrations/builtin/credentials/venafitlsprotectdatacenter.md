---
title: Venafi TLS Protect Datacenter credentials
description: >-
  Venafi TLS Protect Datacenter credentials 文档。使用这些 credentials 在
  n8n 这个 workflow 自动化平台中对 Venafi TLS Protect Datacenter 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Venafi TLS Protect Datacenter credentials
originalFilePath: integrations/builtin/credentials/venafitlsprotectdatacenter.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter
url: >-
  https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter
layout:
  description:
    visible: false
---

# Venafi TLS Protect Datacenter credentials <a href="#venafi-tls-protect-datacenter-credentials" id="venafi-tls-protect-datacenter-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Venafi TLS Protect Datacenter node](../app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 Venafi [TLS Protect Datacenter](https://venafi.com/) 账号。
- 设置 tokens 的 expiration 和 refresh time。更多信息请参考 [Setting up token authentication](https://docs.venafi.com/Docs/current/TopNav/Content/SDK/AuthSDK/t-SDKa-Setup-OAuth.php)。
- 在 **API > Integrations** 中创建一个 [API integration](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/c-APIAppIntegrations-about.php)。详细说明请参考 [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php)。
    - 记下 integration 的 Client ID。
    - 选择在 n8n 中执行所需 operations 需要的 scopes。有关可用 scopes 的更多细节，请参考 [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php) 中的 scopes table。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API integration

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Venafi's API integration documentation](https://docs.venafi.com/Docs/currentSDK/TopNav/Content/SDK/WebSDK/c-sdk-AboutThisGuide.php)。

## 使用 API integration <a href="#using-api-integration" id="using-api-integration"></a>

要配置此 credential，你需要：

- 一个 **Domain**：输入你的 Venafi TLS Protect Datacenter domain。
- 一个 **Client ID**：输入来自你的 API integration 的 **Client ID**。有关创建 API integration 的更多信息，请参考 [前提条件](#prerequisites) 中的信息和链接。
- 一个 **Username**：输入你的 username。
- 一个 **Password**：输入你的 password。
- **Allow Self-Signed Certificates**：如果打开，此 credential 将允许 self-signed certificates。
