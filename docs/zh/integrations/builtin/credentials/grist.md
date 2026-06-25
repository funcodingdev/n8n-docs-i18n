---
title: Grist credentials
description: >-
  Grist credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Grist 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Grist credentials
originalFilePath: integrations/builtin/credentials/grist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/grist'
url: 'https://docs.n8n.io/integrations/builtin/credentials/grist'
layout:
  description:
    visible: false
---

# Grist credentials <a href="#grist-credentials" id="grist-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Grist](../app-nodes/n8n-nodes-base.grist.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Grist](https://getgrist.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Grist's API documentation](https://support.getgrist.com/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：创建 API key 的说明请参考 [Grist API authentication documentation](https://support.getgrist.com/rest-api/#authentication)。
- 选择你的 Grist **Plan Type**。选项包括：
    - Free
    - Paid：如果选择此项，请提供你的 Grist **Custom Subdomain**。这是 `.getgrist.com` 之前的部分。例如，如果完整 Grist domain 是 `n8n.getgrist.com`，这里应输入 `n8n`。
    - Self-Hosted：如果选择此项，请提供你的 Grist **Self-Hosted URL**。这应是完整 URL。
