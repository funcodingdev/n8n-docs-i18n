---
title: Cisco Umbrella credentials
description: >-
  Cisco Umbrella credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Cisco Umbrella。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Cisco Umbrella credentials
originalFilePath: integrations/builtin/credentials/ciscoumbrella.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella'
layout:
  description:
    visible: false
---

# Cisco Umbrella credentials <a href="#cisco-umbrella-credentials" id="cisco-umbrella-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cisco DevNet developer account](https://developer.cisco.com)。
- 一个具备 **Full Admin** role 的 [Cisco Umbrella user account](https://umbrella.cisco.com/)。

## 身份验证方法 <a href="#authentication-methods" id="authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cisco Umbrella 的 API 文档](https://developer.cisco.com/docs/cloud-security/)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/cisco-umbrella/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**
- 一个 **Secret**：生成 API key 时提供

有关创建 Umbrella API key 的说明，请参阅 [Cisco Umbrella Manage API Keys 文档](https://developer.cisco.com/docs/cloud-security/authentication/#manage-api-keys)。
