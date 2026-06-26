---
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 部署

n8n 提供两种不同的部署方式。[n8n Cloud](use-n8n-cloud/) 可在 n8n 运行的实例上快速完成托管式设置。[自托管 n8n](host-n8n/) 允许你在自己的机器或基础设施上运行 n8n。\
\
**部署** 文档帮助你在任一模式下部署、配置、保护和维护 n8n。

<table data-view="cards"><thead><tr><th>部署选项</th><th data-card-target data-type="content-ref">前往章节</th></tr></thead><tbody><tr><td><strong>使用 n8n Cloud</strong><br>由 n8n 管理。更快开始，减少运维工作。</td><td><a href="use-n8n-cloud/">use-n8n-cloud</a></td></tr><tr><td><strong>自托管 n8n</strong><br>使用 Docker、npm、Docker Compose 或受支持的平台自行运行 n8n。</td><td><a href="host-n8n/">host-n8n</a></td></tr></tbody></table>

### 比较部署选项

下面是每个选项的高层概览。如果你仍在决定，请查看[选择你的 n8n](https://n8n.gitbook.io/n8n-docs-next/fTXFsp54tRnnn2McXCeU/choose-how-to-use-n8n)获取更多指导。

#### 使用 n8n Cloud

n8n Cloud 是托管式选项。n8n 会为你运行实例。

如果你希望满足以下需求，请选择 Cloud：

* 以最少设置快速开始
* 减少基础设施和维护工作
* 使用 Cloud 专属的管理和配置工具

{% content-ref url="use-n8n-cloud/" %}
[use-n8n-cloud](use-n8n-cloud/)
{% endcontent-ref %}

#### 自托管 n8n

自托管让你控制 n8n 的运行方式以及环境的管理方式。

如果你希望满足以下需求，请选择自托管：

* 在自己的基础设施上运行 n8n
* 精细控制升级、配置和安全
* 按自定义扩展或平台要求进行设计

<table data-view="cards"><thead><tr><th>自托管主题</th><th data-card-target data-type="content-ref">打开</th></tr></thead><tbody><tr><td><strong>Host n8n 概览</strong><br>从主要自托管落地页开始。</td><td><a href="host-n8n/">host-n8n</a></td></tr><tr><td><strong>安装选项</strong><br>使用 Docker、npm、Docker Compose 或云提供商设置 n8n。</td><td><a href="host-n8n/install-options/">install-options</a></td></tr><tr><td><strong>配置 n8n</strong><br>管理数据库、环境变量、用户、许可证和安全设置。</td><td><a href="host-n8n/configure-n8n/">configure-n8n</a></td></tr><tr><td><strong>保持 n8n 运行</strong><br>监控、记录日志、追踪并更新实例。</td><td><a href="host-n8n/keep-n8n-running/">keep-n8n-running</a></td></tr><tr><td><strong>了解架构</strong><br>了解 n8n 的工作方式以及数据库结构。</td><td><a href="host-n8n/understand-the-architecture/">understand-the-architecture</a></td></tr></tbody></table>

{% content-ref url="host-n8n/" %}
[host-n8n](host-n8n/)
{% endcontent-ref %}
