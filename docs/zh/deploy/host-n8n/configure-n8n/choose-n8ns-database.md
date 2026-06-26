---
contentType: reference
nodeTitle: Choose n8n's database
originalFilePath: hosting/configuration/supported-databases-settings.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/supported-databases-settings'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database'
layout:
  description:
    visible: false
---

# 支持的 databases <a href="#supported-databases" id="supported-databases"></a>

默认情况下，n8n 使用 SQLite 保存 credentials、过去的 executions 和 workflows。n8n 也支持 PostgresDB（仅支持[仍在积极维护的版本](https://www.postgresql.org/support/versioning/)）。

## 按 n8n 安装方式选择 database type <a href="#database-type-by-n8n-installation" id="database-type-by-n8n-installation"></a>

使用的 database type 会因 n8n 安装方式而异：

### 自托管 n8n <a href="#self-hosted-n8n" id="self-hosted-n8n"></a>
默认情况下，自托管安装使用 **SQLite**。你可以通过设置相应环境变量来选择配置 PostgreSQL（请参阅 [PostgresDB configuration](#postgresdb)）。

### n8n Cloud <a href="#n8n-cloud" id="n8n-cloud"></a>

n8n Cloud 安装会根据你的 plan tier 使用不同 database：

- **SQLite**：Trial、Starter 和 Pro plans，以及旧版 Enterprise plans
- **PostgreSQL**：仅 Enterprise Scaling plans

## 共享设置 <a href="#shared-settings" id="shared-settings"></a>

所有 databases 都会使用以下环境变量：

 - `DB_TABLE_PREFIX`（默认：-）- table names 的 prefix

## PostgresDB <a href="#postgresdb" id="postgresdb"></a>

要使用 PostgresDB 作为 database，你可以提供以下环境变量：

 - `DB_TYPE=postgresdb`
 - `DB_POSTGRESDB_DATABASE`（默认：'n8n'）
 - `DB_POSTGRESDB_HOST`（默认：'localhost'）
 - `DB_POSTGRESDB_PORT`（默认：5432）
 - `DB_POSTGRESDB_USER`（默认：'postgres'）
 - `DB_POSTGRESDB_PASSWORD`（默认：空）
 - `DB_POSTGRESDB_SCHEMA`（默认：'public'）
 - `DB_POSTGRESDB_SSL_CA`（默认：undefined）：用于验证连接的 server CA certificate 路径（不支持 opportunistic encryption）
 - `DB_POSTGRESDB_SSL_CERT`（默认：undefined）：client TLS certificate 路径
 - `DB_POSTGRESDB_SSL_KEY`（默认：undefined）：与 certificate 对应的 client private key 路径
 - `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`（默认：true）：是否拒绝未通过验证的 TLS connections

```bash
export DB_TYPE=postgresdb
export DB_POSTGRESDB_DATABASE=n8n
export DB_POSTGRESDB_HOST=postgresdb
export DB_POSTGRESDB_PORT=5432
export DB_POSTGRESDB_USER=n8n
export DB_POSTGRESDB_PASSWORD=n8n
export DB_POSTGRESDB_SCHEMA=n8n

# optional: <a href="#optional" id="optional"></a>
export DB_POSTGRESDB_SSL_CA_FILE=$(pwd)/ca.crt
export DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false

n8n start
```

### 所需权限 <a href="#required-permissions" id="required-permissions"></a>

n8n 需要创建并修改它使用的 tables 的 schemas。

推荐权限：

```sql
CREATE DATABASE n8n-db;
CREATE USER n8n-user WITH PASSWORD 'random-password';
GRANT ALL PRIVILEGES ON DATABASE n8n-db TO n8n-user;
```

### TLS <a href="#tls" id="tls"></a>

你可以在以下配置之间选择：

- 不声明（默认）：使用 `SSL=off` 连接
- 仅声明 CA 和 unauthorized flag：使用 `SSL=on` 连接，并验证 server signature
- 声明 `_{CERT,KEY}` 以及上述配置：使用 certificate 和 key 进行 client TLS authentication

## SQLite <a href="#sqlite" id="sqlite"></a>

如果没有定义任何内容，默认会使用此 database。

Database file 位于：
`~/.n8n/database.sqlite`
