---
contentType: tutorial
nodeTitle: Install with npm
originalFilePath: hosting/installation/npm.md
originalUrl: 'https://docs.n8n.io/hosting/installation/npm'
url: 'https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm'
layout:
  description:
    visible: false
---

# npm <a href="#npm" id="npm"></a>

npm 是在本地机器上快速开始使用 n8n 的方式。你必须已安装 [Node.js](https://nodejs.org/en/)。n8n 要求 Node.js 版本在 20.19 到 24.x 之间，包含这两个版本。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 使用 npx 试用 n8n <a href="#try-n8n-with-npx" id="try-n8n-with-npx"></a>

你可以使用 npx 试用 n8n，而无需安装它。


在 terminal 中运行：

```bash
npx n8n
```

此命令会下载启动 n8n 所需的一切。然后你可以打开 [http://localhost:5678](http://localhost:5678) 访问 n8n，并开始构建 workflows。

## 使用 npm 全局安装 <a href="#install-globally-with-npm" id="install-globally-with-npm"></a>

要全局安装 n8n，请使用 npm：

```bash
npm install n8n -g
```

要安装或更新到特定版本的 n8n，请使用 `@` 语法指定版本。例如：

```bash
npm install -g n8n@0.126.1
```

要安装 `next`：

```bash
npm install -g n8n@next
```

安装完成后，运行以下命令启动 n8n：

```bash
n8n
# or <a href="#or" id="or"></a>
n8n start
```


### 后续步骤 <a href="#next-steps" id="next-steps"></a>

使用 [Quickstarts](/try-it-out/index.md) 试用 n8n。

## 更新 <a href="#updating" id="updating"></a>

要将 n8n 实例更新到 `latest` 版本，请运行：

```bash
npm update -g n8n
```

要安装 `next` 版本：

```bash
npm install -g n8n@next
```

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/WSJc9HCsn26Um2uT6zAQ/" %}

{% hint style="info" %}
**需要 Docker**

tunnel 使用 cloudflared，它作为 Docker container 运行。即使通过 npm 运行 n8n，也请确保你的机器已安装 [Docker](https://docs.docker.com/get-docker/)。
{% endhint %}

对于 npm 安装，请使用 **services only** 方法。将 cloudflared 作为 standalone service 启动，然后在本地运行 n8n：

```bash
# Terminal 1: Start the cloudflared tunnel service <a href="#terminal-1-start-the-cloudflared-tunnel-service" id="terminal-1-start-the-cloudflared-tunnel-service"></a>
pnpm --filter n8n-containers services --services cloudflared

# Terminal 2: Start n8n locally <a href="#terminal-2-start-n8n-locally" id="terminal-2-start-n8n-locally"></a>
pnpm dev
```

`services` 命令会启动 cloudflared，获取 public tunnel URL，并将包含 `WEBHOOK_URL` 和 `N8N_PROXY_HOPS=1` 的 `.env` 文件写入 `packages/cli/bin/.env`。n8n 启动时会自动读取此 `.env`。

完成后清理：

```bash
pnpm --filter n8n-containers services:clean
```

对于 full stack 方法（n8n 和 cloudflared 都在 containers 中），请参阅 [Docker tunnel setup](install-with-docker.md#n8n-with-tunnel)。

## 回滚升级 <a href="#reverting-an-upgrade" id="reverting-an-upgrade"></a>

安装你想回退到的旧版本。

如果升级涉及 database migration：

1. 查看功能文档和 release notes，确认是否有需要手动执行的更改。
1. 在当前版本上运行 `n8n db:revert` 以回滚 database。如果你想回滚多个 database migration，需要重复此过程。

## Windows 故障排除 <a href="#windows-troubleshooting" id="windows-troubleshooting"></a>

如果你在 Windows 上运行 n8n 时遇到问题，请确保 Node.js 环境已正确设置。请按照 Microsoft 的指南[在 Windows 上安装 NodeJS](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)操作。
