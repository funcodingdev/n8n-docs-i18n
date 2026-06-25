---
description: 在 n8n 中使用 JMESPath library 的方法。
contentType: reference
hide:
  - toc
nodeTitle: JMESPath
originalFilePath: code/builtin/jmespath.md
originalUrl: 'https://docs.n8n.io/code/builtin/jmespath'
url: 'https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath'
layout:
  description:
    visible: false
---

# JMESPath 方法 <a href="#jmespath-method" id="jmespath-method"></a>

这是 n8n 提供的方法，用于配合 [JMESPath](../../work-with-data/handle-special-data-types/query-json-data.md) library 工作。

{% hint style="info" %}
**Python 支持**

你可以在 Code node 中使用 Python。它不能在 expression 中使用。
{% endhint %}
{% tabs %}
{% tab title="JavaScript" %}
| 方法 | 描述 | 可在 Code node 中使用？ |
| ------ | ----------- | :-------------------------: |
| `$jmespath()` | 使用 JMESPath 在 JSON object 上执行搜索。 | ✅ |
{% endtab %}

{% tab title="Python" %}
| 方法 | 描述 |
| ------ | ----------- |
| `_jmespath()` | 使用 JMESPath 在 JSON object 上执行搜索。 |
{% endtab %}
{% endtabs %}
