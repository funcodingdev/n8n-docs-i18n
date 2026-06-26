---
title: KoboToolbox credentials
description: >-
  KoboToolbox credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  KoboToolbox 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: KoboToolbox credentials
originalFilePath: integrations/builtin/credentials/kobotoolbox.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox'
url: 'https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox'
layout:
  description:
    visible: false
---

# KoboToolbox credentials <a href="#kobotoolbox-credentials" id="kobotoolbox-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [KoboToolbox trigger](../trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md)
* [KoboToolbox](../app-nodes/n8n-nodes-base.kobotoolbox.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [KoboToolbox](https://www.kobotoolbox.org/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [KoboToolbox's API documentation](https://support.kobotoolbox.org/api.html)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- **API Root URL**：输入你创建账号所在 KoboToolbox server 的 URL。Global KoboToolbox Server 使用 `https://kf.kobotoolbox.org`。European Union KoboToolbox Server 使用 `https://eu.kobotoolbox.org`。
- **API Token**：显示在你的 **Account Settings** 中。更多信息请参考 [Getting your API token](https://support.kobotoolbox.org/api.html#getting-your-api-token)。
