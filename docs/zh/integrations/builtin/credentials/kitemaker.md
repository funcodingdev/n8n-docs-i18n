---
title: Kitemaker credentials
description: >-
  Kitemaker credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Kitemaker 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Kitemaker credentials
originalFilePath: integrations/builtin/credentials/kitemaker.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/kitemaker'
url: 'https://docs.n8n.io/integrations/builtin/credentials/kitemaker'
layout:
  description:
    visible: false
---

# Kitemaker credentials <a href="#kitemaker-credentials" id="kitemaker-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Kitemaker](../app-nodes/n8n-nodes-base.kitemaker.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Kitemaker](https://www.kitemaker.co/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Kitemaker's API documentation](https://kitemakerhq.github.io/rest-docs/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- **Personal Access Token**：从 **Manage > Developer settings** 生成 personal access token。更详细说明请参考 [API Authentication](https://kitemakerhq.github.io/rest-docs/#documentationauthentication)。
