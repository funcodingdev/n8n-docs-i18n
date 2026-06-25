---
title: Action Network credentials
description: >-
  Action Network credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Action Network。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Action Network credentials
originalFilePath: integrations/builtin/credentials/actionnetwork.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/actionnetwork'
url: 'https://docs.n8n.io/integrations/builtin/credentials/actionnetwork'
layout:
  description:
    visible: false
---

# Action Network credentials <a href="#action-network-credentials" id="action-network-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Action Network](../app-nodes/n8n-nodes-base.actionnetwork.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [Action Network API 文档](https://actionnetwork.org/docs/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个已[启用 API key access](#request-api-access) 的 [Action Network](https://actionnetwork.org/) 账号，以及：

- **API Key**

获取 API key：

1. 登录你的 Action Network 账号。
2. 在 **Start Organizing** 菜单中，选择 **Details >** [**API & Sync**](https://actionnetwork.org/apis)。
3. 选择要为其生成 API key 的 list。
4. 为该 list 生成 API key。
5. 复制 **API Key** 并输入到你的 n8n credential 中。

更多信息请参阅 [Action Network API Authentication 说明](https://actionnetwork.org/docs/v2/#auth)。

## 请求 API access <a href="#request-api-access" id="request-api-access"></a>

Action Network 上的每个 user account 和 group 都有单独的 API key，用于访问该 user 或 group 的 data。

你必须明确向 Action Network 请求 API access，可以通过以下两种方式之一完成：

1. 如果你已经是付费客户，请[联系他们](https://actionnetwork.org/contact)请求 partner access。Partner access 包含 API key access。
2. 如果你是 developer，请[申请 developer account](https://actionnetwork.org/developers)。账号申请通过后，你将拥有 API key access。
