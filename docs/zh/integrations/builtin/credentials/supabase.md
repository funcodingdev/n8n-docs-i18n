---
title: Supabase credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Supabase credentials
originalFilePath: integrations/builtin/credentials/supabase.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/supabase
url: https://docs.n8n.io/integrations/builtin/credentials/supabase
description: >-
  Supabase credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Supabase 进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Supabase credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Supabase](../app-nodes/n8n-nodes-base.supabase/)
* [Supabase Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Supabase](https://supabase.com/dashboard/sign-up) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Supabase's API documentation](https://supabase.com/docs/guides/api)。

## 使用 access token <a href="#using-access-token" id="using-access-token"></a>

要配置此 credential，你需要：

* 一个 **Host**
* 一个 **Service Role Secret**

要生成你的 API Key：

1. 在你的 Supabase account 中，前往 **Dashboard**，并创建或选择你要为其创建 API key 的 project。
2. 前往 [**Project Settings > API**](https://supabase.com/dashboard/project/_/settings/api)，查看你的 project 的 API Settings。
3. 从 **Project URL** 部分复制 **URL**，并将其作为 n8n **Host** 输入。更详细的说明请参考 [API URL and keys](https://supabase.com/docs/guides/api#api-url-and-keys)。
4. 显示并复制 `service_role` 的 **Project API key**。复制该 key，并将其作为 n8n **Service Role Secret** 输入。有关 `service_role` privileges 的更多信息，请参考 [Understanding API Keys](https://supabase.com/docs/guides/api/api-keys)。
