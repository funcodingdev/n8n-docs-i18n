---
title: Wait
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Wait
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.wait.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait
description: >-
  n8n 中 Wait node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Wait

使用 Wait node 暂停 workflow 执行。workflow 暂停时，会将 execution 数据卸载到数据库中。满足恢复条件后，workflow 会重新加载数据并继续执行。

## 操作 <a href="#operations" id="operations"></a>

Wait node 可以在以下条件下 **Resume**：

* [**After Time Interval**](n8n-nodes-base.wait.md#after-time-interval)：此 node 等待一段时间。
* [**At Specified Time**](n8n-nodes-base.wait.md#at-specified-time)：此 node 等待到特定时间。
* [**On Webhook Call**](n8n-nodes-base.wait.md#on-webhook-call)：此 node 等待接收到 HTTP 调用。
* [**On Form Submitted**](n8n-nodes-base.wait.md#on-form-submitted)：此 node 等待接收到表单提交。

更详细的说明请参阅下方各节。

### After Time Interval <a href="#after-time-interval" id="after-time-interval"></a>

等待一段时间。

此参数还包含两个字段：

* **Wait Amount**：输入要等待的时间量。
* **Wait Unit**：选择 **Wait Amount** 的计量单位。可选：
  * **Seconds**
  * **Minutes**
  * **Hours**
  * **Days**

这些时间间隔如何工作以及使用哪个时区，详见[基于时间的操作](n8n-nodes-base.wait.md#time-based-operations)。

### At Specified Time <a href="#at-specified-time" id="at-specified-time"></a>

等待到特定日期和时间后继续。使用日期和时间选择器设置 **Date and Time**。

所用时区的更多信息请参阅[基于时间的操作](n8n-nodes-base.wait.md#time-based-operations)。

### On Webhook Call <a href="#on-webhook-call" id="on-webhook-call"></a>

此参数允许 workflow 在 Wait node 接收到 HTTP 调用时恢复。

调用后用于恢复 execution 的 webhook URL 会在运行时生成。Wait node 提供 `$execution.resumeUrl` 变量，因此你可以在需要的位置引用并发送这个尚未生成的 URL，例如发送给第三方服务或放入 email。

workflow 执行时，Wait node 会生成 resume URL，并让 workflow 中使用 `$execution.resumeUrl` 的 webhook 使用它。生成的 URL 对每次 execution 都唯一，因此 workflow 可以包含多个 Wait node；当 webhook URL 被调用时，会按顺序恢复每个 Wait node。

对于这种 **Resume** 方式，请设置下方列出的更多参数。

#### Authentication <a href="#authentication" id="authentication"></a>

选择对 `$execution.resumeUrl` 的传入 resume-webhook 请求是否以及如何进行身份验证。选项包括：

* **Basic Auth**：使用 basic authentication。选择或输入新的 **Credential for Basic Auth**。
* **Header Auth**：使用 header authentication。选择或输入新的 **Credential for Header Auth**。
* **JWT Auth**：使用 JWT authentication。选择或输入新的 **Credential for JWT Auth**。
* **None**：不使用身份验证。

{% hint style="info" %}
**Auth 参考**

有关每种 auth 类型的更多信息，请参阅 [Webhook node | Authentication 文档](n8n-nodes-base.webhook/#supported-authentication-methods)。
{% endhint %}

#### HTTP Method <a href="#http-method" id="http-method"></a>

选择 webhook 应使用的 HTTP method。更多信息请参阅 [Webhook node | HTTP Method 文档](n8n-nodes-base.webhook/#http-method)。

#### Response Code <a href="#response-code" id="response-code"></a>

输入 webhook 应返回的 Response Code。你可以使用常见代码，也可以输入自定义代码。

#### Respond <a href="#respond" id="respond"></a>

从这些选项中设置何时以及如何响应 webhook：

* **Immediately**：node 执行后立即响应。
* **When Last Node Finishes**：返回 workflow 中最后执行的 node 的响应码和数据输出。如果选择此选项，还需要设置：
  * **Response Data**：选择应返回的数据以及使用的格式。选项包括：
    * **All Entries**：以数组形式返回最后一个 node 的所有 entry。
    * **First Entry JSON**：以 JSON 对象形式返回最后一个 node 的第一个 entry 的 JSON 数据。
    * **First Entry Binary**：以二进制文件形式返回最后一个 node 的第一个 entry 的二进制数据。
    * **No Response Body**：返回时不带 body。
* **Using 'Respond to Webhook' Node**：按照 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) node 中的定义响应。

#### Limit Wait Time <a href="#limit-wait-time" id="limit-wait-time"></a>

设置 workflow 是否会在特定限制类型后自动恢复执行（开启），或不会自动恢复（关闭）。如果开启，还需要设置：

* **Limit Type**：从这些选项中选择要强制执行的限制类型：
  * **After Time Interval**：等待一段时间。
    * 输入限制的时间 **Amount**。
    * 选择限制的时间 **Unit**。
  * **At Specified Time**：等待到特定日期和时间后恢复。
    * **Max Date and Time**：使用日期和时间选择器设置此 node 应恢复的指定时间。

#### On Webhook Call 选项 <a href="#on-webhook-call-options" id="on-webhook-call-options"></a>

* **Binary Property**：输入要将接收文件数据写入的二进制属性名称。此选项仅在收到二进制数据时相关。
* **Ignore Bots**：设置是否忽略来自链接预览器、web crawler 等 bot 的请求（开启），或不忽略（关闭）。
* **IP(s) Whitelist**：在此输入 IP 地址，以限制谁（或什么）可以调用 webhook URL。输入以逗号分隔的允许 IP 地址列表。白名单外 IP 的访问会抛出 403 错误。如果留空，所有 IP 地址都可以调用 webhook URL。
* **No Response Body**：设置 n8n 是否应在响应中发送 body（关闭），或阻止 n8n 在响应中发送 body（开启）。
* **Raw Body**：设置是否以 JSON 或 XML 等 raw 格式返回 body（开启），或不返回（关闭）。
* **Response Data**：输入要在响应中发送的任何自定义数据。
* **Response Headers**：在 webhook 响应中发送更多 header。要了解更多 response header，请参阅 [MDN Web Docs | Response header](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)。
* **Webhook Suffix**：输入要附加到 resume URL 的后缀。当 workflow 包含多个 Wait node 时，这有助于为每个 Wait node 创建唯一的 webhook URL。请注意，生成的 `$resumeWebhookUrl` 不会自动包含此后缀；你必须在公开 webhook URL 前手动将其附加进去。

#### On Webhook Call 限制 <a href="#on-webhook-call-limitations" id="on-webhook-call-limitations"></a>

使用 On Webhook Call 时，需要注意一些限制：

* workflow 的 partial execution 会改变 `$resumeWebhookUrl`，因此请确保向目标第三方发送此 URL 的 node 与 Wait node 位于同一次 execution 中。

### On Form Submitted <a href="#on-form-submitted" id="on-form-submitted"></a>

等待表单提交后再继续。设置这些参数：

#### Form Title <a href="#form-title" id="form-title"></a>

输入显示在表单顶部的标题。

#### Form Description <a href="#form-description" id="form-description"></a>

输入显示在标题下方的表单说明。此说明可帮助提示用户如何完成表单。

#### Form Fields <a href="#form-fields" id="form-fields"></a>

使用这些参数设置要显示在表单上的每个字段：

* **Field Label**：输入要在表单中显示的字段标签。
* **Field Type**：选择要在表单中显示的字段类型。可选：
  * **Date**
  * **Dropdown List**：在 **Field Options** 中输入每个 dropdown 选项。
    * **Multiple Choice**：选择用户是否可以选择单个 dropdown 选项（关闭），或多个 dropdown 选项（开启）。
  * **Number**
  * **Password**
  * **Text**
  * **Textarea**
* **Required Field**：设置用户是否必须完成此字段才能提交表单（开启），或可以不完成此字段就提交表单（关闭）。

#### Respond When <a href="#respond-when" id="respond-when"></a>

设置何时响应表单提交。可选：

* **Form Is Submitted**：此 node 接收到表单提交后立即响应。
* **Workflow Finishes**：此 workflow 的最后一个 node 完成时响应。
* **Using 'Respond to Webhook' Node**：[Respond to Webhook](n8n-nodes-base.respondtowebhook.md) node 执行时响应。

#### Limit Wait Time <a href="#limit-wait-time" id="limit-wait-time"></a>

设置 workflow 是否会在特定限制类型后自动恢复执行（开启），或不会自动恢复（关闭）。

如果开启，还需要设置：

* **Limit Type**：从这些选项中选择要强制执行的限制类型：
  * **After Time Interval**：等待一段时间。
    * 输入限制的时间 **Amount**。
    * 选择限制的时间 **Unit**。
  * **At Specified Time**：等待到特定日期和时间后恢复。
    * **Max Date and Time**：使用日期和时间选择器设置此 node 应恢复的指定时间。

#### On Form Response 选项 <a href="#on-form-response-options" id="on-form-response-options"></a>

* **Form Response**：从这些选项中选择希望表单如何以及用什么内容 **Respond With**：
  * **Form Submitted Text**：用户填写表单后，表单会显示 **Text to Show** 中输入的任何文本。如果要显示确认消息，请使用此选项。
  * **Redirect URL**：用户填写表单后，表单会将用户重定向到 **URL to Redirect to**。这必须是有效 URL。
* **Webhook Suffix**：输入要附加到 resume URL 的后缀。当 workflow 包含多个 Wait node 时，这有助于为每个 Wait node 创建唯一的 webhook URL。请注意，生成的 `$resumeWebhookUrl` 不会自动包含此后缀；你必须在公开 webhook URL 前手动将其附加进去。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Wait 集成模板](https://n8n.io/integrations/wait)或[搜索所有模板](https://n8n.io/workflows/)

## 基于时间的操作 <a href="#time-based-operations" id="time-based-operations"></a>

对于基于时间的恢复操作，请注意：

* 对于少于 65 秒的等待时间，workflow 不会将 execution 数据卸载到数据库中。相反，进程会继续运行，并在指定间隔过去后恢复 execution。
* 无论时区设置如何，始终使用 n8n server 时间。Workflow 时区设置以及对其所做的任何更改，都不会影响 Wait node 的时间间隔或指定时间。
