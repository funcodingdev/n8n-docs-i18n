---
title: Debug Helper
description: >-
  n8n 中 Debug Helper node 的文档。n8n 是一个 workflow 自动化
  平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Debug Helper
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.debughelper.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.debughelper'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.debughelper'
layout:
  description:
    visible: false
---

# Debug Helper <a href="#debug-helper" id="debug-helper"></a>

使用 Debug Helper node 可以触发不同类型的错误，或生成随机数据集，帮助测试 n8n workflow。

## 操作 <a href="#operations" id="operations"></a>

通过选择 **Category** 来定义操作：

* **Do Nothing**：不执行任何操作。
* [**Throw Error**](#throw-error)：抛出指定类型和消息的错误。
* [**Out Of Memory**](#out-of-memory)：生成指定内存大小，以模拟内存不足。
* [**Generate Random Data**](#generate-random-data)：按所选格式生成一些随机数据。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

Node 参数取决于所选的 **Category**。**Do Nothing** Category 没有其他参数。

### Throw Error <a href="#throw-error" id="throw-error"></a>

* **Error Type**：选择要抛出的错误类型。可选：
	* **NodeApiError**
	* **NodeOperationError**
	* **Error**
* **Error Message**：输入要抛出的错误消息。

### Out Of Memory <a href="#out-of-memory" id="out-of-memory"></a>

Out of Memory Category 会添加一个参数：**Memory Size to Generate**。输入要生成的大约内存量。

### Generate Random Data <a href="#generate-random-data" id="generate-random-data"></a>

* **Data Type**：选择要生成的随机数据类型。选项包括：
	* **Address**
	* **Coordinates**
	* **Credit Card**
	* **Email**
	* **IPv4**
	* **IPv6**
	* **MAC**
	* **Nanoids**：如果选择此数据类型，还需要输入：
		* **Nanoid Alphabet**：生成器用于生成 nanoid 的字符表。
		* **Nanoid Length**：每个 nanoid 的长度。
	* **URL**
	* **User Data**
	* **UUID**
	* **Version**
* **Seed**：如果希望使用特定 seed 生成数据，请在这里输入。这可以确保数据生成结果保持一致。如果想使用随机数据生成，请将此字段留空。
* **Number of Items to Generate**：输入要生成的随机 item 数量。
* **Output as Single Array**：选择将数据生成为单个数组（开启）还是多个 item（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Debug Helper 集成模板](https://n8n.io/integrations/debughelper)或[搜索所有模板](https://n8n.io/workflows/)
