---
contentType: howto
nodeTitle: Get the binary data buffer
originalFilePath: code/cookbook/code-node/get-binary-data-buffer.md
originalUrl: 'https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer
layout:
  description:
    visible: false
---

# 获取 binary data buffer <a href="#get-the-binary-data-buffer" id="get-the-binary-data-buffer"></a>

binary data buffer 包含 workflow 处理的所有 binary file data。如果你想对 binary data 执行操作，就需要访问它，例如：

* 操作数据：例如向 CSV 文件添加列标题。
* 在计算中使用数据：例如基于它计算 hash value。
* 复杂 HTTP request：例如将文件上传与发送其他数据格式结合起来。

{% hint style="info" %}
**Python 中不可用**

使用 Python 时不支持 `getBinaryDataBuffer()`。
{% endhint %}
你可以使用 n8n 的 `getBinaryDataBuffer()` 函数访问 buffer：


```js
/*
* itemIndex: number. The index of the item in the input data.
* binaryPropertyName: string. The name of the binary property.
* The default in the Read/Write File From Disk node is 'data'.
*/
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(itemIndex, binaryPropertyName);
```

例如：

```js
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(0, 'data');
// Returns the data in the binary buffer for the first input item
```


你应始终使用 `getBinaryDataBuffer()` 函数，并避免使用直接访问 buffer 的旧方法，例如通过 `items[0].binary.data.data` 这样的 expression 定位它。
