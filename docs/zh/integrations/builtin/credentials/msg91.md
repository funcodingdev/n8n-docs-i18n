---
title: MSG91 credentials
description: >-
  MSG91 credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MSG91 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: MSG91 credentials
originalFilePath: integrations/builtin/credentials/msg91.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/msg91'
url: 'https://docs.n8n.io/integrations/builtin/credentials/msg91'
layout:
  description:
    visible: false
---

# MSG91 credentials <a href="#msg91-credentials" id="msg91-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [MSG91](../app-nodes/n8n-nodes-base.msg91.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MSG91](https://msg91.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MSG91's API documentation](https://docs.msg91.com/overview)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Authentication Key**：要获取 Authentication Key，请前往 user menu 并选择 **Authkey**。更多信息请参考 MSG91 的 [Where can I find my authentication key? documentation](https://msg91.com/help/api/where-can-i-find-my-authentication-ke)。

## IP Security <a href="#ip-security" id="ip-security"></a>

MSG91 默认为 authkeys 启用 [IP Security](https://msg91.com/help/api/what-do-you-mean-by-api-security)。

要让 n8n credentials 在启用此设置时正常工作，请将所有 [n8n IP addresses](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/configure-cloud/find-your-ip-addresses) 添加为 MSG91 中的 whitelisted IPs。你可以根据所需安全级别，在以下两个位置之一添加：

- 如果要允许 account 中任意或所有 authkeys 与 n8n 配合使用，请在 **Authkey** page 的 **Company's whitelisted IPs** section 中添加 n8n IP addresses。
- 如果只允许特定 authkeys 与 n8n 配合使用，请在某个 authkey details 的 **Whitelisted IPs** section 中添加 n8n IP addresses。
