---
title: OpenCTI credentials
description: >-
  OpenCTI credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  OpenCTI 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: OpenCTI credentials
originalFilePath: integrations/builtin/credentials/opencti.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/opencti'
url: 'https://docs.n8n.io/integrations/builtin/credentials/opencti'
layout:
  description:
    visible: false
---

# OpenCTI credentials <a href="#opencti-credentials" id="opencti-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [OpenCTI](https://filigran.io/solutions/open-cti/) developer account。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [OpenCTI's documentation](https://docs.opencti.io/latest/)。

这是一个 credential-only node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/opencti/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：要获取 API key，请前往你的 **Profile > API access**。更多信息请参考 OpenCTI [Integrations Authentication documentation](https://docs.opencti.io/latest/deployment/integrations/#authentication)。
