---
title: MySQL node documentation
description: >-
  了解如何在 n8n 中使用 MySQL node。按照技术文档将 MySQL node 集成到你的工作流中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-base.mysql
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql'
layout:
  description:
    visible: false
---

# MySQL node <a href="#mysql-node" id="mysql-node"></a>

使用 MySQL node 自动化 MySQL 中的工作，并将 MySQL 与其他应用集成。n8n 内置支持大量 MySQL 功能，包括执行 SQL 查询，以及在数据库中插入和更新行。

在本页中，你可以找到 MySQL node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [MySQL credentials](../../credentials/mysql.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Operations 操作 <a href="#operations" id="operations"></a>

* Delete
* Execute SQL
* Insert
* Insert or Update
* Select
* Update

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.mysql 集成模板](https://n8n.io/integrations/mysql) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MySQL 的 Connectors and APIs 文档](https://dev.mysql.com/doc/index-connectors.html)。

有关编写 SQL 查询的更多信息，请参阅 MySQL 的 [SELECT 语句文档](https://dev.mysql.com/doc/refman/8.4/en/select.html)。

## 使用查询参数 <a href="#use-query-parameters" id="use-query-parameters"></a>

创建要在 MySQL 数据库上运行的查询时，可以使用 **Options** 部分中的 **Query Parameters** 字段将数据加载到查询中。n8n 会清理查询参数中的数据，从而防止 SQL 注入。

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
users, {{ $json.email }}
```

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。
