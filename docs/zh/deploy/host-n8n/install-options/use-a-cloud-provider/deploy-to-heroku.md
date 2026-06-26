---
contentType: tutorial
nodeTitle: Deploy to Heroku
originalFilePath: hosting/installation/server-setups/heroku.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/heroku'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku
layout:
  description:
    visible: false
---

# 在 Heroku 上托管 n8n <a href="#hosting-n8n-on-heroku" id="hosting-n8n-on-heroku"></a>

本托管指南展示如何在 Heroku 上自托管 n8n。它使用：


- [Docker Compose](https://docs.docker.com/compose/) 创建并定义应用组件以及它们如何协同工作。
- [Heroku's PostgreSQL service](https://devcenter.heroku.com/categories/heroku-postgres) 托管 n8n 的数据存储。
- 一个 **Deploy to Heroku** 按钮，提供只需少量配置的一键部署。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}


## 使用部署模板创建 Heroku 项目 <a href="#use-the-deployment-template-to-create-a-heroku-project" id="use-the-deployment-template-to-create-a-heroku-project"></a>

开始将 n8n 部署到 Heroku 的最快方式，是使用 **Deploy to Heroku** 按钮：

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/n8n-io/n8n-heroku/tree/main)

这会打开 Heroku 上的 **Create New App** 页面。设置项目名称，并选择要部署项目的 region。

### 配置环境变量 <a href="#configure-environment-variables" id="configure-environment-variables"></a>

Heroku 会预填 `app.json` 文件 `env` 部分中定义的配置选项，这也会为 n8n 使用的环境变量设置默认值。

你可以按自己的需求更改这些值。你必须更改以下值：

- **N8N_ENCRYPTION_KEY**，n8n 在保存到 database 前使用它[加密用户账号详情](../../configure-n8n/basic-configuration/use-environment-variables/deployment.md)。
- **WEBHOOK_URL** 应与你创建的应用名称匹配，以确保 webhooks 使用正确 URL。

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

选择 **Deploy app**。

Heroku 构建并部署应用后，会提供 **Manage App** 或 **View** 应用的链接。

{% hint style="info" %}
**Heroku 和 DNS**

请参阅 [Heroku documentation](https://devcenter.heroku.com/categories/networking-dns)，了解如何将你的域名连接到 Heroku 应用。
{% endhint %}
## 更改部署模板 <a href="#changing-the-deployment-template" id="changing-the-deployment-template"></a>

你可以 fork [repository](https://github.com/n8n-io/n8n-heroku)，并从你的 fork 部署，从而修改部署模板。

### Dockerfile <a href="#the-dockerfile" id="the-dockerfile"></a>

默认情况下，Dockerfile 会拉取最新 n8n image。如果你想使用其他版本或固定版本，请更新 `Dockerfile` 顶部行的 image tag。

### Heroku 和暴露端口 <a href="#heroku-and-exposing-ports" id="heroku-and-exposing-ports"></a>

Heroku 不允许基于 Docker 的应用使用 `EXPOSE` 命令定义暴露端口。Heroku 会提供一个 `PORT` 环境变量，并在应用运行时动态填充它。`entrypoint.sh` 文件会覆盖默认 Docker image 命令，改为设置 Heroku 提供的 port 变量。然后你可以在 web browser 中通过端口 80 访问 n8n。

{% hint style="info" %}
**Heroku 的 Docker 限制**

[阅读本指南](https://devcenter.heroku.com/articles/container-registry-and-runtime#unsupported-dockerfile-commands)，了解在 Heroku 上使用 Docker 的限制详情。
{% endhint %}
### 配置 Heroku <a href="#configuring-heroku" id="configuring-heroku"></a>

`heroku.yml` 文件定义你想在 Heroku 上创建的应用。它包含两个部分：

* `setup` > `addons` 定义要使用的 Heroku addons。这里是 PostgreSQL database addon。
* `build` 部分定义 Heroku 如何构建应用。这里使用 Docker buildpack，基于提供的 `Dockerfile` 构建 `web` service。

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
