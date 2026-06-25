---
title: Oracle Database node documentation
description: >-
  了解如何在 n8n 中使用 Oracle Database node。按照技术文档将 Oracle Database node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: App nodes
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.oracledb/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb'
layout:
  description:
    visible: false
---

# Oracle Database node <a href="#oracle-database-node" id="oracle-database-node"></a>

使用 Oracle Database node 自动化 Oracle Database 中的工作，并将 Oracle Database 与其他应用集成。n8n 内置支持大量 Oracle Database 功能，包括执行 SQL statement，以及从 Oracle Database 获取、插入、更新或删除数据。此 node 内部使用 [node-oracledb driver](https://github.com/oracle/node-oracledb)。

在本页中，你可以找到 Oracle Database node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
有关设置身份验证的指导，请参阅 [Oracle Database credentials](../credentials/oracledb.md)。

要求 Oracle Database **19c 或更高版本**。
对于 Transparent Application Continuity (TAC) 和 Sharding 等高级 Oracle Database 功能，还要求 Oracle Client Libraries **19c 或更高版本**。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* [**Delete**](#delete)：删除整个 table 或 table 中的 row
* [**Execute SQL**](#execute-sql)：执行 SQL statement
* [**Insert**](#insert)：向 table 插入 row
* [**Insert or Update**](#insert-or-update)：插入或更新 table 中的 row
* [**Select**](#select)：从 table 中选择 row
* [**Update**](#update)：更新 table 中的 row

### Delete <a href="#delete" id="delete"></a>

使用此操作删除整个 table 或 table 中的 row。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：选择 **Delete**。
- **Schema**：选择包含要操作 table 的 schema。选择 **From list** 从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的 table。选择 **From list** 从下拉列表中选择 table，或选择 **By Name** 输入 table 名称。
- **Command**：要执行的删除动作：
    - **Truncate**：移除 table 的数据，但保留 table 结构。
    - **Delete**：删除匹配 "Select Rows" 条件的 row。如果不选择任何内容，Oracle Database 会删除所有 row。
        - **Select Rows**：定义用于匹配 row 的 **Column**、**Operator** 和 **Value**。该值可以使用 expression 或字符串以 JSON 形式传入。
        - **Combine Conditions**：如何组合 "Select Rows" 中的条件。**AND** 要求所有条件都为 true，而 **OR** 要求至少一个条件为 true。
    - **Drop**：永久删除 table 的数据和结构。

#### Delete 选项 <a href="#delete-options" id="delete-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Statement Batching**：向数据库发送 statement 的方式：
    - **Single Statement**：对所有传入 item 使用单个 statement。
    - **Independently**：对 execution 的每个传入 item 执行一个 statement。
    - **Transaction**：在一个 transaction 中执行所有 statement。如果发生失败，Oracle Database 会回滚所有更改。

### Execute SQL <a href="#execute-sql" id="execute-sql"></a>

使用此操作执行 SQL statement。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：执行 SQL **Execute SQL**。
- **Statement**：要执行的 SQL statement。你可以使用 n8n [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes)，以及 `:1`、`:2` 这样的 positional parameter，或 `:name`、`:id` 这样的 named parameter，配合 [Use bind parameters](#use-bind-parameters) 使用。
要运行 PL/SQL procedure，例如 `demo`，可以使用：
```sql
BEGIN
  demo;
END;
```

#### Execute Statement 选项 <a href="#execute-statement-options" id="execute-statement-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Bind Variable Placeholder Values**：输入 statement 中使用的 bind parameter 值，参见 [Use bind parameters](#use-bind-parameters)。
- **Output Numbers As String**：表示是否应以 String 形式检索数字。
- **Fetch Array Size**：此属性是一个数字，用于设置从 Oracle Database 获取 query row 时使用的内部缓冲区大小。更改它可能影响 query 性能，但不会影响返回给应用的 row 数量。
- **Number of Rows to Prefetch**：这是一个 query 调优选项，用于设置底层 Oracle driver 在 query 内部初始 statement 执行阶段获取的额外 row 数。

### Insert <a href="#insert" id="insert"></a>

使用此操作向 table 插入 row。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：选择 **Insert**。
- **Schema**：选择包含要操作 table 的 schema。选择 **From list** 从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的 table。选择 **From list** 从下拉列表中选择 table，或选择 **By Name** 输入 table 名称。
- **Mapping Column Mode**：如何将 column name 映射到传入数据：
    - **Map Each Column Manually**：为每个 column 选择要使用的值，参见 [Use n8n expressions for bind values](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**：自动将传入数据映射到 Oracle Database 中匹配的 column name。传入数据字段名必须与 Oracle Database 中的 column name 匹配，此功能才会生效。如有必要，可以考虑在此 node 前使用 [edit fields (set) node](../core-nodes/n8n-nodes-base.set.md) 按需调整格式。

#### Insert 选项 <a href="#insert-options" id="insert-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Output Columns**：选择要输出哪些 column。你可以从可用 column 列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Statement Batching**：向数据库发送 statement 的方式：
    - **Single Statement**：对所有传入 item 使用单个 statement。
    - **Independently**：对 execution 的每个传入 item 执行一个 statement。
    - **Transaction**：在一个 transaction 中执行所有 statement。如果发生失败，Oracle Database 会回滚所有更改。

### Insert or Update <a href="#insert-or-update" id="insert-or-update"></a>

使用此操作插入或更新 table 中的 row。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：选择 **Insert or Update**。
- **Schema**：选择包含要操作 table 的 schema。选择 **From list** 从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的 table。选择 **From list** 从下拉列表中选择 table，或选择 **By Name** 输入 table 名称。
- **Mapping Column Mode**：如何将 column name 映射到传入数据：
    - **Map Each Column Manually**：为每个 column 选择要使用的值，参见 [Use n8n expressions for bind values](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**：自动将传入数据映射到 Oracle Database 中匹配的 column name。传入数据字段名必须与 Oracle Database 中的 column name 匹配，此功能才会生效。如有必要，可以考虑在此 node 前使用 [edit fields (set) node](../core-nodes/n8n-nodes-base.set.md) 按需调整格式。

#### Insert or Update 选项 <a href="#insert-or-update-options" id="insert-or-update-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Output Columns**：选择要输出哪些 column。你可以从可用 column 列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Statement Batching**：向数据库发送 statement 的方式：
    - **Single Statement**：对所有传入 item 使用单个 statement。
    - **Independently**：对 execution 的每个传入 item 执行一个 statement。
    - **Transaction**：在一个 transaction 中执行所有 statement。如果发生失败，Oracle Database 会回滚所有更改。

### Select <a href="#select" id="select"></a>

使用此操作选择 table 中的 row。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：选择 **Select**。
- **Schema**：选择包含要操作 table 的 schema。选择 **From list** 从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的 table。选择 **From list** 从下拉列表中选择 table，或选择 **By Name** 输入 table 名称。
- **Return All**：返回所有结果，还是只返回给定 limit 内的结果。
- **Limit**：禁用 **Return All** 时要返回的最大 item 数。
- **Select Rows**：设置选择 row 的条件。定义用于匹配 row 的 **Column**、**Operator** 和 **Value**（作为 `json`）。
**Value** 会因类型而异，例如在 Fixed 模式下：
    - String: "hello", hellowithoutquotes, "hello with space"
    - Number: 12
    - JSON: { "key": "val" }

如果不选择任何内容，Oracle Database 会选择所有 row。
- **Combine Conditions**：如何组合 **Select Rows** 中的条件。**AND** 要求所有条件都为 true，而 **OR** 要求至少一个条件为 true。
- **Sort**：选择如何对选中的 row 排序。从列表中选择或按 ID 选择 **Column**，并选择排序 **Direction**。

#### Select 选项 <a href="#select-options" id="select-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Output Numbers As String**：表示是否应以 String 形式检索数字。
- **Fetch Array Size**：此属性是一个数字，用于设置从 Oracle Database 获取 query row 时使用的内部缓冲区大小。更改它可能影响 query 性能，但不会影响返回给应用的 row 数量。
- **Number of Rows to Prefetch**：这是一个 query 调优选项，用于设置底层 Oracle driver 在 query 内部初始 statement 执行阶段获取的额外 row 数。

### Update <a href="#update" id="update"></a>

使用此操作更新 table 中的 row。

输入这些参数：

- **Credential to connect with**：创建或选择现有 [Oracle Database credential](../credentials/oracledb.md)。
- **Operation**：选择 **Update**。
- **Schema**：选择包含要操作 table 的 schema。选择 **From list** 从下拉列表中选择 schema，或选择 **By Name** 输入 schema 名称。
- **Table**：选择要操作的 table。选择 **From list** 从下拉列表中选择 table，或选择 **By Name** 输入 table 名称。
- **Mapping Column Mode**：如何将 column name 映射到传入数据：
    - **Map Each Column Manually**：为每个 column 选择要使用的值，参见 [Use n8n expressions for bind values](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**：自动将传入数据映射到 Oracle Database 中匹配的 column name。传入数据字段名必须与 Oracle Database 中的 column name 匹配，此功能才会生效。如有必要，可以考虑在此 node 前使用 [edit fields (set) node](../core-nodes/n8n-nodes-base.set.md) 按需调整格式。

#### Update 选项 <a href="#update-options" id="update-options"></a>

- **Auto Commit**：此属性设为 true 时，当前连接中的 transaction 会在 statement 执行结束时自动提交。
- **Output Columns**：选择要输出哪些 column。你可以从可用 column 列表中选择，或使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
- **Statement Batching**：向数据库发送 statement 的方式：
    - **Single Statement**：对所有传入 item 使用单个 statement。
    - **Independently**：对 execution 的每个传入 item 执行一个 statement。
    - **Transaction**：在一个 transaction 中执行所有 statement。如果发生失败，Oracle Database 会回滚所有更改。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [SQL Language Reference](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=SQLRF)。

有关 node-oracledb driver 的更多信息，请参阅 [node-oracledb documentation](https://node-oracledb.readthedocs.io/en/latest/)。

## 使用 bind parameters <a href="#use-bind-parameters" id="use-bind-parameters"></a>

创建要在 Oracle database instance 上运行的 statement 时，你可以使用 **Options** 区域中的 **Bind Variable Placeholder Values** 字段将数据加载到 statement 中。n8n 会清理 statement parameter 中的数据，从而防止 SQL 注入。

例如，你想按颜色查找特定水果。给定以下输入数据：

```js
[
    {
        "FRUIT_ID": 1,
        "FRUIT_NAME": "Apple",
        "COLOR": "Red"
    },
    {
        "FRUIT_ID": 2,
        "FRUIT_NAME": "Banana",
        "COLOR": "Yellow"
    }
]
```

你可以编写如下 statement：

```sql
SELECT * FROM FRUITS WHERE COLOR = :col
```

然后在 **Bind Variable Placeholder Values** 中提供要使用的字段值。你可以提供固定值或 expression。在此示例中，使用 expression，让 node 依次从每个输入 item 中提取颜色：

```js
// fruits is an example table name
fruits, {{ $json.color }}
```

## 使用 n8n Expressions 作为 bind values <a href="#use-n8n-expressions-for-bind-values" id="use-n8n-expressions-for-bind-values"></a>

对于 **Values to Send**，你可以使用 n8n Expressions 提供输入。下面是不同数据类型的示例。你可以输入常量值，也可以引用前一个 item 中的字段（`$json`）：

### JSON <a href="#json" id="json"></a>
- 常量：`{{ { k1: "v1", k2: "v2" } }}`
- 来自前一个 item：`{{ $json.COL_JSON }}`

### VECTOR <a href="#vector" id="vector"></a>
- 常量：`{{ [1, 2, 3, 4.5] }}`
- 来自前一个 item：`{{ $json.COL_VECTOR }}`

### BLOB <a href="#blob" id="blob"></a>
- 常量：`{{ [94, 87, 34] }}` 或 `{{ ' BLOB data string' }}`
- 来自前一个 item：`{{ $json.COL_BLOB }}`

### RAW <a href="#raw" id="raw"></a>
- 常量：`{{ [94, 87, 34] }}`
- 来自前一个 item：`{{ $json.COL_RAW }}`

### BOOLEAN <a href="#boolean" id="boolean"></a>
- 常量：`{{ true }}`
- 来自前一个 item：`{{ $json.COL_BOOLEAN }}`

### NUMBER <a href="#number" id="number"></a>
- 常量：`1234`
- 来自前一个 item：`{{ $json.COL_NUMBER }}`

## VARCHAR <a href="#varchar" id="varchar"></a>
- 常量：`' Hello World '`
- 来自前一个 item：`{{ $json.COL_CHAR }}`

这些示例假设 JSON key（例如 `COL_JSON`、`COL_VECTOR`）会直接映射到相应的 SQL column type。
