---
title: CrowdStrike credentials
description: >-
  CrowdStrike credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 CrowdStrike。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: CrowdStrike credentials
originalFilePath: integrations/builtin/credentials/crowdstrike.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/crowdstrike'
url: 'https://docs.n8n.io/integrations/builtin/credentials/crowdstrike'
layout:
  description:
    visible: false
---

# CrowdStrike credentials <a href="#crowdstrike-credentials" id="crowdstrike-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [CrowdStrike](https://www.crowdstrike.com/en-us/) 账号。

## 身份验证方法 <a href="#authentication-methods" id="authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 CrowdStrike 的文档。其文档需要登录后访问，因此你必须登录官网账号才能访问 API 文档。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/crowdstrike/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- CrowdStrike instance 的 **URL**
- 一个 **Client ID**：在 Crowdstrike 的 **Support > API Clients and Keys** 中创建新的 API Client 时生成。
- 一个 **Client Secret**：在 Crowdstrike 的 **Support > API Clients and Keys** 中创建新的 API Client 时生成。

设置 API client 时，请授予它 `usermgmt:read` scope。n8n 依赖此 scope 来测试 credential 是否可用。

CrowdStrike 博客公开提供了合适步骤的大致说明：[Getting Access to the CrowdStrike API](https://www.crowdstrike.com/blog/tech-center/get-access-falcon-apis/)。CrowdStrike 的完整文档需要登录后访问，因此你必须登录账号才能访问完整 API 文档。
