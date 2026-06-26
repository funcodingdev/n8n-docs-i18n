---
title: Set up source control
description: 将 n8n 连接到你的 Git provider。
contentType: howto
nodeTitle: Set up source control
originalFilePath: source-control-environments/setup.md
originalUrl: 'https://docs.n8n.io/source-control-environments/setup'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control
layout:
  description:
    visible: false
---

# 为 environments 设置 source control <a href="#set-up-source-control-for-environments" id="set-up-source-control-for-environments"></a>

将 Git repository 链接到 n8n instance，并配置 source control。

n8n 使用 source control 提供 environments。更多信息请参考 [Environments in n8n](work-with-environments.md)。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

要在 n8n 中使用 source control，你需要一个 Git repository，并具备以下任一访问方式：

- SSH access（使用 deploy keys），或
- HTTPS access（使用 Personal Access Tokens）

本文档假设你熟悉 Git 和你的 Git provider。

## Step 1：设置 repository 和 branches <a href="#step-1-set-up-your-repository-and-branches" id="step-1-set-up-your-repository-and-branches"></a>

对于 new setup：

1. 创建一个供 n8n 使用的 new repository。
1. 创建所需 branches。例如，如果你计划为 test 和 production 使用不同 environments，请为每个 environment 设置一个 branch。

要帮助决定 use case 需要哪些 branches，请参考 [Branch patterns](choose-branching-patterns.md)。

## Step 2：在 n8n 中配置 Git <a href="#step-2-configure-git-in-n8n" id="step-2-configure-git-in-n8n"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/UqTgO2VbAzax4T8z4Fyh/" %}

## Step 3：设置 authentication <a href="#step-3-set-up-authentication" id="step-3-set-up-authentication"></a>

根据你选择的 connection method 配置 authentication。

### SSH authentication（使用 deploy keys） <a href="#ssh-authentication-using-deploy-keys" id="ssh-authentication-using-deploy-keys"></a>

使用 n8n 中的 SSH key 为 repository 创建 deploy key，以设置 SSH access。该 key 必须具有 write access。

具体步骤取决于你的 Git provider。常见 providers 的帮助 links：

* [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
* [GitLab | Deploy keys](https://docs.gitlab.com/ee/user/project/deploy_keys/)

### HTTPS authentication（使用 Personal Access Tokens） <a href="#https-authentication-using-personal-access-tokens" id="https-authentication-using-personal-access-tokens"></a>

创建具有 repository access permissions 的 Personal Access Token (PAT)。

使用常见 providers 创建 PATs 的帮助 links：

* [GitHub | Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
* [GitLab | Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
* [Bitbucket | App passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)

Token 所需 permissions：

- Repository read/write access
- Contents read/write（GitHub）
- Source code pull/push（GitLab）

## Step 4：连接 n8n 并配置 instance <a href="#step-4-connect-n8n-and-configure-your-instance" id="step-4-connect-n8n-and-configure-your-instance"></a>

1. 在 n8n 的 **Settings** > **Environments** 中，选择 **Connect**。n8n 会连接到你的 Git repository。
1. 在 **Instance settings** 下，选择当前 n8n instance 要使用的 branch。
1. **Optional**：选择 **Protected instance**，防止 users 在此 instance 中编辑 source-controlled resources。这对于保护 production instances 很有用。
1. **Optional**：为 instance 选择 custom color。它会显示在 source control push 和 pull buttons 旁边的 menu 中，帮助 users 识别当前所在 instance。
1. 选择 **Save settings**。
