---
title: Database environment variables
description: >-
  使用环境变量为你的 self-hosted n8n 实例设置和配置数据库。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Database
originalFilePath: hosting/configuration/environment-variables/database.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/database'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database
layout:
  description:
    visible: false
---

# Database 环境变量 <a href="#database-environment-variables" id="database-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

默认情况下，n8n 使用 SQLite。n8n 也支持 PostgreSQL。n8n 已在 v1.0 中[弃用对 MySQL 和 MariaDB 的支持](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/v10-migration-guide#mysql-and-mariadb)。

本页列出用于为 self-hosted n8n 实例配置所选数据库的环境变量。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_TYPE`<br>/`_FILE` | Enum string:<br> `sqlite`, `postgresdb` | `sqlite` | 要使用的数据库。 |
| `DB_TABLE_PREFIX` | * | - | 用于表名的前缀。 |
| `DB_PING_INTERVAL_SECONDS` | Number | `2` | n8n ping 数据库以检查连接是否仍然存活的频率，单位为秒。 |
| `DB_PING_TIMEOUT_MS` | Number | `5000` | n8n 等待单次 ping 响应的时间，单位为毫秒；超时后计为失败。如果设置了已弃用的 `N8N_DB_PING_TIMEOUT`，则回退使用该值。 |
| `DB_PING_MAX_FAILURES_BEFORE_RECOVERY` | Number | `3` | 连续多少次 ping 失败后，n8n 将连接视为丢失并开始恢复。 |
| `DB_RECOVERY_BACKOFF_MIN_MS` | Number | `1000` | n8n 在第一次恢复尝试前等待的时间，单位为毫秒。每次重试会等待更久（exponential backoff）。 |
| `DB_RECOVERY_BACKOFF_MAX_MS` | Number | `30000` | n8n 在恢复尝试之间最长等待的时间，单位为毫秒。它会限制 backoff 上限，且必须大于或等于 `DB_RECOVERY_BACKOFF_MIN_MS`。 |
| `DB_CONNECTION_ACQUISITION_TIMEOUT_MS` | Number | `30000` | 恢复进行期间，一个 query 在快速失败并返回错误前等待的时间，单位为毫秒。设为 `0` 表示无限等待。仅适用于 PostgreSQL。 |

## PostgreSQL <a href="#postgresql" id="postgresql"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_POSTGRESDB_DATABASE`<br>/`_FILE` | String | `n8n` | PostgreSQL database 的名称。 |
| `DB_POSTGRESDB_HOST`<br>/`_FILE` | String | `localhost` | PostgreSQL host。 |
| `DB_POSTGRESDB_PORT`<br>/`_FILE` | Number | `5432` | PostgreSQL port。 |
| `DB_POSTGRESDB_USER`<br>/`_FILE` | String | `postgres` | PostgreSQL user。 |
| `DB_POSTGRESDB_PASSWORD`<br>/`_FILE` | String | - | PostgreSQL password。 |
| `DB_POSTGRESDB_POOL_SIZE`<br>/`_FILE` | Number | `2` | 控制 n8n 应该拥有多少个并行打开的 Postgres 连接。增加该值可能有助于资源利用率，但连接过多可能降低性能。 |
| `DB_POSTGRESDB_CONNECTION_TIMEOUT`<br>/`_FILE` | Number | `20000` | Postgres 连接超时（ms）。 |
| `DB_POSTGRESDB_IDLE_CONNECTION_TIMEOUT`<br>/`_FILE` | Number | `30000` | 空闲连接在被视为空闲并可被驱逐前的时长。 |
| `DB_POSTGRESDB_MAX_CONNECTION_LIFETIME_MS`<br>/`_FILE` | Number | `3600000` | n8n 在回收 pooled connection 前保留该连接的时间，单位为毫秒。回收旧连接有助于避免数据库或网络在 n8n 未察觉的情况下丢弃 stale connections。默认值为一小时。设为 `0` 可禁用回收。 |
| `DB_POSTGRESDB_KEEP_ALIVE`<br>/`_FILE` | Boolean | `true` | 是否在连接上启用 TCP keep-alive。Keep-alive 让 n8n 无需先运行 query 就能发现 dead connection。 |
| `DB_POSTGRESDB_KEEP_ALIVE_INITIAL_DELAY_MS`<br>/`_FILE` | Number | `10000` | n8n 在连接上发送第一个 TCP keep-alive probe 前等待的时间，单位为毫秒。 |
| `DB_POSTGRESDB_SCHEMA`<br>/`_FILE` | String | `public` | PostgreSQL schema。 |
| `DB_POSTGRESDB_SSL_ENABLED`<br>/`_FILE` | Boolean | `false` | 是否启用 SSL。如果定义了 `DB_POSTGRESDB_SSL_CA`、`DB_POSTGRESDB_SSL_CERT` 或 `DB_POSTGRESDB_SSL_KEY`，则自动启用。 |
| `DB_POSTGRESDB_SSL_CA`<br>/`_FILE` | String | - | PostgreSQL SSL certificate authority。 |
| `DB_POSTGRESDB_SSL_CERT`<br>/`_FILE` | String | - | PostgreSQL SSL certificate。 |
| `DB_POSTGRESDB_SSL_KEY`<br>/`_FILE` | String | - | PostgreSQL SSL key。 |
| `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`<br>/`_FILE` | Boolean | `true` | n8n 是否应拒绝未授权的 SSL 连接：`true` 表示拒绝，`false` 表示不拒绝。 |

## SQLite <a href="#sqlite" id="sqlite"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_SQLITE_POOL_SIZE` | Number | `0` | 控制是以 [WAL mode](https://www.sqlite.org/wal.html) 还是 [rollback journal mode](https://www.sqlite.org/lockingv3.html#rollback) 打开 SQLite 文件。设为零时使用 rollback journal mode。大于零时使用 WAL mode，并用该值决定要配置的并行 SQL 读连接数量。WAL mode 的性能和可靠性明显优于 rollback journal mode。 |
| `DB_SQLITE_VACUUM_ON_STARTUP` | Boolean | `false` | 启动时运行 [VACUUM](https://www.sqlite.org/lang_vacuum.html) 操作来重建数据库。它会减小文件大小并优化索引。这是一个长时间运行的阻塞操作，会增加启动时间。 |

## 数据库连接恢复如何工作 <a href="#how-database-connection-recovery-works" id="how-database-connection-recovery-works"></a>

n8n 会持续检查它是否仍能访问你的数据库。如果连接断开，例如数据库重启或网络短暂抖动后，n8n 可以自行修复连接，而不是一直保持故障状态直到你重启 n8n。

下面是本页变量控制的周期：

1. 每隔 `DB_PING_INTERVAL_SECONDS`，n8n 发送一次 ping。每次 ping 都必须在 `DB_PING_TIMEOUT_MS` 内响应。
1. 一旦连续 `DB_PING_MAX_FAILURES_BEFORE_RECOVERY` 次 ping 失败，n8n 会将连接视为丢失。
1. 然后 n8n 会重建连接，并以逐渐增长的等待时间重试；等待时间从 `DB_RECOVERY_BACKOFF_MIN_MS` 开始，且不会超过 `DB_RECOVERY_BACKOFF_MAX_MS`。
1. 在 PostgreSQL 中，恢复进行期间，任何新 query 最多等待 `DB_CONNECTION_ACQUISITION_TIMEOUT_MS` 让连接恢复；之后会失败并返回错误，而不是一直挂起。

{% hint style="info" %}
**适用于所有数据库**

健康检查和恢复周期（`DB_PING_*` 与 `DB_RECOVERY_BACKOFF_*` 变量）适用于每种数据库类型。
其余设置（`DB_CONNECTION_ACQUISITION_TIMEOUT_MS`、`DB_POSTGRESDB_MAX_CONNECTION_LIFETIME_MS`、`DB_POSTGRESDB_KEEP_ALIVE` 和 `DB_POSTGRESDB_KEEP_ALIVE_INITIAL_DELAY_MS`）仅适用于 PostgreSQL。默认值适合大多数部署，因此除非遇到连接问题，否则可以保持不变。
{% endhint %}
