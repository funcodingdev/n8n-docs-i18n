---
title: Google Gemini Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Google Gemini Chat Model node。按照技术文档将 Google Gemini
  Chat Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Gemini Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini
layout:
  description:
    visible: false
---

# Google Gemini Chat Model node <a href="#google-gemini-chat-model-node" id="google-gemini-chat-model-node"></a>

使用 Google Gemini Chat Model node 将 Google 的 Gemini chat models 与 conversational agents 配合使用。

在本页中，你可以找到 Google Gemini Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/googleai.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 completion 的 model。

n8n 会从 Google Gemini API 动态加载 models，你只会看到你的账号可用的 models。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。
* **Safety Settings**：Gemini 支持可调整的 safety settings。有关可用 filters 和 levels 的信息，请参阅 Google 的 [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini)。

## 限制 <a href="#limitations" id="limitations"></a>

### 不支持 proxy <a href="#no-proxy-support" id="no-proxy-support"></a>

Google Gemini Chat Model node 使用 Google 的 SDK，该 SDK 不支持 proxy configuration。

如果你需要代理连接，作为 workaround，可以为 Gemini requests 设置专用 reverse proxy，并将 [Google Gemini credentials](../../credentials/googleai.md) 中的 **Host** 参数改为指向你的 proxy address：

![Google Gemini credentials proxy configuration](../../../.gitbook/assets/google-gemini-proxy-config.png)

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Google Gemini Chat Model node 文档集成模板](https://n8n.io/integrations/google-gemini-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Google Gemini 文档](https://js.langchain.com/docs/integrations/chat/google_generativeai)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}
