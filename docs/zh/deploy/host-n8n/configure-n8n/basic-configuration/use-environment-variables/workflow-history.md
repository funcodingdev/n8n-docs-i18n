---
title: Workflow history environment variables
description: 用于配置 n8n workflow history 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Workflow history
originalFilePath: hosting/configuration/environment-variables/workflow-history.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/workflow-history
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history
layout:
  description:
    visible: false
---

# Workflow history 环境变量 <a href="#workflow-history-environment-variables" id="workflow-history-environment-variables"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_WORKFLOW_HISTORY_PRUNE_TIME` | Number | `-1` | 自动删除 workflow history versions 前保留多久，单位为小时。设为 `-1` 可无限期保留所有 versions。 |
