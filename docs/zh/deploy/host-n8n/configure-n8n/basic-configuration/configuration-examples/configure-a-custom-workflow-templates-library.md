---
title: Configure a custom workflow templates library
description: 为自托管 n8n 实例设置自定义 workflow template library。
contentType: howto
nodeTitle: Configure a custom workflow templates library
originalFilePath: hosting/configuration/configuration-examples/custom-templates.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/custom-templates
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library
layout:
  description:
    visible: false
---

# 配置自定义 workflow templates library <a href="#configure-a-custom-workflow-templates-library" id="configure-a-custom-workflow-templates-library"></a>

n8n 提供 workflow templates[^1] library。自托管 n8n 时，你可以：

* 继续使用 n8n 的 workflow templates library（这是默认行为）
* 禁用 workflow templates
* 创建你自己的 workflow templates library

## 禁用 workflow templates <a href="#disable-workflow-templates" id="disable-workflow-templates"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/d0B6W4LSyDTfMfmxdG4T/" %}

## 使用你自己的 workflow templates library <a href="#use-your-own-workflow-templates-library" id="use-your-own-workflow-templates-library"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/8iCj3lLPJNp281ko0uOE/" %}

## 将你的 workflows 添加到 n8n library <a href="#add-your-workflows-to-the-n8n-library" id="add-your-workflows-to-the-n8n-library"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mr8LBJxxxIAFYHNPNKU2/" %}

[^1]: n8n templates 是由 n8n 和 community members 设计的预构建 workflows，可导入到你的 n8n instance 中。使用 templates 时，你可能需要填写 credentials 并调整配置以适应你的需求。
