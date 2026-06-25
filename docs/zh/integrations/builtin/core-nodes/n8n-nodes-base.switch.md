---
title: Switch
description: >-
  n8n 中 Switch node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Switch
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.switch.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch'
layout:
  description:
    visible: false
---

# Switch <a href="#switch" id="switch"></a>

使用 Switch node 基于比较操作有条件地路由 workflow。它类似 [IF](n8n-nodes-base.if.md) node，但支持多个输出路由。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

选择此 node 应使用的 **Mode**：

* **Rules**：选择此 mode，为每个输出构建匹配规则。
* **Expression**：选择此 mode，编写 expression 以编程方式返回输出索引。

Node 配置取决于你选择的 **Mode**。

### Rules <a href="#rules" id="rules"></a>

要使用此操作配置 node，请使用以下参数：

* 创建 **Routing Rules** 以定义比较条件。
    * 使用数据类型下拉菜单为条件选择数据类型和比较操作类型。例如，要创建晚于特定日期的日期规则，请选择 **Date & Time > is after**。
    * 需要在条件中输入的字段和值会根据你选择的数据类型和比较方式而变化。完整的数据类型比较列表请参阅[可用的数据类型比较](#available-data-type-comparisons)。
* **Rename Output**：开启此控件可重命名用于放入匹配数据的输出字段。输入所需的 **Output Name**。

选择 **Add Routing Rule** 添加更多规则。

#### Rule 选项 <a href="#rule-options" id="rule-options"></a>

你可以使用这些 **Options** 进一步配置此操作：

- **Fallback Output**：选择当 item 不匹配任何规则或条件时如何路由 workflow。
    - **None**：忽略该 item。这是默认行为。
    - **Extra Output**：将 item 发送到额外的单独输出。
    - **Output 0**：将 item 发送到与第一条规则匹配项相同的输出。
- **Ignore Case**：设置评估条件时是否忽略字母大小写（开启），或强制匹配大小写（关闭）。
- **Less Strict Type Validation**：设置是否希望 n8n 根据你选择的 operator 尝试转换值类型（开启），或不转换（关闭）。
- **Send data to all matching outputs**：设置是否将数据发送到所有满足条件的输出（开启），或仅发送到第一个匹配条件的输出（关闭）。

### Expression <a href="#expression" id="expression"></a>

要使用此操作配置 node，请使用以下参数：

- **Number of Outputs**：设置此 node 应具有的输出数量。
- **Output Index**：创建 expression，用于计算每个输入 item 应路由到哪个输出。该 expression 必须返回一个数字。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Switch 集成模板](https://n8n.io/integrations/switch)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用条件创建复杂 n8n 逻辑的更多信息，请参阅[使用条件拆分](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/split-with-conditionals)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/bMMOCQFbQ4YpKDnWQQOg/" %}
