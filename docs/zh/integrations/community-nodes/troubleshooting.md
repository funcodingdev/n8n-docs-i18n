---
contentType: howto
nodeTitle: 故障排查
originalFilePath: integrations/community-nodes/troubleshooting.md
originalUrl: 'https://docs.n8n.io/integrations/community-nodes/troubleshooting'
url: 'https://docs.n8n.io/integrations/community-nodes/troubleshooting'
layout:
  description:
    visible: false
---

# 故障排查和错误 <a href="#troubleshooting-and-errors" id="troubleshooting-and-errors"></a>

## 错误：缺少 package <a href="#error-missing-packages" id="error-missing-packages"></a>

n8n 会将社区 node 直接安装到硬盘上。n8n 启动时必须能访问这些文件，才能加载它们。如果 package 在启动时不可用，你会收到缺少 package 的错误警告。

如果使用 Docker 运行 n8n：根据你的 Docker 设置，在重新创建容器或升级 n8n 版本时，你可能会丢失 package。你必须选择以下任一方式：

* 持久化 `~/.n8n/nodes` 目录内容。这是最佳选项。如果你按照 [Docker installation](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/install-options/install-with-docker) 指南操作，设置步骤中包含持久化该目录。
* 将 `N8N_REINSTALL_MISSING_PACKAGES` 环境变量设置为 `true`。

第二个选项可能会增加启动时间，并可能导致健康检查失败。

## 在 n8n cloud 上阻止加载社区 node <a href="#prevent-loading-community-nodes-on-n8n-cloud" id="prevent-loading-community-nodes-on-n8n-cloud"></a>

如果你的 n8n cloud 实例崩溃且无法启动，可以阻止已安装的社区 node 在实例启动时加载。访问 [Cloud Admin Panel](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/use-the-admin-dashboard) > **Manage**，并将 **Disable all community nodes** 切换为 **`true`**。只有在允许安装社区 node 时，此开关才可见。
