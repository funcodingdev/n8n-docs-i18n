---
title: SearXNG Tool node 文档
description: >-
  了解如何在 n8n 中使用 SearXNG Tool node。按照技术文档将 SearXNG Tool node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: SearXNG Tool node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng
layout:
  description:
    visible: false
---

# SearXNG Tool node <a href="#searxng-tool-node" id="searxng-tool-node"></a>

SearXNG Tool node 允许你使用 SearXNG 将 search capabilities 集成到 workflows 中。SearXNG 会聚合多个 search engines 的结果，且不会跟踪你。

在本页中，你可以找到 SearXNG Tool node 的 node options，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/searxng.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Number of Results**：要检索的 results 数量。默认值为 10。
* **Page Number**：要检索的 search results 页码。默认值为 1。
* **Language**：用于按语言过滤 search results 的两位 [language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)。例如：`en` 表示英语，`fr` 表示法语。默认值为 `en`。
* **Safe Search**：启用或禁用 search results 中的 explicit content 过滤。可以是 None、Moderate 或 Strict。默认值为 None。

## 运行 SearXNG instance <a href="#running-a-searxng-instance" id="running-a-searxng-instance"></a>

此 node 要求 SearXNG service 与你的 n8n instance 运行在同一网络中。请确保你的 n8n instance 可以访问 SearXNG service。

此 node 需要 JSON 格式的 results，而默认 SearXNG configuration 未启用该格式。要启用 JSON output，请在 SearXNG instance 的 `settings.yml` 文件中，将 `json` 添加到 `search.formats` section：

```yaml
search:
  # options available for formats: [html, csv, json, rss]
  formats:
    - html
    - json
```

如果 `formats` section 不存在，请添加它。`settings.yml` 文件的确切位置取决于你安装 SearXNG 的方式。你可以访问 [SearXNG configuration 文档](https://docs.searxng.org/admin/installation-searxng.html#configuration)了解更多。

Search results 的质量和可用性取决于你使用的 SearXNG instance 的 configuration 和 health。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 SearXNG Tool node 文档集成模板](https://n8n.io/integrations/searxng)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SearXNG 文档](https://docs.searxng.org/)。你还可以查看 [LangChain 关于 SearXNG integration 的文档](https://python.langchain.com/docs/integrations/tools/searx_search/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}
