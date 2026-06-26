---
title: VirusTotal credentials
description: >-
  VirusTotal credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 VirusTotal 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: VirusTotal credentials
originalFilePath: integrations/builtin/credentials/virustotal.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/virustotal'
url: 'https://docs.n8n.io/integrations/builtin/credentials/virustotal'
layout:
  description:
    visible: false
---

# VirusTotal credentials <a href="#virustotal-credentials" id="virustotal-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [VirusTotal](https://www.virustotal.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [VirusTotal's documentation](https://docs.virustotal.com/reference/overview)。

这是一个仅用于 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看 [example workflows and related content](https://n8n.io/integrations/virustotal/)。


## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Token**：前往你的 **user account menu > API key** 获取 API key。在你的 n8n credential 中将其输入为 **API Token**。更多信息请参考 [API authentication](https://docs.virustotal.com/reference/authentication)。
