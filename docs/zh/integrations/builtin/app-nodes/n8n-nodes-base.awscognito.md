---
title: AWS Cognito node documentation
description: >-
  了解如何在 n8n 中使用 AWS Cognito node。按照技术文档将 AWS Cognito node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: AWS Cognito node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awscognito.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito'
layout:
  description:
    visible: false
---

# AWS Cognito node <a href="#aws-cognito-node" id="aws-cognito-node"></a>

使用 AWS Cognito node 自动化 AWS Cognito 中的工作，并将 AWS Cognito 与其他应用集成。n8n 内置支持大量 AWS Cognito 功能，包括创建、检索、更新和删除 group、user 与 user pool。

在本页中，你可以找到 AWS Cognito node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/aws.md)找到此 node 的身份验证信息。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Group:
	* Create：创建新 group。
	* Delete：删除现有 group。
	* Get：检索现有 group 的详细信息。
	* Get Many：检索 group 列表。
	* Update：更新现有 group。
* User:
	* Add to Group：将现有 user 添加到 group。
	* Create：创建新 user。
	* Delete：删除 user。
	* Get：检索现有 user 的信息。
	* Get Many：检索 user 列表。
	* Remove From Group：从 group 中移除 user。
	* Update：更新现有 user。
* User Pool:
	* Get：检索现有 user pool 的信息。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AWS Cognito node 文档集成模板](https://n8n.io/integrations/aws-cognito)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AWS Cognito 文档](https://docs.aws.amazon.com/cognito/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}
