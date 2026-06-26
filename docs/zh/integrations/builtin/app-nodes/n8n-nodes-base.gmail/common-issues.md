---
title: Gmail node common issues
description: >-
  n8n 中 Gmail node 的常见问题和疑问文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Gmail node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues
layout:
  description:
    visible: false
---

# Gmail node 常见问题 <a href="#gmail-node-common-issues" id="gmail-node-common-issues"></a>

下面是 [Gmail node](README.md) 的一些常见 errors 和 issues，以及解决或排查步骤。

## 从已发送 messages 中移除 n8n attribution <a href="#remove-the-n8n-attribution-from-sent-messages" id="remove-the-n8n-attribution-from-sent-messages"></a>

如果你使用 node [send a message](message-operations.md#send-a-message) 或 [reply to a message](message-operations.md#reply-to-a-message)，node 会在 email 末尾追加这句话：

> This email was sent automatically with n8n

要移除此 attribution：

1. 在 node 的 **Options** 部分，选择 **Add option**。
2. 选择 **Append n8n attribution**。
3. 关闭 toggle。

更多信息请参考 [Send options](message-operations.md#send-options) 和 [Reply options](message-operations.md#reply-options)。

## Forbidden - perhaps check your credentials <a href="#forbidden-perhaps-check-your-credentials" id="forbidden-perhaps-check-your-credentials"></a>

此 error 会显示在 node 的某些 dropdowns 旁边，例如 **Label Names or IDs** dropdown。完整文本类似如下：

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

当你使用 Google Service Account 作为 credential，并且 credential 未打开 **Impersonate a User** 时，最常出现此 error。

更多信息请参考 [Google Service Account: Finish your n8n credential](../../credentials/google/service-account.md#finish-your-n8n-credential)。

## 401 unauthorized error <a href="#401-unauthorized-error" id="401-unauthorized-error"></a>

完整 error 文本如下：

```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```


当你使用的 credential 及其 scopes 或 permissions 存在问题时，会发生此 error。

解决方法：

1. 对于 [OAuth2](../../credentials/google/oauth-single-service.md) credentials，请确认你已在 **APIs & Services > Library** 中启用 Gmail API。更多信息请参考 [Google OAuth2 Single Service - Enable APIs](../../credentials/google/oauth-single-service.md#enable-apis)。
2. 对于 [Service Account](../../credentials/google/service-account.md) credentials：
    1. [启用 domain-wide delegation](../../credentials/google/service-account.md#enable-domain-wide-delegation)。
    2. 确认已将 Gmail API 作为 domain-wide delegation 配置的一部分添加。

## Bad request - please check your parameters 参数检查错误 <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

如果你输入了不存在的 Message ID、Thread ID 或 Label ID，最常发生此 error。

请使用带该 ID 的 **Get** operation 确认它是否存在。
