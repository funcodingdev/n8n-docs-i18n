---
title: Quick Base credentials
description: >-
  Quick Base credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Quick Base 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Quick Base credentials
originalFilePath: integrations/builtin/credentials/quickbase.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/quickbase'
url: 'https://docs.n8n.io/integrations/builtin/credentials/quickbase'
layout:
  description:
    visible: false
---

# Quick Base credentials <a href="#quick-base-credentials" id="quick-base-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Quick Base](../app-nodes/n8n-nodes-base.quickbase.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Quick Base](https://www.quickbase.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Quick Base's API documentation](https://developer.quickbase.com/auth/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Hostname**：你的 Quick Base URL 中位于 `https://` 和 `/db` 之间的字符串。
- 一个 **User Token**：要生成 token，请选择你的 **Profile > My preferences > My User Information > Manage my user tokens**。详细说明请参考 [Creating and using user tokens](https://helpv2.quickbase.com/hc/en-us/articles/4570374095124-Creating-and-using-user-tokens)。
