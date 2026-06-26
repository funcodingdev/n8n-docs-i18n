---
title: Travis CI credentials
description: >-
  Travis CI credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Travis CI 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Travis CI credentials
originalFilePath: integrations/builtin/credentials/travisci.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/travisci'
url: 'https://docs.n8n.io/integrations/builtin/credentials/travisci'
layout:
  description:
    visible: false
---

# Travis CI credentials <a href="#travis-ci-credentials" id="travis-ci-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Travis CI](../app-nodes/n8n-nodes-base.travisci.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Travis CI](https://travis-ci.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Travis CI's API documentation](https://docs.travis-ci.com/user/developer/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **API Token**：从 **Account Settings >** [**API Token**](https://packagecloud.io/api_token) 获取 API token，或通过 Travis CI [command line client](https://github.com/travis-ci/travis.rb#installation) 生成。
