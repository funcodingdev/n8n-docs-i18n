---
title: Bitwarden credentials
description: >-
  Bitwarden credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Bitwarden。
contentType:
  - integration
  - reference
nodeTitle: Bitwarden credentials
originalFilePath: integrations/builtin/credentials/bitwarden.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/bitwarden'
url: 'https://docs.n8n.io/integrations/builtin/credentials/bitwarden'
layout:
  description:
    visible: false
---

# Bitwarden credentials <a href="#bitwarden-credentials" id="bitwarden-credentials"></a>

你可以使用这些 credentials 验证以下 node：

- [Bitwarden](../app-nodes/n8n-nodes-base.bitwarden.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Bitwarden](https://vault.bitwarden.com/#/register?org=teams) Teams organization 或 Enterprise organization 账号。（Bitwarden 仅向这些 [organization](https://bitwarden.com/help/about-organizations/) plans 提供 Bitwarden Public API。）

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bitwarden 的 Public API 文档](https://bitwarden.com/help/public-api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **Client ID**：生成 API key 时提供
- **Client Secret**：生成 API key 时提供
- **Environment**：
    - 如果你没有 self-host Bitwarden，请选择 **Cloud-hosted**。无需进一步配置。
    - 如果你在自己的 server 上托管 Bitwarden，请选择 **Self-hosted**。在相应字段中输入你的 **Self-hosted domain**。

Client ID 和 Client Secret 必须属于 **Organization API Key**，而不是 Personal API Key。有关生成 Organization API Key 的说明，请参阅 [Bitwarden Public API Authentication 文档](https://bitwarden.com/help/public-api/#authentication)。
