---
title: Alibaba Cloud credentials
description: >-
  Alibaba Cloud credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Alibaba Cloud。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Alibaba Cloud credentials
originalFilePath: integrations/builtin/credentials/alibaba.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/alibaba'
url: 'https://docs.n8n.io/integrations/builtin/credentials/alibaba'
layout:
  description:
    visible: false
---

# Alibaba Cloud credentials <a href="#alibaba-cloud-credentials" id="alibaba-cloud-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Alibaba Cloud Model Studio](../app-nodes/n8n-nodes-langchain.alibabacloud.md)
- [Alibaba Cloud Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Alibaba Cloud](https://www.alibabacloud.com/) 账号，并开通 [Model Studio](https://www.alibabacloud.com/en/product/modelstudio)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Alibaba Cloud Model Studio 文档](https://www.alibabacloud.com/help/en/model-studio/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

1. 登录 [Alibaba Cloud Model Studio 控制台](https://modelstudio.console.alibabacloud.com/)。
2. 在屏幕右上角选择目标区域。
3. 在顶部菜单中选择 **Dashboard**，然后在侧边菜单中选择 **API Key**。
4. 选择 **Create API Key**。
5. 在对话框中选择 workspace 和 key description，然后选择 **OK**。
6. 复制 API key（它只会显示一次），并将其输入到 n8n credential 中。
7. 确保 n8n credential 的区域与你在 Alibaba Cloud Model Studio 控制台中选择的区域一致。

有关更多信息，请参阅 [Alibaba Cloud 的 API key 文档](https://www.alibabacloud.com/help/en/model-studio/developer-reference/get-api-key)。
