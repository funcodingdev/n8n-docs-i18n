---
title: Timezone and localization environment variables
description: 为 self-hosted n8n 实例设置 timezone 和默认语言 locale。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Timezone and localization
originalFilePath: hosting/configuration/environment-variables/timezone-localization.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization
layout:
  description:
    visible: false
---

# Timezone and localization 环境变量 <a href="#timezone-and-localization-environment-variables" id="timezone-and-localization-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `GENERIC_TIMEZONE` | * | `America/New_York` | n8n 实例 timezone。对 schedule nodes（例如 Cron）很重要。 |
| `N8N_DEFAULT_LOCALE` | String | `en` | locale identifier，兼容 [Accept-Language header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)。n8n 不支持 regional identifiers，例如 `de-AT`。当以非默认 locale 运行时，n8n 会以选定 locale 显示 UI strings，并对任何未翻译 strings 回退到 `en`。 |
