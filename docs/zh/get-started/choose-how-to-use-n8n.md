---
description: >-
  在 n8n Cloud 服务和自托管选项之间做选择。了解许可证和 n8n 付费方案。
contentType: overview
nodeTitle: Choose how to use n8n
originalFilePath: choose-n8n.md
originalUrl: 'https://docs.n8n.io/choose-n8n'
url: 'https://docs.n8n.io/get-started/choose-how-to-use-n8n'
layout:
  description:
    visible: false
---

# 选择你的 n8n <a href="#choose-your-n8n" id="choose-your-n8n"></a>

n8n 提供两种主要部署选项：**n8n Cloud**（全托管）和**自托管**（部署在你自己的基础设施上）。

{% hint style="info" %}
**想快速试用 n8n？**

**从 n8n Cloud 开始**，无需安装即可立即使用。

[开始免费试用](https://n8n.io/cloud/){ .md-button .md-button--primary }
{% endhint %}

## 决策指南 <a href="#decision-guide" id="decision-guide"></a>

使用这份指南，为你的需求选择最合适的选项：

| 你的情况 | 推荐选项 | 原因 |
|----------------|-------------------|---------|
| 想快速开始 | **n8n Cloud** | 无需安装 |
| 没有技术经验 | **n8n Cloud** | 托管方案，无需自行配置 |
| 需要可用于生产环境的部署 | **两种选项都可以** | Cloud 和自托管都支持生产使用 |
| 有自定义使用场景 | **自托管** | 可完全控制部署和配置 |
| 想免费使用最多功能 | **自托管 Community Edition** | 免费，并包含几乎完整的功能集 |
| 想免费使用文件夹和调试功能 | **注册后的 Community Edition** | 免费注册即可解锁这些功能 |
| 需要企业功能（SSO、环境、项目等） | **Cloud 付费版或自托管 Enterprise** | 这些功能需要付费方案 |
| 拥有基础设施和技术资源 | **自托管** | 可以管理自己的部署 |

如需了解不同方案的具体功能可用性，请参阅[定价页面](https://n8n.io/pricing/)。

## 优缺点对比 <a href="#pros-and-cons-comparison" id="pros-and-cons-comparison"></a>

| 方面 | n8n Cloud | 自托管 |
|--------|-----------|-------------|
| **安装与部署** |
| 安装 | 优势：无需安装 | 劣势：需要配置（npm、Docker 或服务器） |
| 技术经验 | 优势：不需要 | 劣势：安装和配置需要技术经验 |
| **基础设施管理** |
| 托管 | 优势：由 n8n 全托管 | 劣势：必须自行提供并管理基础设施 |
| 维护 | 优势：由 n8n 处理 | 劣势：由你负责 |
| **控制与自定义** |
| 部署控制 | 劣势：由 n8n 管理 | 优势：完全控制部署 |
| 自定义 | 劣势：受可用选项限制 | 优势：推荐用于自定义使用场景 |
| **成本** |
| 免费选项 | 视情况：提供免费试用 | 优势：免费 Community Edition 包含大多数功能 |
| 付费选项 | 优势：有多种付费方案 | 优势：可选择付费 Enterprise 版本 |
| **功能** |
| 核心功能 | 优势：已包含 | 优势：免费 Community Edition 已包含 |
| 企业功能 | 劣势：需要付费方案 | 劣势：需要 Enterprise 许可证（免费 Community 版本有限） |
| **使用场景** |
| 快速开始 | 优势：非常适合入门 | 视情况：设置时间更长 |
| 生产使用 | 优势：支持 | 优势：推荐用于生产环境 |
| 自定义需求 | 视情况：自定义能力有限 | 优势：推荐用于自定义使用场景 |

**图例**：优势 | 劣势 | 视情况/取决于需求

如需了解不同方案的具体功能可用性，请参阅[定价页面](https://n8n.io/pricing/)。

## 开始使用 <a href="#getting-started" id="getting-started"></a>

准备开始了吗？请选择你的部署方式：

- **[开始使用 n8n Cloud](https://n8n.io/cloud/)** - 注册后即可立即使用
- **[开始使用自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)** - 安装和部署指南

要注册 Community Edition 实例并获得额外功能，请前往 **Settings > Usage and plan**，然后选择 **Unlock**。

## 功能对比 <a href="#feature-comparison" id="feature-comparison"></a>

### 自托管 Community Edition <a href="#self-hosted-community-edition" id="self-hosted-community-edition"></a>

n8n 的 Community Edition 是免费的自托管 n8n 版本，你可以在自己的基础设施上运行。

| 功能 | Community Edition 中不可用 | 可用版本 |
|-----------------|-----------------------------------|--------------|
| **变量与配置** | 自定义变量 | Enterprise 版本，部分 Cloud 付费方案 |
| **环境** | 环境 | Enterprise 版本，部分 Cloud 付费方案 |
| **密钥管理** | 外部密钥 | Enterprise 版本，部分 Cloud 付费方案 |
| **存储** | 二进制数据外部存储 | Enterprise 版本 |
| **日志** | 日志流式传输（标准日志已包含） | Enterprise 版本 |
| **扩展** | 多主模式（队列模式已包含） | Enterprise 版本 |
| **组织管理** | 项目 | Enterprise 版本，部分 Cloud 付费方案 |
| **身份验证** | SSO（SAML、LDAP） | Enterprise 版本 |
| **协作** | 工作流和凭据共享** | Enterprise 版本，部分 Cloud 付费方案 |
| **版本控制** | 使用 Git 进行版本控制 | Enterprise 版本，部分 Cloud 付费方案 |

在 Community Edition 中，只有实例所有者，以及创建工作流或凭据的用户，才能访问这些工作流或凭据。

### 自托管注册版 Community Edition（免费） <a href="#self-hosted-registered-community-edition-free" id="self-hosted-registered-community-edition-free"></a>

使用邮箱注册 Community Edition 后，可以解锁以下额外功能：

| 功能 | 描述 |
|---------|-------------|
| 文件夹 | 将工作流整理到文件夹中 |
| 编辑器内调试 | 处理工作流时复制并固定执行数据 |
| 自定义执行数据 | 保存、查找并标注执行元数据 |

### n8n Cloud 与自托管 Enterprise <a href="#n8n-cloud-vs-self-hosted-enterprise" id="n8n-cloud-vs-self-hosted-enterprise"></a>

n8n Cloud（Enterprise 方案）和自托管 Enterprise 版本都包含上方列出的、Community Edition 缺失的全部功能。

如需了解 Cloud Starter、Pro 和 Business 自托管方案中具体可用的功能，请参阅[定价页面](https://n8n.io/pricing/)。
