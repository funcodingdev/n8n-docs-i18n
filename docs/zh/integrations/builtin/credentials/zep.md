---
title: Zep credentials
description: >-
  Zep credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zep 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Zep credentials
originalFilePath: integrations/builtin/credentials/zep.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zep'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zep'
layout:
  description:
    visible: false
---

# Zep credentials <a href="#zep-credentials" id="zep-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Zep](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)
* [Zep Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zep's Cloud SDK documentation](https://help.getzep.com/install-sdks)。有关 API 的信息，请参考 [Zep's REST API documentation](https://getzep.github.io/zep/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个至少有一个 project 的 [Zep server](https://www.getzep.com/)，以及：

- 一个 **API URL**
- 一个 **API Key**

设置取决于你使用的是 Zep Cloud 还是 self-hosted Zep Open Source。

### Zep Cloud setup <a href="#zep-cloud-setup" id="zep-cloud-setup"></a>

如果你使用 [Zep Cloud](https://app.getzep.com)，请按照以下说明操作：

1. 在 Zep 中，打开 **Project Settings**。
2. 在 **Project Keys** 部分，选择 **Add Key**。
3. 输入 **Key Name**，例如 `n8n integration`。
4. 选择 **Create**。
5. 复制 key，并将其作为 **API Key** 输入到你的 n8n integration。
6. 打开 **Cloud** toggle。

### Self-hosted Zep Open Source setup <a href="#self-hosted-zep-open-source-setup" id="self-hosted-zep-open-source-setup"></a>

{% hint style="warning" %}
**已弃用**

Zep 团队已在 2025 年 4 月[弃用 open source Zep Community Edition](https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/)。这些说明未来可能不再可用。
{% endhint %}

如果你正在 self-hosting Zep Open Source，请按照以下说明操作：

1. 将你的 Zep server 的 JWT token 作为 n8n 中的 **API Key** 输入。
2. 确保 **Cloud** toggle 关闭。
3. 将你的 Zep server 的 URL 输入为 **API URL**。
