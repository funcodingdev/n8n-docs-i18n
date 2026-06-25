---
contentType: overview
nodeTitle: 安装和管理
originalFilePath: integrations/community-nodes/installation/index.md
originalUrl: 'https://docs.n8n.io/integrations/community-nodes/installation'
url: 'https://docs.n8n.io/integrations/community-nodes/installation-and-management'
layout:
  description:
    visible: false
---

# 安装和管理社区 node <a href="#install-and-manage-community-nodes" id="install-and-manage-community-nodes"></a>

安装社区 node 有四种方式：

* 在 n8n 中使用 [nodes panel](install-verified-community-nodes.md)（仅适用于 verified community node）。
* 在 n8n 中[使用 GUI](gui-installation.md)：使用此方法从 npm registry 安装社区 node。
* [从命令行手动安装](manual-installation.md)：如果你的 n8n 实例不支持通过 app 内 GUI 安装，请使用此方法从 npm 安装社区 node。
* [通过环境变量安装](environment-variable-installation.md)：使用此方法以固定的社区 package 集合启动实例，例如通过部署流水线。

{% hint style="info" %}
**仅自托管实例可从 npm 安装**

未验证的社区 node 在 n8n cloud 上不可用，需要[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n。
{% endhint %}
