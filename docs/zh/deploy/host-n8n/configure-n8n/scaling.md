---
contentType: overview
nodeTitle: Scaling
originalFilePath: hosting/scaling/overview.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/overview'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling'
layout:
  description:
    visible: false
---

# 扩展 n8n <a href="#scaling-n8n" id="scaling-n8n"></a>

当你以较大规模运行 n8n，拥有大量用户、workflows 或 executions 时，需要更改 n8n configuration 以确保良好性能。

n8n 可根据你的需求以不同 [modes](scaling/enable-queue-mode.md) 运行。`queue` mode 提供最佳 scalability。配置详情请参阅 [Queue mode](scaling/enable-queue-mode.md)。

你可以配置 data saving 和 pruning 来提升 database performance。详情请参阅 [Execution data](scaling/manage-execution-data.md)。
