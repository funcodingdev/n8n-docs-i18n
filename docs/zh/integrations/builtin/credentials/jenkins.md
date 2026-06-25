---
title: Jenkins credentials
description: >-
  Jenkins credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Jenkins 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Jenkins credentials
originalFilePath: integrations/builtin/credentials/jenkins.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/jenkins'
url: 'https://docs.n8n.io/integrations/builtin/credentials/jenkins'
layout:
  description:
    visible: false
---

# Jenkins credentials <a href="#jenkins-credentials" id="jenkins-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Jenkins](../app-nodes/n8n-nodes-base.jenkins.md)


## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Jenkins](https://www.jenkins.io/) instance 上创建账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Jenkins 不提供公开 API documentation；每个页面的 API documentation 可从用户界面右下角获取。有关该服务的更多信息，请参考这些详情页。有关 API 和 API wrappers 的信息，请参考 [Jenkins Remote Access API](https://www.jenkins.io/doc/book/using/remote-access-api/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- **Jenkins Username**：token 所属用户的 username
- **Personal API Token**：从该用户的 **profile details > Configure > Add new token** 生成。更多细节请参考[这些 Stack Overflow 说明](https://stackoverflow.com/questions/45466090/how-to-get-the-api-token-for-jenkins)。
- **Jenkins Instance URL**

Jenkins 在 2018 年重建了 API token 设置。如果你使用较旧的 Jenkins instance，请确保使用的是非 legacy API token。更多信息请参考 [Security Hardening: New API token system in Jenkins 2.129+](https://www.jenkins.io/blog/2018/07/02/new-api-token-system/)。
