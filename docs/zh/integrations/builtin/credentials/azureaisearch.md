---
title: Azure AI Search credentials
description: >-
  Azure AI Search credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Azure AI Search。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Azure AI Search credentials
originalFilePath: integrations/builtin/credentials/azureaisearch.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/azureaisearch'
url: 'https://docs.n8n.io/integrations/builtin/credentials/azureaisearch'
layout:
  description:
    visible: false
---

# Azure AI Search credentials <a href="#azure-ai-search-credentials" id="azure-ai-search-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Azure AI Search Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 一个 [Azure subscription](https://azure.microsoft.com)
- 一个在 [Azure Portal](https://portal.azure.com/) 中创建的 Azure AI Search service

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

此 node 使用 API key 身份验证。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure AI Search 文档](https://learn.microsoft.com/azure/search/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **Endpoint**：你的 Azure AI Search service URL（格式：`https://your-service.search.windows.net`）
- **API Key**：Admin key（读写）或 query key（只读）

获取这些值：

1. 在 [Azure Portal](https://portal.azure.com/) 中导航到你的 Azure AI Search service
2. 从 **Overview** 区域复制 **URL**
3. 前往 **Settings** > **Keys** 并复制：
   - **Admin key**，用于完整读写访问；或
   - **Query key**，用于只读查询
4. 在 n8n 中输入这些值

{% hint style="info" %}
**API key 权限**

Admin keys 提供完整访问权限，包括创建和删除 index。Query keys 提供只读访问权限。请根据你的 workflow 需求选择。
{% endhint %}

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 身份验证错误 <a href="#authentication-errors" id="authentication-errors"></a>

**API key 身份验证失败**：
- 验证 API key 是否正确，且未在 Azure Portal 中重新生成
- 确认写入操作（insert/update）使用的是 admin key
- 检查 key 是否未过期或未被轮换

### 连接问题 <a href="#connection-issues" id="connection-issues"></a>

- 验证 endpoint URL 格式：`https://your-service.search.windows.net`
- 确认你的 Azure AI Search service 正在运行
- 检查 network security rules 和 firewall settings 是否允许你的 n8n instance 访问
