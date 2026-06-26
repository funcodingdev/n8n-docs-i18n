---
title: 前置条件
description: >-
  n8n OEM deployment 的 infrastructure sizing guidance 和 deployment best practices。
contentType: explanation
nodeTitle: Prerequisites
originalFilePath: hosting/oem-deployment/prerequisites.md
originalUrl: 'https://docs.n8n.io/hosting/oem-deployment/prerequisites'
url: 'https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/prerequisites'
layout:
  description:
    visible: false
---

# 前置条件 <a href="#prerequisites" id="prerequisites"></a>

这里提供的 requirements 是基于 n8n Cloud 的示例，仅用于说明。你的 requirements 可能会因 users、workflows 和 executions 数量而异。请联系 n8n 获取更多信息。

| Component | Sizing | Supported |
| :-------- | :----- | :-------- |
| CPU/vCPU | 最低 10 CPU cycles，按需 scaling | 任何 public 或 private cloud |
| Database | 512 MB - 4 GB SSD | SQLite 或 PostgreSQL |
| Memory | 320 MB - 2 GB | |

## CPU 注意事项 <a href="#cpu-considerations" id="cpu-considerations"></a>

n8n 不是 CPU-intensive，因此即使是 AWS 和 GCP 等 providers 的小型 instances，也足以满足大多数 use cases。通常，memory requirements 比 CPU requirements 更重要，所以规划 infrastructure 时应重点关注 memory。

## Database 注意事项 <a href="#database-considerations" id="database-considerations"></a>

n8n 使用 database 存储 credentials[^1]、past executions 和 workflows。

n8n 的核心功能之一是可以灵活选择 database。所有 supported databases 都有不同的优缺点，你需要逐一考虑，并选择最适合自身需求的 database。默认情况下，如果指定位置不存在 database，n8n 会创建一个 SQLite database。

n8n 建议每个 n8n instance 都拥有 dedicated database。这有助于防止 dependencies 和潜在 performance degradation。如果无法为每个 n8n instance 提供 dedicated database，n8n 建议使用 Postgres 的 schema feature。

对于 Postgres，database 必须已存在于 DB-instance 上。n8n process 使用的 database user 需要对其使用或创建的所有 tables 拥有 full permissions。n8n 会创建并维护 database schema。

### Best practices <a href="#best-practices" id="best-practices"></a>

* SSD storage。
* 在 containerized cloud environments 中，停止/启动 container 时，确保 volume 被持久化并挂载。否则所有 data 都会丢失。
* 如果使用 Postgres，不要使用 `tablePrefix` configuration option。它将在不久后 deprecated。
* 关注新 versions 的 changelog，并在 downgrade 前考虑回滚 migrations。
* 至少设置基本的 database security 和 stability mechanisms，例如 IP allow lists 和 backups。

## Memory 注意事项 <a href="#memory-considerations" id="memory-considerations"></a>

n8n instance 通常不需要大量可用 memory。例如，处于 idle 状态的 n8n Cloud instance 需要约 100MB。真正决定 memory requirements 的，是你的 workflows 性质和正在处理的数据。

例如，大多数 nodes 只是将 data 传递给 workflow 中的下一个 node，而 [Code node](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/using-the-code-node) 会创建 data 的 pre-processing 和 post-processing copy。处理大型 binary files 时，这可能会消耗所有可用资源。

## Deployment 建议 <a href="#deployment-recommendations" id="deployment-recommendations"></a>

详细 setup options 请参阅 [hosting documentation](../install-options/use-a-cloud-provider/README.md)。

### User data <a href="#user-data" id="user-data"></a>

n8n 建议你遵循与 n8n Cloud 内部相同或类似的实践：使用 [Rook](https://rook.io/) 保存 user data，并且如果某台 n8n server 宕机，就在另一台机器上使用相同 data 启动新 instance。

因此，除非发生 catastrophic failure，或者用户希望在你规定的 retention period（n8n Cloud 为两周）内重新激活 account，否则你不需要使用 backups。

### Backups <a href="#backups" id="backups"></a>

n8n 建议通过附加另一个 container 创建 nightly backups，并将所有 data 复制到第二个 container。这样 RAM usage 可以忽略不计，因此不会影响你可以放在 server 上的 users 数量。

### Restarting <a href="#restarting" id="restarting"></a>

如果你的 instance down 或正在 restarting，在此期间错过的 executions（例如 Cron 或 Webhook nodes）无法恢复。如果维持 100% uptime 对你很重要，你需要在它前面构建另一个 proxy 来缓存 data。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。
