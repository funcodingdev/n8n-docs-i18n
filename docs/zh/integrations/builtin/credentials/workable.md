---
title: Workable credentials
description: >-
  Workable credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Workable 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Workable credentials
originalFilePath: integrations/builtin/credentials/workable.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/workable'
url: 'https://docs.n8n.io/integrations/builtin/credentials/workable'
layout:
  description:
    visible: false
---

# Workable credentials <a href="#workable-credentials" id="workable-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Workable Trigger](../trigger-nodes/n8n-nodes-base.workabletrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Workable](https://www.workable.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Workable's API documentation](https://workable.readme.io/reference/generate-an-access-token)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Subdomain**：你的 Workable subdomain 是 Workable domain 中位于 `https://` 和 `.workable.com` 之间的部分。因此如果完整 domain 是 `https://n8n.workable.com`，subdomain 就是 `n8n`。subdomain 也显示在你的 Workable **Company Profile** 页面。
- 一个 **Access Token**：前往你的 **profile >** [**Integrations**](https://workable.com/backend/settings/integrations) **> Apps**，并选择 **Generate API token**。更多信息请参考 [Generate a new token](https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#Generateanewtoken)。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Token scopes</strong></p><p>如果你将此 credential 与 <a href="../trigger-nodes/n8n-nodes-base.workabletrigger.md">Workable Trigger</a> node 一起使用，请在生成 token 时选择 <code>r_candidates</code> 和 <code>r_jobs</code> scopes。如果你以其他方式使用此 credential，请选择与你的 use case 相关的 scopes。</p><p>有关 scopes 的更多信息，请参考 <a href="https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#SupportedAPIscopes">Supported API scopes</a>。</p></div>
