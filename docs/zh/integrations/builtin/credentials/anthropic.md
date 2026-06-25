---
title: Anthropic credentials
description: >-
  Anthropic credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Anthropic。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Anthropic credentials
originalFilePath: integrations/builtin/credentials/anthropic.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/anthropic'
url: 'https://docs.n8n.io/integrations/builtin/credentials/anthropic'
layout:
  description:
    visible: false
---

# Anthropic credentials <a href="#anthropic-credentials" id="anthropic-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Anthropic](../app-nodes/n8n-nodes-langchain.anthropic.md)
- [Anthropic Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Anthropic 的文档](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个有 Claude 访问权限的 [Anthropic Console 账号](https://console.anthropic.com)。

然后：

1. 在 Anthropic Console 中，打开 **Settings >** [**API Keys**](https://console.anthropic.com/settings/keys)。
2. 选择 **+ Create Key**。
3. 为你的 key 设置 **Name**，例如 `n8n-integration`。
4. 选择 **Copy Key** 复制 key。
5. 在 n8n credential 中将其输入为 **API Key**。
6. （可选）如需向 API requests 添加 custom headers：
    1. 启用 **Add Custom Header** toggle。
    2. 输入 custom header 的 **Header Name**。
    3. 输入 custom header 的 **Header Value**。

有关更多信息，请参阅 Anthropic 的 [Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude) 和 [Quickstart](https://docs.anthropic.com/en/docs/quickstart)。
