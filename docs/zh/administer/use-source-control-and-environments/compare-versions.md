---
title: Compare changes with workflow diffs
description: 使用 workflow diffs 比较 local 和 remote changes
contentType: howto
nodeTitle: Compare versions
originalFilePath: source-control-environments/using/compare-changes.md
originalUrl: 'https://docs.n8n.io/source-control-environments/using/compare-changes'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions
layout:
  description:
    visible: false
---

# 使用 workflow diffs 比较 changes <a href="#compare-changes-with-workflow-diffs" id="compare-changes-with-workflow-diffs"></a>

Workflow diffs 允许你 visually compare instance 上的 workflow 与 connected Git repository 中保存的最新 version 之间的 changes。这有助于你在决定 push 或 pull 到不同 environments 前，了解 workflow 的 exact changes。

{% hint style="info" %}
**功能可用性**

- 可用于 Enterprise
- 只有在 instance 上[启用 environments features](set-up-source-control.md) 后，Workflow diffs 才可用
{% endhint %}

## 访问 workflow diffs <a href="#accessing-workflow-diffs" id="accessing-workflow-diffs"></a>

你可以从两个位置访问 workflow diffs：

1. **Pushing changes 时**：在 commit modal 中，点击要 review 的 workflow 旁边的 workflow diff icon
2. **Pulling changes 时**：在 modified changes modal 中，点击要 review 的 workflow 旁边的 workflow diff icon

## 理解 workflow diff view <a href="#understanding-the-workflow-diff-view" id="understanding-the-workflow-diff-view"></a>

打开 workflow diff 后，n8n 会垂直堆叠显示两个 workflows：

### Pushing 时 <a href="#when-pushing" id="when-pushing"></a>

* **Top panel**（Remote branch）：Git repository 中的 latest version
* **Bottom panel**（Local）：workflow 当前 locally saved version

### Pulling 时 <a href="#when-pulling" id="when-pulling"></a>

* **Top panel**（Local）：n8n instance 上的 current version
* **Bottom panel**（Remote branch）：你从 Git repository pull 的 version

在两种情况下，top panel 始终显示将被 changes update 的 workflow。

Diff view 会 highlight 三类 changes：

* **Added nodes and connectors**：New node additions 或 connectors 会显示为 green，并带有 "N" icon
* **Modified nodes and connectors**：Existing nodes 或 connectors 的 modifications 会显示为 orange，并带有 "M" icon
* **Deleted nodes and connectors**：Node 或 connector deletions 会显示为 red，并带有 "D" icon

## Review node changes <a href="#reviewing-node-changes" id="reviewing-node-changes"></a>

对于 modified nodes，你还可以 compare specific changes。点击 modified nodes 可显示 changes 的 JSON diff。你可以 review 该 node 在给定 change 前后的 exact configuration。

## 查看 changes summary <a href="#viewing-the-summary-of-changes" id="viewing-the-summary-of-changes"></a>

右上角的 **changes** button 显示 changes 数量。这表示 node、node connectors 以及 general workflow settings updates 中的 changes 总数。

## 在每个 change 之间导航 <a href="#navigating-through-each-change" id="navigating-through-each-change"></a>

你可以使用右上角的 **next** 和 **previous** arrows 按 logical order 浏览 changes。使用左上角的 **back** button 返回 commit 或 pull modal，选择不同 workflow 来 review changes。

## 谁可以使用 workflow diffs <a href="#who-can-use-workflow-diffs" id="who-can-use-workflow-diffs"></a>

只有可以为 instance push 或 pull commits 的 users 可以 access workflow diffs：

* instance owners
* instance admins
* project admins
