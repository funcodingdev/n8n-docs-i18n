---
title: Odoo credentials
description: >-
  Odoo credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Odoo 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Odoo credentials
originalFilePath: integrations/builtin/credentials/odoo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/odoo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/odoo'
layout:
  description:
    visible: false
---

# Odoo credentials <a href="#odoo-credentials" id="odoo-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Odoo](../app-nodes/n8n-nodes-base.odoo.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（推荐）
- Password

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Odoo's External API documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html)。

如果你刚开始使用 Odoo，请参考 Odoo [Getting Started tutorial](https://www.odoo.com/slides/getting-started-15)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Odoo](https://www.odoo.com/) database 上的 user account，以及：

- 你的 **Site URL**
- 你的 **Username**
- 一个 **API key**
- 你的 **Database name**

使用 API key 设置 credential：

1. 将你的 Odoo server 或 site URL 输入为 **Site URL**。
2. 输入你的 **Username**，该值应与你在 Odoo **Change password** screen 中看到的显示一致。
4. 要使用 API key，请前往 **Your Profile > Preferences > Account Security > Developer API Keys**。
    - 如果没有此选项，你可能需要升级 Odoo plan。更多信息请参考[所需 plan type](#required-plan-type)。
5. 选择 **New API Key**。
6. 为 key 输入 **Description**，例如 `n8n integration`。
7. 选择 **Generate Key**。
8. 复制 key，并在你的 n8n credential 中将其输入为 **Password or API key**。
9. 输入你的 Odoo **Database name**，也称为 instance name。

更多信息请参考 [Odoo API Keys](https://www.odoo.com/documentation/15.0/developer/reference/external_api.html?#api-keys)。

## 使用 password <a href="#using-password" id="using-password"></a>

要配置此 credential，你需要一个 [Odoo](https://www.odoo.com/) database 上的 user account，以及：

- 你的 **Site URL**
- 你的 **Username**
- 你的 **Password**
- 你的 **Database name**

使用 password 设置 credential：

1. 将你的 Odoo server 或 site URL 输入为 **Site URL**。
2. 输入你的 **Username**，该值应与你在 Odoo **Change password** screen 中看到的显示一致。
3. 要使用 password，请在 **Password or API key** 字段中输入你的 user password。
4. 输入你的 Odoo **Database name**，也称为 instance name。

{% hint style="info" %}
**Password compatibility**

如果你尝试 password credential，但某个 node function 无法工作，请改用 API key。Odoo 对某些 modules 或某些 settings 要求使用 API key。
{% endhint %}

## 所需 plan type <a href="#required-plan-type" id="required-plan-type"></a>

{% hint style="info" %}
**所需 plan type**

只有 **Custom** Odoo plan 可以访问 external API。（One App Free 或 Standard plans 不提供访问权限。）

更多信息请参考 [Odoo Pricing Plans](https://www.odoo.com/pricing-plan)。
{% endhint %}
