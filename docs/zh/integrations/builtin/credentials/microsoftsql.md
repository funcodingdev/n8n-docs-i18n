---
title: Microsoft SQL credentials
description: >-
  Microsoft SQL credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Microsoft SQL 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft SQL credentials
originalFilePath: integrations/builtin/credentials/microsoftsql.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftsql'
url: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftsql'
layout:
  description:
    visible: false
---

# Microsoft SQL credentials <a href="#microsoft-sql-credentials" id="microsoft-sql-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Microsoft SQL](../app-nodes/n8n-nodes-base.microsoftsql.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Microsoft SQL server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server) database 上创建 user account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- SQL database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何连接到该服务的更多信息，请参考 [Microsoft's Connect to SQL Server documentation](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver16&tabs=sqldb#connect-to-sql-server)。

## 使用 SQL database connection <a href="#using-sql-database-connection" id="using-sql-database-connection"></a>

要配置此 credential，你需要：

- **Server** name
- **Database** name
- 你的 **User** account/ID
- 你的 **Password**
- 用于连接的 **Port**
- **Domain** name
- 是否使用 **TLS**
- 是否 **Ignore SSL Issues**
- **Connect Timeout**
- **Request Timeout**
- connection 应使用的 **TDS Version**

设置 database connection：

1. 将 SQL Server Host Name 作为 **Server** 输入。在已有 SQL Server connection 中，host name 位于 instance name 之前，格式为 `HOSTNAME\INSTANCENAME`。查找 host name：
    - 在 **Object Explorer** 面板中，它是 database 的顶层对象。
    - 在 query window 的 footer 中。
    - 查看当前 connection **Properties**，并查找 **Name** 或 **Display Name**。
    - 更多信息请参考[连接到 SQL Server 后查找 SQL Server Instance Name](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#when-youre-connected-to-sql-server)。你也可以在 [Error logs](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server) 中找到相关信息。
2. 将 SQL Server Instance Name 作为 **Database** name 输入。使用上方列出的查找 host name 的相同步骤查找此名称。
    - 如果在这些位置都看不到 instance name，则 database 使用默认的 `MSSQLSERVER` instance name。
3. 输入你的 **User** account name 或 ID。
4. 输入你的 **Password**。
5. 对于 **Port**：
    - SQL Server 默认使用 `1433`。
    - 如果无法通过 1433 端口连接，请在 [Error logs](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server) 中查找短语 `Server is listening on`，以确定应输入的端口号。
6. 只有当多个 domains 中的 users 访问你的 database 时，才需要输入 **Domain** name。运行此 SQL query 获取 domain name：

    ```sql
    SELECT DEFAULT_DOMAIN()[DomainName];
    ```

7. 选择是否使用 **TLS**。
8. 选择是否 **Ignore SSL Issues**：如果开启，即使 SSL certificate validation 失败，credential 也会连接。
9. 输入 n8n 尝试完成初始连接后断开的毫秒数，作为 **Connect Timeout**。更多信息请参考 [SqlConnection.ConnectionTimeout property documentation](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectiontimeout)。
    - SQL Server 以秒存储此 timeout，而 n8n 以毫秒存储。如果你复制 SQL Server defaults，请在此处输入数字前乘以 100。
10. 输入 n8n 在给定 request 上等待多久后 timeout 的毫秒数，作为 **Request Timeout**。这基本上是 query timeout 参数。更多信息请参考 [Troubleshoot query time-out errors](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-query-timeouts#explanation)。
11. 从 **TDS Version** 下拉菜单中选择要使用的 Tabular Data Stream (TDS) protocol。如果 server 不支持你在此处选择的版本，connection 会使用协商得到的替代版本。有关 TDS versions 与不同 SQL Server versions 和 .NET frameworks 兼容性的更详细拆解，请参考 [Appendix A: Product Behavior](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tds/135d0ebe-5c4c-4a94-99bf-1811eccb9f4a)。选项包括：
    - **7_4 (SQL Server 2012 ~ 2019)**：TDS version 7.4。
    - **7_3_B (SQL Server 2008R2)**：TDS version 7.3.B。
    - **7_3_A (SQL Server 2008)**：TDS version 7.3.A。
    - **7_2 (SQL Server 2005)**：TDS version 7.2。
    - **7_1 (SQL Server 2000)**：TDS version 7.1。
