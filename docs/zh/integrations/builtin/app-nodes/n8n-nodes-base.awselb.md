---
title: AWS Elastic Load Balancing node documentation
description: >-
  了解如何在 n8n 中使用 AWS Elastic Load Balancing node。按照技术文档将 AWS Elastic Load Balancing node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: AWS Elastic Load Balancing node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awselb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb'
layout:
  description:
    visible: false
---

# AWS Elastic Load Balancing node <a href="#aws-elastic-load-balancing-node" id="aws-elastic-load-balancing-node"></a>

使用 AWS Elastic Load Balancing node 自动化 AWS ELB 中的工作，并将 AWS ELB 与其他应用集成。n8n 内置支持大量 AWS ELB 功能，包括添加、获取、移除和删除 certificate 与 load balancer。

在本页中，你可以找到 AWS ELB node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [AWS ELB credentials](../credentials/aws.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Listener Certificate
	* Add
	* Get Many
	* Remove
* Load Balancer
	* Create
	* Delete
	* Get
	* Get Many

此 node 支持创建和管理 application load balancer 与 network load balancer。它当前不支持 gateway load balancer。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AWS Elastic Load Balancing node 文档集成模板](https://n8n.io/integrations/aws-elb)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [AWS ELB 文档](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}
