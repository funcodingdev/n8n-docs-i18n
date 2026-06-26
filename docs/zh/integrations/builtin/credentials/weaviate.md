---
title: Weaviate credentials
description: >-
  Weaviate credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Weaviate 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Weaviate credentials
originalFilePath: integrations/builtin/credentials/weaviate.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/weaviate'
url: 'https://docs.n8n.io/integrations/builtin/credentials/weaviate'
layout:
  description:
    visible: false
---

# Weaviate credentials <a href="#weaviate-credentials" id="weaviate-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Weaviate Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何连接到 Weaviate 的更多信息，请参考 [Weaviate's connection documentation](https://docs.weaviate.io/weaviate/connections)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

### 连接类型：Weaviate Cloud <a href="#connection-type-weaviate-cloud" id="connection-type-weaviate-cloud"></a>

创建你的 [Weaviate Cloud Database](https://docs.weaviate.io/cloud/quickstart)，并[按照这些说明从 Weaviate Cloud Database 获取以下参数值](https://docs.weaviate.io/cloud/quickstart#13-connect-to-your-weaviate-cloud-instance)：

* **Weaviate Cloud Endpoint**
* **Weaviate Api Key**

注意：Weaviate 提供一个用于测试的 free sandbox option。

### 连接类型：Custom Connection <a href="#connection-type-custom-connection" id="connection-type-custom-connection"></a>

对于此 Connection Type，你需要在自己的 server 上[部署 Weaviate](https://docs.weaviate.io/deploy)，并配置为 n8n 可以访问。有关创建和使用 API keys 的信息，请参考 [Weaviate's authentication documentation](https://docs.weaviate.io/deploy/configuration/authentication#api-key-authentication)。

然后你可以提供 custom connection 的参数：

* **Weaviate Api Key**：你的 Weaviate API key。
* **Custom Connection HTTP Host**：用于 HTTP API calls 的 Weaviate instance domain name 或 IP address。
* **Custom Connection HTTP Port**：你的 Weaviate instance 用于 HTTP API calls 的运行 port。默认是 8080。
* **Custom Connection HTTP Secure**：是否通过 HTTPS 连接到 Weaviate 以进行 HTTP API calls。
* **Custom Connection gRPC Host**：用于 gRPC 的 Weaviate instance hostname 或 IP address。
* **Custom Connection gRPC Port**：你的 Weaviate instance 的 gRPC API port。默认是 50051。
* **Custom Connection gRPC Secure**：是否通过 HTTPS 连接到 Weaviate 以进行 gRPC。

如需 community support，请参考 [Weaviate Forums](https://forum.weaviate.io/)。
