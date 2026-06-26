---
title: Xata credentials
description: >-
  Xata credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Xata 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Xata credentials
originalFilePath: integrations/builtin/credentials/xata.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/xata'
url: 'https://docs.n8n.io/integrations/builtin/credentials/xata'
layout:
  description:
    visible: false
---

# Xata credentials <a href="#xata-credentials" id="xata-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Xata](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Xata](https://xata.io/) database，或在现有 database 上创建账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Xata's documentation](https://xata.io/docs/rest-api/authentication)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **Database Endpoint**：Workspace API 要求你使用此格式标识要从中请求信息的 database：`https://{workspace-display-name}-{workspace-id}.{region}.xata.sh/db/{dbname}`。更多信息请参考 [Workspace API](https://xata.io/docs/rest-api#workspace-api)。
    - `{workspace-display-name}`：workspace display name 是一个可选 identifier，你可以将其包含在 Database Endpoint 中。API 会忽略它，但如果你保存多个 credentials，包含它可以更容易判断此 database 属于哪个 workspace。
    - `{workspace-id}`：workspace 的唯一 ID，6 个字母数字字符。
    - `{region}`：database 的 hosting region。此值必须与 database region configuration 匹配。
    - `{dbname}`：你正在交互的 database 名称。
- 一个 **Branch**：输入你的 database 的 GitHub branch 名称。
- 一个 **API Key**：要生成 API key，请前往 [**Account Settings**](https://app.xata.io/settings) 并选择 **+ Add a key**。更多信息请参考 [Generate an API Key](https://xata.io/docs/rest-api#generate-an-api-key)。
