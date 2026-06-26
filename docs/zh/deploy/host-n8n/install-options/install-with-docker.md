---
contentType: tutorial
nodeTitle: Install with Docker
originalFilePath: hosting/installation/docker.md
originalUrl: 'https://docs.n8n.io/hosting/installation/docker'
url: 'https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker'
layout:
  description:
    visible: false
---

# Docker 安装 <a href="#docker-installation" id="docker-installation"></a>

n8n 建议在大多数自托管场景中使用 [Docker](https://www.docker.com/)。它提供干净、隔离的环境，避免操作系统和工具不兼容，并让 database 和环境管理更简单。

你也可以通过 [Docker Compose](use-a-cloud-provider/use-docker-compose.md) 在 Docker 中使用 n8n。你可以在 [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting) 中找到适用于不同架构的 Docker Compose 配置。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

你也可以跟随我们的视频指南操作：

{% embed url="https://www.youtube.com/embed/6ET3G7GiqZA?si=mwCKbtyLqNCRc2pa" %}

## 先决条件 <a href="#prerequisites" id="prerequisites"></a>

继续之前，请先安装 Docker：

* [Docker Desktop](https://docs.docker.com/get-docker/) 可用于 Mac、Windows 和 Linux。Docker Desktop 包含 Docker Engine 和 Docker Compose。
* [Docker Engine](https://docs.docker.com/engine/install/) 和 [Docker Compose](https://docs.docker.com/compose/install/linux/) 也可作为 Linux 上的独立 packages 使用。适合没有图形环境的 Linux 机器，或你不想使用 Docker Desktop UI 的场景。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 启动 n8n <a href="#starting-n8n" id="starting-n8n"></a>

在 terminal 中运行以下命令，将 `<YOUR_TIMEZONE>` placeholders 替换为[你的时区](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)：

```shell
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
 -e TZ="<YOUR_TIMEZONE>" \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

此命令会创建用于存储持久数据的 volume，下载所需的 n8n image，并使用以下设置启动 container：

* 在 host 上映射并暴露端口 `5678`。
* 为 container 设置时区：
	* `TZ` environment variable 会设置系统时区，控制 `date` 等 scripts 和 commands 的返回结果。
	* [`GENERIC_TIMEZONE` environment variable](../configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md) 会为 [Schedule Trigger node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.scheduletrigger) 等面向 schedule 的 nodes 设置正确时区。
* 为 n8n configuration file 强制执行安全文件权限。
* 启用 [task runners](../configure-n8n/set-up-task-runners.md)，这是在 n8n 中执行 tasks 的推荐方式。
* 将 `n8n_data` volume 挂载到 `/home/node/.n8n` 目录，以便在 container 重启之间持久保存数据。

运行后，你可以打开以下地址访问 n8n：
[http://localhost:5678](http://localhost:5678)

## 与 PostgreSQL 一起使用 <a href="#using-with-postgresql" id="using-with-postgresql"></a>

默认情况下，n8n 使用 SQLite 保存 credentials[^1]、过去的 executions 和 workflows。n8n 也支持 PostgreSQL，可使用如下环境变量进行配置。

{% hint style="info" %}
**仍建议持久化 `.n8n` 目录**

使用 PostgreSQL 时，n8n 不需要使用 `.n8n` 目录保存 SQLite database file。不过，该目录仍包含其他重要数据，例如 encryption keys、instance logs 和 source control feature assets。虽然你可以绕过其中一些要求（例如设置 [`N8N_ENCRYPTION_KEY` environment variable](../configure-n8n/basic-configuration/use-environment-variables/deployment.md)），但最好继续为该目录映射 persistent volume，以避免潜在问题。
{% endhint %}

要将 n8n 与 PostgreSQL 一起使用，请执行以下命令，并将 placeholders（以尖括号表示，例如 `<POSTGRES_USER>`）替换为你的实际值：

```shell
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
 -e TZ="<YOUR_TIMEZONE>" \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -e DB_TYPE=postgresdb \
 -e DB_POSTGRESDB_DATABASE=<POSTGRES_DATABASE> \
 -e DB_POSTGRESDB_HOST=<POSTGRES_HOST> \
 -e DB_POSTGRESDB_PORT=<POSTGRES_PORT> \
 -e DB_POSTGRESDB_USER=<POSTGRES_USER> \
 -e DB_POSTGRESDB_SCHEMA=<POSTGRES_SCHEMA> \
 -e DB_POSTGRESDB_PASSWORD=<POSTGRES_PASSWORD> \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

你可以在 [n8n hosting repository](https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres) 中找到 PostgreSQL 的完整 `docker-compose` 文件。

## 更新 <a href="#updating" id="updating"></a>

要更新 n8n，请在 Docker Desktop 中导航到 **Images** tab，并从 context menu 中选择 **Pull** 下载最新 n8n image：

![Docker Desktop](../../.gitbook/assets/docker_desktop.png)

你也可以使用 command line 拉取最新版本或特定版本：

```shell
# Pull latest (stable) version <a href="#pull-latest-stable-version" id="pull-latest-stable-version"></a>
docker pull docker.n8n.io/n8nio/n8n

# Pull specific version <a href="#pull-specific-version" id="pull-specific-version"></a>
docker pull docker.n8n.io/n8nio/n8n:1.81.0

# Pull next (unstable) version <a href="#pull-next-unstable-version" id="pull-next-unstable-version"></a>
docker pull docker.n8n.io/n8nio/n8n:next
```

拉取更新后的 image 后，停止你的 n8n container 并重新启动它。你也可以使用 command line。将以下命令中的 `<container_id>` 替换为你在第一条命令中找到的 container ID：

```shell
# Find your container ID <a href="#find-your-container-id" id="find-your-container-id"></a>
docker ps -a

# Stop the container with the `<container_id>` <a href="#stop-the-container-with-the-lesscontaineridgreater" id="stop-the-container-with-the-lesscontaineridgreater"></a>
docker stop <container_id>

# Remove the container with the `<container_id>` <a href="#remove-the-container-with-the-lesscontaineridgreater" id="remove-the-container-with-the-lesscontaineridgreater"></a>
docker rm <container_id>

# Start the container <a href="#start-the-container" id="start-the-container"></a>
docker run --name=<container_name> [options] -d docker.n8n.io/n8nio/n8n
```

### 更新 Docker Compose <a href="#updating-docker-compose" id="updating-docker-compose"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/yA5x9FIRtnDGdghFU93g/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/WSJc9HCsn26Um2uT6zAQ/" %}

### Full stack <a href="#full-stack" id="full-stack"></a>

这会在 containers 中一起运行 n8n 和 cloudflared。tunnel URL 会在启动时打印出来，一切都会自动连好：

```shell
pnpm stack --tunnel
```

### Services only <a href="#services-only" id="services-only"></a>

如果你更愿意使用 `pnpm dev` 或 `pnpm start` 在本地运行 n8n，可以将 cloudflared 作为 standalone service 启动：

```shell
# Terminal 1: Start the cloudflared tunnel service <a href="#terminal-1-start-the-cloudflared-tunnel-service" id="terminal-1-start-the-cloudflared-tunnel-service"></a>
pnpm --filter n8n-containers services --services cloudflared

# Terminal 2: Start n8n locally <a href="#terminal-2-start-n8n-locally" id="terminal-2-start-n8n-locally"></a>
pnpm dev
```

`services` 命令会：

1. 启动 cloudflared，并指向 `host.docker.internal:5678`（你的本地 n8n）。
2. 从 cloudflared 的 metrics endpoint 获取 public tunnel URL。
3. 将包含 `WEBHOOK_URL` 和 `N8N_PROXY_HOPS=1` 的 `.env` 文件写入 `packages/cli/bin/.env`。
4. `pnpm dev` 和 `pnpm start` 会通过 dotenv 自动读取该 `.env`。

完成后清理：

```shell
pnpm --filter n8n-containers services:clean
```

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

* 在 [Docker image](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n) 的 README 文件中查找更多 Docker 设置相关信息。
{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}

[^1]: 在 n8n 中，credentials 保存用于连接特定 apps 和 services 的身份验证信息。使用你的身份验证信息（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与该 service 交互。
