---
contentType: howto
nodeTitle: Filter out unwanted data
originalFilePath: data/data-filtering.md
originalUrl: 'https://docs.n8n.io/data/data-filtering'
url: 'https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data'
layout:
  description:
    visible: false
---

# 筛选数据 <a href="#filtering-data" id="filtering-data"></a>

在 n8n 中，filtering 会根据你的目标表示不同含义。本指南同时介绍 UI 中的可视化筛选，以及 workflow execution 期间的数据筛选。

## 在 UI 中可视化筛选数据 <a href="#filter-data-visually-in-the-ui" id="filter-data-visually-in-the-ui"></a>

{% hint style="info" %}
**功能可用性**

适用于 Community、Cloud Pro 和 Enterprise 计划。
{% endhint %}

在 node 的 **INPUT** 和 **OUTPUT** 面板中搜索和筛选数据。你可以用它检查 node 数据并查找特定 item。

如需搜索：

1. 在 node 中，在 **INPUT** 或 **OUTPUT** 面板选择 **Search** <img src="../../../build/.gitbook/assets/search.png" alt="Search icon" data-size="line">。
1. 输入搜索词。

n8n 会在你输入时实时筛选，显示包含该词的对象或行。

筛选只是视觉层面的：n8n 不会更改或删除数据。关闭并重新打开 node 后，filter 会重置。

## 在 workflow execution 期间筛选数据 <a href="#filter-data-during-workflow-execution" id="filter-data-during-workflow-execution"></a>

如需在工作流中实际移除或筛选数据，请使用以下方式：

### 筛除 item <a href="#filter-out-items" id="filter-out-items"></a>

如需基于条件从工作流中移除整个 item，请使用 [Filter node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.filter)。此 node 会评估条件，并只传递符合条件的 item。

### 筛除字段 <a href="#filter-out-fields" id="filter-out-fields"></a>

如需从 item 或对象中移除特定字段，同时保留 item 本身，请使用 [Edit Fields (Set) node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.set)。将其配置为移除不需要的字段。

### 筛选数组元素 <a href="#filter-array-elements" id="filter-array-elements"></a>

如需筛选 item 内数组中的元素，请在 expression 或 Code node 中使用 `.filter()` 方法。例如：

```javascript
{{ $json.myArray.filter(item => item.value > 10) }}
```

这会移除不符合条件的数组元素，同时保留 item 结构。

### 筛除先前 execution 中的重复 item <a href="#filter-out-duplicate-items-from-previous-executions" id="filter-out-duplicate-items-from-previous-executions"></a>

如需移除工作流先前 execution 中已出现过的 item，请使用 [Remove Duplicates](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.removeduplicates) node。当某个事件多次触发但你只想处理第一次出现时，可以使用此方式。
