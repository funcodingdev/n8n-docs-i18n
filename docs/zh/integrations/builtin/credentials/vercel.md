---
title: Vercel AI Gateway credentials
description: >-
  Vercel AI Gateway credentials 文档。使用这些 credentials 在 n8n 这个
  workflow 自动化平台中对 Vercel AI Gateway 进行身份验证。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Vercel AI Gateway credentials
originalFilePath: integrations/builtin/credentials/vercel.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/vercel'
url: 'https://docs.n8n.io/integrations/builtin/credentials/vercel'
layout:
  description:
    visible: false
---

# Vercel AI Gateway credentials <a href="#vercel-ai-gateway-credentials" id="vercel-ai-gateway-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Chat Vercel AI Gateway](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Vercel](https://vercel.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OIDC token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Vercel AI Gateway documentation](https://vercel.com/docs/ai-gateway)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

要生成你的 API Key：

1. [登录 Vercel](https://vercel.com/login) 或[创建账号](https://vercel.com/signup)。
2. 前往 Vercel dashboard，并选择 **AI Gateway** tab。
3. 在左侧 sidebar 中选择 **API keys**。
4. 选择 **Add key**，然后从 Dialog 继续选择 **Create key**。
4. 复制你的 key，并将其作为 **API Key** 添加到 n8n。

## 使用 OIDC token <a href="#using-oidc-token" id="using-oidc-token"></a>

要配置此 credential，你需要：

- 一个 **OIDC token**

要生成你的 OIDC token：

1. 在 local development 中，使用 `vc link` command 将你的 application 链接到 Vercel project。
2. 运行 `vercel env pull` command，从 Vercel 拉取 environment variables。
3. 复制你的 token，并将其作为 **OIDC TOKEN** 添加到 n8n。
