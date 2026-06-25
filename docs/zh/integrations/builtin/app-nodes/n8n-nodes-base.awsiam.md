---
title: AWS IAM node documentation
description: >-
  了解如何在 n8n 中使用 AWS IAM node。按照技术文档将 AWS IAM node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: AWS IAM node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam'
layout:
  description:
    visible: false
---

# AWS IAM node <a href="#aws-iam-node" id="aws-iam-node"></a>

使用 AWS IAM node 自动化 AWS Identity and Access Management (IAM) 中的工作，并将 AWS IAM 与其他应用集成。n8n 内置支持大量 AWS IAM 功能，包括创建、更新、获取和删除 user 与 group，以及管理 group membership。

在本页中，你可以找到 AWS IAM node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/aws.md)找到此 node 的身份验证信息。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **User**:
	* **Add to Group**：将现有 user 添加到 group。
	* **Create**：创建新 user。
	* **Delete**：删除 user。
	* **Get**：检索 user。
	* **Get Many**：检索 user 列表。
	* **Remove From Group**：从 group 中移除 user。
	* **Update**：更新现有 user。
* **Group**:
	* **Create**：创建新 group。
	* **Delete**：删除 group。
	* **Get**：检索 group。
	* **Get Many**：检索 group 列表。
	* **Update**：更新现有 group。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AWS IAM node 文档集成模板](https://n8n.io/integrations/aws-iam)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AWS IAM 文档](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}
