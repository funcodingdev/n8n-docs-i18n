---
title: Beeminder credentials
description: >-
  Beeminder credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Beeminder。
contentType:
  - integration
  - reference
nodeTitle: Beeminder credentials
originalFilePath: integrations/builtin/credentials/beeminder.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/beeminder'
url: 'https://docs.n8n.io/integrations/builtin/credentials/beeminder'
layout:
  description:
    visible: false
---

# Beeminder credentials <a href="#beeminder-credentials" id="beeminder-credentials"></a>

你可以使用这些 credentials 验证以下 node：

- [Beeminder](../app-nodes/n8n-nodes-base.beeminder.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Beeminder](https://www.beeminder.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API user token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Beeminder 的 API 文档](https://api.beeminder.com/#beeminder-api-reference)。

## 使用 API user token <a href="#using-api-user-token" id="using-api-user-token"></a>

要配置此 credential，你需要：

- **User** name：应与生成 Auth Token 的用户匹配。
- 该用户的个人 **Auth Token**。可使用以下任一方法生成：
    - 在 GUI 中：从 **Account Settings** 内的 [Apps & API](https://help.beeminder.com/article/110-apps-and-api#API-token) 选项获取
    - 在 API 中：通过调用 [`auth_token` API endpoint](https://api.beeminder.com/#auth) 获取
