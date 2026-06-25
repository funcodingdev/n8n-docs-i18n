---
title: Respond to Webhook
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Respond to Webhook
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook
description: >-
  n8n 中 Respond to Webhook node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
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

# Respond to Webhook

使用 Respond to Webhook node 控制对传入 webhook 的响应。此 node 与 [Webhook](n8n-nodes-base.webhook/) node 配合使用。

{% hint style="info" %}
**只对第一个数据 item 运行一次**

Respond to Webhook node 运行一次，并使用第一个传入的数据 item。更多信息请参阅[返回多个数据 item](n8n-nodes-base.respondtowebhook.md#return-more-than-one-data-item-deprecated)。
{% endhint %}

## 如何使用 Respond to Webhook <a href="#how-to-use-respond-to-webhook" id="how-to-use-respond-to-webhook"></a>

要使用 Respond to Webhook node：

1. 添加一个 [Webhook](n8n-nodes-base.webhook/) node 作为 workflow 的 trigger node。
2. 在 Webhook node 中，将 **Respond** 设置为 **Using 'Respond to Webhook' node**。
3. 在 workflow 的任意位置添加 Respond to Webhook node。如果希望它返回其他 node 的数据，请将它放在这些 node 之后。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用这些参数配置 node 行为。

### Respond With <a href="#respond-with" id="respond-with"></a>

选择要在 webhook 响应中发送的数据。

* **All Incoming Items**：使用输入中的所有 JSON item 进行响应。
* **Binary File**：使用 **Response Data Source** 中定义的二进制文件进行响应。
* **First Incoming Item**：使用第一个传入 item 的 JSON 进行响应。
* **JSON**：使用 **Response Body** 中定义的 JSON 对象进行响应。
* **JWT Token**：使用 JSON Web Token（JWT）进行响应。
* **No Data**：不返回响应 payload。
* **Redirect**：重定向到 **Redirect URL** 中设置的 URL。
* **Text**：使用 **Response Body** 中设置的文本进行响应。默认会发送 HTML（`Content-Type: text/html`）。

## Node 选项 <a href="#node-options" id="node-options"></a>

选择 **Add Option** 查看并设置选项。

* **Response Code**：设置要使用的[响应码](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)。
* **Response Headers**：定义要发送的响应 header。
* **Put Response in Field**：当你使用 **All Incoming Items** 或 **First Incoming Item** 响应时可用。设置包含响应数据的字段名称。
* **Enable Streaming**：启用后，使用 streaming 将数据返回给用户。需要 trigger 已配置 **Response mode** 为 **Streaming**。

## n8n 如何保护 HTML 响应 <a href="#how-n8n-secures-html-responses" id="how-n8n-secures-html-responses"></a>

从 n8n 1.103.0 开始，n8n 会自动将发往 webhook 的 HTML 响应用 `<iframe>` 标签包裹。这是一种保护 instance 用户的安全机制。

这会带来以下影响：

* HTML 会在沙箱 iframe 中渲染，而不是直接在父级 document 中渲染。
* 尝试访问顶层 window 或 local storage 的 JavaScript 代码会失败。
* 身份验证 header 在沙箱 iframe 中不可用（例如 basic auth）。你需要使用替代方案，例如在 HTML 中嵌入短期 access token。
* 相对 URL（例如 `<form action="/">`）无法工作。请改用绝对 URL。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Respond to Webhook 集成模板](https://n8n.io/integrations/respond-to-webhook)或[搜索所有模板](https://n8n.io/workflows/)

## Workflow 行为 <a href="#workflow-behavior" id="workflow-behavior"></a>

使用 Respond to Webhook node 时，workflow 行为如下：

* workflow 完成但未执行 Respond to Webhook node：返回状态为 200 的标准消息。
* workflow 在第一个 Respond to Webhook node 执行前出错：workflow 返回状态为 500 的错误消息。
* 第二个 Respond to Webhook node 在第一个之后执行：workflow 会忽略它。
* Respond to Webhook node 执行了，但没有 webhook：workflow 会忽略 Respond to Webhook node。

## 输出发送给 webhook 的响应 <a href="#output-the-response-sent-to-the-webhook" id="output-the-response-sent-to-the-webhook"></a>

默认情况下，Respond to Webhook node 有一个输出分支，其中包含该 node 的输入数据。

你可以选择启用第二个输出分支，其中包含发送给 webhook 的响应。要启用这个次级输出，请在 canvas 上打开 Respond to Webhook node，然后选择 **Settings** 标签页。启用 **Enable Response Output Branch** 选项。

该 node 现在会有两个输出：

* **Input Data**：原始输出，会传递 node 的输入。
* **Response**：发送给 webhook 的响应对象。

## 返回多个数据 item（已弃用） <a href="#return-more-than-one-data-item-deprecated" id="return-more-than-one-data-item-deprecated"></a>

{% hint style="info" %}
**已在 1.22.0 中弃用**

n8n 1.22.0 增加了使用 **All Incoming Items** 选项返回所有数据 item 的支持。n8n 建议升级到最新版本，而不是使用本节描述的 workaround。
{% endhint %}

Respond to Webhook node 运行一次，并使用第一个传入的数据 item。使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 时也是如此。你无法使用 Loop node 强制循环：workflow 会运行，但 webhook 响应仍然只包含第一次执行的结果。

如果需要返回多个数据 item，请选择以下选项之一：

* 不要使用 Respond to Webhook node，而是在 Webhook node 的 **Respond** 中使用 **When Last Node Finishes** 选项。当你想返回 workflow 最终输出的数据时使用此方式。
* 使用 [Aggregate](n8n-nodes-base.aggregate.md) node 在将数据传递给 Respond to Webhook node 之前，把多个 item 转换为单个 item。将 **Aggregate** 设置为 **All Item Data (Into a Single List)**。
