---
title: AI Assistant environment variables
description: 用于配置 AI Assistant 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: AI Assistant
originalFilePath: hosting/configuration/environment-variables/ai-assistant.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/ai-assistant'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant
layout:
  description:
    visible: false
---

# AI Assistant 环境变量 <a href="#ai-assistant-environment-variables" id="ai-assistant-environment-variables"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_AI_ASSISTANT_BASE_URL` | String | (empty) | AI assistant 服务的 Base URL，指定为 `https://ai-assistant.n8n.io `。如果你 self-host n8n 并想启用 AI Assistant，则此项为必填。 |
