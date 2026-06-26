---
title: Supabase node common issues
contentType:
  - integration
  - reference
priority: high
nodeTitle: Supabase node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues
description: >-
  n8n 中 Supabase node 的常见问题文档。包含问题详情和建议解决方案。
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

# Common issues

这里列出 [Supabase node](./) 的一些常见错误和问题，以及解决或排查步骤。

## Filtering rows by metadata <a href="#filtering-rows-by-metadata" id="filtering-rows-by-metadata"></a>

要按 [Supabase metadata](https://supabase.com/docs/guides/ai/python/metadata) 过滤行，请将 **Select Type** 设置为 **String**。

之后，你可以在 **Filters (String)** 参数中构造查询，使用受 [MongoDB selectors](https://www.mongodb.com/docs/manual/reference/operator/query/) 格式启发的 [Supabase metadata query language](https://supabase.com/docs/guides/ai/python/metadata#metadata-query-language) 来过滤 metadata。使用 [Postgres `->>` arrow JSON operator](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING) 访问 metadata 属性，如下所示（花括号表示需要填写的组件）：

```
metadata->>{your-property}={comparison-operator}.{comparison-value}
```

例如，要访问 metadata 中的 `age` 属性，并返回大于或等于 21 的结果，可以在 **Filters (String)** 字段中输入以下内容：

```
metadata->>age=gte.21
```

你可以组合这些 operator 来构造更复杂的查询。

## Can't connect to a local Supabase database when using Docker <a href="#cant-connect-to-a-local-supabase-database-when-using-docker" id="cant-connect-to-a-local-supabase-database-when-using-docker"></a>

当你在 Docker 中运行 Supabase 时，需要配置网络，以便 n8n 可以连接到 Supabase。

解决方案取决于你托管这两个组件的方式。

### 如果只有 Supabase 在 Docker 中 <a href="#if-only-supabase-is-in-docker" id="if-only-supabase-is-in-docker"></a>

如果只有 Supabase 在 Docker 中运行，[self-hosting guide](https://supabase.com/docs/guides/self-hosting/docker) 使用的 Docker Compose 文件已经让 Supabase 绑定到正确的接口。

配置 [Supabase credentials](../../credentials/supabase.md) 时，`localhost` 地址应该可以正常工作（将 **Host** 设置为 `localhost`）。

### If Supabase and n8n are running in separate Docker containers <a href="#if-supabase-and-n8n-are-running-in-separate-docker-containers" id="if-supabase-and-n8n-are-running-in-separate-docker-containers"></a>

如果 n8n 和 Supabase 都在 Docker 中运行，但位于不同容器中，可以使用 Docker networking 将它们连接起来。

将 Supabase 配置为在容器内部绑定到 `0.0.0.0`，以监听所有接口（官方 [Docker compose configuration](https://supabase.com/docs/guides/self-hosting/docker) 已经这样配置）。如果你还没有在同一个 Docker Compose 文件中一起管理它们，请将 Supabase 和 n8n 组件添加到同一个[用户定义 bridge network](https://docs.docker.com/engine/network/drivers/bridge/)。

配置 [Supabase credentials](../../credentials/supabase.md) 时，使用 Supabase API gateway 容器名称（默认为 `supabase-kong`）作为 host 地址，而不是 `localhost`。例如，如果你使用默认配置，应将 **Host** 设置为 `http://supabase-kong:8000`。

## Records are accessible through Postgres but not Supabase <a href="#records-are-accessible-through-postgres-but-not-supabase" id="records-are-accessible-through-postgres-but-not-supabase"></a>

如果使用 Supabase node 查询 record 时返回空结果，但可以通过 [Postgres](../n8n-nodes-base.postgres/) node 或 Postgres client 访问这些 record，可能是 Supabase 的 [Row Level Security (RLS)](https://supabase.com/docs/guides/database/postgres/row-level-security) policy 存在冲突。

当你使用 Table Editor 在 public schema 中创建表时，Supabase 总是会启用 RLS。RLS 处于活动状态时，在你创建 policy 之前，API 不会使用 public `anon` key 返回任何数据。这是一项安全措施，用于确保你只暴露有意暴露的数据。

要以 `anon` 角色访问启用了 RLS 的表中的数据，请[创建 policy](https://supabase.com/docs/guides/database/postgres/row-level-security#creating-policies)，以启用你打算使用的访问模式。
