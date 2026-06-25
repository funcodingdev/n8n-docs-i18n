---
title: Cisco Secure Endpoint credentials
description: >-
  Cisco Secure Endpoint credentials 文档。使用这些 credentials 在 n8n 这个
  workflow automation platform 中验证 Cisco Secure Endpoint。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Cisco Secure Endpoint credentials
originalFilePath: integrations/builtin/credentials/ciscosecureendpoint.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint'
layout:
  description:
    visible: false
---

# Cisco Secure Endpoint credentials <a href="#cisco-secure-endpoint-credentials" id="cisco-secure-endpoint-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cisco DevNet developer account](https://developer.cisco.com)。
- 访问一个 [Cisco Secure Endpoint license](https://www.cisco.com/site/us/en/products/security/endpoint-security/secure-endpoint/index.html)。

## 身份验证方法 <a href="#authentication-methods" id="authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cisco Secure Endpoint 的文档](https://developer.cisco.com/docs/secure-endpoint/introduction/)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/cisco-secure-endpoint/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- Cisco Secure Endpoint 的 **Region**。可选项包括：
    - Asia Pacific, Japan, and China
    - Europe
    - North America
- 一个 **Client ID**：注册 SecureX API Client 时提供
- 一个 **Client Secret**：注册 SecureX API Client 时提供

要获取 Client ID 和 Client Secret，你需要注册一个 SecureX API Client。有关详细说明，请参阅 [Cisco Secure Endpoint authentication 文档](https://developer.cisco.com/docs/secure-endpoint/authentication/#authentication)。在 n8n credential 中使用 SecureX **Client Password** 作为 **Client Secret**。
