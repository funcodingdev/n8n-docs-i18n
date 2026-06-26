---
description: n8n performance 和 resource consumption benchmarking。
contentType: explanation
nodeTitle: Measure performance
originalFilePath: hosting/scaling/performance-benchmarking.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/performance-benchmarking'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance'
layout:
  description:
    visible: false
---

# Performance and benchmarking <a href="#performance-and-benchmarking" id="performance-and-benchmarking"></a>

n8n 在单实例上每秒最多可处理 220 次 workflow executions，并且可以通过添加更多 instances 进一步扩展。

本文档概述 n8n 的 performance benchmarking。它描述影响性能的因素，并包含两个 benchmark 示例。

## 性能因素 <a href="#performance-factors" id="performance-factors"></a>

n8n 的性能取决于以下因素：

* workflow type
* n8n 可用的 resources
* 你如何配置 n8n scaling options

## 运行自己的 benchmarking <a href="#run-your-own-benchmarking" id="run-your-own-benchmarking"></a>

要为你的使用场景获得准确估算，请运行 n8n 的 [benchmarking framework](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/benchmark)。该 repository 包含更多 benchmarking 信息。

## 示例：单实例性能 <a href="#example-single-instance-performance" id="example-single-instance-performance"></a>

此测试衡量 requests per second 增加时 response time 如何增加。它关注调用 Webhook Trigger node 时的 response time。

设置：

- Hardware：ECS c5a.large instance（4GB RAM）
- n8n setup：单个 n8n instance（以 main mode 运行，使用 Postgres database）
- Workflow：Webhook Trigger node、Edit Fields node

<figure markdown>
  <img src="../../../.gitbook/assets/benchmarking-single-instance-100-250.png" alt="">
  <figcaption>此图显示 Webhook Trigger node 请求在 100 秒内获得响应的百分比，以及该比例如何随 load 变化。在更高 load 下，n8n 通常仍会处理数据，但响应时间会超过 100 秒。</figcaption>
</figure>

## 示例：多实例性能 <a href="#example-multi-instance-performance" id="example-multi-instance-performance"></a>

此测试衡量 requests per second 增加时 response time 如何增加。它关注调用 Webhook Trigger node 时的 response time。

设置：

- Hardware：七个 ECS c5a.4xlarge instances（每个 8GB RAM）
- n8n setup：两个 webhook instances、四个 worker instances、一个 database instance（MySQL）、一个运行 n8n 和 Redis 的 main instance
- Workflow：Webhook Trigger node、Edit Fields node
- Multi-instance setups 使用 [Queue mode](enable-queue-mode.md)

<figure markdown>
  <img src="../../../.gitbook/assets/benchmarking-multi-instance-500-2500.png" alt="">
  <figcaption>此图显示 Webhook Trigger node 请求在 100 秒内获得响应的百分比，以及该比例如何随 load 变化。在更高 load 下，n8n 通常仍会处理数据，但响应时间会超过 100 秒。</figcaption>
</figure>
