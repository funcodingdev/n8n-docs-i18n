---
title: Postgres credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Postgres credentials
originalFilePath: integrations/builtin/credentials/postgres.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/postgres
url: https://docs.n8n.io/integrations/builtin/credentials/postgres
description: >-
  Postgres credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Postgres 进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Postgres credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Postgres](../app-nodes/n8n-nodes-base.postgres/)
* [Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
* [Postgres Chat Memory](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md)
* [PGVector Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md)

{% hint style="info" %}
**Agent node 用户**

Agent node 不支持 SSH tunnels。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 Postgres server 上[创建 user account](https://www.postgresql.org/docs/current/sql-createuser.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Postgres's documentation](https://www.postgresql.org/docs/16/index.html)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

要配置此 credential，你需要：

* server 的 **Host** 或 domain name。
* **Database** name。
* **User** name。
* user **Password**。
* **Ignore SSL Issues**：设置 SSL validation 失败时 credential 是否仍连接。
* **SSL**：选择连接中是否使用 SSL。
* 用于连接的 **Port** number。
* **SSH Tunnel**：选择是否使用 SSH 加密与 Postgres server 的 network connection。

设置 database connection：

1.  输入 Postgres server 的 **Host** 或 domain name。你可以运行 `/conninfo` command 确认 host name，或运行此 query：

    ```
    SELECT inet_server_addr();
    ```
2. 输入 **Database** name。运行 `/conninfo` command 确认 database name。
3. 输入你希望连接时使用的 **User** name。
4. 输入该 user 的 **Password**。
5. **Ignore SSL Issues**：如果启用此项，即使 SSL validation 失败，credential 也会继续连接。
6. **SSL**：选择连接中是否使用 SSL。更多信息请参考 Postgres [SSL Support](https://www.postgresql.org/docs/16/libpq-ssl.html)。选项包括：
   * **Allow**：将 `ssl-mode` parameter 设置为 `allow`。先尝试非 SSL connection；如果失败，再尝试 SSL connection。
   * **Disable**：将 `ssl-mode` parameter 设置为 `disable`。只尝试非 SSL connection。
   * **Require**：将 `ssl-mode` parameter 设置为 `require`。只尝试 SSL connection。如果存在 root CA file，则验证 server certificate 是否由可信 certificate authority (CA) 签发。
7.  输入用于连接的 **Port** number。你可以运行 `/conninfo` command 确认 host name，或运行此 query：

    ```
    SELECT inet_server_port();
    ```
8. **SSH Tunnel**：启用此设置，通过 SSH 连接到 database。有关使用 SSH 的一些指导，请参考 [SSH tunnel limitations](postgres.md#ssh-tunnel-limitations)。启用后，你需要：
   1. 选择 **SSH Authenticate with**，以设置要创建的 SSH Tunnel type：
      * 如果要使用 password 连接到 SSH，请选择 **Password**。
      * 如果要使用 identity file（private key）和 passphrase 连接到 SSH，请选择 **Private Key**。
   2. 输入你要连接的 remote bind address 作为 **SSH Host**。
   3. **SSH Port**：输入 SSH tunnel 的 local port number。
   4. **SSH Postgres Port**：输入 tunnel 的 remote end，也就是 database server 正在使用的 port number。
   5. **SSH User**：输入用于登录的 username。
   6. 如果你为 SSH Authenticate with 选择了 **Password**，请添加 user 的 **SSH Password**。
   7. 如果你为 **SSH Authenticate with** 选择了 **Private Key**：
      1. 添加用于 SSH 的 **Private Key** 或 identity file 内容。
      2. 如果 **Private Key** 创建时带有 passphrase，请输入该 **Passphrase**。如果 **Private Key** 没有 passphrase，请将此字段留空。

更多信息请参考 [Secure TCP/IP Connections with SSH Tunnels](https://www.postgresql.org/docs/16/ssh-tunnels.html)。

### SSH tunnel limitations <a href="#ssh-tunnel-limitations" id="ssh-tunnel-limitations"></a>

仅在以下情况下使用 **SSH Tunnel** 设置：

* 你将 credential 用于 [Postgres](../app-nodes/n8n-nodes-base.postgres/) node（Agent node 不支持 SSH tunnels）。
* 你有一个 SSH server 与 Postgres server 运行在同一台机器上。
* 你有一个可以使用 `ssh` 登录的 user account。
