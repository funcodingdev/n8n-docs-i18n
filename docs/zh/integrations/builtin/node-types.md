---
contentType: overview
nodeTitle: Node 类型
originalFilePath: integrations/builtin/node-types.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/node-types'
url: 'https://docs.n8n.io/integrations/builtin/node-types'
layout:
  description:
    visible: false
---

# 内置集成 <a href="#built-in-integrations" id="built-in-integrations"></a>

本节包含 node[^1] 库：n8n 中每个内置 node 及其 credential 的参考文档。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/nqwVeyXZtOyDsX8afllD/" %}

## Core node <a href="#core-nodes" id="core-nodes"></a>

Core node 可以是 action 或 trigger[^2]。大多数 node 会连接到特定外部服务，而 core node 提供逻辑、调度或通用 API 调用等功能。

## Cluster node <a href="#cluster-nodes" id="cluster-nodes"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/nQYOCBZiuZBtHlBAOFq9/" %}

## Credential <a href="#credentials" id="credentials"></a>

外部服务需要一种识别和认证用户的方式。这些数据可以是 API key、电子邮件/密码组合，也可以是很长的多行私钥。你可以将它们作为 credential[^3] 保存在 n8n 中。

n8n 中的 node 随后可以请求这些 credential 信息。作为另一层安全保护，只有具备特定访问权限的 node 类型才能访问 credential。

为确保数据安全，这些数据会加密保存到数据库中。n8n 使用随机个人加密密钥，该密钥会在 n8n 首次运行时自动生成，并保存在 `~/.n8n/config` 下。

要进一步了解如何创建、管理和共享 credential，请参阅[管理 credential](/credentials/index.md)。

## 社区 node <a href="#community-nodes" id="community-nodes"></a>

n8n 支持由社区构建的自定义 node。有关安装和使用这些 node 的指导，请参阅[社区 node](../community-nodes/installation-and-management/README.md)。

如果需要构建自己的自定义 node 并发布到 [npm](https://www.npmjs.com/) 的帮助，请参阅[创建 node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview) 获取更多信息。

[^1]: 在 n8n 中，node 是你组合起来创建 workflow 的独立组件。Node 定义 workflow 应何时运行，允许你获取、发送和处理数据，可以定义流控制逻辑，并连接外部服务。
[^2]: Trigger node 是一种特殊 node，负责在响应特定条件时执行 workflow。所有生产 workflow 都至少需要一个 trigger 来决定 workflow 何时运行。
[^3]: 在 n8n 中，credential 存储用于连接特定 app 和服务的认证信息。使用认证信息（用户名和密码、API key、OAuth secret 等）创建 credential 后，你可以使用关联的 app node 与服务交互。
