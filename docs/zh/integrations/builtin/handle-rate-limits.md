---
title: 处理 API 速率限制
contentType: howto
nodeTitle: 处理速率限制
originalFilePath: integrations/builtin/rate-limits.md
originalUrl: https://docs.n8n.io/integrations/builtin/rate-limits
url: https://docs.n8n.io/integrations/builtin/handle-rate-limits
description: 使用 n8n 集成时如何处理 API 速率限制。
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

# 处理速率限制

API[^1] 速率限制是对请求频率的限制。例如，API 可能会限制你每分钟或每天可发出的请求数量。

API 也可能限制你在单个请求中可以发送的数据量，或 API 在单个响应中发送的数据量。

## 识别速率限制问题 <a href="#identify-rate-limit-issues" id="identify-rate-limit-issues"></a>

当 n8n node 触发速率限制时，它会报错。n8n 会在 node 输出面板中显示错误消息，其中包括来自服务的错误消息。

如果 n8n 从服务收到 429 错误（请求过多），错误消息会是 **The service is receiving too many requests from you**。

要检查所用服务的速率限制，请参阅该服务的 API 文档。

## 处理集成中的速率限制 <a href="#handle-rate-limits-for-integrations" id="handle-rate-limits-for-integrations"></a>

n8n 集成中有两种处理速率限制的方式：使用 Retry On Fail 设置，或组合使用 [Loop Over Items](core-nodes/n8n-nodes-base.splitinbatches.md) 和 [Wait](core-nodes/n8n-nodes-base.wait.md) node：

* Retry On Fail 会在 API 请求尝试之间加入暂停。
* 使用 Loop Over Items 和 Wait，你可以将请求数据拆成更小的 chunk，并在请求之间暂停。

### 启用 Retry On Fail <a href="#enable-retry-on-fail" id="enable-retry-on-fail"></a>

启用 Retry On Fail 后，如果第一次请求失败，node 会自动再次尝试该请求。

1. 打开 node。
2. 选择 **Settings**。
3. 启用 **Retry On Fail** 开关。
4. 配置重试设置：如果用它规避速率限制，请将 **Wait Between Tries (ms)** 设置为超过速率限制的值。例如，如果你使用的 API 允许每秒一个请求，请将 **Wait Between Tries (ms)** 设置为 `1000`，以等待 1 秒。

### 使用 Loop Over Items 和 Wait <a href="#use-loop-over-items-and-wait" id="use-loop-over-items-and-wait"></a>

使用 Loop Over Items node 对输入 item 分批，并使用 Wait node 在每次请求之间加入暂停。

1. 在调用 API 的 node 之前添加 Loop Over Items node。有关如何配置该 node，请参阅 [Loop Over Items](core-nodes/n8n-nodes-base.splitinbatches.md)。
2. 在调用 API 的 node 之后添加 Wait node，并将其连接回 Loop Over Items node。有关如何配置该 node，请参阅 [Wait](core-nodes/n8n-nodes-base.wait.md)。

例如，要在使用 OpenAI 时处理速率限制：

!["使用 Loop Over Items node 和 Wait node 处理 OpenAI API 速率限制的工作流截图"](../.gitbook/assets/loop-wait.png)

## 在 HTTP Request node 中处理速率限制 <a href="#handle-rate-limits-in-the-http-request-node" id="handle-rate-limits-in-the-http-request-node"></a>

HTTP Request node 有用于处理速率限制和大量数据的内置设置。

### 批量请求 <a href="#batch-requests" id="batch-requests"></a>

使用 Batching 选项发送多个请求，减少请求大小，并在请求之间加入暂停。这等同于使用 Loop Over Items 和 Wait。

1. 在 HTTP Request node 中，选择 **Add Option** > **Batching**。
2. 设置 **Items per Batch**：这是每个请求中包含的输入 item 数量。
3. 设置 **Batch Interval (ms)**，在请求之间加入延迟。例如，如果你使用的 API 允许每秒一个请求，请将 **Wait Between Tries (ms)** 设置为 `1000`，以等待 1 秒。

### 分页结果 <a href="#paginate-results" id="paginate-results"></a>

当 API 需要发送的数据超过单个响应可处理的范围时，会对结果进行分页。有关 HTTP Request node 中分页的更多信息，请参阅 [HTTP Request node | Pagination](core-nodes/n8n-nodes-base.httprequest/#pagination)。

[^1]: API，即应用程序编程接口，提供对服务数据和功能的程序化访问。API 让软件更容易与外部系统交互。它们通常作为传统面向用户界面的替代方式提供，后者一般通过网页浏览器或 UI 访问。
