---
title: TimescaleDB credentials
description: >-
  TimescaleDB credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 TimescaleDB 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: TimescaleDB credentials
originalFilePath: integrations/builtin/credentials/timescaledb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/timescaledb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/timescaledb'
layout:
  description:
    visible: false
---

# TimescaleDB credentials <a href="#timescaledb-credentials" id="timescaledb-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [TimescaleDB](../app-nodes/n8n-nodes-base.timescaledb.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

一个可用的 [TimescaleDB](https://www.timescale.com/) instance。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Timescale documentation](https://docs.timescale.com/)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

要配置此 credential，你需要：

- **Host**：你的 TimescaleDB server 的 fully qualified server name 或 IP address。
- **Database**：要连接的 database 名称。
- 一个 **User**：你希望用于登录的 user name。
- 一个 **Password**：输入你要连接的 database user 的 password。
- **Ignore SSL Issues**：如果打开，即使 SSL certificate validation 失败，n8n 也会继续连接，并且你不会看到 **SSL** selector。
- **SSL**：此设置控制连接的 `ssl-mode` connection string。选项包括：
    - **Allow**：将 `ssl-mode` 参数设为 `allow`。先尝试非 SSL connection；如果失败，再尝试 SSL connection。
    - **Disable**：将 `ssl-mode` 参数设为 `disable`。只尝试非 SSL connection。
    - **Require**：将 `ssl-mode` 参数设为 `require`，这是 TimescaleDB connection strings 的默认值。只尝试 SSL connection。如果存在 root CA file，则验证 server certificate 是否由受信任的 certificate authority (CA) 签发。
- **Port**：TimescaleDB server 的 port number。

有关非 SSL 字段的更多信息，请参考 [Timescale connection settings documentation](https://docs.tigerdata.com/integrations/latest/find-connection-details/)。有关 SSL 选项的更多信息，请参考 [Connect with a stricter SSL](https://docs.tigerdata.com/use-timescale/latest/security/strict-ssl/)。
