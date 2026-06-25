---
title: 自定义变量
description: 自定义变量允许你在 n8n workflow 中存储和复用值。
contentType: howto
nodeTitle: Define custom variables
originalFilePath: code/variables.md
originalUrl: 'https://docs.n8n.io/code/variables'
url: 'https://docs.n8n.io/build/code-in-n8n/define-custom-variables'
layout:
  description:
    visible: false
---

# 自定义变量 <a href="#custom-variables" id="custom-variables"></a>

{% hint style="info" %}
**功能可用性**

* Self-hosted Enterprise 和 Pro Cloud 方案可用。
* 只有实例 owner 和 admin 可以创建变量。
{% endhint %}

自定义变量是只读变量，可用于在 n8n workflow 中存储和复用值。

{% hint style="warning" %}
**变量作用域和可用性**

* **全局变量** 对 n8n 实例上的所有人可用，跨所有 project 生效。
* **Project 作用域变量** 只在创建它的特定 project 内可用。
* Project 作用域变量在 1.118.0 及以上版本可用。以前的版本只支持从左侧菜单访问的全局变量。
{% endhint %}

## 创建变量 <a href="#create-variables" id="create-variables"></a>

你可以从 overview 页面或特定 project 访问 **Variables** 标签页。

要创建新变量：

1. 在 **Variables** 标签页中，选择 **Add Variable**。
2. 输入 **Key** 和 **Value**。key 最大长度为 50 个字符，value 最大长度为 1000 个字符。n8n 将 key 和 value 中可使用的字符限制为大小写字母、数字和下划线（`A-Z`、`a-z`、`0-9`、`_`）。
3. 选择 **Scope**（仅从 overview 页面创建时可用）：
    * **Global**：该变量在 n8n 实例的所有 project 中可用。
    * **Project**：该变量只在特定 project 中可用（你可以选择哪个 project）。
    * 从 project 页面创建时，scope 会自动设置为该 project。
4. 选择 **Save**。该变量现在可根据其 scope 在 workflow 中使用。

## 编辑和删除变量 <a href="#edit-and-delete-variables" id="edit-and-delete-variables"></a>

要编辑或删除变量：

1. 在 **Variables** 标签页中，将鼠标悬停在要更改的变量上。
2. 选择 **Edit** 或 **Delete**。

## 在 workflow 中使用变量 <a href="#use-variables-in-workflows" id="use-variables-in-workflows"></a>

你可以在 Code node 和 expression[^1] 中访问变量：

```javascript
// Access a variable
$vars.<variable-name>
```

所有变量都是字符串。

workflow 执行期间，n8n 会将变量替换为变量值。如果变量没有值，n8n 会将其值视为 `undefined`。这种情况下 workflow 不会自动失败。

{% hint style="info" %}
**变量优先级**

当 project 作用域变量与全局变量具有相同 key 时，在该 project 的 workflow 中，project 作用域变量值优先并覆盖全局变量值。
{% endhint %}

变量是只读的。你必须使用 UI 更改值。如果需要在 workflow 内设置和访问自定义数据，请使用 [Workflow static data](cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。

[^1]: 在 n8n 中，expression 允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n expression 语法，通过前序 node、其他 workflow 或 n8n 环境中的数据来定义值。
