---
title: SerpApi (Google Search) node 文档
description: >-
  了解如何在 n8n 中使用 SerpApi (Google Search) node。按照技术文档将 SerpApi (Google
  Search) node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: SerpApi (Google Search) node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi
layout:
  description:
    visible: false
---

# SerpApi (Google Search) node <a href="#serpapi-google-search-node" id="serpapi-google-search-node"></a>

{% hint style="warning" %}
**Deprecated**

此 node 已弃用，并会在未来版本中移除。请改用 verified **SerpApi Official** community node。
{% endhint %}

SerpAPI node 允许 workflow 中的 agent[^1] 调用 Google Search API。

在本页中，你可以找到 SerpAPI node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/serp.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Country**：输入你想使用的 country code。支持的 countries 和 country codes 请参阅 [Google GL Parameter: Supported Google Countries](https://serpapi.com/google-countries)。
* **Device**：选择用于获取 search results 的 device。
* **Explicit Array**：选择是否强制 SerpApi 获取 Google results，即使 cached version 已存在（开启）或不强制（关闭）。
* **Google Domain**：输入要使用的 Google Domain。支持的 domains 请参阅 [Supported Google Domains](https://serpapi.com/google-domains)。
* **Language**：输入你想使用的 language code。支持的 languages 和 language codes 请参阅 [Google HL Parameter: Supported Google Languages](https://serpapi.com/google-languages)。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 SerpApi (Google Search) node 文档集成模板](https://n8n.io/integrations/serpapi)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Serp 文档](https://serpapi.com/search-api)。你还可以查看 [LangChain 关于 Serp integration 的文档](https://js.langchain.com/docs/integrations/tools/serpapi/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。
