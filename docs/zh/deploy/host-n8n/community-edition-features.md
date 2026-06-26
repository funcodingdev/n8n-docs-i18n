---
title: Community edition features
contentType: explanation
hide:
  - tags
nodeTitle: Community edition features
originalFilePath: hosting/community-edition-features.md
originalUrl: https://docs.n8n.io/hosting/community-edition-features
url: https://docs.n8n.io/deploy/host-n8n/community-edition-features
description: >-
  Community edition 与其他付费计划之间可用功能的差异。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
tags:
  - Community edition
  - Enterprise edition
---

# Community edition 功能

Community edition 包含几乎完整的 n8n 功能集，但不包含此处列出的功能。

Community edition 不包含这些功能：

* [Custom Variables](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/define-custom-variables)
* [Environments](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments)
* [External secrets](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/use-external-secret-stores)
* [External storage for binary data](configure-n8n/scaling/use-external-storage.md)
* [Log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems)（[Logging](keep-n8n-running/set-up-logging.md) _包含_ 在内）
* [Multi-main mode](configure-n8n/scaling/enable-queue-mode.md#multi-main-setup)（[Queue mode](configure-n8n/scaling/enable-queue-mode.md) _包含_ 在内）
* [Projects](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)
* SSO（[SAML](configure-n8n/security/configure-sso.md)、[LDAP](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/connect-ldap)）
* Sharing（[workflows](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/share-with-others)、[credentials](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/share-credentials-securely)）（只有实例所有者和创建它们的用户可以访问 workflows 和 credentials）
* [Version control using Git](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments)

这些功能可用于：Enterprise Cloud plan，包括自托管 Enterprise edition。其中部分功能也可用于 Starter 和 Pro Cloud plans，以及自托管 Business plan。

请参阅 [pricing](https://n8n.io/pricing/) 作为参考。

## 已注册的 Community Edition <a href="#registered-community-edition" id="registered-community-edition"></a>

你可以注册 n8n community edition 来解锁额外功能。注册时使用邮箱，并接收一个 license key。

注册后会为 community edition 解锁这些功能：

* Folders：将 workflows 整理到清晰的文件夹中
* [Debug in editor](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/debug-executions)：处理 workflow 时复制并 pin[^1] execution data
* [Custom execution data](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/customize-executions-data)：保存、查找并标注 execution metadata

要注册新的 community edition 实例，请在初始账号创建期间选择该选项。

要注册现有的 community edition 实例：

1. 选择左下角的 **three dots icon** <img src="../.gitbook/assets/three-dots-horizontal (1).png" alt="three dots icon" data-size="line">。
2. 选择 **Settings**，然后选择 **Usage and plan**。
3. 选择 **Unlock** 输入你的邮箱，然后选择 **Send me a free license key**。
4. 检查你输入的账号对应的邮箱。

拿到 license key 后，可点击 license 邮件中的按钮激活，或访问 **Options > Settings > Usage and plan** 并选择 **Enter activation key**。

激活后，你的 license 不会过期。我们未来可能会更改解锁的功能。这不会影响此前已经解锁的功能。

[^1]: Data pinning 允许你在 workflow 开发期间临时冻结某个 node 的输出数据。这让你可以使用可预测的数据开发 workflows，而无需反复向外部服务发起请求。Production workflows 会忽略 pinned data，并在每次 execution 时请求新数据。
