---
title: HaloPSA credentials
description: >-
  HaloPSA credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  HaloPSA 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: HaloPSA credentials
originalFilePath: integrations/builtin/credentials/halopsa.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/halopsa'
url: 'https://docs.n8n.io/integrations/builtin/credentials/halopsa'
layout:
  description:
    visible: false
---

# HaloPSA credentials <a href="#halopsa-credentials" id="halopsa-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [HaloPSA](../app-nodes/n8n-nodes-base.halopsa.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [HaloPSA](https://halopsa.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [HaloPSA's API documentation](https://usehalo.com/halopsa/guides/1823/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 选择你的 **Hosting Type**：
    - **On Premise Solution**：如果你在自己的服务器上托管 Halo application，请选择此项
    - **Hosted Solution Of Halo**：如果你的 application 由 Halo 托管，请选择此项。如果选择此项，你需要提供 **Tenant**。
- **HaloPSA Authorisation Server URL**：你的 Authorisation Server URL 会显示在 HaloPSA 的 **Configuration > Integrations > Halo API** 中的 [API Details](https://halopsa.com/guides/article/?kbid=1737)。
- **Resource Server** URL：你的 Resource Server 会显示在 HaloPSA 的 **Configuration > Integrations > Halo API** 中的 [API Details](https://halopsa.com/guides/article/?kbid=1737)。
- **Client ID**：通过在 Halo API 设置中注册 application 获取。详细说明请参考 [HaloPSA's Authorisation documentation](https://usehalo.com/halopsa/guides/1823/)。n8n 建议使用这些设置：
    - 选择 `Client Credentials` 作为 **Authentication Method**。
    - 使用 `all` permission。
- **Client Secret**：通过在 Halo API 设置中注册 application 获取。
- 你的 **Tenant** 名称：如果 **Hosting Type** 选择了 **Hosted Solution of Halo**，你必须提供 tenant 名称。你的 tenant 名称会显示在 HaloPSA 的 **Configuration > Integrations > Halo API** 中的 [API Details](https://halopsa.com/guides/article/?kbid=1737)。

HaloPSA 会同时使用 application permissions 和 agent 的 permissions 来决定 API 访问权限。
