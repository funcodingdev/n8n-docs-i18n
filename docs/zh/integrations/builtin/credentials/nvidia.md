---
title: NVIDIA Nemotron credentials
description: >-
  NVIDIA Nemotron credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 NVIDIA Nemotron 进行身份验证。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: NVIDIA Nemotron credentials
originalFilePath: integrations/builtin/credentials/nvidia.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/nvidia'
url: 'https://docs.n8n.io/integrations/builtin/credentials/nvidia'
layout:
  description:
    visible: false
---

# NVIDIA Nemotron credentials <a href="#nvidia-nemotron-credentials" id="nvidia-nemotron-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [NVIDIA Nemotron Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md)

单个 credential 覆盖两种 deployment modes：

- **Cloud**：由 NVIDIA 托管在 [build.nvidia.com](https://build.nvidia.com/) 上的 Nemotron models。
- **Self-hosted NIM**：运行在你自己 infrastructure 上的 [NVIDIA Inference Microservice](https://docs.nvidia.com/nim/) container。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

对于 cloud access，请创建一个 [NVIDIA build](https://build.nvidia.com/) 账号。

对于 self-hosted access，请运行一个暴露 OpenAI-spec compatible endpoint 的 NIM container。设置指导请参考 [NVIDIA NIM documentation](https://docs.nvidia.com/nim/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（连接到不强制身份验证的 self-hosted NIM 时可选）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

可用 Nemotron models 列表请参考 NVIDIA 的 [build catalogue](https://build.nvidia.com/models)，self-hosting 指导请参考 [NIM documentation](https://docs.nvidia.com/nim/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Base URL**：要调用的 OpenAI-spec compatible endpoint。对于 build.nvidia.com cloud，请使用默认值 `https://integrate.api.nvidia.com/v1`；或将其替换为你的 self-hosted NIM URL（例如 `http://localhost:8000/v1`）。
- 一个 **API Key**：build.nvidia.com cloud 需要它。对于不要求身份验证的 self-hosted NIM，请留空。

为 build.nvidia.com 生成 API key：

1. 登录你的 [NVIDIA build](https://build.nvidia.com/) 账号。
2. 在 catalogue 中打开一个 Nemotron model，并选择 **Get API Key**。
3. 复制你的 key，并在 n8n 中将其添加为 **API Key**。

连接到 self-hosted NIM：

1. 将 **Base URL** 设置为你的 NIM endpoint，并包含 `/v1` path（例如 `http://localhost:8000/v1`）。
2. 如果你的 NIM 要求身份验证，请将 token 粘贴到 **API Key**。否则，将该字段留空。
