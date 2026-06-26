---
title: Zulip credentials
description: >-
  Zulip credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zulip 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zulip credentials
originalFilePath: integrations/builtin/credentials/zulip.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zulip'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zulip'
layout:
  description:
    visible: false
---

# Zulip credentials <a href="#zulip-credentials" id="zulip-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Zulip](../app-nodes/n8n-nodes-base.zulip.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zulip](https://zulip.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zulip's API documentation](https://zulip.com/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **URL**：输入你的 Zulip domain 的 URL。
- 一个 **Email** address：输入用于登录 Zulip 的 email address。
- 一个 **API Key**：在 **Gear cog > Personal Settings > Account & privacy > API Key** 中获取你的 API key。更多信息请参考 [API Keys](https://zulip.com/api/api-keys)。
