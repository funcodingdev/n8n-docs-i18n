---
description: 如何使用 console.log() 或 print()
contentType: howto
nodeTitle: Output to the browser console
originalFilePath: code/cookbook/code-node/console-log.md
originalUrl: 'https://docs.n8n.io/code/cookbook/code-node/console-log'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console
layout:
  description:
    visible: false
---

# 在 Code node 中使用 `console.log()` 或 `print()` 输出到浏览器 console <a href="#output-to-the-browser-console-with-consolelog-or-print-in-the-code-node" id="output-to-the-browser-console-with-consolelog-or-print-in-the-code-node"></a>

你可以在 Code node 中使用 `console.log()` 或 `print()`，帮助编写和调试代码。

如需打开浏览器 console 的帮助，请参阅 [Balsamiq 的这篇指南](https://balsamiq.com/support/faqs/browserconsole/)。

## console.log (JavaScript) <a href="#consolelog-javascript" id="consolelog-javascript"></a>

关于 `console.log()` 的技术信息，请参阅 [MDN developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)。

例如，将以下代码复制到 Code node 中，然后打开 console 并运行该 node：

```js
let a = "apple";
console.log(a);
```

## print (Python) <a href="#print-python" id="print-python"></a>

关于 `print()` 的技术信息，请参阅 [Real Python's guide](https://realpython.com/python-print/)。

例如，将 Code node 的 **Language** 设置为 **Python**，将以下代码复制到 node 中，然后打开 console 并运行该 node：

```python
a = "apple"
print(a)
```

### 处理 `[object Object]` 输出 <a href="#handling-an-output-of-object-object" id="handling-an-output-of-object-object"></a>

如果打印时 console 显示 `[object Object]`，请检查数据类型，然后按需转换。

检查数据类型：

```python
print(type(myData))
```

#### JsProxy <a href="#jsproxy" id="jsproxy"></a>

如果 `type()` 输出 `<class 'pyodide.ffi.JsProxy'>`，你需要使用 `to_py()` 将 JsProxy 转换为原生 Python object。处理 n8n node 数据结构中的数据（例如 node 输入和输出）时会出现这种情况。例如，如果你想打印 workflow 中前一个 node 的数据：

```python
previousNodeData = _("<node-name>").all();
for item in previousNodeData:
	# item is of type <class 'pyodide.ffi.JsProxy'>
	# You need to convert it to a Dict
	itemDict = item.json.to_py()
	print(itemDict)
```

关于此 class 的更多信息，请参阅 Pyodide 文档中的 [JsProxy](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.JsProxy)。
