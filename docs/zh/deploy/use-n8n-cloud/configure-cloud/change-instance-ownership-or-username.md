---
title: Change Instance Ownership or Username
Description: 更改实例所有权或用户名。
contentType: howto
nodeTitle: Change instance ownership or username
originalFilePath: manage-cloud/change-ownership-or-username.md
originalUrl: 'https://docs.n8n.io/manage-cloud/change-ownership-or-username'
url: >-
  https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username
layout:
  description:
    visible: false
---

## 更改实例所有权 <a href="#change-instance-ownership" id="change-instance-ownership"></a>

你可以进入所有者账号的 **Settings > Personal** 页面，并编辑 **Email** 字段来更改实例所有权。完成更改后，向下滚动并按 **Save**。
请注意，要使更改生效，新邮箱地址不能关联到任何其他 n8n 账号，因为每个实例只能有一个 **unique owner email**。如果目标邮箱已经关联到现有用户，请先更改或删除该用户，让该邮箱可用。

更改邮箱会同时更改实例所有者、你用于登录的邮箱，以及接收发票和一般沟通邮件的邮箱。

如果 workspace 已停用，将不会有 **Settings** 页面，也无法更改邮箱地址或所有者信息。

## 更改实例用户名 <a href="#change-instance-username" id="change-instance-username"></a>

目前无法更改用户名。

如果你希望实例使用不同名称，需要创建新账号并将工作迁移过去。[import/export documentation](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/export-and-import) 说明了如何将你的工作迁移到新的 n8n 实例。
