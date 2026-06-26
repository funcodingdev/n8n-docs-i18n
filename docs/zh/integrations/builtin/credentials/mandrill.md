---
title: Mandrill credentials
description: >-
  Mandrill credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mandrill 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Mandrill credentials
originalFilePath: integrations/builtin/credentials/mandrill.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mandrill'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mandrill'
layout:
  description:
    visible: false
---

# Mandrill credentials <a href="#mandrill-credentials" id="mandrill-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mandrill](../app-nodes/n8n-nodes-base.mandrill.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 Mailchimp [Transactional email account](https://mailchimp.com/features/transactional-email-infrastructure/)
- 使用你的 Mailchimp account 登录 [Mandrill](https://mandrillapp.com/login/)。

如果你已经有 Standard plan 或更高级别的 Mailchimp account，请在该账号中启用 [Transactional Emails](https://mailchimp.com/help/add-or-remove-transactional-email) 以使用 Mandrill。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mailchimp's Transactional API documentation](https://mailchimp.com/developer/transactional/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：从 Mandrill [Settings](https://mandrillapp.com/settings) 生成 API key。更详细说明请参考 Mailchimp 的 [Generate your API key documentation](https://mailchimp.com/developer/transactional/guides/quick-start/#generate-your-api-key)。
