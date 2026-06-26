---
title: Milvus credentials
description: >-
  Milvus credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Milvus 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Milvus credentials
originalFilePath: integrations/builtin/credentials/milvus.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/milvus'
url: 'https://docs.n8n.io/integrations/builtin/credentials/milvus'
layout:
  description:
    visible: false
---

# Milvus credentials <a href="#milvus-credentials" id="milvus-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Milvus Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建并运行一个 [Milvus](https://milvus.io/) instance。更多信息请参考 [Install Milvus](https://milvus.io/docs/install-overview.md)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关身份验证设置的更多信息，请参考 [Milvus's Authentication documentation](https://milvus.io/docs/authenticate.md?tab=docker#Authenticate-User-Access)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

* **Base URL**：你的 Milvus instance 的 base URL。默认值为 `http://localhost:19530`。
* **Username**：用于对 Milvus instance 进行身份验证的 username。默认值为 `root`。
* **Password**：用于对 Milvus instance 进行身份验证的 password。默认值为 `Milvus`。
