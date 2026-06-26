---
description: User management best practices。
contentType: explanation
nodeTitle: Follow best practices
originalFilePath: user-management/best-practices.md
originalUrl: 'https://docs.n8n.io/user-management/best-practices'
url: 'https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices'
layout:
  description:
    visible: false
---

# User management best practices <a href="#best-practices-for-user-management" id="best-practices-for-user-management"></a>

本页面包含与 n8n 中 user management 相关的 best practices 建议。

## 所有 platforms <a href="#all-platforms" id="all-platforms"></a>

* n8n 建议 owners 为自己创建一个 member-level account。Owners 可以查看所有 workflows，但没有办法查看某个特定 workflow 是谁创建的，因此如果你以 owner 身份构建和编辑 workflows，就有覆盖他人 work 的风险。
* Users 必须小心不要同时编辑同一个 workflow。虽然可以这样做，但 users 会互相覆盖 changes。
* 要在 accounts 之间移动 workflows，请将 workflow export 为 JSON，然后 import 到 new account。请注意，此操作会丢失 workflow history。
* Webhook paths 在整个 instance 中必须唯一。这意味着每个 webhook path 必须对所有 workflows 和所有 users 唯一。默认情况下，n8n 会为 webhook path 生成一个较长 random value，但 users 可以将其编辑为自己的 custom path。如果两个 users 设置相同 path value：
    * Path 会对第一个运行或 published 的 workflow 生效。
    * 其他 workflows 如果尝试使用相同 path 运行，将报错。

## Self-hosted <a href="#self-hosted" id="self-hosted"></a>

如果你在 reverse proxy 后运行 n8n，请设置以下 environment variables，以便 n8n 使用正确 URL 生成 emails：

* `N8N_HOST`
* `N8N_PORT`
* `N8N_PROTOCOL`
* `N8N_EDITOR_BASE_URL`

有关这些 variables 的更多信息，请参阅 [Environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables)。
