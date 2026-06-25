---
title: Home Assistant credentials
description: >-
  Home Assistant credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Home Assistant 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Home Assistant credentials
originalFilePath: integrations/builtin/credentials/homeassistant.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/homeassistant'
url: 'https://docs.n8n.io/integrations/builtin/credentials/homeassistant'
layout:
  description:
    visible: false
---

# Home Assistant credentials <a href="#home-assistant-credentials" id="home-assistant-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Home Assistant](../app-nodes/n8n-nodes-base.homeassistant.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Home Assistant's API documentation](https://developers.home-assistant.io/docs/api/rest)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要[安装](https://www.home-assistant.io/installation/) Home Assistant、创建一个 [Home Assistant](https://www.home-assistant.io/getting-started/onboarding) 账号，并准备：

- 你的 **Host**
- **Port**
- Long-Lived **Access Token**

生成 access token 并设置 credential：

1. 要生成 **Access Token**，请登录 Home Assistant 并打开你的 [User profile](https://my.home-assistant.io/redirect/profile)。
2. 在 **Long-Lived Access Tokens** 区域生成一个新 token。
3. 复制此 token，并在 n8n 中将它填为你的 **Access Token**。
4. 输入 Home Assistant **Host** 的 URL 或 IP 地址，不要包含 `http://` 或 `https://` 协议，例如 `your.awesome.home`。
5. 对于 **Port**，输入合适的端口：
	- 如果你没有修改端口，并且通过 `http://` 访问 Home Assistant，请保留默认值 `8123`。
	- 如果你没有修改端口，并且通过 `https://` 访问 Home Assistant，请输入 `443`。
	- 如果你已将 Home Assistant 配置为使用特定端口，请输入该端口。
6. 如果你已在 Home Assistant 的 [config.yml map key](https://developers.home-assistant.io/docs/add-ons/configuration/?_highlight=ssl#add-on-configuration) 中启用 SSL，请在 n8n 中开启 **SSL** toggle。如果你不确定，并且你是通过 `https://` 而不是 `http://` 访问 home assistant UI，最好开启此设置。
