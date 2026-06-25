---
title: SQL AI Agent node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 SQL Agent。按照技术文档将 SQL Agent
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: SQL AI Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent
layout:
  description:
    visible: false
---

# SQL AI Agent node <a href="#sql-ai-agent-node" id="sql-ai-agent-node"></a>

{% hint style="info" %}
**功能已移除**

n8n 已在 2025 年 2 月移除此功能。
{% endhint %}

SQL Agent 使用 SQL 数据库作为数据源。它可以理解自然语言问题，将其转换为 SQL 查询，执行查询，并以用户友好的格式展示结果。此 agent 适合为数据库构建自然语言接口。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](README.md)。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 SQL Agent。

### Data Source <a href="#data-source" id="data-source"></a>

选择 node 要用作数据源的数据库。选项包括：

* **MySQL**：选择此选项以使用 MySQL 数据库。
    * 还需要选择 **Credential for MySQL**。
* **SQLite**：选择此选项以使用 SQLite 数据库。
    * 你必须在 Agent 之前添加 [Read/Write File From Disk](../../../core-nodes/n8n-nodes-base.readwritefile.md) node，以读取你的 SQLite 文件。
    * 还需要输入来自 Read/Write File From Disk node 的 SQLite 文件的 **Input Binary Field** 名称。
* **Postgres**：选择此选项以使用 Postgres 数据库。
    * 还需要选择 **Credential for Postgres**。

{% hint style="warning" %}
**Postgres 和 MySQL Agents**

如果你使用 [Postgres](../../../credentials/postgres.md) 或 [MySQL](../../../credentials/mysql.md)，此 agent 不支持 credential tunnel 选项。
{% endhint %}

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 SQL Agent node 的行为：

### Ignored Tables <a href="#ignored-tables" id="ignored-tables"></a>

如果你希望 node 忽略数据库中的某些表，请输入要忽略的表的逗号分隔列表。

如果留空，agent 不会忽略任何表。

### Include Sample Rows <a href="#include-sample-rows" id="include-sample-rows"></a>

输入要包含在给 agent 的 prompt 中的 sample row 数量。默认值为 `3`。

Sample rows 可帮助 agent 理解数据库 schema，但也会增加使用的 token 数量。

### Included Tables <a href="#included-tables" id="included-tables"></a>

如果你只想包含数据库中的特定表，请输入要包含的表的逗号分隔列表。

如果留空，agent 会包含所有表。

### Prefix Prompt <a href="#prefix-prompt" id="prefix-prompt"></a>

输入要在 **Prompt** 文本之前发送给 agent 的消息。此初始消息可以为 agent 提供更多上下文和指导，说明它能做什么、不能做什么，以及如何设置响应格式。

n8n 会用一个示例填充此字段。

### Suffix Prompt <a href="#suffix-prompt" id="suffix-prompt"></a>

输入要在 **Prompt** 文本之后发送给 agent 的消息。

可用的 LangChain expressions：

* `{chatHistory}`：此对话中的消息历史，对维护上下文很有用。
* `{input}`：包含用户 prompt。
* `{agent_scratchpad}`：用于在下一次迭代中记住的信息。

n8n 会用一个示例填充此字段。

### Limit <a href="#limit" id="limit"></a>

输入要返回的最大结果数。

默认值为 `10`。

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。
