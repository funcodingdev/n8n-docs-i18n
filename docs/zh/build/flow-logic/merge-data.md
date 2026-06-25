---
contentType: howto
description: 在 n8n 工作流中合并数据流。
nodeTitle: Merge data
originalFilePath: flow-logic/merging.md
originalUrl: 'https://docs.n8n.io/flow-logic/merging'
url: 'https://docs.n8n.io/build/flow-logic/merge-data'
layout:
  description:
    visible: false
---

# 合并数据 <a href="#merging-data" id="merging-data"></a>

合并会将多个数据流汇集在一起。你可以根据工作流需求，使用不同节点实现这一点。

- 合并来自不同数据流或节点的数据：使用 [Merge](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.merge) 节点，将来自多个来源的数据合并为一个。
- 合并来自多次节点执行的数据：在需要合并某个节点多次执行或多个节点产生的数据时，使用 [Code](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 节点处理复杂场景。
- 比较并合并数据：使用 [Compare Datasets](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.comparedatasets) 节点，根据比较结果比较、合并并输出数据流。

下面各节会更详细地介绍每种方法。

## 合并来自不同数据流的数据 <a href="#merge-data-from-different-data-streams" id="merge-data-from-different-data-streams"></a>

如果工作流发生了[拆分](split-with-conditionals.md)，你可以将分离的数据流重新合并为一个数据流。

这里有一个[示例工作流](https://n8n.io/workflows/1747-joining-different-datasets/)，展示不同类型的合并：追加数据集、只保留新 items，以及只保留已有 items。[Merge node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.merge) 文档包含每种合并操作的详细信息。

{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/1747" %}

## 合并来自不同节点的数据 <a href="#merge-data-from-different-nodes" id="merge-data-from-different-nodes"></a>

你可以使用 Merge node 合并来自两个前置节点的数据，即使工作流没有拆分成多个独立数据流。如果你想基于多个节点生成的数据创建单个数据集，这会很有用。

<figure>
<img src="../../../build/.gitbook/assets/merge-node-data.png" alt="">
<figcaption>合并来自两个前置节点的数据</figcaption>
</figure>

## 合并来自多次节点执行的数据 <a href="#merge-data-from-multiple-node-executions" id="merge-data-from-multiple-node-executions"></a>

使用 Code node 合并来自多次节点执行的数据。这在某些[循环](loop.md)场景中很有用。

{% hint style="info" %}
**节点执行和工作流执行**

本节介绍如何合并来自多次节点执行的数据。这指的是一个节点在单次工作流执行期间执行多次的情况。
{% endhint %}
请参考这个使用 Loop Over Items 和 Wait 人为创建多次执行的[示例工作流](https://n8n.io/workflows/1814-merge-multiple-runs-into-one/)。

{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/1814" %}

## 比较、合并并再次拆分 <a href="#compare-merge-and-split-again" id="compare-merge-and-split-again"></a>

[Compare Datasets](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.comparedatasets) 节点会在合并前比较数据流。它最多输出四个不同的数据流。

示例请参阅这个[示例工作流](https://n8n.io/workflows/1943-comparing-data-with-the-compare-datasets-node/)。

{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/1943" %}
