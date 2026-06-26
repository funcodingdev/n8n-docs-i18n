---
title: Mist credentials
description: >-
  Mist credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mist 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Mist credentials
originalFilePath: integrations/builtin/credentials/mist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mist'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mist'
layout:
  description:
    visible: false
---

# Mist credentials <a href="#mist-credentials" id="mist-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mist](https://www.mist.com/) 账号和 organization。详细说明请参考 [Create a Mist account and Organization](https://www.mist.com/documentation/create-mist-org/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mist's documentation](https://www.mist.com/documentation/mist-api-introduction/)。如果你已登录 Mist account，请前往 [https://api.mist.com/api/v1/docs/Home](https://api.mist.com/api/v1/docs/Home) 查看完整 API documentation。

这是一个 credential-only node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/mist/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **API Token**：你可以使用 User API token 或 Org API token。有关生成 User API token 的说明，请参考 [How to generate a user API token](https://www.mist.com/documentation/using-postman/)。有关生成 Org API token 的说明，请参考 [Org API token](https://www.mist.com/documentation/org-api-token/)。
- 选择你所在的 **Region**。选项包括：
    - **Europe**：如果你的 cloud environment 位于任一 EMEA region，请选择此选项。
    - **Global**：如果你的 cloud environment 位于任一 global region，请选择此选项。
