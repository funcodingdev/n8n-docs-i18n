---
title: MySQL node common issues
description: >-
  n8n 中 MySQL node 的常见问题文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: MySQL node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues
layout:
  description:
    visible: false
---

# MySQL node common issues <a href="#mysql-node-common-issues" id="mysql-node-common-issues"></a>

这里列出 [MySQL node](README.md) 的一些常见错误和问题，以及解决或排查步骤。

## Update rows by composite key <a href="#update-rows-by-composite-key" id="update-rows-by-composite-key"></a>

MySQL node 的 **Update** 操作允许你提供 **Column to Match On** 和一个值来更新表中的行。这适用于单列值可以唯一标识单独行的表。

对于使用[复合键](https://en.wikipedia.org/wiki/Composite_key)的表，不能使用这种模式，因为这类表需要多列才能唯一标识一行。一个示例是 `mysql` 数据库中的 MySQL [`user` table](https://mariadb.com/kb/en/mysql-user-table/)，其中需要同时使用 `user` 和 `host` 列才能唯一标识行。

要更新带复合键的表，请改用 **Execute SQL** 操作手动编写查询。在那里，你可以匹配多个值，例如下面这个同时匹配 `customer_id` 和 `product_id` 的示例：

```sql
UPDATE orders SET quantity = 3 WHERE customer_id = 538 AND product_id = 800;
```

## Can't connect to a local MySQL server when using Docker <a href="#cant-connect-to-a-local-mysql-server-when-using-docker" id="cant-connect-to-a-local-mysql-server-when-using-docker"></a>

当你在 Docker 中运行 n8n 或 MySQL 时，需要配置网络，以便 n8n 可以连接到 MySQL。

解决方案取决于你托管这两个组件的方式。

### 如果只有 MySQL 在 Docker 中 <a href="#if-only-mysql-is-in-docker" id="if-only-mysql-is-in-docker"></a>

如果只有 MySQL 在 Docker 中运行，请将 MySQL 配置为监听所有接口，也就是在容器内部绑定到 `0.0.0.0`（官方镜像已经这样配置）。

运行容器时，使用 `-p` 标志[发布端口](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)。默认情况下，MySQL 运行在 3306 端口，因此 Docker 命令应如下所示：

```shell
docker run -p 3306:3306 --name my-mysql -d mysql:latest
```

配置 [MySQL credentials](../../credentials/mysql.md) 时，`localhost` 地址应该可以正常工作（将 **Host** 设置为 `localhost`）。

### 如果只有 n8n 在 Docker 中 <a href="#if-only-n8n-is-in-docker" id="if-only-n8n-is-in-docker"></a>

如果只有 n8n 在 Docker 中运行，请将 MySQL 配置为在主机上绑定到 `0.0.0.0`，以监听所有接口。

如果你在 **Linux** 上使用 Docker 运行 n8n，请在启动容器时使用 `--add-host` 标志，将 `host.docker.internal` 映射到 `host-gateway`。例如：

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

如果你使用 Docker Desktop，这会自动为你配置好。

配置 [MySQL credentials](../../credentials/mysql.md) 时，使用 `host.docker.internal` 作为 **Host** 地址，而不是 `localhost`。

### If MySQL and n8n are running in separate Docker containers <a href="#if-mysql-and-n8n-are-running-in-separate-docker-containers" id="if-mysql-and-n8n-are-running-in-separate-docker-containers"></a>

如果 n8n 和 MySQL 都在 Docker 中运行，但位于不同容器中，可以使用 Docker networking 将它们连接起来。

将 MySQL 配置为在容器内部绑定到 `0.0.0.0`，以监听所有接口（官方镜像已经这样配置）。将 MySQL 和 n8n 容器都添加到同一个[用户定义 bridge network](https://docs.docker.com/engine/network/drivers/bridge/)。

配置 [MySQL credentials](../../credentials/mysql.md) 时，使用 MySQL 容器名称作为 host 地址，而不是 `localhost`。例如，如果你将 MySQL 容器命名为 `my-mysql`，则应将 **Host** 设置为 `my-mysql`。

### If MySQL and n8n are running in the same Docker container <a href="#if-mysql-and-n8n-are-running-in-the-same-docker-container" id="if-mysql-and-n8n-are-running-in-the-same-docker-container"></a>

如果 MySQL 和 n8n 在同一个 Docker 容器中运行，`localhost` 地址不需要任何特殊配置。你可以将 MySQL 配置为监听 `localhost`，并在 n8n 的 [MySQL credentials](../../credentials/ollama.md) 中将 **Host** 配置为使用 `localhost`。

## Decimal numbers returned as strings <a href="#decimal-numbers-returned-as-strings" id="decimal-numbers-returned-as-strings"></a>

默认情况下，MySQL node 会以字符串形式返回 [`DECIMAL` values](https://dev.mysql.com/doc/refman/8.4/en/fixed-point-types.html)。这是有意设计的，用于避免 JavaScript 表示数字的方式存在限制而导致精度损失。你可以在 n8n 使用的 [MySQL library](https://sidorares.github.io/node-mysql2/docs/api-and-configurations) 文档中了解更多有关此决策的信息。

如果要以数字而不是字符串输出 decimal 值，并忽略精度损失风险，请启用 **Output Decimals as Numbers** 选项。这会将这些值输出为数字而不是字符串。

作为替代方案，你可以在 MySQL node 之后，使用带 [`toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) 的 `toFloat()` 函数，或使用 [Edit Fields (Set) node](../../core-nodes/n8n-nodes-base.set.md)，手动将字符串转换为 decimal。请注意，你仍可能需要考虑潜在的精度损失。
