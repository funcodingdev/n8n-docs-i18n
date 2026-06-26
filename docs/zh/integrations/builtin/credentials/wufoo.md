---
title: Wufoo credentials
description: >-
  Wufoo credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Wufoo 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Wufoo credentials
originalFilePath: integrations/builtin/credentials/wufoo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/wufoo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/wufoo'
layout:
  description:
    visible: false
---

# Wufoo credentials <a href="#wufoo-credentials" id="wufoo-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Wufoo Trigger](../trigger-nodes/n8n-nodes-base.wufootrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Wufoo](https://wufoo.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Wufoo's API documentation](https://wufoo.github.io/docs/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：从 [Wufoo Form Manager](https://app.wufoo.com/#/form-manager) 获取你的 API key。在 form 右侧选择 **More > API Information**。更多信息请参考 [Using API Information and Webhooks](https://help.surveymonkey.com/en/wufoo/integrations/wufoo-api/)。
- 一个 **Subdomain**：你的 subdomain 是 Wufoo URL 中 `https://` 之后、`wufoo.com` 之前的部分。因此如果完整 domain 是 `https://n8n.wufoo.com`，subdomain 就是 `n8n`。Admins 可以在 [**Account Manager**](https://help.surveymonkey.com/en/wufoo/account/account-manager/) 中查看 subdomain。更多信息请参考 [Your Subdomain](https://help.surveymonkey.com/en/wufoo/account/your-subdomain/)。
