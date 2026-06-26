---
title: Zabbix credentials
description: >-
  Zabbix credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zabbix 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zabbix credentials
originalFilePath: integrations/builtin/credentials/zabbix.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zabbix'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zabbix'
layout:
  description:
    visible: false
---

# Zabbix credentials <a href="#zabbix-credentials" id="zabbix-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zabbix Cloud](https://www.zabbix.com/) 账号，或 self-host 你自己的 Zabbix server。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api)。

这是一个仅用于 credential 的 node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看 [example workflows and related content](https://n8n.io/integrations/zabbix/)。


## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Token**：你的 Zabbix user 的 API key。
- **URL**：你的 Zabbix server 的 URL。不要在 URL 中包含 `/zabbix`。

有关向该服务进行身份验证的更多信息，请参考 [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api#authentication)。
