---
title: PostHog credentials
description: >-
  PostHog credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  PostHog 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: PostHog credentials
originalFilePath: integrations/builtin/credentials/posthog.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/posthog'
url: 'https://docs.n8n.io/integrations/builtin/credentials/posthog'
layout:
  description:
    visible: false
---

# PostHog credentials <a href="#posthog-credentials" id="posthog-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [PostHog](../app-nodes/n8n-nodes-base.posthog.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [PostHog](https://posthog.com/) 账号，或在你的 server 上托管 PostHog。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [PostHog's API documentation](https://posthog.com/docs/api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- API **URL**：输入 API requests 的正确 domain：
    - 在 US Cloud 上，对 public POST-only endpoints 使用 `https://us.i.posthog.com`，对 private endpoints 使用 `https://us.posthog.com`。
    - 在 EU Cloud 上，对 public POST-only endpoints 使用 `https://eu.i.posthog.com`，对 private endpoints 使用 `https://eu.posthog.com`。
    - 对于 self-hosted instances，请使用你的 self-hosted domain。
    - 通过检查你的 PostHog instance URL 确认具体值。
- 一个 **API Key**：你使用的 API key 取决于你访问的是 public 还是 private endpoints：
    - 对于 public POST-only endpoints，请使用来自 project **General** Settings 的 [Project API key](https://app.posthog.com/project/settings)。
    - 对于 private endpoints，请使用来自 User account **Personal API Keys** Settings 的 [Personal API key](https://app.posthog.com/settings/user-api-keys)。更多信息请参考 [How to obtain a personal API key](https://posthog.com/docs/api#private-endpoint-authentication)。
