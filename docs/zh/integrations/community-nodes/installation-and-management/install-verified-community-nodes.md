---
contentType: howto
nodeTitle: 安装 verified community node
originalFilePath: integrations/community-nodes/installation/verified-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/verified-install
url: >-
  https://docs.n8n.io/integrations/community-nodes/installation-and-management/install-verified-community-nodes
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

# 安装 verified community node

{% hint style="info" %}
**仅限 n8n 实例 owner 和 admin**

n8n 实例 owner 和 admin 账户可以安装和管理 verified community node。实例 owner 是设置和管理用户管理的人。n8n 实例的所有成员都可以在自己的 workflow 中使用已安装的社区 node。
{% endhint %}

## 安装社区 node <a href="#install-a-community-node" id="install-a-community-node"></a>

要安装 [verified community node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/deploy-your-node/submit-community-nodes#submit-your-node-for-verification-by-n8n)：

1. 前往 **Canvas** 并打开 **nodes panel**（选择 `+` 或按 ++n++）。
2. **Search** 你要查找的 node。如果存在匹配的 verified community node，你会在 nodes panel 底部看到 **More from the community** 部分。
3. 选择要安装的 node。这会进入该 node 的详细视图，显示所有支持的 action。
4. 选择 **install**。这会为你的实例安装该 node，并允许所有成员在自己的 workflow 中使用它。
5. 现在你可以将该 node 添加到 workflow 中。

{% hint style="info" %}
**启用 verified community node 安装**

有些用户可能不希望在实例的 nodes panel 中显示 verified community node。在 n8n cloud 上，实例 owner 可以在 [Cloud Admin Panel](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/use-the-admin-dashboard) 中切换此功能。自托管用户可以使用[环境变量](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)控制此功能是否可用。
{% endhint %}

## 卸载社区 node <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

要卸载社区 node：

1. 前往 **Settings** > **Community nodes**。
2. 在要卸载的 node 上，选择 **Options** <img src="../../.gitbook/assets/three-dot-options-menu (2).png" alt="Three dots options menu" data-size="line">。
3. 选择 **Uninstall package**。
4. 在确认弹窗中选择 **Uninstall Package**。
