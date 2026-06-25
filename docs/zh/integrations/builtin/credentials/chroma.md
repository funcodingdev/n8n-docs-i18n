---
title: Chroma credentials
description: >-
  Chroma credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Chroma。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Chroma credentials
originalFilePath: integrations/builtin/credentials/chroma.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/chroma'
url: 'https://docs.n8n.io/integrations/builtin/credentials/chroma'
layout:
  description:
    visible: false
---

# Chroma credentials <a href="#chroma-credentials" id="chroma-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- Chroma Vector Store

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>
创建并运行一个 [Chroma](https://www.trychroma.com/home) instance。有关更多信息，请参阅 [Running Chroma in Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>
- API key
- Instance URL

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Chroma 的文档](https://docs.trychroma.com/docs/overview/getting-started)。使用 cloud instance 时也可参阅 [Chroma Cloud](https://docs.trychroma.com/cloud/getting-started)。

查看 n8n 的 [Advanced AI](/advanced-ai/index.md) 文档。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Chroma](https://www.trychroma.com/) 账号。你还需要以下信息：

- 一个 **API Key**
- 你的 **Tenant ID**
- 你的 **Database Name**

设置步骤：

1. 前往 **Cloud Dashboard**。
2. 创建一个 **Database**
3. 点击你想访问的 database 对应的 **Settings**。
4. 点击 **Create API key and copy code**
5. 在 n8n credential 中输入你的 **API Key**、**Tenant ID** 和 **Database Name**

## 使用 Instance URL <a href="#using-instance-url" id="using-instance-url"></a>

要配置此 credential，你需要：

- **Base URL:** 你的 Chroma instance 的 base URL。默认值是 `http://localhost:8000`
