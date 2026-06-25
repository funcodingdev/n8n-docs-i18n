---
contentType: howto
nodeTitle: GUI 安装
originalFilePath: integrations/community-nodes/installation/gui-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/gui-install
url: >-
  https://docs.n8n.io/integrations/community-nodes/installation-and-management/gui-installation
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# GUI 安装

{% hint style="info" %}
**仅限 Owner 和 Admin 用户**

只有拥有 Owner 或 Admin 角色的用户，才能在自托管 n8n 实例上从 npm 安装和管理社区 node。实例 owner 是设置和管理用户管理的人。
{% endhint %}

## 安装社区 node <a href="#install-a-community-node" id="install-a-community-node"></a>

要从 npm 安装社区 node：

1. 前往 **Settings** > **Community Nodes**。
2. 选择 **Install**。
3. 找到要安装的 node：
   1. 选择 **Browse**。n8n 会带你进入 npm 搜索结果页，显示所有带有 `n8n-community-node-package` 关键词标签的 npm package。
   2. 浏览结果列表。你可以过滤结果或添加更多关键词。
   3. 找到所需 package 后，记下 package 名称。如果要安装特定版本，也请记下版本号。
   4. 返回 n8n。
4.  输入 npm package 名称，也可以选择输入版本号或 dist-tag。例如，假设有一个用于访问名为 “Storms” 的天气 API 的社区 node。Package 名称是 n8n-node-storms，并且有三个主版本。<br>

    * 要安装名为 n8n-node-weather 的 package 的最新版本：在 **Enter npm package name** 中输入 `n8n-nodes-storms`。
    * 要安装版本 2.3：在 **Enter npm package name** 中输入 `n8n-node-storms@2.3`。
    * 要从 `beta` 等 dist-tag 安装：在 **Enter npm package name** 中输入 `n8n-node-storms@beta`。你可以使用 package 作者发布的任何 [npm dist-tag](https://docs.npmjs.com/cli/commands/npm-dist-tag)，例如 `beta`、`next` 或 `latest`。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Dist-tag 只会在安装时解析一次</strong></p><p>当你使用 dist-tag 安装 package 时，n8n 会在当时将该 tag 解析为当前版本。未来更新不会跟随该 dist-tag。例如，如果你安装 <code>n8n-node-storms@beta</code>，且 <code>beta</code> 指向版本 <code>2.0.0-beta.1</code>，n8n 会安装该特定版本。后续更新会与已安装的 semver 版本比较，而不是与 <code>beta</code> tag 比较。</p></div>
5. 同意使用社区 node 的[风险](../risks.md)：选择 **I understand the risks of installing unverified code from a public source.**
6. 选择 **Install**。n8n 会安装该 node，并返回 **Settings** 中的 **Community Nodes** 列表。

{% hint style="info" %}
**封禁列表中的 node**

n8n 维护了一份阻止安装的社区 node 封禁列表。更多信息请参阅 [n8n 社区 node 封禁列表](../blocklist.md)。
{% endhint %}

## 卸载社区 node <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

要卸载社区 node：

1. 前往 **Settings** > **Community nodes**。
2. 在要卸载的 node 上，选择 **Options** <img src="../../.gitbook/assets/three-dot-options-menu (2).png" alt="Three dots options menu" data-size="line">。
3. 选择 **Uninstall package**。
4. 在确认弹窗中选择 **Uninstall Package**。

## 升级社区 node <a href="#upgrade-a-community-node" id="upgrade-a-community-node"></a>

{% hint style="warning" %}
**版本中的 breaking change**

Node 开发者可能会在新版本中引入 breaking change。Breaking change 是会破坏既有功能的更新。根据 node 开发者选择的版本管理方式，升级到包含 breaking change 的版本可能导致所有使用该 node 的 workflow 失效。升级 node 时请谨慎。如果发现升级导致问题，可以[降级](gui-installation.md#downgrade-a-community-node)。
{% endhint %}

\### 升级到最新版本

你可以在 **Settings** > **community nodes** 的 node 列表中将社区 node 升级到最新版本。

当社区 node 有新版本可用时，n8n 会在该 node 上显示 **Update** 按钮。点击该按钮即可升级到最新版本。

### 升级到特定版本 <a href="#upgrade-to-a-specific-version" id="upgrade-to-a-specific-version"></a>

要升级到特定版本（不是最新版本的版本），请先卸载该 node，然后重新安装，并确保指定目标版本。更多指导请按照[安装](gui-installation.md#install-a-community-node)说明操作。

## 降级社区 node <a href="#downgrade-a-community-node" id="downgrade-a-community-node"></a>

如果社区 node 的某个特定版本存在问题，你可能希望回滚到之前的版本。

为此，请卸载社区 node，然后重新安装，并指定特定 node 版本。更多指导请按照[安装](gui-installation.md#install-a-community-node)说明操作。
