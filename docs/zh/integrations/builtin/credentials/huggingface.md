---
title: Hugging Face credentials
description: >-
  Hugging Face credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Hugging Face 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Hugging Face credentials
originalFilePath: integrations/builtin/credentials/huggingface.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/huggingface'
url: 'https://docs.n8n.io/integrations/builtin/credentials/huggingface'
layout:
  description:
    visible: false
---

# Hugging Face credentials <a href="#hugging-face-credentials" id="hugging-face-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Hugging Face Inference](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md)
* [Embeddings Hugging Face Inference](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Hugging Face's documentation](https://huggingface.co/docs/api-inference/quicktour)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Hugging Face](https://huggingface.co/) 账号，并准备：

- **API Key**：Hugging Face 将它们称为 API tokens。

获取 API token：

1. 打开你的 Hugging Face profile，进入 [**Tokens**](https://huggingface.co/settings/tokens) 区域。
2. 复制其中列出的 token。它应该以 `hf_` 开头。
3. 在 n8n credential 中将此 API token 填为 **API Key**。

更多信息请参考 [Get your API token](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token)。
