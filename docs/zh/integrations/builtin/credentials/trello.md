---
title: Trello credentials
description: >-
  Trello credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Trello 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Trello credentials
originalFilePath: integrations/builtin/credentials/trello.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/trello'
url: 'https://docs.n8n.io/integrations/builtin/credentials/trello'
layout:
  description:
    visible: false
---

# Trello credentials <a href="#trello-credentials" id="trello-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Trello](../app-nodes/n8n-nodes-base.trello.md)
- [Trello Trigger](../trigger-nodes/n8n-nodes-base.trellotrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Trello's API documentation](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Trello](https://trello.com/) 账号，以及：

- 一个 **API Key**
- 一个 **API Token**

要同时生成 API Key 和 API Token，请创建一个 Trello Power-Up：

1. 打开 Trello [Power-Up Admin Portal](https://trello.com/power-ups/admin)。
2. 选择 **New**。
3. 为你的 Power-Up 输入 **Name**，例如 `n8n integration`。
4. 选择 Power-Up 应能访问的 **Workspace**。
5. 将 **iframe connector URL** 留空。
6. 输入适当的 contact information。
7. 选择 **Create**。
8. 这应该会打开 Power-Up 的 **API Key** 页面。（如果没有，请打开该页面。）
9. 选择 **Generate a new API Key**。
10. 从 Trello 复制 **API key**，并将其输入到你的 n8n credential。
11. 在你的 Trello API key 页面中，将你的 n8n base URL 输入为 **Allowed origin**。
12. 在 **Capabilities** 中，确保选择必要选项。
13. 选择 Trello **API Key** 旁边的 **Token** 链接。
14. 出现提示时，选择 **Allow** 以授予请求的所有 permissions。
15. 复制 Trello **Token**，并将其作为 n8n **API Token** 输入。

有关 API keys 和 tokens 的更多信息，请参考 Trello 的 [API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#api-introduction)。有关创建 Power-Ups 的更多信息，请参考 Trello 的 [Power-Up Admin Portal](https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-power-ups/#power-up-admin-portal)。
