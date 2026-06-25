---
contentType: howto
nodeTitle: Expressions versus data nodes
originalFilePath: data/expressions.md
originalUrl: 'https://docs.n8n.io/data/expressions'
url: 'https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes'
layout:
  description:
    visible: false
---

# Expressions 与 data nodes 对比 <a href="#expressions-versus-data-nodes" id="expressions-versus-data-nodes"></a>

n8n 提供多种处理和转换数据的方式。理解何时使用每种方式，有助于构建高效工作流。

| 方式 | 适用场景 | 示例 | 可用范围 |
|---|---|---|---|
| Expressions | 使用现有数据设置单个参数值 | 提取 `{{$json.city}}`、格式化日期、简单数学计算 | Cloud 和 Self-hosted |
| Code node | 为复杂转换编写完整 JavaScript/Python | 重组数据、遍历 item、使用外部库 | Cloud 和 Self-hosted |
| AI Transform node | 从自然语言生成转换代码 | `Group by user and sum totals`、`categorize by sentiment` | 仅 Cloud |
| 其他 data transformation nodes | 通过可视化界面执行常见操作 | 聚合 item、拆分数组、排序数据、移除重复项 | Cloud 和 Self-hosted |

### Expressions <a href="#expressions" id="expressions"></a>

Expression 是一些类似 JavaScript 的小段代码，你可以使用 n8n 的 `{{ ... }}` 语法直接放入 node 参数中。它们可以使用前序 node 的数据、工作流元数据或环境变量，动态设置参数值。

{% hint style="info" %}
**能用 expression 时优先使用**

Expression 的优势是可以立即预览计算值，因此应尽量使用 expression。
{% endhint %}

**何时使用 expression：**

* 从前序 node 数据中提取值。例如 `{{$json.body.city}}`。
* 直接在字段中执行轻量转换或计算。
* 避免添加额外 node，并让逻辑贴近你正在设置的参数。

### Code node <a href="#code-node" id="code-node"></a>

[Code node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 是一个专用 node，你可以在其中编写作为工作流步骤运行的 JavaScript 或 Python。它允许你访问前序 node 的传入数据，并通过添加、移除或更新 item 来操作这些数据。你可以创建任何需要的自定义函数，并通过 `$` 语法使用 n8n 内置方法和变量。

**何时使用 Code node：**

* 你需要比 expression 更复杂的逻辑或数据转换，例如重组数组和对象、聚合或拆分 item，以及自定义算法。
* 你希望一次转换多个 item。
* 你希望使用 promise、`console.log`，或在自托管环境中使用外部 npm 模块。

### AI Transform node <a href="#ai-transform-node" id="ai-transform-node"></a>

此 node 会基于简短自然语言 prompt 生成代码片段。它具备上下文感知能力，理解工作流中的 node 和数据类型。生成的代码在该 node 中是只读的；你可以将其复制到 Code node 中编辑。

**何时使用 AI Transform node：**

* 你知道想要什么转换，但不想手写代码。
* 你希望 AI 起草转换逻辑，然后直接在该 node 中运行，或复制到 Code node 中进一步自定义。

### Other data transformation nodes <a href="#other-data-transformation-nodes" id="other-data-transformation-nodes"></a>

n8n 提供了一组用于转换数据的 node：

* [Aggregate](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.aggregate)：获取独立 item 或其部分内容，并将其分组为单独 item。
* [Limit](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.limit)：移除超出指定最大数量的 item。
* [Remove Duplicates](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.removeduplicates)：识别并删除在所有字段或部分字段上相同的 item。
* [Sort](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.sort)：按所需顺序组织列表，或生成随机选择。
* [Split Out](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.splitout)：将包含列表的单个 data item 拆分为多个 item。
* [Summarize](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.summarize)：以类似 Excel 数据透视表的方式聚合 item。

**何时使用 data transformation nodes：**

* 你需要的操作符合某个特定 transformation node 的用途。
* 你希望使用带引导 UI 的 no-code 方案。
* 相比编写 expression 或代码，你更偏好可视化构建工作流。
