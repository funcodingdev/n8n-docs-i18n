---
contentType: howto
nodeTitle: 手动安装
originalFilePath: integrations/community-nodes/installation/manual-install.md
originalUrl: 'https://docs.n8n.io/integrations/community-nodes/installation/manual-install'
url: >-
  https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation
layout:
  description:
    visible: false
---

# 从 npm 手动安装社区 node <a href="#manually-install-community-nodes-from-npm" id="manually-install-community-nodes-from-npm"></a>

你可以在自托管 n8n 上从 npm registry 手动安装社区 node。

在以下情况下，你需要手动安装社区 node：

* 你的 n8n 实例以 queue mode 运行。
* 你想安装 [private package](https://docs.npmjs.com/creating-and-publishing-private-packages)。

## 安装社区 node <a href="#install-a-community-node" id="install-a-community-node"></a>

访问 Docker shell：

```sh
docker exec -it n8n sh
```

如果 `~/.n8n/nodes` 尚不存在，请创建它并进入该目录：

```sh
mkdir ~/.n8n/nodes
cd ~/.n8n/nodes
```

安装 node：

```sh
npm i n8n-nodes-nodeName
```

然后重启 n8n。

## 卸载社区 node <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

访问 Docker shell：

```sh
docker exec -it n8n sh
```

运行 npm uninstall：

```sh
npm uninstall n8n-nodes-nodeName
```

## 升级社区 node <a href="#upgrade-a-community-node" id="upgrade-a-community-node"></a>

{% hint style="warning" %}
**版本中的 breaking change**

Node 开发者可能会在新版本中引入 breaking change。Breaking change 是会破坏既有功能的更新。根据 node 开发者选择的版本管理方式，升级到包含 breaking change 的版本可能导致所有使用该 node 的 workflow 失效。升级 node 时请谨慎。如果发现升级导致问题，可以[降级](#upgrade-or-downgrade-to-a-specific-version)。
{% endhint %}

### 升级到最新版本 <a href="#upgrade-to-the-latest-version" id="upgrade-to-the-latest-version"></a>

访问 Docker shell：

```sh
docker exec -it n8n sh
```

运行 npm update：

```sh
npm update n8n-nodes-nodeName
```

### 升级或降级到特定版本 <a href="#upgrade-or-downgrade-to-a-specific-version" id="upgrade-or-downgrade-to-a-specific-version"></a>

访问 Docker shell：

```sh
docker exec -it n8n sh
```

运行 npm uninstall 移除当前版本：

```sh
npm uninstall n8n-nodes-nodeName
```

运行 npm install 并指定版本：

```sh
# 将 2.1.0 替换为你的版本号 <a href="#replace-210-with-your-version-number" id="replace-210-with-your-version-number"></a>
npm install n8n-nodes-nodeName@2.1.0
```
