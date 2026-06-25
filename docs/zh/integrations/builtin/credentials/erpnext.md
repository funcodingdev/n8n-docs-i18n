---
title: ERPNext credentials
description: >-
  ERPNext credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 ERPNext。
contentType:
  - integration
  - reference
nodeTitle: ERPNext credentials
originalFilePath: integrations/builtin/credentials/erpnext.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/erpnext'
url: 'https://docs.n8n.io/integrations/builtin/credentials/erpnext'
layout:
  description:
    visible: false
---

# ERPNext credentials <a href="#erpnext-credentials" id="erpnext-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [ERPNext](../app-nodes/n8n-nodes-base.erpnext.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [ERPNext](https://erpnext.com) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ERPNext 文档](https://docs.erpnext.com/docs/user/manual/en/introduction)。

有关使用 framework 的更多信息，请参阅 [ERPNext developer 文档](https://frappeframework.com/docs/user/en/introduction)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：从你自己的 ERPNext user account 中的 **Settings > My Settings > API Access** 生成。
- 一个 **API Secret**：随 API key 一起生成。
- 你的 ERPNext **Environment**：
    - 对于 **Cloud-hosted**：
        - 你的 ERPNext **Subdomain**：请参阅 [FAQs](#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account)
        - 你的 **Domain**：在 `erpnext.com` 和 `frappe.cloud` 之间选择。
    - 对于 **Self-hosted**：
        - 你托管 ERPNext 的完整限定 **Domain**
- 选择是否 **Ignore SSL Issues**：选中后，即使 SSL certificate validation 不可用，n8n 也会连接。

如果你是 ERPNext System Manager，也可以为其他 users 生成 API keys 和 secrets。有关更多信息，请参阅 [ERPNext Adding Users 文档](https://docs.erpnext.com/docs/user/manual/en/adding-users)。

## 如何查找 ERPNext cloud-hosted 账号的 subdomain <a href="#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account" id="how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account"></a>

你可以通过查看浏览器地址栏找到 ERPNext subdomain。`https://` 和 `.erpnext.com` 或 `frappe.cloud` 之间的字符串就是 subdomain。

例如，如果地址栏中的 URL 是 `https://n8n.erpnext.com`，则 subdomain 是 `n8n`。
