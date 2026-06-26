---
title: RabbitMQ credentials
description: >-
  RabbitMQ credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 RabbitMQ 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: RabbitMQ credentials
originalFilePath: integrations/builtin/credentials/rabbitmq.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/rabbitmq'
url: 'https://docs.n8n.io/integrations/builtin/credentials/rabbitmq'
layout:
  description:
    visible: false
---

# RabbitMQ credentials <a href="#rabbitmq-credentials" id="rabbitmq-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [RabbitMQ](../app-nodes/n8n-nodes-base.rabbitmq.md)
- [RabbitMQ Trigger](../trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- User connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [RabbitMQ's Connections documentation](https://www.rabbitmq.com/docs/connections)。

## 使用 user connection <a href="#using-user-connection" id="using-user-connection"></a>

要配置此 credential，你需要已安装 [RabbitMQ broker](https://www.rabbitmq.com/)，并且：

1. 输入 RabbitMQ broker 的 **Hostname**。
2. 输入 connection 应使用的 **Port**。
3. 输入 connection 应用于登录的 **User**。
    - 默认值为 `guest`。RabbitMQ 建议在 production environments 中使用不同的 user。更多信息请参考 [Access Control | The Basics](https://www.rabbitmq.com/docs/access-control#basics)。如果你将 `guest` account 用于非 localhost connection，请参考下面的 [`guest` user issues](#guest-user-issues) 进行故障排查。
4. 输入该 user 的 **Password**。
    - `guest` user 的默认 password 是 `guest`。
5. 输入 connection 应使用的 [virtual host](https://www.rabbitmq.com/docs/vhosts)，作为 **Vhost**。默认 virtual host 是 `/`。
6. 选择 connection 是否应使用 **SSL**。如果启用，还需要设置：
    - **Passwordless**：选择 SSL certificate connection 是使用 SASL mechanism EXTERNAL（关闭）还是不使用 password（开启）。如果开启，还需要输入：
        - **Client Certificate**：粘贴要使用的 SSL client certificate 文本。
        - **Client Key**：粘贴要使用的 SSL client key。
        - **Passphrase**：粘贴要使用的 SSL passphrase。
    - **CA Certificates**：粘贴要使用的 SSL CA certificates 文本。

## guest user issues <a href="#guest-user-issues" id="guest-user-issues"></a>

如果你为 credential 使用 `guest` user，并尝试访问 remote host，可能会看到 connection error。RabbitMQ logs 会显示类似这样的 error：

    [error] <0.918.0> PLAIN login refused: user 'guest' can only connect via localhost

这是因为 RabbitMQ 禁止默认 `guest` user 从 remote hosts 连接。它只能通过 `localhost` 连接。

要解决此 error，你可以：

- 更新 `guest` user，允许它 remote host access。
- 创建或使用其他 user 来连接 remote host。`guest` user 是默认唯一受限制的 user。

更多信息请参考 ["guest" user can only connect from localhost](https://www.rabbitmq.com/docs/access-control#loopback-users)。
