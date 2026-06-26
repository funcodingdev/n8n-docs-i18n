---
title: Postgres node documentation
description: >-
  了解如何在 n8n 中使用 Postgres node。按照技术文档将 Postgres node 集成到你的工作流中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: n8n-nodes-base.postgres
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres'
layout:
  description:
    visible: false
---

# Postgres node <a href="#postgres-node" id="postgres-node"></a>

使用 Postgres node 自动化 Postgres 中的工作，并将 Postgres 与其他应用集成。n8n 内置支持大量 Postgres 功能，包括执行查询，以及在数据库中插入和更新行。

在本页中，你可以找到 Postgres node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [Postgres credentials](../../credentials/postgres.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Operations 操作 <a href="#operations" id="operations"></a>

* [**Delete**](#delete)：删除整张表或表中的行
* [**Execute Query**](#execute-query)：执行 SQL 查询
* [**Insert**](#insert)：向表中插入行
* [**Insert or Update**](#insert-or-update)：插入或更新表中的行
* [**Select**](#select)：从表中选择行
* [**Update**](#update)：更新表中的行

### Delete <a href="#delete" id="delete"></a>

使用此操作删除整张表或表中的行。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Delete**。
- **Schema**：选择包含要操作表的 schema。选择 **From list** 可从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的表。选择 **From list** 可从下拉列表中选择表，或选择 **By Name** 输入表名。
- **Command**：要执行的删除动作：
	- **Truncate**：移除表数据，但保留表结构。
		- **Restart Sequences**：是否在 Truncate 过程中将自增列重置为初始值。
	- **Delete**：删除匹配 "Select Rows" 条件的行。如果未选择任何内容，Postgres 会删除所有行。
		- **Select Rows**：定义用于匹配行的 **Column**、**Operator** 和 **Value**。
		- **Combine Conditions**：如何组合 "Select Rows" 中的条件。**AND** 要求所有条件为 true，而 **OR** 只要求至少一个条件为 true。
	- **Drop**：永久删除表的数据和结构。

#### Delete options <a href="#delete-options" id="delete-options"></a>

- **Cascade**：是否同时 drop 所有依赖此表的对象，例如 view 和 sequence。使用 **Truncate** 或 **Drop** command 时可用。
- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。

### Execute Query <a href="#execute-query" id="execute-query"></a>

使用此操作执行 SQL 查询。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Execute Query**。
- **Query**：要执行的 SQL 查询。你可以使用 n8n [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 和 `$1`、`$2`、`$3` 等 token 来构建 [prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html)，以便配合 [query parameters](#use-query-parameters) 使用。

#### Execute Query options <a href="#execute-query-options" id="execute-query-options"></a>

- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Query Parameters**：要用作 [query parameters](#use-query-parameters) 的逗号分隔值列表。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。
- **Replace Empty Strings with NULL**：是否将输入中的空字符串替换为 NULL。处理从电子表格软件导出的数据时，这可能很有用。

### Insert <a href="#insert" id="insert"></a>

使用此操作向表中插入行。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Insert**。
- **Schema**：选择包含要操作表的 schema。选择 **From list** 可从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的表。选择 **From list** 可从下拉列表中选择表，或选择 **By Name** 输入表名。
- **Mapping Column Mode**：如何将列名映射到传入数据：
	- **Map Each Column Manually**：选择每列要使用的值。
	- **Map Automatically**：自动将传入数据映射到 Postgres 中匹配的列名。要使此模式生效，传入数据字段名必须与 Postgres 中的列名匹配。如有需要，请考虑在此 node 之前使用 [edit fields (set) node](../../core-nodes/n8n-nodes-base.set.md) 调整格式。

#### Insert options <a href="#insert-options" id="insert-options"></a>

- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Output Columns**：选择要输出的列。你可以从可用列列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。
- **Skip on Conflict**：如果 insert 违反 unique 或 exclusion constraint，是否跳过该行而不是抛出错误。
- **Replace Empty Strings with NULL**：是否将输入中的空字符串替换为 NULL。处理从电子表格软件导出的数据时，这可能很有用。

### Insert or Update <a href="#insert-or-update" id="insert-or-update"></a>

使用此操作插入或更新表中的行。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Insert or Update**。
- **Schema**：选择包含要操作表的 schema。选择 **From list** 可从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的表。选择 **From list** 可从下拉列表中选择表，或选择 **By Name** 输入表名。
- **Mapping Column Mode**：如何将列名映射到传入数据：
	- **Map Each Column Manually**：选择每列要使用的值。
	- **Map Automatically**：自动将传入数据映射到 Postgres 中匹配的列名。要使此模式生效，传入数据字段名必须与 Postgres 中的列名匹配。如有需要，请考虑在此 node 之前使用 [edit fields (set) node](../../core-nodes/n8n-nodes-base.set.md) 调整格式。

#### Insert or Update options <a href="#insert-or-update-options" id="insert-or-update-options"></a>

- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Output Columns**：选择要输出的列。你可以从可用列列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。
- **Replace Empty Strings with NULL**：是否将输入中的空字符串替换为 NULL。处理从电子表格软件导出的数据时，这可能很有用。

### Select <a href="#select" id="select"></a>

使用此操作选择表中的行。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Select**。
- **Schema**：选择包含要操作表的 schema。选择 **From list** 可从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的表。选择 **From list** 可从下拉列表中选择表，或选择 **By Name** 输入表名。
- **Return All**：是返回所有结果，还是只返回给定限制内的结果。
- **Limit**：禁用 **Return All** 时要返回的最大 item 数。
- **Select Rows**：设置选择行的条件。定义用于匹配行的 **Column**、**Operator** 和 **Value**。如果未选择任何内容，Postgres 会选择所有行。
- **Combine Conditions**：如何组合 **Select Rows** 中的条件。**AND** 要求所有条件为 true，而 **OR** 只要求至少一个条件为 true。
- **Sort**：选择如何排序选中的行。从列表或按 ID 选择一个 **Column**，并选择排序 **Direction**。

#### Select options <a href="#select-options" id="select-options"></a>

- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Output Columns**：选择要输出的列。你可以从可用列列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。

### Update <a href="#update" id="update"></a>

使用此操作更新表中的行。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Postgres credential](../../credentials/postgres.md)。
- **Operation**：选择 **Update**。
- **Schema**：选择包含要操作表的 schema。选择 **From list** 可从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的表。选择 **From list** 可从下拉列表中选择表，或选择 **By Name** 输入表名。
- **Mapping Column Mode**：如何将列名映射到传入数据：
	- **Map Each Column Manually**：选择每列要使用的值。
	- **Map Automatically**：自动将传入数据映射到 Postgres 中匹配的列名。要使此模式生效，传入数据字段名必须与 Postgres 中的列名匹配。如有需要，请考虑在此 node 之前使用 [edit fields (set) node](../../core-nodes/n8n-nodes-base.set.md) 调整格式。

#### Update options <a href="#update-options" id="update-options"></a>

- **Connection Timeout**：尝试连接数据库的秒数。
- **Delay Closing Idle Connection**：在将 idle connection 视为可关闭之前等待的秒数。
- **Query Batching**：向数据库发送查询的方式：
	- **Single Query**：对所有传入 item 使用单个查询。
	- **Independently**：为执行中的每个传入 item 执行一个查询。
	- **Transaction**：在 transaction 中执行所有查询。如果发生失败，Postgres 会回滚所有更改。
- **Output Columns**：选择要输出的列。你可以从可用列列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Output Large-Format Numbers As**：输出 `NUMERIC` 和 `BIGINT` 列的格式：
	- **Numbers**：用于标准数字。
	- **Text**：如果预期数字超过 16 位，请使用此选项。否则数字可能不正确。
- **Replace Empty Strings with NULL**：是否将输入中的空字符串替换为 NULL。处理从电子表格软件导出的数据时，这可能很有用。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.postgres 集成模板](https://n8n.io/integrations/postgres) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Postgres 提供了一个 trigger node。你可以在[这里](../../trigger-nodes/n8n-nodes-base.postgrestrigger.md)找到 trigger node 文档。

## 使用查询参数 <a href="#use-query-parameters" id="use-query-parameters"></a>

创建要在 Postgres 数据库上运行的查询时，可以使用 **Options** 部分中的 **Query Parameters** 字段将数据加载到查询中。n8n 会清理查询参数中的数据，从而防止 SQL 注入。

例如，你想通过电子邮件地址查找一个人。给定以下输入数据：

```js
[
    {
        "email": "alex@example.com",
        "name": "Alex",
        "age": 21
    },
    {
        "email": "jamie@example.com",
        "name": "Jamie",
        "age": 33
    }
]
```

你可以编写如下查询：

```sql
SELECT * FROM $1:name WHERE email = $2;
```

然后在 **Query Parameters** 中提供要使用的字段值。你可以提供固定值或表达式。在此示例中，使用表达式，以便 node 可以依次从每个输入 item 中提取电子邮件地址：

```js
// users is an example table name
{{ [ 'users', $json.email ] }}
```

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或错误以及建议解决方案，请参阅[常见问题](common-issues.md)。
