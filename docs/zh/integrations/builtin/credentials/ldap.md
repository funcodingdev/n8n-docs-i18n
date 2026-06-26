---
title: LDAP credentials
description: >-
  LDAP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  LDAP 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: LDAP credentials
originalFilePath: integrations/builtin/credentials/ldap.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ldap'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ldap'
layout:
  description:
    visible: false
---

# LDAP credentials <a href="#ldap-credentials" id="ldap-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [LDAP](../core-nodes/n8n-nodes-base.ldap.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

使用 Lightweight Directory Access Protocol (LDAP) 创建 server directory。

一些常见 LDAP providers 包括：

* [Jumpcloud](https://jumpcloud.com/blog/how-to-connect-your-application-to-ldap)
* [Azure ADDS](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/tutorial-configure-ldaps)
* [Okta](https://help.okta.com/en-us/Content/Topics/Directory/LDAP-interface-connection-settings.htm)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- LDAP server details

## 相关资源 <a href="#related-resources" id="related-resources"></a>

详细信息请参考你的 LDAP provider 自己的文档。

有关 LDAP 的一般信息，请参考 [Basic LDAP concepts](https://ldap.com/basic-ldap-concepts/) 了解基础概览，并参考 [The LDAP Bind Operation](https://ldap.com/the-ldap-bind-operation/) 了解 bind operation 和 authentication 的工作方式。

## 使用 LDAP server details <a href="#using-ldap-server-details" id="using-ldap-server-details"></a>

要配置此 credential，你需要：

- **LDAP Server Address**：使用 LDAP server 的 IP address 或 domain。
- **LDAP Server Port**：使用连接到 LDAP server 的端口号。
- **Binding DN**：使用 LDAP server 的 Binding Distinguished Name (Bind DN)。这是 credential 应该用来登录的 user account。如果你使用 Active Directory，它可能类似于 `cn=administrator, cn=Users, dc=n8n, dc=io`。有关如何识别此 DN 和相关 password 的更多信息，请参考你的 LDAP provider 文档。
- **Binding Password**：使用 **Binding DN** user 的 password。
- 选择 **Connection Security**：选项包括：
    - `None`
    - `TLS`
    - `STARTTLS`
- _可选：_ 输入以秒为单位的数值来设置 **Connection Timeout**。
