---
title: Securing n8n
contentType: overview
nodeTitle: Security
originalFilePath: hosting/securing/overview.md
originalUrl: 'https://docs.n8n.io/hosting/securing/overview'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security'
layout:
  description:
    visible: false
---

# 保护 n8n <a href="#securing-n8n" id="securing-n8n"></a>

保护你的 n8n 实例可以有多种形式。

从高层看，你可以：

* 执行 [security audit](security/run-security-audits.md) 以识别安全风险。
* [设置 SSL](security/set-up-ssl.md) 以强制使用安全连接。
* 为用户账号管理[设置 Single Sign-On](security/configure-sso.md)。
* 在嵌入 n8n 时，使用 [token exchange](/hosting/oem-deployment/token-exchange.md) 从你自己的 identity provider 登录用户，或代表用户调用 n8n APIs。
* 为用户使用 [two-factor authentication (2FA)](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/require-two-factor-auth)。
* 启用 [encryption key rotation](security/rotate-encryption-keys.md)，定期替换用于加密 credentials 和其他敏感数据的 key。
* 为 [OAuth 2.0 credentials 启用 JWE token decryption](security/decrypt-oauth-20-tokens-with-jwe.md)，以便你的 identity provider 可以加密 access 和 ID tokens，且只有你的实例能够解密。

你还可以保护 workflows 处理的敏感数据：

* [Redact execution data](security/redact-execution-data.md)，隐藏 workflow executions 的 input 和 output data。

更细粒度地说，可以考虑阻止或退出你不需要的功能或数据收集：

* 如果没有使用 [public API](security/disable-the-public-api.md)，可以禁用它。
* [退出 n8n 自动收集的匿名数据的 data collection](security/control-telemetry.md)。
* [阻止特定 nodes](security/block-specific-nodes.md) 对用户可用。
* [防护 SSRF attacks](security/enable-ssrf-protection.md)，控制 workflow nodes 可以连接到哪些 hosts 和 IP ranges。
* [限制账号注册](security/verify-user-emails.md)，只允许 email-verified users 注册。
