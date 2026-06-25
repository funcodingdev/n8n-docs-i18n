---
title: n8n Form Trigger node 文档
description: >-
  了解如何在 n8n 中使用 n8n Form Trigger node。按照技术文档将
  n8n Form Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: n8n Form Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger'
layout:
  description:
    visible: false
---

# n8n Form Trigger node <a href="#n8n-form-trigger-node" id="n8n-form-trigger-node"></a>

使用 n8n Form trigger 可以在用户提交表单时启动 workflow，并从表单中获取输入数据。该 node 会为你生成可使用的表单网页。

你可以添加 [n8n Form](n8n-nodes-base.form.md) node，继续为表单添加更多页面。

## 构建和测试 workflow <a href="#build-and-test-workflows" id="build-and-test-workflows"></a>

构建或测试 workflow 时，请使用 **Test URL**。使用 test URL 可以确保你能在编辑器 UI 中查看传入数据，这对调试很有用。

有两种测试方式：

- 选择 **Execute Step**。n8n 会打开表单。提交表单后，n8n 会运行该 node，但不会运行 workflow 的其余部分。
- 选择 **Execute Workflow**。n8n 会打开表单。提交表单后，n8n 会运行整个 workflow。

## 生产 workflow <a href="#production-workflows" id="production-workflows"></a>

当 workflow 准备就绪后，切换为使用 **Production URL**。然后你可以发布 workflow，用户提交表单时 n8n 会自动运行它。

使用 production URL 时，请确保已保存并发布 workflow。通过 Form trigger 流动的数据在使用 production URL 时不会显示在编辑器 UI 中。

## 使用 query parameter 设置默认选项 <a href="#set-default-selections-with-query-parameters" id="set-default-selections-with-query-parameters"></a>

你可以在 n8n Form Trigger 提供的初始 URL 上使用 [query parameter](https://en.wikipedia.org/wiki/Query_string#Web_forms) 来设置字段初始值。表单中的每个[页面](n8n-nodes-base.form.md)都会收到发送到 n8n Form Trigger URL 的相同 query parameter。

{% hint style="info" %}
**仅限生产环境**

Query parameter 仅在生产模式下使用表单时可用。测试模式下，n8n 不会根据 query parameter 填充字段值。
{% endhint %}


使用 query parameter 时，请对任何包含特殊字符的字段名或值进行 [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding)。这可以确保 n8n 使用给定字段的初始值。你可以使用 [URL Encode/Decode](https://www.url-encode-decode.com/) 等工具，用 percent-encoding 格式化 query parameter。

例如，假设你有一个包含以下属性的表单：

* Production URL: `https://my-account.n8n.cloud/form/my-form`
* Fields:
	* `name`: `Jane Doe`
	* `email`: `jane.doe@example.com`

通过 query parameter 和 percent-encoding，可以使用以下 URL 将初始字段值设置为上面的数据：

```
https://my-account.n8n.cloud/form/my-form?email=jane.doe%40example.com&name=Jane%20Doe
```

这里，percent-encoding 会将 at 符号（`@`）替换为字符串 `%40`，并将空格字符（` `）替换为字符串 `%20`。无论这些字段出现在表单的哪个页面上，都会设置它们的初始值。


## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

以下是主要的 node 配置字段：

### Authentication <a href="#authentication" id="authentication"></a>

- **Basic Auth**
- **None**

#### 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 用于访问 HTTP Request 目标 app 或服务的 **Username**。
- 与该 username 对应的 **Password**。

### Form URLs <a href="#form-urls" id="form-urls"></a>

Form Trigger node 有两个 URL：**Test URL** 和 **Production URL**。n8n 会在 node 面板顶部显示这些 URL。选择 **Test URL** 或 **Production URL** 可以切换 n8n 显示的 URL。

![Screenshot of the form URLs](../../.gitbook/assets/form-urls.png)

- **Test URL**：如果 workflow 未激活，当你选择 **Execute Step** 或 **Execute Workflow** 时，n8n 会注册一个测试 webhook。调用该 URL 时，n8n 会在 workflow 中显示数据。
- **Production URL**：发布 workflow 时，n8n 会注册一个生产 webhook。使用 production URL 时，n8n 不会在 workflow 中显示数据。你仍然可以查看生产 execution 的 workflow 数据。选择 workflow 中的 **Executions** 标签页，然后选择要查看的 workflow execution。

### Form Path <a href="#form-path" id="form-path"></a>

为表单设置自定义 slug。

### Form Title <a href="#form-title" id="form-title"></a>

输入表单标题。n8n 会将 **Form Title** 显示为网页标题和表单上的主 `h1` 标题。

### Form Description <a href="#form-description" id="form-description"></a>

输入表单描述。n8n 会将 **Form Description** 显示为表单主 `h1` 标题下方的副标题。使用 `\n` 或 `<br>` 添加换行。

有关允许和受限 HTML 标签的信息，请参阅 [HTML 安全和允许的标签](#html-security-and-allowed-tags)。

### Form Elements <a href="#form-elements" id="form-elements"></a>

为表单创建问题字段。选择 **Add Form Element** 添加新字段。

每个字段都有以下设置：

- **Field Label**：输入渲染后的表单上显示在输入字段上方的标签。
- **Field Name**：此名称用于 Form Trigger node 的输出。可用它在下游 node 中引用表单字段。
- **Element Type**：可选择 **Checkboxes**、**Custom HTML**、**Date**、**Dropdown**、**Email**、**File**、**Hidden Field**、**Number**、**Password**、**Radio Buttons**、**Text** 或 **Textarea**。
	- 选择 **Checkboxes** 可在表单中包含复选框元素。默认情况下，表单用户可选择的复选框数量没有限制。你可以通过将 **Limit Selection** 选项指定为 **Exact Number**、**Range** 或 **Unlimited** 来设置限制。
	- 选择 **Custom HTML** 可插入任意 HTML。
		- 你可以包含链接、图片、视频等元素。不能包含 `<script>`、`<style>` 或 `<input>` 元素。更多信息请参阅 [HTML 安全和允许的标签](#html-security-and-allowed-tags)。
		- 默认情况下，Custom HTML 字段不会包含在 node 输出中。要在输出中包含 Custom HTML 内容，请填写关联的 **Element Name** 字段。
    - 选择 **Date** 可在表单中包含日期选择器。有关日期格式化的更多信息，请参阅 [Date and time with Luxon](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/handle-special-data-types/work-with-dates-and-times)。
	- 选择 **Dropdown List** > **Add Field Option** 可添加多个选项。默认情况下，下拉框是单选。要将其改为多选，请开启 **Multiple Choice**。
	- 选择 **Radio Buttons** 可在表单中包含单选按钮元素。
	- 选择 **Hidden Field** 可包含一个不会显示在表单上的表单元素。你可以使用 **Field Value** 参数设置默认值，或使用 [query parameter](#set-default-selections-with-query-parameters) 为该字段传值。
- **Placeholder**：定义在兼容表单元素内显示的示例文本。**Email**、**Number**、**Password**、**Text** 和 **Textarea** 支持 placeholder。
- **Default value**：定义将在兼容表单元素中预填充或预选的默认值。除 **Custom HTML**、**File**、**Hidden Field** 和 **Password** 以外，所有表单元素都支持默认值。
- **Required Field**：开启后要求用户在表单中完成此字段。

### Respond When <a href="#respond-when" id="respond-when"></a>

选择 n8n 何时向表单提交发送响应。你可以在以下时机响应：

- **Form Is Submitted**：用户提交表单后立即向用户发送响应。
- **Workflow Finishes**：如果希望 workflow 完成执行后再向用户发送响应，请使用此选项。如果 workflow 出错，它会向用户发送响应，告知提交表单时出现问题。

## Node 选项 <a href="#node-options" id="node-options"></a>

选择 **Add Option** 可查看更多配置选项：

- **Append n8n Attribution**：关闭后隐藏表单底部的 **Form automated with n8n** 标识。
- **Button Label**：表单提交按钮使用的标签。n8n 会将 **Button Label** 显示为提交按钮名称。
- **Form Path**：表单 URL 的最后一段，同时适用于测试和生产。它会替换自动生成的 UUID，作为最后的组件。
- **Ignore Bots**：开启后忽略来自链接预览器、网络爬虫等 bot 的请求。
- **Use Workflow Timezone**：开启后使用 [Workflow settings](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/configure-workflow-settings) 中的时区，而不是 UTC（默认）。这会影响 node 输出中的 `submittedAt` timestamp 值。
- **Custom Form Styling**：使用 CSS 覆盖公开表单界面的默认样式。该字段会预填充默认样式，因此你只需修改需要的部分。

## 自定义 Form Trigger node 行为 <a href="#customizing-form-trigger-node-behavior" id="customizing-form-trigger-node-behavior"></a>

### 使用换行格式化响应文本 <a href="#format-response-text-with-line-breaks" id="format-response-text-with-line-breaks"></a>

你可以使用以下方法之一为表单响应文本添加换行：

• 在 formSubmittedText 字段中使用 HTML 格式，而不是纯文本
• 在发送响应前，将换行字符（`\n`）替换为 HTML break 标签（`<br>`）
• 如果需要更多格式控制，可以考虑使用自定义 HTML 响应页面

### 使用身份验证限制表单访问 <a href="#restrict-form-access-with-authentication" id="restrict-form-access-with-authentication"></a>

你可以使用以下选项之一为表单添加身份验证：

• 使用 OTP（One-Time Password）字段配合 TOTP node 验证，实现基于 token 的身份验证
• 添加 Wait node，并将表单身份验证作为第二个表单页面
• 在数据库中存储 hashed password，并与表单提交内容比较以进行验证
• 如果需要高级身份验证，请使用 Google Forms 等外部身份验证提供方

## HTML 安全和允许的标签 <a href="#html-security-and-allowed-tags" id="html-security-and-allowed-tags"></a>

n8n Form Trigger 会自动清理 **Form Description** 字段和 **Custom HTML** 表单元素中的 HTML 内容，以防止安全漏洞。虽然支持使用 HTML 进行格式化，但某些标签和属性会受到限制。

### 允许的 HTML 标签 <a href="#allowed-html-tags" id="allowed-html-tags"></a>

你可以使用以下标签进行格式化：`<a>`、`<b>`、`<br>`、`<code>`、`<div>`、`<em>`、`<h1>` 到 `<h6>`、`<i>`、`<iframe>`、`<img>`、`<li>`、`<ol>`、`<p>`、`<pre>`、`<span>`、`<strong>`、`<sub>`、`<sup>`、`<table>`、`<tbody>`、`<td>`、`<tfoot>`、`<th>`、`<thead>`、`<tr>`、`<u>`、`<ul>`、`<video>` 和 `<source>`。

### 受限标签 <a href="#restricted-tags" id="restricted-tags"></a>

出于安全考虑，以下标签会被自动移除：`<script>`、`<style>`、`<input>`、`<form>`、`<button>`，以及其他可能启用 XSS 攻击或干扰表单功能的危险元素。

### 属性限制 <a href="#attribute-restrictions" id="attribute-restrictions"></a>

只有特定标签允许使用特定属性：

* 链接（`<a>`）：`href`、`target`、`rel`
* 图片（`<img>`）：`src`、`alt`、`width`、`height`
* 视频（`<video>`）：`controls`、`autoplay`、`loop`、`muted`、`poster`、`width`、`height`
* Iframe（`<iframe>`）：`src`、`width`、`height`、`frameborder`、`allow`、`allowfullscreen`、`referrerpolicy`（会自动 sandbox）
* 表格单元格（`<td>`、`<th>`）：`colspan`、`rowspan`、`scope`、`headers`

清理过程中会移除所有其他属性。只允许 `http://` 和 `https://` URL scheme。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n Form Trigger node 集成模板](https://n8n.io/integrations/n8n-form-trigger)或[搜索所有模板](https://n8n.io/workflows/)
