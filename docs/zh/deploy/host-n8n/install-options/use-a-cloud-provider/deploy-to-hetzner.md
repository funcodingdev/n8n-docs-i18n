---
contentType: tutorial
nodeTitle: Deploy to Hetzner
originalFilePath: hosting/installation/server-setups/hetzner.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/hetzner'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner
layout:
  description:
    visible: false
---

# 在 Hetzner cloud 上托管 n8n <a href="#hosting-n8n-on-hetzner-cloud" id="hosting-n8n-on-hetzner-cloud"></a>

本托管指南展示如何在 Hetzner cloud server 上自托管 n8n。它使用：

* [Caddy](https://caddyserver.com)（reverse proxy）允许从互联网访问 Server。
* [Docker Compose](https://docs.docker.com/compose/) 创建并定义应用组件以及它们如何协同工作。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 创建 server <a href="#create-a-server" id="create-a-server"></a>

1. [登录](https://console.hetzner.cloud/) Hetzner Cloud Console。
2. 选择用于托管 server 的项目，或选择 **+ NEW PROJECT** 创建新项目。
3. 在要添加 server 的项目 tile 上选择 **+ CREATE SERVER**。

你可以按需求更改大部分设置；但由于本指南使用 Docker 运行应用，请在 **Image** 部分，从 **APPS** tab 中选择 "Docker CE"。

{% hint style="info" %}
**Type**

创建 server 时，Hetzner 会要求你选择 plan。对于大多数使用级别，CPX11 type 已经足够。
{% endhint %}
{% hint style="info" %}
**SSH keys**

Hetzner 允许你在 SSH 和基于密码的身份验证之间选择。SSH 更安全。本指南后续假设你使用 SSH。
{% endhint %}
## 登录 server <a href="#log-in-to-your-server" id="log-in-to-your-server"></a>

本指南后续需要你使用带 SSH 的 terminal 登录 server。更多信息请参阅 [Access with SSH/rsync/BorgBackup](https://docs.hetzner.com/robot/storage-box/access/access-ssh-rsync-borg)。你可以在项目 server 列表中找到 public IP。

## 安装 Docker Compose <a href="#install-docker-compose" id="install-docker-compose"></a>

Hetzner Docker app image 未安装 Docker compose。使用以下命令安装：

```shell
apt update && apt -y upgrade
apt install docker-compose-plugin
```

## Clone 配置 repository <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Docker Compose、n8n 和 Caddy 需要一系列 folders 和 configuration files。你可以从[此 repository](https://github.com/n8n-io/n8n-docker-caddy) 将它们 clone 到 server 的 root user folder。以下步骤会说明需要更改哪个文件以及要做哪些更改。

使用以下命令 clone repository：

```shell
git clone https://github.com/n8n-io/n8n-docker-caddy.git
```

然后切换到你 clone 的 repository root：

```shell
cd n8n-docker-caddy
```

## 默认 folders 和 files <a href="#default-folders-and-files" id="default-folders-and-files"></a>

Host operating system（server）会将你创建的两个 folders 复制到 Docker containers，使它们可供 Docker 使用。这两个 folders 是：

- `caddy_config`：保存 Caddy configuration files。
- `local_files`：用于存放你上传或使用 n8n 添加的 files。

### 创建 Docker volume <a href="#create-docker-volume" id="create-docker-volume"></a>

要在重启之间持久化 Caddy cache 并加快启动速度，请创建一个 Docker 可在重启之间复用的 [Docker volume](https://docs.docker.com/storage/volumes/)：

```shell
docker volume create caddy_data
```

为 n8n data 创建 Docker volume：

```shell
sudo docker volume create n8n_data
```

## 设置 DNS <a href="#set-up-dns" id="set-up-dns"></a>

n8n 通常运行在 subdomain 上。请在你的 provider 中为 subdomain 创建 DNS record，并将它指向 server 的 IP address。具体步骤取决于你的 DNS provider，但通常需要为 n8n subdomain 创建新的 "A" record。DigitalOcean 提供了 [An Introduction to DNS Terminology, Components, and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts)。

## 打开端口 <a href="#open-ports" id="open-ports"></a>

n8n 作为 web application 运行，因此 server 需要允许端口 80 的非安全流量和端口 443 的安全流量进入。

运行以下两个命令，在 server firewall 中打开这些端口：

```shell
sudo ufw allow 80
sudo ufw allow 443
```

## 配置 n8n <a href="#configure-n8n" id="configure-n8n"></a>

n8n 需要设置一些环境变量，传递给 Docker container 中运行的应用。示例 `.env` 文件包含需要替换为你自己的值的 placeholders。

使用以下命令打开文件：

```shell
nano .env
```

该文件包含 inline comments，帮助你了解需要更改的内容。

有关 n8n environment variables 的详细信息，请参阅 [Environment variables](../../configure-n8n/basic-configuration/use-environment-variables/README.md)。

## Docker Compose 文件 <a href="#the-docker-compose-file" id="the-docker-compose-file"></a>

Docker Compose 文件（`docker-compose.yml`）定义应用需要的 services，此处为 Caddy 和 n8n。

- Caddy service definition 定义它使用的 ports 以及要复制到 containers 的 local volumes。
- n8n service definition 定义它使用的 ports、n8n 运行所需的 environment variables（部分定义在 `.env` 文件中），以及需要复制到 containers 的 volumes。

Docker Compose 文件使用 `.env` 文件中设置的 environment variables，因此你应该不需要更改它的内容；如需查看，请运行以下命令：

```shell
nano docker-compose.yml
```

## 配置 Caddy <a href="#configure-caddy" id="configure-caddy"></a>

Caddy 需要知道它应该服务哪些 domains，以及要向外部世界暴露哪个 port。编辑 `caddy_config` folder 中的 `Caddyfile` 文件。

```shell
nano caddy_config/Caddyfile
```

将 placeholder subdomain 改成你的 subdomain。如果你按照步骤将 subdomain 命名为 n8n，那么完整域名类似 `n8n.example.com`。`reverse_proxy` 设置中的 `n8n` 告诉 Caddy 使用 `docker-compose.yml` 文件中定义的 service definition：

```text
n8n.<domain>.<suffix> {
    reverse_proxy n8n:5678 {
      flush_interval -1
    }
}
```

## 启动 Docker Compose <a href="#start-docker-compose" id="start-docker-compose"></a>

使用以下命令启动 n8n 和 Caddy：

```shell
docker compose up -d
```

这可能需要几分钟。

## 测试设置 <a href="#test-your-setup" id="test-your-setup"></a>

在 browser 中打开由先前定义的 subdomain 和 domain name 组成的 URL。输入先前定义的 user name 和 password，你应该就能访问 n8n。

## 停止 n8n 和 Caddy <a href="#stop-n8n-and-caddy" id="stop-n8n-and-caddy"></a>

你可以使用以下命令停止 n8n 和 Caddy：

```shell
sudo docker compose stop
```

## 更新 <a href="#updating" id="updating"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/yA5x9FIRtnDGdghFU93g/" %}

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
