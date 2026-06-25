---
title: Fortinet FortiGate credentials
description: >-
  Fortinet FortiGate credentials 文档。使用这些 credentials 在 n8n 这个
  workflow automation platform 中验证 Fortinet FortiGate。
contentType:
  - integration
  - reference
nodeTitle: Fortinet FortiGate credentials
originalFilePath: integrations/builtin/credentials/fortigate.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/fortigate'
url: 'https://docs.n8n.io/integrations/builtin/credentials/fortigate'
layout:
  description:
    visible: false
---

# Fortinet FortiGate credentials <a href="#fortinet-fortigate-credentials" id="fortinet-fortigate-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Fortinet FortiGate](https://www.fortinet.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Fortinet FortiGate 的 API 文档](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/fortinet-fortigate/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 API **Access Token**：要生成 access token，请创建一个 [REST API administrator](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/399023/rest-api-administrator)。

有关 FortiGate 中 token-based authentication 的更多信息，请参阅 [Fortinet FortiGate Using APIs 文档](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis)。
