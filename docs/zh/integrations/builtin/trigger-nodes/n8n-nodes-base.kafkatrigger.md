---
title: Kafka Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Kafka Trigger node。按照技术文档将 Kafka Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Kafka Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger
layout:
  description:
    visible: false
---

# Kafka Trigger node <a href="#kafka-trigger-node" id="kafka-trigger-node"></a>

[Kafka](https://kafka.apache.org/) 是一个开源分布式事件流平台，可用于高性能数据 pipeline、流式分析、数据集成和关键任务应用。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/kafka.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**Schema Registry**

要使用经过身份验证的 Confluent Schema Registry（例如 Confluent Cloud）解码消息，请在 node 中启用 **Use Schema Registry**，并添加 [Schema Registry credential](/integrations/builtin/credentials/schemaregistry.md)。
{% endhint %}

{% hint style="warning" %}
**消息压缩**

Kafka Trigger 可以消费未压缩消息和使用 **GZIP** 压缩的消息。它无法解码使用 **LZ4**、**Snappy** 或 **ZSTD** 压缩的消息（这是 Confluent 和 JVM producer 的常见默认值）：消费这类 topic 会因 unsupported-compression-format 错误而失败。要消费该 topic，请配置 producer 使用 gzip 或不使用压缩。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Kafka Trigger integrations](https://n8n.io/integrations/kafka-trigger/) 页面。
{% endhint %}
