---
title: Wolfram|Alpha credentials
description: >-
  Wolfram|Alpha credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Wolfram|Alpha 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Wolfram|Alpha credentials
originalFilePath: integrations/builtin/credentials/wolframalpha.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/wolframalpha'
url: 'https://docs.n8n.io/integrations/builtin/credentials/wolframalpha'
layout:
  description:
    visible: false
---

# Wolfram|Alpha credentials <a href="#wolframoralpha-credentials" id="wolframoralpha-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Wolfram|Alpha](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Wolfram|Alpha's Simple API documentation](https://products.wolframalpha.com/simple-api/documentation)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个已注册的 [Wolfram ID](https://account.wolfram.com)，以及：

- 一个 **App ID**

要获取 App ID：

1. 打开 Wolfram|Alpha Developer Portal，并前往 [**API Access**](https://developer.wolframalpha.com/access)。
2. 选择 **Get an App ID**。
3. 为你的 application 输入 **Name**，例如 `n8n integration`。
4. 为你的 application 输入 **Description**。
5. 选择 **Simple API** 作为 **API**。
6. 选择 **Submit**。
6. 复制生成的 **App ID**，并将其输入到你的 n8n credential。

更多信息请参考 [Wolfram|Alpha Simple API documentation](https://products.wolframalpha.com/simple-api/documentation) 中的 **Getting Started**。

## 解决 Forbidden connection error <a href="#resolve-forbidden-connection-error" id="resolve-forbidden-connection-error"></a>

如果你输入 App ID 后收到 credential 为 **Forbidden** 的 error，请确认你已经为 Wolfram ID 验证了 email address：

1. 前往你的 [Wolfram ID Details](https://account.wolfram.com/wolframid)。
2. 如果你没有在 **Email address** 下方看到 **Verified** label，请选择链接发送 **verification email**。
3. 你必须打开该 email 中的链接来验证 email address。

验证可能需要几分钟才会同步到 API，但同步完成后，重试 n8n credential 应该会成功。
