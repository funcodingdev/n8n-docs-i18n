---
title: AMQP credentials
description: >-
  AMQP credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 AMQP。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: AMQP credentials
originalFilePath: integrations/builtin/credentials/amqp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/amqp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/amqp'
layout:
  description:
    visible: false
---

# AMQP credentials <a href="#amqp-credentials" id="amqp-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [AMQP Sender](../app-nodes/n8n-nodes-base.amqp.md)
- [AMQP Trigger](../trigger-nodes/n8n-nodes-base.amqptrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

安装一个兼容 AMQP 1.0 的 message broker，例如 [ActiveMQ](https://activemq.apache.org/)。可参阅 [AMQP Products](https://www.amqp.org/about/examples) 查看可选方案列表。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- AMQP connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Advanced Message Queuing Protocol (AMQP) 是一种面向消息中间件的开放标准应用层协议。AMQP 的定义特性包括消息导向、队列、路由、可靠性和安全性。有关更多信息，请参阅 [OASIS AMQP Version 1.0 Standard](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html)。

有关该服务的更多信息，请参阅你的 provider 文档。可将 [ActiveMQ 的 API 文档](https://activemq.apache.org/components/classic/documentation/rest) 作为示例参考。

## 使用 AMQP connection <a href="#using-amqp-connection" id="using-amqp-connection"></a>

要配置此 credential，你需要：

- **Hostname**：输入 AMQP message broker 的 hostname。
- **Port**：输入连接应使用的端口号。
- **User**：输入用于建立连接的用户名。
    - 例如，ActiveMQ 中的默认用户名是 `admin`。
- **Password**：输入该用户的密码。
    - 例如，ActiveMQ 中的默认密码是 `admin`。
- _可选：_ **Transport Type**：输入 `tcp` 或 `tls`。

有关更详细的说明，请参阅你的 provider 文档。
