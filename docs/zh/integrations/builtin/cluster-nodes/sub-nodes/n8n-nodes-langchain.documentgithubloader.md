---
title: GitHub Document Loader node 文档
description: >-
  了解如何在 n8n 中使用 GitHub Document Loader node。按照技术文档将 GitHub
  Document Loader node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: GitHub Document Loader node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader
layout:
  description:
    visible: false
---

# GitHub Document Loader node <a href="#github-document-loader-node" id="github-document-loader-node"></a>

{% hint style="warning" %}
**Deprecated**

此 node 已弃用，并会在未来版本中移除。
{% endhint %}

使用 GitHub Document Loader node 从 GitHub repository 加载数据，用于 [vector stores](#user-content-fn-1)[^1] 或 summarization。

在本页中，你可以找到 GitHub Document Loader node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/github.md)找到此 node 的身份验证信息。此 node 不支持 OAuth 身份验证。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text Splitting**：选择：
	* **Simple**：使用 [Recursive Character Text Splitter](n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)，chunk size 为 1000，overlap 为 200。
	* **Custom**：允许你连接所选的 text splitter。
* **Repository Link**：输入 GitHub repository 的 URL。
* **Branch**：输入要使用的 branch name。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Recursive**：选择是否包含 sub-folders 和 files（开启）或不包含（关闭）。
* **Ignore Paths**：输入要忽略的 directories。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 GitHub Document Loader node 文档集成模板](https://n8n.io/integrations/github-document-loader)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7MPhMVJM8wcmiOf5zn2m/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。
