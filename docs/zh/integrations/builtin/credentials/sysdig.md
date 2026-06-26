---
title: Sysdig credentials
description: >-
  Sysdig credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Sysdig 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Sysdig credentials
originalFilePath: integrations/builtin/credentials/sysdig.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/sysdig'
url: 'https://docs.n8n.io/integrations/builtin/credentials/sysdig'
layout:
  description:
    visible: false
---

# Sysdig Management credentials <a href="#sysdig-management-credentials" id="sysdig-management-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Sysdig](https://sysdig.com) 账号，或配置一个 local instance。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access Key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Sysdig's documentation](https://docs.sysdig.com/en/docs/developer-tools/sysdig-api/)。

这是一个仅用于 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。

## 使用 API access key <a href="#using-api-access-key" id="using-api-access-key"></a>

要配置此 credential，你需要：

- 一个 **Access Key**

有关如何从 application 获取 Access Key 的说明，请参考 [Sysdig Agent Access Keys documentation](https://docs.sysdig.com/en/docs/administration/agent_access_key/)。
