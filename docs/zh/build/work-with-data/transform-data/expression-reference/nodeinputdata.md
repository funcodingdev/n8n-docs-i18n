---
nodeTitle: Nodeinputdata
originalFilePath: data/expression-reference/nodeinputdata.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/nodeinputdata'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata
layout:
  description:
    visible: false
---
# NodeInputData <a href="#nodeinputdata" id="nodeinputdata"></a>

## `$input`.**`all()`** <a href="#dollarinputall" id="dollarinputall"></a>

**描述：** 返回当前 node 输入 item 的数组

**语法：** `$input`.all(branchIndex?, runIndex?)

**返回：** Array<Item>

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支索引。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$input`.**`first()`** <a href="#dollarinputfirst" id="dollarinputfirst"></a>

**描述：** 返回当前 node 的第一个输入 item

**语法：** `$input`.first(branchIndex?, runIndex?)

**返回：** Item

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支索引。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$input`.**`item`** <a href="#dollarinputitem" id="dollarinputitem"></a>

**描述：** 返回当前正在处理的输入 item

**语法：** `$input`.`$input`.**`item`**

**返回：** Item

**来源：** 自定义 n8n 功能

## `$input`.**`last()`** <a href="#dollarinputlast" id="dollarinputlast"></a>

**描述：** 返回当前 node 的最后一个输入 item

**语法：** `$input`.last(branchIndex?, runIndex?)

**返回：** Item

**来源：** 自定义 n8n 功能

**参数：**

  * `branchIndex` (Number) - 可选 - 要使用的 node 输出分支索引。默认为第一个分支（index 0）
  * `runIndex` (Number) - 可选 - 要使用的 node 运行次数。默认为第一次运行（index 0）

## `$input`.**`params`** <a href="#dollarinputparams" id="dollarinputparams"></a>

**描述：** 当前 node 的配置设置。这些是你配置 node 时在 node 内填写的参数（例如其 operation）。

**语法：** `$input`.`$input`.**`params`**

**返回：** NodeParams

**来源：** 自定义 n8n 功能
