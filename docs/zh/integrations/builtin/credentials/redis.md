---
title: Redis credentials
description: >-
  Redis credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Redis 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Redis credentials
originalFilePath: integrations/builtin/credentials/redis.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/redis'
url: 'https://docs.n8n.io/integrations/builtin/credentials/redis'
layout:
  description:
    visible: false
---

# Redis credentials <a href="#redis-credentials" id="redis-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Redis](../app-nodes/n8n-nodes-base.redis.md)
- [Redis Chat Memory](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)
- [Redis Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Redis's developer documentation](https://redis.readthedocs.io/en/stable/index.html)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

你需要 [Redis](https://redis.io/) server 上的 user account，以及：

- 一个 **Password**
- **Host** name
- **Port** number
- 一个 **Database Number**
- **SSL**

配置此 credential：

1. 输入你的 user account **Password**。
2. 输入 Redis server 的 **Host** name。默认值为 `localhost`。
3. 输入 connection 应使用的 **Port** number。默认值为 `6379`。
    - 该数字应与你运行 `INFO` command 时列出的 `tcp_port` 匹配。
4. 输入 **Database Number**。默认值为 `0`。
5. 如果 connection 应使用 SSL，请打开 **SSL** toggle。如果此 toggle 关闭，connection 仅使用 TCP。
6. 如果启用 **SSL**，你可以选择 **disable TLS verification**。启用此 toggle 可使用 self-signed certificates。警告：这会降低 connection 的安全性。

更多信息请参考 [Connecting to Redis | Generic client](https://redis.readthedocs.io/en/stable/connections.html)。
