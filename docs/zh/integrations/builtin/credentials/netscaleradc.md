---
title: Netscaler ADC credentials
description: >-
  Netscaler ADC credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Netscaler ADC 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Netscaler ADC credentials
originalFilePath: integrations/builtin/credentials/netscaleradc.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/netscaleradc'
url: 'https://docs.n8n.io/integrations/builtin/credentials/netscaleradc'
layout:
  description:
    visible: false
---

# Netscaler ADC credentials <a href="#netscaler-adc-credentials" id="netscaler-adc-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Netscaler ADC node](../app-nodes/n8n-nodes-base.netscaleradc.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

安装一个 [NetScaler/Citrix ADC appliance](https://docs.netscaler.com/en-us/citrix-adc/current-release/getting-started-with-citrix-adc)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Netscaler ADC's 14.1 NITRO API documentation](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

* 一个 **URL**：输入你的 NetScaler/Citrix ADC instance 的 URL。
* 一个 **Username**：输入你的 NetScaler/Citrix ADC username。
* 一个 **Password**：输入你的 NetScaler/Citrix ADC password。

更多信息请参考 [Performing Basic Netscaler ADC Operations](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/performing-basic-netscaler-operations)。
