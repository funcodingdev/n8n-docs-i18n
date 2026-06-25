---
title: Baserow credentials
description: >-
  Baserow credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Baserow。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Baserow credentials
originalFilePath: integrations/builtin/credentials/baserow.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/baserow'
url: 'https://docs.n8n.io/integrations/builtin/credentials/baserow'
layout:
  description:
    visible: false
---

# Baserow credentials <a href="#baserow-credentials" id="baserow-credentials"></a>

你可以使用这些 credentials 验证以下 node：

- [Baserow](../app-nodes/n8n-nodes-base.baserow.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在任意托管的 Baserow instance 或 self-hosted instance 上创建一个 [Baserow](https://baserow.io/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- Token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Baserow 的文档](https://baserow.io/docs/index)。

有关 API 的更多信息，请参阅 [Baserow 自动生成的 API 文档](https://baserow.io/api-docs)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 你的 Baserow **Host**
- 用于登录的 **Username** 和 **Password**

按照以下步骤操作：

1. 输入 Baserow instance 的 **Host**：
    - 对于 Baserow-hosted instance：保留为 `https://api.baserow.io`。
    - 对于 self-hosted instance：设置为你的 self-hosted instance API URL。
2. 输入 n8n 应使用的 user account 的 **Username**。
3. 输入该 user account 的 **Password**。

有关创建 user accounts 的信息，请参阅 [Baserow API Authentication 文档](https://baserow.io/docs/apis/rest-api#authentication)。

## 使用 token <a href="#using-a-token" id="using-a-token"></a>

要配置 database token credential，你需要：

- 你的 Baserow **Host**
- 在 Baserow.io 上创建的 **Database token**，这需要使用 **Username** 和 **Password** 登录。

### 创建 database token <a href="#creating-the-database-token" id="creating-the-database-token"></a>

1. 在 [Baserow](https://baserow.io/login) 中，使用你的 username 和 password 登录。
2. 点击左上角的 workspace，并选择 **My Settings**。
3. 在打开的屏幕中，点击 **Database tokens**。
4. 点击 **Create token**。
5. 输入 token 的 **Name** 和 **Workspace**。
6. 点击 **Create token** 完成。

要在 n8n 中创建 credential，请按照以下步骤操作：

1. 输入 Baserow instance 的 **Host**：
    - 对于 Baserow-hosted instance：保留为 `https://api.baserow.io`。
    - 对于 self-hosted instance：设置为你的 self-hosted instance API URL。
2. 输入你创建的 **Database Token**。
