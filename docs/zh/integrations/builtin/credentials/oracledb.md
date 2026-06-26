---
title: Oracle Database credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Oracle Database credentials
originalFilePath: integrations/builtin/credentials/oracledb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/oracledb
url: https://docs.n8n.io/integrations/builtin/credentials/oracledb
description: >-
  Oracle Database credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Oracle Database 进行身份验证。
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

# Oracle Database credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [OracleDB](../app-nodes/app-nodes.md)
* [Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
* [Oracle Database Vector Store](../../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md)
* [Embeddings Oracle Database](../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md)

{% hint style="info" %}
这些 nodes 不支持 SSH tunnels。它们要求 Oracle Database **19c 或更高版本**。对于 Transparent Application Continuity (TAC) 和 Sharding 等高级 Oracle Database features，它们还要求 Oracle Client Libraries **19c 或更高版本**。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Oracle Database](https://www.oracle.com/pls/topic/lookup?ctx=dblatest\&id=GUID-F0246961-558F-480B-AC0F-14B50134621C) server 上创建一个 user account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Oracle Database documentation](https://docs.oracle.com/en/database/oracle/oracle-database)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

要配置此 credential，你需要：

* **User** name。
* 该 user 的 **Password**。
* **Connection String**：要连接的 Oracle Database instance。该 string 可以是 Easy Connect string、来自 tnsnames.ora file 的 TNS Alias，或 Oracle Database instance。
* **Use Optional Oracle Client Libraries**：如果你想使用 Oracle Database advanced features，请启用此项。此选项内部使用 node-oracledb Thick mode。还需要额外设置才能启用 node-oracledb Thick mode。更多信息请参考 [Enabling Thick mode documentation](https://node-oracledb.readthedocs.io/en/latest/user_guide/initialization.html#enabling-node-oracledb-thick-mode)。官方 n8n docker images 中不提供此选项。
* **Use SSL**：如果你的 Connection String 使用 SSL，请启用此项，并为 SSL Authentication 配置额外详细信息。
* **Wallet Password**：用于解密 Privacy Enhanced Mail (PEM)-encoded private certificate 的 password（如果已加密）。
* **Wallet Content**：建立到 Oracle Database 的 mutual TLS (mTLS) connection 所需的 security credentials。
* **Distinguished Name**：应与 certificate DN 匹配的 distinguished name (DN)。
* **Match Distinguished Name**：除了常规 certificate verification 外，是否还应匹配 server certificate DN。
* **Allow Weak Distinguished Name Match**：是否执行会同时检查 listener 和 server certificates 的安全 DN matching 行为。
* **Pool Min**：创建 pool 时建立到 database 的 connections 数量。
* **Pool Max**：connection pool 可以增长到的最大 connections 数量。
* **Pool Increment**：每当 connection request 超过当前 open connections 数量时打开的 connections 数量。
* **Pool Maximum Session Life Time**：每当 connection request 超过当前 open connections 数量时打开的 connections 数量。
* **Pool Connection Idle Timeout**：每当 connection request 超过当前 open connections 数量时打开的 connections 数量。
* **Connection Class Name**：DRCP/PRCP Connection Class。更多信息请参考 [Enabling DRCP](https://docs.oracle.com/en/database/oracle/oracle-database/26/admin/managing-processes.html#GUID-BB76E57C-3F16-4C85-AEF6-BA14FC1B4777)。
* **Connection Timeout**：application 建立 Oracle Net connection 的 timeout duration（秒）。
* **Transport Connection Timeout**：等待建立到 database host 的 connection 的最大秒数。
* **Keepalive Probe Interval**：发送 keepalive probes 之间的分钟数。

设置 database connection credential：

1. 在你的 n8n credential 中，将 database username 输入为 **User**。
2. 输入该 user 的 **Password**。
3. 在你的 n8n credential 中，将 database connection string 输入为 **Connection String**。
4. 如果你的 database 使用 SSL，并且你想为连接配置 **SSL**，请在 credential 中启用此选项。启用后，在这些字段中输入 Oracle Database SSL certificate 的信息：
   1. 如果有 wallet password，请在 **Wallet Password** 字段中输入。
   2. 在 **Wallet Content** 字段的 'Expanded' layout 中输入 PEM-encoded wallet file、**ewallet.pem** contents。这会确保保留 PEM-encoded wallet file 中的所有 whitespaces。直接复制粘贴到 **Wallet Content** 字段会去掉 whitespaces 并导致 connection errors。

有关使用 TLS connections 的更多信息，请参考 [node-oracledb](https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#mutual-tls-connections-to-oracle-cloud-autonomous-database)。
