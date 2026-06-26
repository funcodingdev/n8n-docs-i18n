---
title: Source control environment variables
description: 用于设置 source control 默认 SSH key type 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Source control
originalFilePath: hosting/configuration/environment-variables/source-control.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/source-control'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control
layout:
  description:
    visible: false
---

# Source control 环境变量 <a href="#source-control-environment-variables" id="source-control-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

n8n 使用基于 Git 的 source control 支持 environments。关于如何将 Git repository 链接到 n8n 实例并配置 source control，请参考 [Source control and environments](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments/set-up-source-control)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE` | String | `ed25519` | 设为 `rsa`，可让 RSA 成为 [Source control setup](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments/set-up-source-control) 的默认 SSH key type。 |
