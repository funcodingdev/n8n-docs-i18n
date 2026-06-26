---
title: Splunk credentials
description: >-
  Splunk credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Splunk 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Splunk credentials
originalFilePath: integrations/builtin/credentials/splunk.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/splunk'
url: 'https://docs.n8n.io/integrations/builtin/credentials/splunk'
layout:
  description:
    visible: false
---

# Splunk credentials <a href="#splunk-credentials" id="splunk-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Splunk](../app-nodes/n8n-nodes-base.splunk.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- [下载并安装](https://www.splunk.com/en_us/download/splunk-enterprise.html) Splunk Enterprise。
- 在 **Settings > Tokens** 中[启用 token authentication](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/EnableTokenAuth)。

{% hint style="info" %}
**免费试用 Splunk Cloud Platform 账号无法访问 REST API**

免费试用 Splunk Cloud Platform 账号没有 REST API 访问权限。请确保你拥有所需权限。更多细节请参考 [Access requirements and limitations for the Splunk Cloud Platform REST API](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2203/RESTTUT/RESTandCloud)。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API auth token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Splunk's Enterprise API documentation](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog)。

## 使用 API auth token <a href="#using-api-auth-token" id="using-api-auth-token"></a>

要配置此 credential，你需要：

- 一个 **Auth Token**：启用 token authentication 后，在 **Settings > Tokens** 中创建 auth token。更多信息请参考 [Creating authentication tokens](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/CreateAuthTokens)。
- 一个 **Base URL**：你的 Splunk 实例地址。它应包含 protocol、domain 和 port，例如：`https://localhost:8089`。
- **Allow Self-Signed Certificates**：如果打开，即使 SSL validation 失败，n8n 也会继续连接。

## 所需 capabilities <a href="#required-capabilities" id="required-capabilities"></a>

你的 Splunk platform 账号和 role 必须具备特定 capabilities，才能创建 authentication tokens：

- `edit_tokens_own`：如果你要为自己创建 tokens，则需要此 capability。
- `edit_tokens_all`：如果你要为实例上的任意 user 创建 tokens，则需要此 capability。

更多信息请参考 [Define roles on the Splunk platform with capabilities](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/Rolesandcapabilities)。
