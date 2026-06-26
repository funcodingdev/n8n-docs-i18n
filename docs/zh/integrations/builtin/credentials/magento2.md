---
title: Magento 2 credentials
description: >-
  Magento 2 credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Magento 2 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Magento 2 credentials
originalFilePath: integrations/builtin/credentials/magento2.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/magento2'
url: 'https://docs.n8n.io/integrations/builtin/credentials/magento2'
layout:
  description:
    visible: false
---

# Magento 2 credentials <a href="#magento-2-credentials" id="magento-2-credentials"></a>

你可以使用这些 credentials 对以下 node 进行身份验证：

- [Magento 2](../app-nodes/n8n-nodes-base.magento2.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Magento (Adobe Commerce)](https://business.adobe.com/products/commerce.html) 账号。
- 将 store 设置为 **Allow OAuth Access Tokens to be used as standalone Bearer tokens**。
    - 前往 **Admin > Stores > Configuration > Services > OAuth > Consumer Settings**。
    - 将 **Allow OAuth Access Tokens to be used as standalone Bearer tokens** 选项设置为 **Yes**。
    - 你也可以运行以下命令从 CLI 启用此设置：

        ```
        bin/magento config:set oauth/consumer/enable_integration_as_bearer 1
        ```

在 n8n 更新 Magento 2 credentials 以使用 OAuth 之前，此步骤是必需的。更多信息请参考 [Integration Tokens](https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token/#integration-tokens)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Magento's API documentation](https://developer.adobe.com/commerce/docs/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- **Host**：输入你的 Magento store 地址。
- **Access Token**：从 [**Admin Panel**](https://docs.magento.com/user-guide/stores/admin.html) 获取 access token：
    1. 前往 **System > Extensions > Integrations**。
    2. 添加新的 Integration。
    3. 前往 **API** 标签页，并选择你希望 n8n integration 访问的 Magento resources。
    4. 从 **Integrations** 页面，**Activate** 新 integration。
    5. 选择 **Allow** 显示 access token，以便复制并输入到 n8n。
