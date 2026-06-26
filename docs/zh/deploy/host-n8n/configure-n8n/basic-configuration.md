---
title: Configuration methods
description: 如何为 n8n 设置环境变量。
contentType: howto
nodeTitle: Basic configuration
originalFilePath: hosting/configuration/configuration-methods.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-methods'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration'
layout:
  description:
    visible: false
---

# 配置 <a href="#configuration" id="configuration"></a>

你可以使用环境变量更改 n8n 的 settings。可用配置的完整列表请参阅 [Environment Variables](basic-configuration/use-environment-variables/README.md)。

## 通过命令行设置环境变量 <a href="#set-environment-variables-by-command-line" id="set-environment-variables-by-command-line"></a>

### npm <a href="#npm" id="npm"></a>

对于 npm，请在 terminal 中设置所需的环境变量。具体命令取决于你的 command line。

Bash CLIs：

```bash
export <variable>=<value>
```

在 cmd.exe 中：

```bash
set <variable>=<value>
```

在 PowerShell 中：

```powershell
$env:<variable>=<value>
```

### Docker <a href="#docker" id="docker"></a>

在 Docker 中，你可以从 command line 使用 `-e` flag：

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e N8N_TEMPLATES_ENABLED="false" \
 docker.n8n.io/n8nio/n8n
```


## Docker Compose 文件 <a href="#docker-compose-file" id="docker-compose-file"></a>

在 Docker 中，你可以在 `docker-compose.yaml` 文件的 `n8n: environment:` 元素中设置环境变量。

例如：

```yaml
n8n:
    environment:
      - N8N_TEMPLATES_ENABLED=false
```

## 将敏感数据保存在单独文件中 <a href="#keeping-sensitive-data-in-separate-files" id="keeping-sensitive-data-in-separate-files"></a>

你可以为单个环境变量追加 `_FILE`，以便在单独文件中提供其配置，从而避免通过环境变量传递敏感详情。n8n 会从给定名称的文件加载数据，因此可以从 [Docker-Secrets](https://docs.docker.com/engine/swarm/secrets/) 和 [Kubernetes-Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) 加载数据。

有关每个变量的详情，请参阅 [Environment variables](basic-configuration/use-environment-variables/README.md)。

虽然大多数环境变量都可以使用 `_FILE` suffix，但它对 credentials[^1] 和 database configuration 等敏感数据更有用。下面是一些示例：

```yaml
CREDENTIALS_OVERWRITE_DATA_FILE=/path/to/credentials_data
DB_TYPE_FILE=/path/to/db_type
DB_POSTGRESDB_DATABASE_FILE=/path/to/database_name
DB_POSTGRESDB_HOST_FILE=/path/to/database_host
DB_POSTGRESDB_PORT_FILE=/path/to/database_port
DB_POSTGRESDB_USER_FILE=/path/to/database_user
DB_POSTGRESDB_PASSWORD_FILE=/path/to/database_password
DB_POSTGRESDB_SCHEMA_FILE=/path/to/database_schema
DB_POSTGRESDB_SSL_CA_FILE=/path/to/ssl_ca
DB_POSTGRESDB_SSL_CERT_FILE=/path/to/ssl_cert
DB_POSTGRESDB_SSL_KEY_FILE=/path/to/ssl_key
DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED_FILE=/path/to/ssl_reject_unauth
```

[^1]: 在 n8n 中，credentials 保存用于连接特定 apps 和 services 的身份验证信息。使用你的身份验证信息（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与该 service 交互。
