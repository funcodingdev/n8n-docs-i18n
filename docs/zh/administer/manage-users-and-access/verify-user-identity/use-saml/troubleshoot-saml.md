---
title: Troubleshooting SAML SSO
description: 如果遇到 SAML 问题，可检查事项列表。
contentType: howto
nodeTitle: Troubleshoot SAML
originalFilePath: user-management/saml/troubleshooting.md
originalUrl: 'https://docs.n8n.io/user-management/saml/troubleshooting'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml
layout:
  description:
    visible: false
---

# Troubleshooting SAML SSO <a href="#troubleshooting-saml-sso" id="troubleshooting-saml-sso"></a>

如果测试 SAML setup 时出现 error，请检查以下内容：

* 你在 IdP 中创建的 app 是否支持 SAML？
* 是否在 IdP 的正确 fields 中输入了 n8n redirect URL 和 entity ID？
* Metadata XML 是否正确？检查你复制到 n8n 的 metadata 是否格式正确。

如需更多 support，请使用 [forum](https://community.n8n.io/)，如果你有 paid support plan，也可以联系 support representative。
