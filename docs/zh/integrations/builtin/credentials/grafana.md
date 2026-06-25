---
title: Grafana credentials
description: >-
  Grafana credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Grafana 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Grafana credentials
originalFilePath: integrations/builtin/credentials/grafana.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/grafana'
url: 'https://docs.n8n.io/integrations/builtin/credentials/grafana'
layout:
  description:
    visible: false
---

# Grafana credentials <a href="#grafana-credentials" id="grafana-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Grafana](../app-nodes/n8n-nodes-base.grafana.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Grafana](https://grafana.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何对该服务进行身份验证的更多信息，请参考 [Grafana's API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：创建 API key 的详细说明请参考[创建 API key 文档](https://grafana.com/docs/grafana/latest/administration/api-keys/#create-an-api-key)。
- 你的 Grafana instance 的 **Base URL**，例如：`https://n8n.grafana.net`。
