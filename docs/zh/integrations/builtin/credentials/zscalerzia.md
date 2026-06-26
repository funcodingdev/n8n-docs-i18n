---
title: Zscaler ZIA credentials
description: >-
  Zscaler ZIA credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zscaler ZIA 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Zscaler ZIA credentials
originalFilePath: integrations/builtin/credentials/zscalerzia.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zscalerzia'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zscalerzia'
layout:
  description:
    visible: false
---

# Zscaler ZIA credentials <a href="#zscaler-zia-credentials" id="zscaler-zia-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Zscaler Internet Access (ZIA)](https://www.zscaler.com/products/zscaler-internet-access) cloud instance 上创建一个 admin account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth and API key combo

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zscaler ZIA's documentation](https://help.zscaler.com/zia/getting-started-zia-api)。

这是一个仅用于 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看 [example workflows and related content](https://n8n.io/integrations/zscaler-zia/)。

## 使用 basic auth and API key combo <a href="#using-basic-auth-and-api-key-combo" id="using-basic-auth-and-api-key-combo"></a>

要配置此 credential，你需要：

- 一个 **Base URL**：输入你的 Zscaler ZIA cloud name 的 base URL。要获取 base URL，请登录 ZIA Admin Portal，并前往 **Administration > Cloud Service API Security**。base URL 会同时显示在 **Cloud Service API Key** tab 和 **OAuth 2.0 Authorization Servers** tab 中。
- 一个 **Username**：输入你的 ZIA admin username。
- 一个 **Password**：输入你的 ZIA admin password。
- 一个 **Api Key**：通过 **Administration > Cloud Service API Security > Cloud Service API Key** 创建 API key。

更详细的说明请参考 [About Cloud Service API Key](https://help.zscaler.com/zia/about-cloud-service-api-key)。
