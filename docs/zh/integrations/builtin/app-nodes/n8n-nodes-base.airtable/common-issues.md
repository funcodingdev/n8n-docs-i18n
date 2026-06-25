---
title: Airtable node common issues
description: >-
  n8n 中 Airtable node 常见问题和疑问的文档。n8n 是一款 workflow 自动化平台。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Airtable node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues
layout:
  description:
    visible: false
---

# Airtable node 常见问题 <a href="#airtable-node-common-issues" id="airtable-node-common-issues"></a>

以下是 [Airtable node](README.md) 的一些常见错误和问题，以及解决或排查步骤。

## Forbidden - perhaps check your credentials <a href="#forbidden-perhaps-check-your-credentials" id="forbidden-perhaps-check-your-credentials"></a>

当尝试执行当前访问级别不允许的 action 时，会显示此错误。完整文本大致如下：

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

当你使用的 credential 在你尝试管理的资源上没有所需 scope 时，最常出现此错误。

更多信息请参阅 [Airtable credentials](../../credentials/airtable.md) 和 [Airtable scopes 文档](https://airtable.com/developers/web/api/scopes)。

## Service is receiving too many requests from you <a href="#service-is-receiving-too-many-requests-from-you" id="service-is-receiving-too-many-requests-from-you"></a>

Airtable 对使用 personal access token 生成的请求数量有严格 API 限制。

如果每个 base 每秒发送超过五个请求，你会收到 429 错误，表示发送了过多请求。恢复请求前必须等待 30 秒。对于每个 access token 跨所有 base 发送超过 50 个请求，也适用同样限制。

你可以在 [Airtable rate limits 文档](https://airtable.com/developers/web/api/rate-limits)中了解更多信息。如果你在 Airtable node 中遇到 rate limit，请考虑实现[处理 rate limit](../../handle-rate-limits.md) 页面上的建议之一。
