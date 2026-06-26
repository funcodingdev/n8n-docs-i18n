---
title: MySQL credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: MySQL credentials
originalFilePath: integrations/builtin/credentials/mysql.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mysql
url: https://docs.n8n.io/integrations/builtin/credentials/mysql
description: >-
  MySQL credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MySQL 进行身份验证。
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

# MySQL credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [MySQL](../app-nodes/n8n-nodes-base.mysql/)
* [Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)

{% hint style="info" %}
**Agent node 用户**

Agent node 不支持 SSH tunnels。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [MySQL](https://www.mysql.com/) server database 上创建一个 user account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MySQL's documentation](https://dev.mysql.com/doc/refman/8.3/en/)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

要配置此 credential，你需要：

* server **Host**：database 的 host name 或 IP address。
* **Database** name。
* **User** name。
* 该 user 的 **Password**。
* MySQL server 使用的 **Port** number。
* **Connect Timeout**：初始 database connection 期间发生 timeout 前的毫秒数。
* **SSL**：如果你的 database 使用 SSL，请启用此项，并添加 SSL certificate 的详细信息。
* **SSH Tunnel**：选择是否通过 SSH tunnel 连接。SSH tunnel 允许未加密流量通过加密连接传输，并让经过授权的远程访问可以连接受 firewall 保护、无法从外部直接连接的 servers。

设置 database connection credential：

1.  在你的 n8n credential 中，将 database 的 hostname 输入为 **Host**。运行此 query 确认 hostname：

    ```
    SHOW VARIABLES WHERE Variable_name = 'hostname';
    ```
2.  在你的 n8n credential 中，将 database 名称输入为 **Database**。运行此 query 确认 database name：

    ```
    SHOW DATABASES;
    ```
3. 输入 database 中某个 **User** 的 username。该 user 应该具备 n8n 要执行相关 actions 所需的适当 permissions。
4. 输入该 user 的 **Password**。
5.  输入 MySQL server 使用的 **Port** number（默认值为 `3306`）。运行此 query 确认 port number：

    ```
    SHOW VARIABLES WHERE Variable_name = 'port';
    ```
6.  输入你希望 node 使用的 **Connect Timeout**。Connect Timeout 是初始 database connection 期间，node 在 timeout 前应等待的毫秒数。n8n 默认使用 `10000`，这也是 MySQL 默认的 10 秒。如果你想匹配 database 的 `connect_timeout`，请运行此 query 获取它，然后乘以 1000 后再输入到 n8n：

    ```
    SHOW VARIABLES WHERE Variable_name = 'connect_timeout';
    ```
7. 如果你的 database 使用 SSL，并且你想为连接使用 **SSL**，请在 credential 中启用此选项。启用后，在以下字段中输入 MySQL SSL certificate 的信息：
   1. 在 **CA Certificate** 字段中输入 `ca.pem` file contents。
   2. 在 **Client Private Key** 字段中输入 `client-key.pem` file contents。
   3. 在 **Client Certificate** 字段中输入 `client-cert.pem` file contents。
8. 如果你想为连接使用 **SSH Tunnel**，请在 credential 中启用此选项。否则跳过。如果启用：
   1. 选择 **SSH Authenticate with**，以设置要创建的 SSH Tunnel type：
      * 如果要使用 password 连接到 SSH，请选择 **Password**。
      * 如果要使用 identity file（private key）和 passphrase 连接到 SSH，请选择 **Private Key**。
   2. 输入 **SSH Host**。n8n 使用此 host 创建格式为 `[user@]host:port` 的 SSH URI。
   3. 输入 **SSH Port**。n8n 使用此 port 创建格式为 `[user@]host:port` 的 SSH URI。
   4. 输入要用于连接的 **SSH User**。n8n 使用此 user 创建格式为 `[user@]host:port` 的 SSH URI。
   5. 如果你为 **SSH Authenticate with** 选择了 **Password**，请添加 **SSH Password**。
   6. 如果你为 **SSH Authenticate with** 选择了 **Private Key**：
      1. 添加用于 SSH 的 **Private Key** 或 identity file 内容。这等同于在 MySQL 中配合 `shell-connect()` command 使用 `ssh-identity-file` option。
      2. 如果 **Private Key** 创建时带有 passphrase，请输入该 **Passphrase**。这等同于在 MySQL 中配合 `shell-connect()` command 使用 `ssh-identity-pass` option。如果 **Private Key** 没有 passphrase，请将此字段留空。

有关在 MySQL 中使用 SSL certificates 的更多信息，请参考 [MySQL | Creating SSL and RSA Certificates and Keys](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-rsa-files.html)。有关在 MySQL 中使用 SSH tunnels 的更多信息，请参考 [MySQL | Using an SSH Tunnel](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-connection-ssh.html)。
