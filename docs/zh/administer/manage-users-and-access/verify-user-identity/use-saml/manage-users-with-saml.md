---
title: Manage users with SAML
description: 启用 SAML 后如何管理 users 和 user logins。
contentType: howto
nodeTitle: Manage users with SAML
originalFilePath: user-management/saml/managing.md
originalUrl: 'https://docs.n8n.io/user-management/saml/managing'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml
layout:
  description:
    visible: false
---

# 使用 SAML 管理 users <a href="#manage-users-with-saml" id="manage-users-with-saml"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/9DXSTQsxYGisAV8xk6p4/" %}

有一些 user management tasks 会受 SAML 影响。

## 让 users 豁免 SAML <a href="#exempt-users-from-saml" id="exempt-users-from-saml"></a>

你可以允许 users 不使用 SAML login。操作方式：

1. 前往 **Settings** > **Users**。
2. 选择要豁免 SAML 的 user 旁边的 menu icon。
3. 选择 **Allow Manual Login**。

## 删除 users <a href="#deleting-users" id="deleting-users"></a>

如果你从 IdP 中移除 user，他们仍会保持 logged in 到 n8n。你也需要从 n8n 中手动移除他们。删除 users 的 guidance 请参考 [Manage users](../../add-and-remove-users.md)。
