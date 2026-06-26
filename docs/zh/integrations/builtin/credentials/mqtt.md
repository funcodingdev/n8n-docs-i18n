---
title: MQTT credentials
description: >-
  MQTT credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MQTT 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: MQTT credentials
originalFilePath: integrations/builtin/credentials/mqtt.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mqtt'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mqtt'
layout:
  description:
    visible: false
---

# MQTT credentials <a href="#mqtt-credentials" id="mqtt-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [MQTT](../app-nodes/n8n-nodes-base.mqtt.md)
- [MQTT Trigger](../trigger-nodes/n8n-nodes-base.mqtttrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

安装一个 [MQTT broker](https://mqtt.org/)。

MQTT 在 [MQTT Software](https://mqtt.org/software/) 中提供了 Servers/Brokers 列表。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Broker connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 MQTT protocol 的更多信息，请参考 [MQTT's documentation](https://mqtt.org/)。

有关更详细的配置和细节，请参考你的 broker provider 文档。

## 使用 broker connection <a href="#using-broker-connection" id="using-broker-connection"></a>

要配置此 credential，你需要：

- 你的 MQTT broker 的 **Protocol**
- **Host**
- **Port**
- 用于身份验证的 **Username** 和 **Password**
- 如果你使用 **SSL**，则需要相关 certificates 和 keys

设置步骤：

1. 选择 broker 的 **Protocol**，它决定 n8n 使用的 URL。选项包括：
    - **Mqtt**：使用标准 `mqtt:` protocol 开头的 URL。
    - **Mqtts**：使用安全的 `mqtts:` protocol 开头的 URL。
    - **Ws**：使用 WebSocket `ws:` protocol 开头的 URL。
2. 输入你的 broker **Host**。
3. 输入 n8n 应用于连接 broker host 的 **Port** number。
4. 输入用于登录 broker 的 **Username**。
5. 输入该 user 的 **Password**。
6. 如果你想在离线时接收 QoS 1 和 2 messages，请关闭 **Clean Session** toggle。
7. 输入你希望 credential 使用的 **Client ID**。如果留空，n8n 会为你生成一个。你可以使用固定或基于 expression 的 Client ID。
    - Client IDs 有助于识别和跟踪连接访问。n8n 建议使用包含 `n8n` 的值，便于审计。
8. 如果你的 MQTT broker 使用 SSL，请打开 **SSL** toggle。打开后：
    1. 选择是否使用带 certificates 的 **Passwordless** connection，这类似于 SASL mechanism EXTERNAL。如果启用：
        1. 选择是否 **Reject Unauthorized Certificate**：如果关闭，即使 certificate validation 失败，n8n 也会继续连接。
        2. 添加 SSL **Client Certificate**。
        3. 为 Client Certificate 添加 SSL **Client Key**。
    2. 添加一个或多个 SSL **CA Certificates**。

有关更详细的配置说明，请参考你的 MQTT broker provider 文档。
