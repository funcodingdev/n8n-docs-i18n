---
title: Trellix ePO credentials
description: >-
  Trellix ePO credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Trellix ePO 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Trellix ePO credentials
originalFilePath: integrations/builtin/credentials/trellixepo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/trellixepo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/trellixepo'
layout:
  description:
    visible: false
---

# Trellix ePO credentials <a href="#trellix-epo-credentials" id="trellix-epo-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Trellix ePolicy Orchestrator](https://www.trellix.com/products/epo/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Trellix ePO's documentation](https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-D87A6839-AED2-47B0-BE93-5BF83F710278.html)。

这是一个仅用于 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看 [example workflows and related content](https://n8n.io/integrations/trellix-epo/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个用于连接的 **Username**。
- 该 user account 的 **Password**。

n8n 使用这些字段以 `-u username:pw` 格式构建 `-u` 参数。更多信息请参考 [Web API basics](https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-2503B69D-2BCE-4491-9969-041838B39C1F.html)。
