---
contentType: tutorial
description: 使用 Docker Compose 安装并运行 n8n
nodeTitle: Use Docker Compose
originalFilePath: hosting/installation/server-setups/docker-compose.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/docker-compose'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose
layout:
  description:
    visible: false
---

# Docker-Compose <a href="#docker-compose" id="docker-compose"></a>

这些说明介绍如何使用 Docker Compose 在 Linux server 上运行 n8n。

如果你已经安装了 Docker 和 Docker-Compose，可以从[第 3 步](#3-dns-setup)开始。

你可以在 [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting) 中找到适用于不同架构的 Docker Compose 配置。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 1. 安装 Docker 和 Docker Compose <a href="#1-install-docker-and-docker-compose" id="1-install-docker-and-docker-compose"></a>

安装 Docker 和 Docker Compose 的方式取决于你的 Linux distribution。你可以在下面链接中找到每个组件的具体说明：

* [Docker Engine](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/linux/)

按照安装说明完成后，输入以下命令验证 Docker 和 Docker Compose 是否可用：

```shell
docker --version
docker compose version
```

## 2. 可选：Non-root user access <a href="#2-optional-non-root-user-access" id="2-optional-non-root-user-access"></a>

你可以选择授予无需 `sudo` 命令即可运行 Docker 的访问权限。

要授予当前登录用户访问权限（假设该用户拥有 `sudo` access），请运行：

```shell
sudo usermod -aG docker ${USER}
# Register the `docker` group membership with current session without changing your primary group <a href="#register-the-docker-group-membership-with-current-session-without-changing-your-primary-group" id="register-the-docker-group-membership-with-current-session-without-changing-your-primary-group"></a>
exec sg docker newgrp
```

要授予其他用户访问权限，请输入以下命令，并将 `<USER_TO_RUN_DOCKER>` 替换为相应 username：

```shell
sudo usermod -aG docker <USER_TO_RUN_DOCKER>
```

你需要从该用户的任何现有 sessions 中运行 `exec sg docker newgrp`，该用户才能访问新的 group permissions。

你可以输入以下命令验证当前 session 是否识别 `docker` group：

```shell
groups
```

## 3. DNS 设置 <a href="#3-dns-setup" id="3-dns-setup"></a>

要在线或在网络上托管 n8n，请创建指向 server 的专用 subdomain。

添加 A record，将 subdomain 路由到相应位置：

| Record type | Name                              | Destination                |
|-------------|-----------------------------------|----------------------------|
| A           | `n8n`（或你想要的 subdomain） | `<your_server_IP_address>` |

## 4. 创建 `.env` 文件 <a href="#4-create-an-env-file" id="4-create-an-env-file"></a>

创建一个 project directory，用于存储 n8n environment configuration 和 Docker Compose files，并进入该目录：

```shell
mkdir n8n-compose
cd n8n-compose
```

在 `n8n-compose` 目录中创建 `.env` 文件，用于自定义 n8n 实例详情。请将其更改为与你自己的信息匹配：

```shell title=".env file"
# DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from <a href="#domainname-and-subdomain-together-determine-where-n8n-will-be-reachable-from" id="domainname-and-subdomain-together-determine-where-n8n-will-be-reachable-from"></a>
# The top level domain to serve from <a href="#the-top-level-domain-to-serve-from" id="the-top-level-domain-to-serve-from"></a>
DOMAIN_NAME=example.com

# The subdomain to serve from <a href="#the-subdomain-to-serve-from" id="the-subdomain-to-serve-from"></a>
SUBDOMAIN=n8n

# The above example serve n8n at: https://n8n.example.com <a href="#the-above-example-serve-n8n-at-httpsn8nexamplecom" id="the-above-example-serve-n8n-at-httpsn8nexamplecom"></a>

# Optional timezone to set which gets used by Cron and other scheduling nodes <a href="#optional-timezone-to-set-which-gets-used-by-cron-and-other-scheduling-nodes" id="optional-timezone-to-set-which-gets-used-by-cron-and-other-scheduling-nodes"></a>
# New York is the default value if not set <a href="#new-york-is-the-default-value-if-not-set" id="new-york-is-the-default-value-if-not-set"></a>
GENERIC_TIMEZONE=Europe/Berlin

# The email address to use for the TLS/SSL certificate creation <a href="#the-email-address-to-use-for-the-tlsssl-certificate-creation" id="the-email-address-to-use-for-the-tlsssl-certificate-creation"></a>
SSL_EMAIL=user@example.com
```

## 5. 创建 local files 目录 <a href="#5-create-local-files-directory" id="5-create-local-files-directory"></a>

在 project directory 中，创建名为 `local-files` 的目录，用于在 n8n instance 和 host system 之间共享 files（例如使用 [Read/Write Files from Disk node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.readwritefile)）：

```shell
mkdir local-files
```

下面的 Docker Compose 文件可以自动创建此目录，但手动创建可确保它具有正确的 ownership 和 permissions。

## 6. 创建 Docker Compose 文件 <a href="#6-create-docker-compose-file" id="6-create-docker-compose-file"></a>

创建 `compose.yaml` 文件。将以下内容粘贴到文件中：

```yaml title="compose.yaml file"
services:
  traefik:
    image: "traefik"
    restart: always
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.web.http.redirections.entryPoint.to=websecure"
      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.mytlschallenge.acme.tlschallenge=true"
      - "--certificatesresolvers.mytlschallenge.acme.email=${SSL_EMAIL}"
      - "--certificatesresolvers.mytlschallenge.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - traefik_data:/letsencrypt
      - /var/run/docker.sock:/var/run/docker.sock:ro

  n8n:
    image: docker.n8n.io/n8nio/n8n
    restart: always
    ports:
      - "127.0.0.1:5678:5678"
    labels:
      - traefik.enable=true
      - traefik.http.routers.n8n.rule=Host(`${SUBDOMAIN}.${DOMAIN_NAME}`)
      - traefik.http.routers.n8n.tls=true
      - traefik.http.routers.n8n.entrypoints=web,websecure
      - traefik.http.routers.n8n.tls.certresolver=mytlschallenge
      - traefik.http.middlewares.n8n.headers.SSLRedirect=true
      - traefik.http.middlewares.n8n.headers.STSSeconds=315360000
      - traefik.http.middlewares.n8n.headers.browserXSSFilter=true
      - traefik.http.middlewares.n8n.headers.contentTypeNosniff=true
      - traefik.http.middlewares.n8n.headers.forceSTSHeader=true
      - traefik.http.middlewares.n8n.headers.SSLHost=${DOMAIN_NAME}
      - traefik.http.middlewares.n8n.headers.STSIncludeSubdomains=true
      - traefik.http.middlewares.n8n.headers.STSPreload=true
      - traefik.http.routers.n8n.middlewares=n8n@docker
    environment:
      - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
      - N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - NODE_ENV=production
      - WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - TZ=${GENERIC_TIMEZONE}
    volumes:
      - n8n_data:/home/node/.n8n
      - ./local-files:/files

volumes:
  n8n_data:
  traefik_data:
```

上面的 Docker Compose 文件配置了两个 containers：一个用于 n8n，另一个运行 [traefik](https://github.com/traefik/traefik)，它是用于管理 TLS/SSL certificates 并处理 routing 的 application proxy。

它还会创建并挂载两个 [Docker Volumes](https://docs.docker.com/engine/storage/volumes/)，并挂载你之前创建的 `local-files` 目录：

| Name | Type | Container mount | Description |
|-----------------|-------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `n8n_data` | [Volume](https://docs.docker.com/engine/storage/volumes/) | `/home/node/.n8n` | n8n 保存 SQLite database file 和 encryption key 的位置。 |
| `traefik_data` | [Volume](https://docs.docker.com/engine/storage/volumes/) | `/letsencrypt` | traefik 保存 TLS/SSL certificate data 的位置。 |
| `./local-files` | [Bind](https://docs.docker.com/engine/storage/bind-mounts/) | `/files` | n8n instance 与 host 之间共享的 local directory。在 n8n 中，使用 `/files` path 从该目录读取或写入。 |

## 7. 启动 Docker Compose <a href="#7-start-docker-compose" id="7-start-docker-compose"></a>

输入以下命令启动 n8n：

```shell
sudo docker compose up -d
```

要停止 containers，请输入：

```shell
sudo docker compose stop
```

## 8. 完成 <a href="#8-done" id="8-done"></a>

现在你可以使用 `.env` 文件配置中定义的 subdomain + domain 组合访问 n8n。上面的示例会得到 `https://n8n.example.com`。

n8n 只能通过安全 HTTPS 访问，不能通过普通 HTTP 访问。

如果无法访问实例，请检查 server 的 firewall settings 和 DNS configuration。

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
