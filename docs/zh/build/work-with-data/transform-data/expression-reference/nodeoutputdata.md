---
nodeTitle: Nodeoutputdata
originalFilePath: data/expression-reference/nodeoutputdata.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/nodeoutputdata'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata
layout:
  description:
    visible: false
---
# NodeOutputData <a href="#nodeoutputdata" id="nodeoutputdata"></a>

## `$()`.**`all()`** <a href="#dollarall" id="dollarall"></a>

**描述：** 返回 node 输出 item 的数组

**语法：** `$()`.all(branchIndex?, runIndex?)

**返回：** Array<Item>

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$()`.**`first()`** <a href="#dollarfirst" id="dollarfirst"></a>

**描述：** 返回 node 输出的第一个 item

**语法：** `$()`.first(branchIndex?, runIndex?)

**返回：** Item

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$()`.**`isExecuted`** <a href="#dollarisexecuted" id="dollarisexecuted"></a>

**描述：** 如果 node 已执行则为 <code>true</code>，否则为 <code>false</code>

**语法：** `$()`.`$()`.**`isExecuted`**

**返回：** Boolean

**来源：** 自定义 n8n 功能

## `$()`.**`item`** <a href="#dollaritem" id="dollaritem"></a>

**描述：** 返回匹配 item，即用于生成当前 node 中当前 item 的那个 item。<a href="/data/data-mapping/data-item-linking/">更多信息</a>

**语法：** `$()`.`$()`.**`item`**

**返回：** Item

**来源：** 自定义 n8n 功能

## `$()`.**`itemMatching()`** <a href="#dollaritemmatching" id="dollaritemmatching"></a>

**描述：** 返回匹配 item，即用于生成当前 node 中指定索引 item 的那个 item。<a href="/data/data-mapping/data-item-linking/">更多信息</a>

**语法：** `$()`.itemMatching(currentItemIndex?)

**返回：** Item

**来源：** 自定义 n8n 功能

**参数：**

  * `currentItemIndex` (Number) - 当前 node 中要匹配的 item 索引。

## `$()`.**`last()`** <a href="#dollarlast" id="dollarlast"></a>

**描述：** 返回 node 输出的最后一个 item

**语法：** `$()`.last(branchIndex?, runIndex?)

**返回：** Item

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$()`.**`params`** <a href="#dollarparams" id="dollarparams"></a>

**描述：** 给定 node 的配置设置。这些是你在 node UI 中填写的参数（例如其 operation）。

**语法：** `$()`.`$()`.**`params`**

**返回：** NodeParams

**来源：** 自定义 n8n 功能
