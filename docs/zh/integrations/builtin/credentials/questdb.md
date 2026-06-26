---
title: QuestDB credentials
description: >-
  QuestDB credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  QuestDB 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: QuestDB credentials
originalFilePath: integrations/builtin/credentials/questdb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/questdb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/questdb'
layout:
  description:
    visible: false
---

# QuestDB credentials <a href="#questdb-credentials" id="questdb-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [QuestDB](../app-nodes/n8n-nodes-base.questdb.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [QuestDB](https://questdb.io/) instance 上创建 user account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [QuestDB's documentation](https://questdb.io/docs)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

要配置此 credential，你需要：

- **Host**：输入 server 的 host name 或 IP address。
- **Database**：输入 database name，例如 `qdb`。
- **User**：输入 user account 的 username，该值按 `server.conf` 中的 `pg.user` 或 `pg.readonly.user` property 配置。默认值为 `admin`。
- **Password**：输入 user account 的 password，该值按 `server.conf` 中的 `pg.password` 或 `pg.readonly.password` property 配置。默认值为 `quest`。
- **SSL**：选择 connection 是否应使用 SSL，这会设置 `sslmode` parameter。选项包括：
    - **Allow**
    - **Disable**
    - **Require**
- **Port**：输入用于 connection 的 port number。默认值为 `8812`。

更多信息请参考 [List of supported connection properties](https://questdb.io/docs/reference/api/postgres/#list-of-supported-connection-properties)。
