---
title: Configure the Base URL for n8n's front end access
description: >-
  配置 Base URL 环境变量，以定义 n8n front end 访问 back end REST API 的路径。
contentType: howto
nodeTitle: Configure the Base URL
originalFilePath: hosting/configuration/configuration-examples/base-url.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/base-url'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url
layout:
  description:
    visible: false
---

# 配置 n8n front end 访问用的 Base URL <a href="#configure-the-base-url-for-n8ns-front-end-access" id="configure-the-base-url-for-n8ns-front-end-access"></a>

{% hint style="warning" %}
**需要手动 UI build**

此 use case 涉及配置 `VUE_APP_URL_BASE_API` environmental variable，这需要手动 build `n8n-editor-ui` package。你不能将它与默认 n8n Docker image 一起使用，因为此变量的默认设置为 `/`，表示使用 root-domain。
{% endhint %}

你可以配置 front end 用于连接 back end REST API 的 Base URL。当你想将 n8n 的 front end 和 back end 分开托管时，这会很有用。

```bash
export VUE_APP_URL_BASE_API=https://n8n.example.com/
```
有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/deployment.md)。
