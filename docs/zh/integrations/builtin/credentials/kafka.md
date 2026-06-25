---
title: Kafka credentials
description: >-
  Kafka credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Kafka 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Kafka credentials
originalFilePath: integrations/builtin/credentials/kafka.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/kafka'
url: 'https://docs.n8n.io/integrations/builtin/credentials/kafka'
layout:
  description:
    visible: false
---

# Kafka credentials <a href="#kafka-credentials" id="kafka-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Kafka](../app-nodes/n8n-nodes-base.kafka.md)
- [Kafka Trigger](../trigger-nodes/n8n-nodes-base.kafkatrigger.md)

{% hint style="info" %}
**Schema Registry**

这些 credentials 用于对 Kafka brokers 进行身份验证。要连接到已验证身份的 Confluent Schema Registry 以进行 Avro encoding 和 decoding，请使用单独的 [Schema Registry credentials](/integrations/builtin/credentials/schemaregistry.md)。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Client ID

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参考 [Kafka's documentation](https://kafka.apache.org/documentation/)。

如果你刚开始使用 Kafka，请参考 [Apache Kafka Quickstart](https://kafka.apache.org/quickstart) 完成初始设置。

有关在 Kafka 中使用 SSL 的信息，请参考 [Encryption and Authentication using SSL](https://kafka.apache.org/documentation/#security_ssl)。

## 使用 client ID <a href="#using-client-id" id="using-client-id"></a>

要配置此 credential，你需要正在运行的 Kafka environment，并准备：

- **Client ID**
- 相关 **Brokers** 列表
- 如果你的 Kafka environment 使用 authentication，还需要 username/password authentication details

设置步骤：

1. 在 credential 的 **Client ID** 字段中输入 client 或 consumer group 的 `CLIENT-ID`。
2. 输入 credential 要使用的相关 **Brokers** 的逗号分隔列表，格式为 `<broker-service-name>:<port>`。使用你在 `services` 列表中定义 broker 时给它的名称。例如，`kafka-1:9092,kafka-2:9092` 会添加端口为 `9092` 的 `kafka-1` 和 `kafka-2` brokers。
3. 如果你的 Kafka environment 不使用 SSL，请关闭 **SSL** toggle。
4. 如果你已在 Kafka environment 中使用 SASL 启用 authentication，请开启 **Authentication** toggle。然后添加：
    1. **Username**
    2. **Password**
    3. 选择 broker 配置的 **SASL Mechanism**。更多信息请参考 [SASL configuration](https://kafka.apache.org/documentation/#security_sasl_config)。选项包括：
        - `Plain`
        - `scram-sha-256`
        - `scram-sha-512`
