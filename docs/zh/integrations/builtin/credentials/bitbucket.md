---
title: Bitbucket credentials
description: >-
  Bitbucket credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Bitbucket。
contentType:
  - integration
  - reference
nodeTitle: Bitbucket credentials
originalFilePath: integrations/builtin/credentials/bitbucket.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/bitbucket'
url: 'https://docs.n8n.io/integrations/builtin/credentials/bitbucket'
layout:
  description:
    visible: false
---

# Bitbucket credentials <a href="#bitbucket-credentials" id="bitbucket-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Bitbucket Trigger](../trigger-nodes/n8n-nodes-base.bitbuckettrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Bitbucket](https://www.bitbucket.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bitbucket 的 API 文档](https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication)。

## 配置 Bitbucket access token <a href="#configuring-bitbucket-access-token" id="configuring-bitbucket-access-token"></a>

1. 登录 Bitbucket，并打开你的 account 或 personal settings。
2. 找到 API tokens 或 security settings 区域。
3. 创建新的 API token，为其设置符合使用场景的名称和到期日期。
4. 选择 Bitbucket 作为 app，然后选择所需的 scopes（permissions）：

    ```bash
    read:user:bitbucket
    read:workspace:bitbucket
    read:repository:bitbucket
    read:webhook:bitbucket
    write:webhook:bitbucket
    delete:webhook:bitbucket
    ```

5. 检查并创建 token。复制生成的 token 并添加到 n8n。Bitbucket 只会显示 token 一次。

有关详细说明，请参阅 [Create an API token](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)。
