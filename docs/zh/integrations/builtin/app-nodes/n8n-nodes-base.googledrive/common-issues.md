---
title: Google Drive node common issues
description: >-
  n8n 中 Google Drive node 的常见问题和解决方案文档。包含问题详情和建议解决方式。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Drive node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues
layout:
  description:
    visible: false
---

# Google Drive node common issues <a href="#google-drive-node-common-issues" id="google-drive-node-common-issues"></a>

这里列出 [Google Drive node](README.md) 的一些常见错误和问题，以及解决或排查步骤。

## Google hasn't verified this app <a href="#google-hasnt-verified-this-app" id="google-hasnt-verified-this-app"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/uEYII1oKijzYurya61sf/" %}

## Google Cloud app becoming unauthorized <a href="#google-cloud-app-becoming-unauthorized" id="google-cloud-app-becoming-unauthorized"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/PlbR0ntmBBE0DgjKiavq/" %}

## Google Drive OAuth error <a href="#google-drive-oauth-error" id="google-drive-oauth-error"></a>

如果使用 OAuth 身份验证方法，你可能会看到一个错误，提示由于应用不符合 Google 对应用安全性的要求，无法登录。

此问题最常见的实际原因是 Google 的 OAuth 配置与 n8n 中的 URL 不匹配。为避免这个问题，请先查看 Google 错误消息中包含的所有链接，其中会包含实际发生的确切错误详情。

如果你是自托管 n8n，请检查用于构造外部 URL 的 n8n 配置项。确认 [`N8N_EDITOR_BASE_URL`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment) 和 [`WEBHOOK_URL`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) 环境变量使用完整限定域名。

## Get recent files from Google Drive <a href="#get-recent-files-from-google-drive" id="get-recent-files-from-google-drive"></a>

要从 Google Drive 获取最近的文件，需要按修改时间对文件排序。为此，你需要搜索已有文件并获取它们的修改时间。然后可以对文件排序，找出最近的文件，并使用另一个 Google Drive node 通过 ID 指向该文件。

流程如下：

1. 向画布添加一个 **Google Drive** node。
2. 选择 **File/Folder** resource 和 **Search** operation。
3. 启用 **Return All**，以便遍历所有文件进行排序。
4. 将 **What to Search** filter 设置为 **Files**。
5. 在 **Options** 中，将 **Fields** 设置为 **All**。
6. 将 **Sort** node 连接到 **Google Drive** node 的输出。
7. 选择 **Simple** 排序类型。
8. 在 **Fields To Sort By** 部分，将 `modifiedTime` 输入为 **Field Name**。
9. 选择 **Descending** 排序顺序。
10. 在 **Sort** node 的输出后添加一个 **Limit** node。
11. 将 **Max Items** 设置为 **1**，以保留最近的文件。
12. 将另一个 **Google Drive** node 连接到 **Limit** node 的输出。
13. 选择 **File** 作为 **Resource**，并选择你需要的 operation。
14. 在 **File** 选择项中，选择 **By ID**。
15. 选择 **Expression**，并输入 `{{ $json.id }}` 作为表达式。

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%22cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7%22%0A%20%20%7D%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22operation%22%3A%20%22download%22%2C%0A%20%20%20%20%20%20%20%20%22fileId%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22__rl%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%22value%22%3A%20%22%3D%7B%7B%20%24json.id%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22mode%22%3A%20%22id%22%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2245b53bcd-7dcf-4266-8b6e-bfc12008f9e2%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Google%20Drive1%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.googleDrive%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201500%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22ba223e7c-4fed-41dd-8c80-2e8fd742629f%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.manualTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20620%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22resource%22%3A%20%22fileFolder%22%2C%0A%20%20%20%20%20%20%20%20%22searchMethod%22%3A%20%22query%22%2C%0A%20%20%20%20%20%20%20%20%22returnAll%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%22filter%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22whatToSearch%22%3A%20%22files%22%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22fields%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%2A%22%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2242799909-16f3-4f0a-9ad9-4dd0375814a0%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Google%20Drive%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.googleDrive%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20840%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22sortFieldsUi%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22sortField%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22fieldName%22%3A%20%22modifiedTime%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22order%22%3A%20%22descending%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22bfb8baa6-1b8c-4540-9ad6-b5d7c3f7521b%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sort%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.sort%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201060%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%222883d39a-f7d9-4244-bf7d-b06878678ccc%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Limit%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.limit%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201280%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Google%20Drive%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Google%20Drive%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Sort%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Sort%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Limit%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Limit%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Google%20Drive1%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/get-most-recent-file.json" %}
