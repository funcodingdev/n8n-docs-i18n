---
title: Troubleshooting for OIDC SSO
description: 在 n8n 中使用 OIDC 时需要注意的事项和 troubleshooting。
contentType: howto
nodeTitle: Troubleshoot OIDC
originalFilePath: user-management/oidc/troubleshooting.md
originalUrl: 'https://docs.n8n.io/user-management/oidc/troubleshooting'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc
layout:
  description:
    visible: false
---

# Troubleshooting OIDC SSO <a href="#troubleshooting-oidc-sso" id="troubleshooting-oidc-sso"></a>

## Known issues <a href="#known-issues" id="known-issues"></a>

### 不支持 state parameter <a href="#state-parameter-not-supported" id="state-parameter-not-supported"></a>

使用强制要求 `state` CSRF token parameter 的 OIDC providers 时，authentication 会失败并显示 error：

```json
{"code":0,"message":"authorization response from the server is an error"}
```

n8n 当前的 OIDC implementation 不处理某些 OIDC providers 作为 CSRF attacks 防护措施发送的 `state` parameter。

目前唯一 workaround 是在可能的情况下配置你的 OIDC provider，禁用 `state` parameter。

n8n 正在计划在 future release 中添加对 OIDC `state` parameter 的完整支持。

### 不支持 PKCE <a href="#pkce-not-supported" id="pkce-not-supported"></a>

要求 PKCE (Proof Key for Code Exchange) 的 OIDC providers 可能会 authentication 失败，或 reject n8n 的 authorization requests。n8n 当前的 OIDC implementation 不支持 PKCE。

唯一 workaround 是在你的 provider settings 中可用时，配置 OIDC provider 不要求 n8n client 使用 PKCE。

n8n 计划在 future release 中添加 PKCE support。
