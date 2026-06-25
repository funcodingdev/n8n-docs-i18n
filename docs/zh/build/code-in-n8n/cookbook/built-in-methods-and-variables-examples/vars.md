---
description: 访问你的 environment 自定义变量。
contentType: reference
nodeTitle: vars
originalFilePath: code/cookbook/builtin/vars.md
originalUrl: 'https://docs.n8n.io/code/cookbook/builtin/vars'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars
layout:
  description:
    visible: false
---

# `vars` <a href="#vars" id="vars"></a>

{% hint style="info" %}
**功能可用性**

* Self-hosted Enterprise、Pro 和 Enterprise Cloud 方案可用。
* 你需要访问 n8n 实例 owner account 才能创建变量。
{% endhint %}

`vars` 包含 active environment 的所有[变量](../../define-custom-variables.md)。它是只读的：你可以使用 `vars` 访问变量，但必须使用 UI 设置变量。

{% tabs %}
{% tab title="JavaScript" %}
```js
// Access a variable
$vars.<variable-name>
```
{% endtab %}

{% tab title="Python" %}
```python
# Access a variable
_vars.<variable-name>
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**`vars` 和 `env`**

`vars` 提供对用户创建变量的访问。它是 [Environments](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments) 功能的一部分。`env` 提供对 n8n 实例[配置环境变量](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables)的访问。
{% endhint %}
