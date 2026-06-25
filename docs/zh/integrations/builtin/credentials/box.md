---
title: Box credentials
description: >-
  Box credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Box。
contentType:
  - integration
  - reference
nodeTitle: Box credentials
originalFilePath: integrations/builtin/credentials/box.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/box'
url: 'https://docs.n8n.io/integrations/builtin/credentials/box'
layout:
  description:
    visible: false
---

# Box credentials <a href="#box-credentials" id="box-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Box](../app-nodes/n8n-nodes-base.box.md)
- [Box Trigger](../trigger-nodes/n8n-nodes-base.boxtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Box](https://www.box.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Box 的 API 文档](https://developer.box.com/reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零配置 OAuth2，或需要了解 OAuth web flow 中发生的细节，需要创建一个 Custom App。有关更多信息，请参阅 [Box OAuth2 Setup 文档](https://developer.box.com/guides/authentication/oauth2/oauth2-setup/)。
