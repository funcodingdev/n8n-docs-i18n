---
title: SecurityScorecard credentials
description: >-
  SecurityScorecard credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SecurityScorecard 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: SecurityScorecard credentials
originalFilePath: integrations/builtin/credentials/securityscorecard.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/securityscorecard'
url: 'https://docs.n8n.io/integrations/builtin/credentials/securityscorecard'
layout:
  description:
    visible: false
---

# SecurityScorecard credentials <a href="#securityscorecard-credentials" id="securityscorecard-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SecurityScorecard](../app-nodes/n8n-nodes-base.securityscorecard.md)


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SecurityScorecard](https://securityscorecard.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SecurityScorecard's Developer documentation](https://securityscorecard.readme.io/docs/integrate-ratings-platform-services) 和 [API documentation](https://securityscorecard.readme.io/reference/introduction)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：通过以下两种方式之一生成 API key：
    * 作为用户在 [**My Settings > API**](https://platform.securityscorecard.io/#/my-settings/api) 中生成。更多信息请参考 [Get an API key](https://securityscorecard.readme.io/docs/getting-started#step-1-get-an-api-key)。
    * 作为 bot user：查看 bot user 并选择 **create token**。更多信息请参考 [Authenticate with a bot user](https://securityscorecard.readme.io/docs/authentication#)。
