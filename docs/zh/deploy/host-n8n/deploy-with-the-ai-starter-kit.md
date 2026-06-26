---
title: Self-hosted AI Starter Kit
description: >-
  使用 n8n 精选的自托管 AI Starter Kit 获取一组 AI 元素，快速开始构建 AI workflows。
contentType: howto
nodeTitle: Deploy with the AI starter kit
originalFilePath: hosting/starter-kits/ai-starter-kit.md
originalUrl: 'https://docs.n8n.io/hosting/starter-kits/ai-starter-kit'
url: 'https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit'
layout:
  description:
    visible: false
---

# 自托管 AI Starter Kit <a href="#self-hosted-ai-starter-kit" id="self-hosted-ai-starter-kit"></a>

Self-hosted AI Starter Kit 是一个开放的 docker compose template，可快速搭建功能完整的 Local AI 和 Low Code 开发环境。

它由 [n8n](https://github.com/n8n-io) 精选维护，将自托管 n8n 平台与一组兼容的 AI 产品和组件组合在一起，帮助你开始构建自托管 AI workflows。

## 包含内容 <a href="#whats-included" id="whats-included"></a>

✅ [**Self-hosted n8n**](README.md)：低代码平台，拥有 400 多个 integrations 和高级 AI 组件。

✅ [**Ollama**](https://ollama.com/)：跨平台 LLM 平台，用于安装和运行最新的本地 LLM。

✅ [**Qdrant**](https://qdrant.tech/)：开源、高性能 vector store，带有全面的 API。

✅ [**PostgreSQL**](https://www.postgresql.org/)：Data Engineering 领域的可靠主力，可安全处理大量数据。

## 你可以构建什么 <a href="#what-you-can-build" id="what-you-can-build"></a>

⭐️ 可安排预约的 [AI Agents](#user-content-fn-1)[^1]{ data-preview}

⭐️ 不泄露数据的公司 PDF 摘要

⭐️ 用于公司沟通和 IT 运维的更智能 Slackbots

⭐️ 私有、低成本的财务文档分析

## 获取套件 <a href="#get-the-kit" id="get-the-kit"></a>


前往 [GitHub repository](https://github.com/n8n-io/self-hosted-ai-starter-kit) clone repo 并开始使用。


{% hint style="info" %}
**仅用于测试**

n8n 设计此 kit 是为了帮助你开始使用自托管 AI workflows。它并未针对生产环境完全优化，但组合了能够良好协作的稳健组件，适合 proof-of-concept 项目。请根据你的需求进行自定义。用于生产环境前，请做好安全配置和加固。
{% endhint %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models (LLMs) 理解用户输入，并根据可用的信息和资源决定如何最好地处理请求。
