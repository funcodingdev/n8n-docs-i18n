---
title: Help Scout credentials
description: >-
  Help Scout credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Help Scout 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Help Scout credentials
originalFilePath: integrations/builtin/credentials/helpscout.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/helpscout'
url: 'https://docs.n8n.io/integrations/builtin/credentials/helpscout'
layout:
  description:
    visible: false
---

# Help Scout credentials <a href="#help-scout-credentials" id="help-scout-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Help Scout](../app-nodes/n8n-nodes-base.helpscout.md)
- [Help Scout Trigger](../trigger-nodes/n8n-nodes-base.helpscouttrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Help Scout](https://www.helpscout.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Help Scout's API documentation](https://developer.helpscout.com/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从头配置 OAuth2，或想了解 OAuth web flow 中发生的更多细节，需要创建一个 Help Scout app。更多信息请参考 [Help Scout OAuth documentation](https://developer.helpscout.com/mailbox-api/overview/authentication/#oauth2-application) 中的说明。
