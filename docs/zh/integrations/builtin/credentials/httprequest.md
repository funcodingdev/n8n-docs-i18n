---
title: HTTP Request credentials
contentType:
  - integration
  - reference
priority: critical
nodeTitle: HTTP Request credentials
originalFilePath: integrations/builtin/credentials/httprequest.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/httprequest
url: https://docs.n8n.io/integrations/builtin/credentials/httprequest
description: >-
  HTTP Request credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  HTTP Request 进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# HTTP Request credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [HTTP Request](../core-nodes/n8n-nodes-base.httprequest/)
* [HTTP Request Tool (legacy)](../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

你必须使用要查询的 app 或服务所要求的身份验证方式。

如果你需要使用 SSL certificate 保护身份验证，请参考[提供 SSL certificate](httprequest.md#provide-an-ssl-certificate) 了解所需信息。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Predefined credential type
* Basic auth (generic credential type)
* Custom auth (generic credential type)
* Digest auth (generic credential type)
* Header auth (generic credential type)
* Bearer auth (generic credential type)
* OAuth1 (generic credential type)
* OAuth2 (generic credential type)
* Query auth (generic credential type)

有关 generic credential types 的更多信息，请参考 [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)。

{% hint style="info" %}
**Predefined credential types**

只要你要连接的服务有可用的 credential type，n8n 建议尽量使用 predefined credential types。与配置 generic credentials 相比，它提供了更简单的 credentials 设置和管理方式。

对于 n8n 已经有对应平台 node 的部分 APIs，你可以使用 [Predefined credential types](../custom-api-actions-for-existing-nodes.md#predefined-credential-types) 执行自定义操作。例如，n8n 有 Asana node，并且支持在 HTTP Request node 中使用你的 Asana credentials。更多信息请参考 [Custom operations](../custom-api-actions-for-existing-nodes.md)。
{% endhint %}

## 使用 predefined credential type <a href="#using-predefined-credential-type" id="using-predefined-credential-type"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ZmZC9v8B1NG5lgRY44yF/" %}

更多信息请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/vIyn1XsEkjlolZzHTfTG/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/tq6Yob45CR8oPKrT6Ggr/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fjWxEWe1g0CDvsx1igf6/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/JeIbggto5Oi1mPf9SOYv/" %}

## 使用 OAuth1 <a href="#using-oauth1" id="using-oauth1"></a>

如果你的 app 或服务支持 OAuth1 身份验证，请使用此 generic authentication。

要配置此 credential，请输入：

* **Authorization URL**：也称为 Resource Owner Authorization URI。此 URL 通常以 `/oauth1/authorize` 结尾。临时 credentials 会发送到这里，以提示用户完成授权。
* **Access Token URL**：这是用于首次请求临时 credentials 的 URI。此 URL 通常以 `/oauth1/request` 或 `/oauth1/token` 结尾。
* **Consumer Key**：也称为 client key，类似用户名。它指定调用中使用的 `oauth_consumer_key`。
* **Consumer Secret**：也称为 client secret，类似密码。
* **Request Token URL**：这是授权后用于将临时 credentials 转换为长期 credentials 的 URI。此 URL 通常以 `/oauth1/access` 结尾。
* 选择 auth handshake 使用的 **Signature Method**。它指定调用中使用的 `oauth_signature_method`。选项包括：
  * **HMAC-SHA1**
  * **HMAC-SHA256**
  * **HMAC-SHA512**

对于大多数 OAuth1 integrations，你需要配置 app、service 或 integration，以便为这些字段生成大部分值。请将 n8n 中的 **OAuth Redirect URL** 用作该服务的 redirect URL 或 redirect URI。

阅读更多关于 [OAuth1](https://oauth.net/1/) 和 [OAuth1 authorization flow](https://oauth1.wp-api.org/docs/basics/Auth-Flow.html) 的信息。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

如果你的 app 或服务支持 OAuth2 身份验证，请使用此 generic authentication。

配置此 credential 的要求取决于所选 **Grant Type**。有关每种 grant type 的更多信息，请参考 [OAuth Grant Types](https://oauth.net/2/grant-types/)。

对于大多数 OAuth2 integrations，你需要配置 app、service 或 integration。请将 n8n 中的 **OAuth Redirect URL** 用作该服务的 redirect URL 或 redirect URI。

阅读更多关于 [OAuth2](https://oauth.net/2/) 的信息。

### Authorization Code grant type <a href="#authorization-code-grant-type" id="authorization-code-grant-type"></a>

使用 Authorization Code grant type 将 authorization code 交换为 access token。auth flow 使用 redirect URL 将用户返回到 client。然后 application 从 URL 获取 authorization code，并用它请求 access token。更多信息请参考 [Authorization Code Request](https://www.oauth.com/oauth2-servers/access-tokens/authorization-code-request/)。

要配置此 credential，请选择 **Authorization Code** 作为 **Grant Type**。

然后输入：

* **Authorization URL**
* **Access Token URL**
* **Client ID**：用于登录的 ID 或 username。
* **Client Secret**：用于登录的 secret 或 password。
* _可选：_ 为 credential 输入一个或多个 **Scope**。如果未指定，credential 会请求 client 可用的所有 scopes。
* _可选：_ 某些服务需要更多 query parameters。如果你的服务需要，请将它们添加为 **Auth URI Query Parameters**。
* **Authentication** type：选择最适合你用例的选项。选项包括：
  * **Header**：将 credentials 作为 basic auth header 发送。
  * **Body**：在 request body 中发送 credentials。
* _可选：_ 选择是否 **Ignore SSL Issues**。开启后，即使 SSL validation 失败，n8n 也会连接。

### Client Credentials grant type <a href="#client-credentials-grant-type" id="client-credentials-grant-type"></a>

当 applications 请求 access token 来访问自己的资源，而不是代表用户访问资源时，请使用 Client Credentials grant type。更多信息请参考 [Client Credentials](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)。

要配置此 credential，请选择 **Client Credentials** 作为 **Grant Type**。

然后输入：

* **Access Token URL**：用于启动 OAuth2 flow 的 URL。通常此 URL 以 `/token` 结尾。
* **Client ID**：用于登录 client 的 ID 或 username。
* **Client Secret**：用于登录 client 的 secret 或 password。
* _可选：_ 为 credential 输入一个或多个 **Scope**。大多数服务不支持 Client Credentials grant type 的 scopes；只有你的服务支持时才在这里输入 scopes。
* **Authentication** type：选择最适合你用例的选项。选项包括：
  * **Header**：将 credentials 作为 basic auth header 发送。
  * **Body**：在 request body 中发送 credentials。
* _可选：_ 选择是否 **Ignore SSL Issues**。开启后，即使 SSL validation 失败，n8n 也会连接。

### PKCE grant type <a href="#pkce-grant-type" id="pkce-grant-type"></a>

Proof Key for Code Exchange (PKCE) grant type 是 Authorization Code flow 的扩展，用于防止 CSRF 和 authorization code injection attacks。

要配置此 credential，请选择 **PKCE** 作为 **Grant Type**。

然后输入：

* **Authorization URL**
* **Access Token URL**
* **Client ID**：用于登录的 ID 或 username。
* **Client Secret**：用于登录的 secret 或 password。
* _可选：_ 为 credential 输入一个或多个 **Scope**。如果未指定，credential 会请求 client 可用的所有 scopes。
* _可选：_ 某些服务需要更多 query parameters。如果你的服务需要，请将它们添加为 **Auth URI Query Parameters**。
* **Authentication** type：选择最适合你用例的选项。选项包括：
  * **Header**：将 credentials 作为 basic auth header 发送。
  * **Body**：在 request body 中发送 credentials。
* _可选：_ 选择是否 **Ignore SSL Issues**。开启后，即使 SSL validation 失败，n8n 也会连接。

## 使用 query auth <a href="#using-query-auth" id="using-query-auth"></a>

如果你的 app 或服务支持以单个 key/value query parameter 传递身份验证，请使用此 generic authentication。（如果需要多个 query parameters，请使用 [Custom Auth](httprequest.md#using-custom-auth)。）

要配置此 credential，请输入：

* query parameter key 或 **Name**
* query parameter **Value**

## 使用 custom auth <a href="#using-custom-auth" id="using-custom-auth"></a>

如果你的 app 或服务支持以多个 key/value query parameters 传递身份验证，或者你需要比其他 generic auth 选项更灵活的方式，请使用此 generic authentication。

**Custom Auth** credential 需要使用 JSON 数据定义 credential。你可以使用 `headers`、`qs`、`body`，或混合使用。查看下面的示例开始配置。

### 发送两个 headers <a href="#sending-two-headers" id="sending-two-headers"></a>

```
{
	"headers": {
		"X-AUTH-USERNAME": "username",
		"X-AUTH-PASSWORD": "password"
	}
}
```

### Body <a href="#body" id="body"></a>

```
{
	 "body" : {
		"user": "username",
		"pass": "password"
	}
}
```

### Query string <a href="#query-string" id="query-string"></a>

```
{
	"qs": {
		"appid": "123456",
		"apikey": "my-api-key"
	}
}
```

### 发送 header 和 query string <a href="#sending-header-and-query-string" id="sending-header-and-query-string"></a>

```
{
	"headers": {
		"api-version": "202404"
	},
	"qs": {
		"apikey": "my-api-key"
	}
}
```

## 提供 SSL certificate <a href="#provide-an-ssl-certificate" id="provide-an-ssl-certificate"></a>

你可以随 HTTP request 发送 SSL certificate。请将 SSL certificate 创建为单独的 credential，以供 node 使用：

1. 在 HTTP Request node **Settings** 中，开启 **SSL Certificates**。
2. 在 **Parameters** 标签页，将已有 SSL Certificate credential 添加到 **Credential for SSL Certificates**，或创建一个新的 credential。

要配置 SSL Certificates credential，你需要添加：

* Certificate Authority **CA** bundle
* **Certificate** (CRT)：根据签发 CA 以及其格式化 cert 的方式，也可能显示为 Public Key
* **Private Key** (KEY)
* _可选：_ 如果 **Private Key** 已加密，请输入 private key 的 **Passphrase**。

如果你的 SSL certificate 在单个文件中（例如 `.pfx` 文件），需要打开该文件，从中复制详细信息并粘贴到对应字段：

* 将 Public Key/CRT 输入为 **Certificate**
* 将 **Private Key**/KEY 输入到该字段
