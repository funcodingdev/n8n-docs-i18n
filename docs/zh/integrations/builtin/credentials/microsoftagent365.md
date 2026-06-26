---
title: Microsoft Agent 365 credentials
description: >-
  Microsoft Agent 365 credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Microsoft Agent 365 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft Agent 365 credentials
originalFilePath: integrations/builtin/credentials/microsoftagent365.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365'
url: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365'
layout:
  description:
    visible: false
---

# Microsoft Agent 365 credentials <a href="#microsoft-agent-365-credentials" id="microsoft-agent-365-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Microsoft Agent 365 Trigger](../cluster-nodes/root-nodes/root-nodes.md)

{% hint style="warning" %}
**早期预览**

Microsoft Agent 365 是 early preview feature。你需要加入 [Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/) 才能获得 early access。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 已加入 [Microsoft Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)
- [Microsoft Azure](https://azure.microsoft.com/) 账号
- 使用 Agent 365 CLI 创建的 Agent 365 blueprint

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2 (App Registration)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Microsoft Agent 365 developer documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- **Tenant ID**：你的 Microsoft Entra tenant ID
- **Client ID**：来自 Azure app registration 的 Application (client) ID
- **Client Secret**：为 app registration 生成的 secret

设置 credential：

1. 在 [Microsoft Entra ID](https://entra.microsoft.com/#home) 中找到 Tenant ID，并将其作为 **Tenant ID** 复制到 n8n。
2. 打开 [Microsoft Application Registration Portal](https://aka.ms/appregistrations)，并按照 Microsoft Agent 365 的 [custom client app registration guide](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/custom-client-app-registration) 操作。创建 custom client app 后，将 Application (client) ID 复制到 n8n，作为 **Client ID**。
3. 按照 [credentials guide](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret) 生成 client secret，并复制 **Value** 列中的 **Secret**，然后将其粘贴到 n8n，作为 **Client Secret**。

我们建议使用 [Agent 365 CLI](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/agent-365-cli) 创建 agent blueprint 和 manifest。
