---
title: Nodes environment variables
description: >-
  用于在 self-hosted n8n 中配置 nodes management 和 node-specific limits 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Nodes
originalFilePath: hosting/configuration/environment-variables/nodes.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/nodes'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes
layout:
  description:
    visible: false
---

# Nodes 环境变量 <a href="#nodes-environment-variables" id="nodes-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

本页列出在 n8n 中管理 nodes[^1] 的环境变量配置选项，包括指定要加载或排除的 nodes、在 Code node 中导入 built-in 或 external modules、启用 community nodes，以及配置 node-specific limits。

## Nodes 和 community node 设置 <a href="#nodes-and-community-node-settings" id="nodes-and-community-node-settings"></a>

| Variable                                 | Type             | Default                       | Description                                                                                                                                                                                                                           |
|:-----------------------------------------|:-----------------|:------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `N8N_COMMUNITY_PACKAGES_AUTH_TOKEN`      | String           | -                             | private npm registry 的 authentication token。与 `N8N_COMMUNITY_PACKAGES_REGISTRY` 一起使用，可在从 private registry 安装 community nodes 时进行请求身份验证。 |
| `N8N_COMMUNITY_PACKAGES_ENABLED`         | Boolean          | `true`                        | 启用（true）或禁用（false）安装和加载 community nodes 的功能。如果设为 false，无论各自设置如何，verified 和 unverified community packages 都不可用。 |
| `N8N_COMMUNITY_PACKAGES_PREVENT_LOADING` | Boolean          | `false`                       | 阻止（true）或允许（false）在实例启动时加载已安装的 community nodes。如果某个故障 node 阻止实例启动，可使用此项。                                                                               |
| `N8N_COMMUNITY_PACKAGES_REGISTRY`        | String           | `https://registry.npmjs.org`  | 用于拉取 community packages 的 NPM registry URL（需要 license）。                                                                                                                                                                  |
| `N8N_CUSTOM_EXTENSIONS`                  | String           | -                             | 指定包含 custom nodes 的目录路径。                                                                                                                                                                         |
| `N8N_PYTHON_ENABLED`                     | Boolean          | `true`                        | 是否在 Code node 上启用 Python execution。                                                                                                                                                                                  |
| `N8N_UNVERIFIED_PACKAGES_ENABLED`        | Boolean          | `true`                        | 当 `N8N_COMMUNITY_PACKAGES_ENABLED` 为 true 时，此变量控制是否启用从 NPM registry 安装和使用 unverified community nodes（true）或不启用（false）。                                        |
| `N8N_VERIFIED_PACKAGES_ENABLED`          | Boolean          | `true`                        | 当 `N8N_COMMUNITY_PACKAGES_ENABLED` 为 true 时，此变量控制是否在 nodes panel 中显示 verified community nodes 以便安装和使用（true），或隐藏它们（false）。                                       |
| `NODE_FUNCTION_ALLOW_BUILTIN`            | String           | -                             | 允许用户在 Code node 中导入特定 built-in modules。使用 * 可允许全部。n8n 默认禁用模块导入。                                                                                                   |
| `NODE_FUNCTION_ALLOW_EXTERNAL`           | String           | -                             | 允许用户在 Code node 中导入特定 external modules（来自 `n8n/node_modules`）。n8n 默认禁用模块导入。                                                                                             |
| `NODES_ERROR_TRIGGER_TYPE`               | String           | `n8n-nodes-base.errorTrigger` | 指定用作 Error Trigger 的 node type。                                                                                                                                                                                      |
| `NODES_EXCLUDE`                          | Array of strings | `[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.localFileTrigger\"]`                             | 指定不加载哪些 nodes。例如，如果用户不可信，要阻止可能存在安全风险的 nodes：`NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"@n8n/n8n-nodes-langchain.lmChatDeepSeek\"]"`。要启用所有 nodes，请指定 `NODES_EXCLUDE: "[]"`。                       |
| `NODES_INCLUDE`                          | Array of strings | -                             | 指定要加载哪些 nodes。                                                                                                                                                                                                          |

## Compression node 设置 <a href="#compression-node-settings" id="compression-node-settings"></a>

| Variable                                             | Type   | Default        | Description                                                                          |
|:-----------------------------------------------------|:-------|:---------------|:-------------------------------------------------------------------------------------|
| `N8N_COMPRESSION_NODE_MAX_DECOMPRESSED_SIZE_BYTES`   | Number | `2147483648`   | 最大解压输出总大小，单位为 bytes。默认值为 2 GiB。                   |
| `N8N_COMPRESSION_NODE_MAX_ZIP_ENTRIES`               | Number | `5000`         | ZIP archive 中允许的最大 entries 数量。                                   |

## 管理已安装的 community packages <a href="#manage-installed-community-packages" id="manage-installed-community-packages"></a>

{% hint style="info" %}
**从 n8n v2.21.0 起可用**

{% endhint %}

通过环境变量预配置已安装的 [community packages](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/community-nodes/installation-and-management)。关于 `*_MANAGED_BY_ENV` pattern，请参阅 [Manage instance settings using environment variables](../../manage-settings-using-environment-variables.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/w3ftfKhp9KdsaTfUFHE8/" %}

[^1]: 在 n8n 中，nodes 是你用来组合创建 workflows 的独立组件。Nodes 定义 workflow 何时运行，允许你获取、发送和处理数据，可以定义 flow control logic，并连接 external services。
