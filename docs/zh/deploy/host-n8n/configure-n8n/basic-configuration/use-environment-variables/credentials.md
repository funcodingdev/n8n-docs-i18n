---
title: Credentials environment variables
description: >-
  通过环境变量管理默认 credentials，并为你的 self-hosted n8n 实例覆盖 credentials。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Credentials
originalFilePath: hosting/configuration/environment-variables/credentials.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/credentials'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials
layout:
  description:
    visible: false
---

# Credentials 环境变量 <a href="#credentials-environment-variables" id="credentials-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

使用以下环境变量启用 credential overwrites。详情请参考 [Credential overwrites](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/credential-overwrites)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `CREDENTIALS_OVERWRITE_DATA`<br>/`_FILE` | * | - | credentials 的 overwrites。 |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | String | - | 用于获取 credentials 的 API endpoint。 |
| `CREDENTIALS_OVERWRITE_PERSISTENCE` | Boolean | `false` | 为 credential overwrites 启用数据库持久化。多实例或 queue mode 需要此项，以便通过 publish/subscribe 方式将 overwrites 传播到 workers。 |
| `CREDENTIALS_DEFAULT_NAME` | String | `My credentials` | credentials 的默认名称。 |
