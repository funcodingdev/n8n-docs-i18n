---
title: Environments in n8n
description: 了解 n8n 中 environments 背后的概念。
contentType: explanation
nodeTitle: Work with environments
originalFilePath: source-control-environments/understand/environments.md
originalUrl: 'https://docs.n8n.io/source-control-environments/understand/environments'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments
layout:
  description:
    visible: false
---

# n8n 中的 Environments <a href="#environments-in-n8n" id="environments-in-n8n"></a>

n8n 将 environments feature 构建在 Git 这一 version control software 之上。本文档帮助你了解：

* Environments 的目的。
* Environments 在 n8n 中如何工作。

## Environments：是什么以及为什么需要 <a href="#environments-what-and-why" id="environments-what-and-why"></a>

在 software development 中，environment 是 code 周围的所有 infrastructure 和 tooling，包括运行 software 的 tools，以及这些 tools 的具体 configuration。有关 software development 中 environments 的更详细介绍，请参考 [Codecademy | Environments](https://www.codecademy.com/article/environments)。

n8n 中的 low-code development 与之类似。n8n 是你构建和运行 workflows 的地方。你的 instance 可能有特定 configurations：在 Cloud 上，n8n 决定 configuration；在 self-hosted instances 上，有大量 [configuration options](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration)。你可能还更改过 instance settings。n8n 与你的 instance 特定 configuration 和 settings 的组合，就是 workflows 运行所在的 environment。

拥有多个 environment 有很多优势。常见 pattern 是为 development 和 production 使用不同 environments：

* Development：执行 work 并进行 changes。
* Production：live environment。

这样的 setup 可帮助你更改 workflows，而不破坏正在使用的 workflows。

## n8n 中的 environments <a href="#environments-in-n8n" id="environments-in-n8n"></a>

在 n8n 中，一个 environment 由两部分组成：n8n instance 和 Git branch：

* n8n instance 是你构建和运行 workflows 的地方。
* Git branch 存储 workflows 的 copies，以及 tags、variable 和 credential stubs。

n8n 不会将 credentials 和 variable values 与 Git sync。设置 new instance 时，你必须手动设置 credentials 和 variable values。更多信息请参考 [Push and pull | What gets committed](push-and-pull-changes.md#what-gets-committed)。

如何在 environments 之间复制 work，取决于 branch 和 n8n instance configuration：

* 多个 instances，一个 branch：你可以从一个 instance push 到 Git branch，然后将 work pull 到另一个 instance。
* 多个 instances，多个 branches：你需要在 Git provider 中创建 pull request 并 merge。例如，如果你有 development、test 和 production branches，且每个 branch 都链接到自己的 instance，则需要将 development branch merge 到 test，才能让 development instance 的 work 可用于 test instance。更多信息（包括部分自动化此 process 的步骤）请参考 [Copy work between environments](move-work-between-environments.md)。

有关 push 和 pull work 的详细 guidance，请参考 [Push and pull](push-and-pull-changes.md)。

要了解如何将 n8n instance 链接到 Git，请参考 [Set up source control](set-up-source-control.md)，或按照 [Tutorial: Create environments with source control](tutorial-create-environments-with-source-control.md) 使用 n8n 推荐 configurations 设置 environments。
