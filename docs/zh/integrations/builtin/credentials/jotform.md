---
title: Jotform credentials
description: >-
  Jotform credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Jotform 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Jotform credentials
originalFilePath: integrations/builtin/credentials/jotform.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/jotform'
url: 'https://docs.n8n.io/integrations/builtin/credentials/jotform'
layout:
  description:
    visible: false
---

# Jotform credentials <a href="#jotform-credentials" id="jotform-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Jotform Trigger](../trigger-nodes/n8n-nodes-base.jotformtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Jotform's API documentation](https://api.jotform.com/docs/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Jotform](https://www.jotform.com/) 账号，并准备：

- **API Key**
- **API Domain**

设置步骤：

1. 前往 **Settings >** [**API**](https://www.jotform.com/myaccount/api)。
2. 选择 **Create New Key**。
3. 在 Jotform 中选择 **Name**，将 API key 名称更新为有意义的名称，例如 `n8n integration`。
4. 复制 **API Key**，并将其输入到你的 n8n credential。
5. 在 n8n 中，根据你使用的 forms 选择适用的 **API Domain**：
    - **api.jotform.com**：除非其他 form 类型适用于你，否则使用此项。
    - **eu-api.jotform.com**：如果你使用 Jotform [EU Safe Forms](https://www.jotform.com/eu-safe-forms/)，请选择此项。
    - **hipaa-api.jotform.com**：如果你使用 Jotform [HIPAA forms](https://www.jotform.com/hipaa/)，请选择此项。

有关创建 keys 和 API domains 的更多信息，请参考 [Jotform API documentation](https://api.jotform.com/docs/)。
