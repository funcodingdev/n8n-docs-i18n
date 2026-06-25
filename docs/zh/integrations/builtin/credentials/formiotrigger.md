---
title: Form.io Trigger credentials
description: >-
  Form.io Trigger credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Form.io Trigger。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Form.io Trigger credentials
originalFilePath: integrations/builtin/credentials/formiotrigger.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/formiotrigger'
url: 'https://docs.n8n.io/integrations/builtin/credentials/formiotrigger'
layout:
  description:
    visible: false
---

# Form.io Trigger credentials <a href="#formio-trigger-credentials" id="formio-trigger-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Form.io Trigger](../trigger-nodes/n8n-nodes-base.formiotrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Form.io 的 API 文档](https://apidocs.form.io/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要一个 [Form.io](https://www.form.io/) 账号，以及：

- 你的 **Environment**
- 登录 **Email address**
- 你的 **Password**

设置 credential：

1. 选择你的 **Environment**：
    - 如果你不是自己托管 Form.io，请选择 **Cloud hosted**。
    - 如果你自己托管 Form.io，请选择 **Self-hosted**。然后添加：
        - 你的 **Self-Hosted Domain**。只使用 domain 本身。例如，如果你在 `https://yourserver.com/yourproject/manage/view` 查看 form，则 Self-Hosted Domain 是 `https://yourserver.com`。
2. 输入用于登录 Form.io 的 **Email address**。
3. 输入用于登录 Form.io 的 **Password**。
