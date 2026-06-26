---
title: 设置 Single Sign-On (SSO)
description: 为你的 self-hosted n8n 实例设置 SAML 或 OIDC Single Sign-On。
contentType: howto
nodeTitle: Configure SSO
originalFilePath: hosting/securing/set-up-sso.md
originalUrl: 'https://docs.n8n.io/hosting/securing/set-up-sso'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso'
layout:
  description:
    visible: false
---

# 设置 Single Sign-On (SSO) <a href="#set-up-single-sign-on-sso" id="set-up-single-sign-on-sso"></a>

{% hint style="info" %}
**功能可用性**

* Business 和 Enterprise plans 可用。
* 你需要是 instance owner 或 admin，才能启用和配置 SAML 或 OIDC。
{% endhint %}

n8n 支持用于 single sign-on (SSO) 的 SAML 和 OIDC authentication protocols。关于这两种协议、它们的差异和各自优势的一般信息，请参阅 [OIDC vs SAML](https://www.onelogin.com/learn/oidc-vs-saml)。

* [设置 SAML](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/use-saml/set-up-saml)：在 n8n 中设置 SAML 的通用指南，并链接到常见 identity providers (IdPs) 的资源。
* [设置 OIDC](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc)：在 n8n 中设置 OpenID Connect (OIDC) SSO 的通用指南。

## 使用环境变量配置 SSO <a href="#configure-sso-with-environment-variables" id="configure-sso-with-environment-variables"></a>

你也可以通过环境变量而不是 UI 配置 SSO。从 n8n v2.18.0 起可用。完整变量列表请参阅 [SSO environment variables](../basic-configuration/use-environment-variables/sso.md)；关于 activation pattern 的工作方式，请参阅 [Manage instance settings using environment variables](../manage-settings-using-environment-variables.md)。
