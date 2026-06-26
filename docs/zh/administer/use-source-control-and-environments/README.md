---
title: Source control and environments
description: n8n 中 source control 和 environments 概览
contentType: overview
hide:
  - toc
nodeTitle: Use source control and environments
originalFilePath: source-control-environments/index.md
originalUrl: 'https://docs.n8n.io/source-control-environments'
url: 'https://docs.n8n.io/administer/'
layout:
  description:
    visible: false
---

# Source control and environments <a href="#source-control-and-environments" id="source-control-and-environments"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/2T2SmMUgiLyck7FDDwRD/" %}

n8n 使用 Git-based source control 来支持 environments。将 n8n instances 连接到 Git repository 后，你可以创建多个由 Git branches 支持的 n8n environments。

本 section 包括：

* [Understand](understand-source-control.md)：
	* [Environments in n8n](work-with-environments.md)：environments 的目的，以及它们在 n8n 中如何工作。
	* [Git and n8n](use-git-in-n8n.md)：n8n 如何使用 Git。
	* [Branch patterns](choose-branching-patterns.md)：n8n instances 和 Git branches 之间可能的关系。
* [Set up source control for environments](set-up-source-control.md)：如何将 n8n instance 连接到 Git。
* [Using](/source-control-environments/using/index.md)：
	* [Push and pull](push-and-pull-changes.md)：将 work 发送到 Git，并从 Git fetch work 到你的 instance。
	* [Copy work between environments](move-work-between-environments.md)：如何在不同 n8n instances 之间复制 work。
* [Tutorial: Create environments with source control](tutorial-create-environments-with-source-control.md)：端到端 tutorial，使用 n8n 推荐的 configurations 设置 environments。

相关 sections：

* [Variables](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/define-custom-variables)：可复用 values。
* [External secrets](../manage-credentials/use-external-secret-stores.md)：使用 external secrets vault 管理 credentials[^1]。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。
