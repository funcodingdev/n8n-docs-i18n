---
title: Rundeck credentials
description: >-
  Rundeck credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Rundeck 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Rundeck credentials
originalFilePath: integrations/builtin/credentials/rundeck.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/rundeck'
url: 'https://docs.n8n.io/integrations/builtin/credentials/rundeck'
layout:
  description:
    visible: false
---

# Rundeck credentials <a href="#rundeck-credentials" id="rundeck-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Rundeck](../app-nodes/n8n-nodes-base.rundeck.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Rundeck](https://www.rundeck.com/) server 上创建 user account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Rundeck's API documentation](https://docs.rundeck.com/docs/api/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 你的 **URL**：输入 Rundeck server 的 base URL，例如 `http://myserver:4440`。更多信息请参考 [URLs](https://docs.rundeck.com/docs/api/#urls)。
- 一个 user API **Token**：要生成 user API token，请前往你的 **Profile > User API Tokens**。更多信息请参考 [User API tokens](https://docs.rundeck.com/docs/manual/10-user.html#user-api-tokens)。
