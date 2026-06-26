---
title: Marketstack credentials
description: >-
  Marketstack credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Marketstack 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Marketstack credentials
originalFilePath: integrations/builtin/credentials/marketstack.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/marketstack'
url: 'https://docs.n8n.io/integrations/builtin/credentials/marketstack'
layout:
  description:
    visible: false
---

# Marketstack credentials <a href="#marketstack-credentials" id="marketstack-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Marketstack](../app-nodes/n8n-nodes-base.marketstack.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Marketstack](https://marketstack.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Marketstack's API documentation](https://marketstack.com/documentation)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：在 Marketstack [account dashboard](https://marketstack.com/dashboard) 中查看和生成 API keys。
- 选择是否 **Use HTTPS**：请根据你的 Marketstack account plan level 进行选择：
    - Free plan：关闭 **Use HTTPS**
    - 所有其他 plans：开启 **Use HTTPS**
