---
title: Venafi TLS Protect Cloud credentials
description: >-
  Venafi TLS Protect Cloud credentials 文档。使用这些 credentials 在 n8n
  这个 workflow 自动化平台中对 Venafi TLS Protect Cloud 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Venafi TLS Protect Cloud credentials
originalFilePath: integrations/builtin/credentials/venafitlsprotectcloud.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud'
url: 'https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud'
layout:
  description:
    visible: false
---

# Venafi TLS Protect Cloud credentials <a href="#venafi-tls-protect-cloud-credentials" id="venafi-tls-protect-cloud-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Venafi TLS Protect Cloud node](../app-nodes/n8n-nodes-base.venafitlsprotectcloud.md)
* [Venafi TLS Protect Cloud Trigger node](../trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 Venafi [TLS Protect Cloud](https://venafi.com/tls-protect/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Venafi TLS Protect Cloud's API documentation](https://docs.venafi.cloud/api/vaas-rest-api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Region**：选择与你业务需求匹配的 region。如果你位于 European Union，请选择 **EU**。否则选择 **US**。
- 一个 **API Key**：前往你的 **avatar > Preferences > API Keys** 获取 API key。你也可以使用 VCert 获取 API key。更多信息请参考 [Obtaining an API Key](https://docs.venafi.cloud/api/obtaining-api-key/)。
