---
title: Postgres node common issues
description: >-
  n8n 中 Postgres node 的常见问题文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Postgres node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues
layout:
  description:
    visible: false
---

# Postgres node common issues <a href="#postgres-node-common-issues" id="postgres-node-common-issues"></a>

这里列出 [Postgres node](README.md) 的一些常见错误和问题，以及解决或排查步骤。

## 使用参数动态填充 SQL `IN` group <a href="#dynamically-populate-sql-in-groups-with-parameters" id="dynamically-populate-sql-in-groups-with-parameters"></a>

在 Postgres 中，你可以使用 SQL [`IN` comparison construct](https://www.postgresql.org/docs/current/functions-comparisons.html#FUNCTIONS-COMPARISONS-IN-SCALAR) 在多组值之间进行比较：

```sql
SELECT color, shirt_size FROM shirts WHERE shirt_size IN ('small', 'medium', 'large');
```

虽然可以在查询中使用 n8n [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 动态填充 `IN` group 中的值，但将其与 [query parameters](README.md#use-query-parameters) 结合使用，可以通过自动清理输入提供额外保护。

要使用 query parameters 构造 `IN` group 查询：

1. 将 **Operation** 设置为 **Execute Query**。
2. 在 **Options** 中，选择 **Query Parameters**。
3. 使用表达式从输入数据中选择一个数组。例如 `{{ $json.input_shirt_sizes }}`。
4. 在 **Query** 参数中，使用带空括号集的 `IN` construct 编写查询。例如：
	```sql
	SELECT color, shirt_size FROM shirts WHERE shirt_size IN ();
	```
5. 在 `IN` 括号内部，使用表达式为查询参数数组中的 item 数量动态创建基于索引的 placeholder（例如 `$1`、`$2` 和 `$3`）。由于 placeholder 变量从 1 开始编号，你可以将每个数组索引加一来实现：
	```sql
	SELECT color, shirt_size FROM shirts WHERE shirt_size IN ({{ $json.input_shirt_sizes.map((i, pos) => "$" + (pos+1)).join(', ') }});
	```

使用此技巧时，n8n 会根据数组中的 item 数量，自动为 `IN` 值创建正确数量的 [prepared statement placeholders](https://www.postgresql.org/docs/current/sql-prepare.html)。

## 处理 timestamp 和 time zone <a href="#working-with-timestamps-and-time-zones" id="working-with-timestamps-and-time-zones"></a>

为避免 n8n 和 Postgres 解释 timestamp 与 time zone 数据时出现复杂情况，请遵循以下通用建议：

- **存储和传递日期时使用 UTC**：使用 UTC 有助于避免在不同表示和系统之间转换日期时产生时区混淆。
- **设置执行时区**：使用[环境变量](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone)（自托管）或[设置](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/configure-cloud/set-your-timezone)（n8n Cloud）设置 n8n 的全局时区。你可以在 [workflow settings](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/configure-workflow-settings) 中设置 workflow 专属时区。
- **使用 ISO 8601 格式**：[ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) 会用标准化字符串编码月中的日期、月份、年份、小时、分钟和秒。n8n 在 node 之间以字符串传递日期，并使用 [Luxon](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/handle-special-data-types/work-with-dates-and-times) 解析日期。如果需要显式转换为 ISO 8601，可以使用 [Date & Time node](../../core-nodes/n8n-nodes-base.datetime.md)，并将自定义格式设置为字符串 `yyyy-MM-dd'T'HH:mm:ss`。

## 将 Date 列输出为日期字符串而不是 ISO datetime 字符串 <a href="#outputting-date-columns-as-date-strings-instead-of-iso-datetime-strings" id="outputting-date-columns-as-date-strings-instead-of-iso-datetime-strings"></a>

n8n 使用 [`pg` package](https://www.npmjs.com/package/pg) 与 Postgres 集成，这会影响 n8n 处理 Postgres 中 date、timestamp 和相关类型的方式。

默认情况下，`pg` package 会将 `DATE` 值解析为 `new Date(row_value)`，这会生成一个遵循 [ISO 8601 datetime string](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) 格式的日期。例如，根据实例的时区设置，日期 `2025-12-25` 可能会生成 datetime string `2025-12-25T23:00:00.000Z`。

要绕过此问题，请使用 [Postgres `TO_CHAR` function](https://www.postgresql.org/docs/current/functions-formatting.html#FUNCTIONS-FORMATTING) 在查询时将日期格式化为预期格式：

```sql
SELECT TO_CHAR(date_col, 'YYYY-MM-DD') AS date_col_as_date FROM table_with_date_col
```

这会生成不包含时间或时区组件的日期字符串。继续前面的示例，使用此转换时，日期 `2025-12-25` 会生成字符串 `2025-12-25`。你可以在 [`pg` package documentation on dates](https://node-postgres.com/features/types#date--timestamp--timestamptz) 中了解更多信息。
