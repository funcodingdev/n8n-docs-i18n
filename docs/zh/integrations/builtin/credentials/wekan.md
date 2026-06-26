---
title: Wekan credentials
description: >-
  Wekan credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Wekan 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Wekan credentials
originalFilePath: integrations/builtin/credentials/wekan.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/wekan'
url: 'https://docs.n8n.io/integrations/builtin/credentials/wekan'
layout:
  description:
    visible: false
---

# Wekan credentials <a href="#wekan-credentials" id="wekan-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Wekan](../app-nodes/n8n-nodes-base.wekan.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在你的 server 上安装 [Wekan](https://github.com/wekan/wekan/wiki)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关向该服务进行身份验证的更多信息，请参考 [Wekan's API documentation](https://github.com/wekan/wekan/wiki/REST-API)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **Username**：输入你的 Wekan username。
- 一个 **Password**：输入你的 Wekan password。
- 一个 **URL**：输入你的 Wekan domain。
