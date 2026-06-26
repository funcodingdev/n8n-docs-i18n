---
title: External secrets environment variables
description: >-
  配置 self-hosted n8n 实例检查 external secrets 更新的间隔。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: External secrets
originalFilePath: hosting/configuration/environment-variables/external-secrets.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/external-secrets
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets
layout:
  description:
    visible: false
---

# External secrets 环境变量 <a href="#external-secrets-environment-variables" id="external-secrets-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

你可以使用 external secrets store 管理 n8n 的 credentials。详情请参考 [External secrets](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/use-external-secret-stores)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL` | Number | `300` (5 minutes) | 检查 secret 更新的频率，单位为秒。 |
