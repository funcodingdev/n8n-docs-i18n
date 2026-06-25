---
contentType: explanation
nodeTitle: 风险
originalFilePath: integrations/community-nodes/risks.md
originalUrl: 'https://docs.n8n.io/integrations/community-nodes/risks'
url: 'https://docs.n8n.io/integrations/community-nodes/risks'
layout:
  description:
    visible: false
---

# 使用社区 node 的风险 <a href="#risks-when-using-community-nodes" id="risks-when-using-community-nodes"></a>

从 npm 安装社区 node 意味着你会将来自公共来源的未验证代码安装到 n8n 实例中。这存在一些风险。

风险包括：

* 系统安全：社区 node 对运行 n8n 的机器拥有完全访问权限，可以执行任何操作，包括恶意操作。
* 数据安全：你使用的任何社区 node 都可以访问 workflow 中的数据。
* Breaking change：node 开发者可能会在新版本中引入 breaking change。Breaking change 是会破坏既有功能的更新。根据 node 开发者选择的版本管理方式，升级到包含 breaking change 的版本可能导致所有使用该 node 的 workflow 失效。升级 node 时请谨慎。

{% hint style="info" %}
**n8n 会审查 verified community node**

除了 npm 上公开可用的社区 node，n8n 还会检查部分 node，并将它们作为 [nodes panel 中的 verified community node](installation-and-management/install-verified-community-nodes.md) 提供。这些 node 必须满足一组数据和系统安全要求才能获批。
{% endhint %}

## 报告不良社区 node <a href="#report-bad-community-nodes" id="report-bad-community-nodes"></a>



你可以将不良社区 node 报告给 [security@n8n.io](mailto: security@n8n.io)



## 禁用社区 node <a href="#disable-community-nodes" id="disable-community-nodes"></a>

如果你自托管 n8n，可以通过将 `N8N_COMMUNITY_PACKAGES_ENABLED` 设置为 `false` 来禁用社区 node。在 n8n cloud 上，请访问 [Cloud Admin Panel](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/use-the-admin-dashboard)，并在那里禁用社区 node。更多信息请参阅[故障排查](troubleshooting.md)。
