---
title: MISP credentials
description: >-
  MISP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MISP 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: MISP credentials
originalFilePath: integrations/builtin/credentials/misp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/misp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/misp'
layout:
  description:
    visible: false
---

# MISP credentials <a href="#misp-credentials" id="misp-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [MISP](../app-nodes/n8n-nodes-base.misp.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

安装并运行一个 [MISP](https://misp.github.io/MISP/) instance。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MISP's Automation API documentation](https://www.circl.lu/doc/misp/automation)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：在 MISP 中，这类 key 称为 Automation keys。可以从 **Event Actions > Automation** 获取 automation key。有关生成更多 keys 的说明，请参考 [MISP's automation keys documentation](https://www.circl.lu/doc/misp/automation/#automation-key)。
- 一个 **Base URL**：你的 MISP URL。
- 选择是否 **Allow Unauthorized Certificates**：如果启用，即使 SSL certificate validation 失败，此 credential 也会继续连接。
