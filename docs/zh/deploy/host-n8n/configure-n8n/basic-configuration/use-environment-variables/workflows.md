---
title: Workflows environment variables
description: >-
  用于配置 n8n workflows 的环境变量，包括默认命名、onboarding flow 偏好、tag management 和 caller policy
  settings。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Workflows
originalFilePath: hosting/configuration/environment-variables/workflows.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/workflows'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows
layout:
  description:
    visible: false
---

# Workflows 环境变量 <a href="#workflows-environment-variables" id="workflows-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_ONBOARDING_FLOW_DISABLED` | Boolean | `false` | 是否在创建新 workflow 时禁用 onboarding tips：`true` 表示禁用，`false` 表示不禁用。 |
| `N8N_WORKFLOW_ACTIVATION_BATCH_SIZE` | Number | `1` | 启动期间同时 publish 的 workflows 数量。 |
| `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION` | String | `workflowsFromSameOwner` | 哪些 workflows 可以调用某个 workflow。选项包括：`any`、`none`、`workflowsFromAList`、`workflowsFromSameOwner`。此功能需要 [Workflow sharing](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/share-with-others)。 |
| `N8N_WORKFLOW_TAGS_DISABLED` | Boolean | `false` | 是否禁用 workflow tags：`true` 表示禁用 tags，`false` 表示启用 tags。 |
| `WORKFLOWS_DEFAULT_NAME` | String | `My workflow` | 新 workflows 使用的默认名称。 |
