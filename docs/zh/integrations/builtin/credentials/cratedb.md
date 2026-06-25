---
title: CrateDB credentials
description: >-
  CrateDB credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 CrateDB。
contentType:
  - integration
  - reference
nodeTitle: CrateDB credentials
originalFilePath: integrations/builtin/credentials/cratedb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cratedb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cratedb'
layout:
  description:
    visible: false
---

# CrateDB credentials <a href="#cratedb-credentials" id="cratedb-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [CrateDB](../app-nodes/n8n-nodes-base.cratedb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

一个可用的 CrateDB instance。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- account connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [CrateDB 的文档](https://cratedb.com/docs/crate/reference/en/latest/)。

## 使用 account connection <a href="#using-account-connection" id="using-account-connection"></a>

要配置此 credential，你需要：

- 你的 **Host** name
- 你的 **Database** name
- 一个 **User** name
- user **Password**
- 设置 **SSL** 参数。有关更多信息，请参阅 [CrateDB Secured Communications (SSL/TLS) 文档](https://cratedb.com/docs/crate/reference/en/5.7/admin/ssl.html#admin-ssl)。n8n 支持的选项包括：
    - Allow
    - Disable
    - Require
- 一个 **Port** number

有关这些字段及其默认值的详细说明，请参阅 [Connect to a CrateDB cluster 文档](https://cratedb.com/docs/crate/clients-tools/en/latest/connect/)。
