---
title: Harvest credentials
description: >-
  Harvest credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Harvest 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Harvest credentials
originalFilePath: integrations/builtin/credentials/harvest.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/harvest'
url: 'https://docs.n8n.io/integrations/builtin/credentials/harvest'
layout:
  description:
    visible: false
---

# Harvest credentials <a href="#harvest-credentials" id="harvest-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Harvest](../app-nodes/n8n-nodes-base.harvest.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Harvest](https://www.getharvest.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Harvest's API documentation](https://help.getharvest.com/api-v2/)。

## 使用 API Access Token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- Personal **Access Token**：创建 personal access token 的说明请参考 [Harvest Personal Access Token Authentication documentation](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#personal-access-tokens)。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从头配置 OAuth2，或想了解 OAuth web flow 中发生的更多细节，请参考 [Harvest OAuth2 documentation](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#oauth2-application) 中的说明来设置 OAuth。
