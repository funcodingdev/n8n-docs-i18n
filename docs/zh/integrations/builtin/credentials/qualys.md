---
title: Qualys credentials
description: >-
  Qualys credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Qualys 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Qualys credentials
originalFilePath: integrations/builtin/credentials/qualys.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/qualys'
url: 'https://docs.n8n.io/integrations/builtin/credentials/qualys'
layout:
  description:
    visible: false
---

# Qualys credentials <a href="#qualys-credentials" id="qualys-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Qualys](https://www.qualys.com/) user account，user role 可以是 Contact 以外的任意角色。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Qualys's documentation](https://qualysguard.qg2.apps.qualys.com/qwebhelp/fo_portal/api_doc/index.htm)。

这是一个 credential-only node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/qualys/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **Username**
- 一个 **Password**
- 一个 **Requested With** string：输入 user description，例如 user agent，或保留默认值 `n8n application`。这会设置必需的 `X-Requested-With` header。
