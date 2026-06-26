---
description: 保护、管理和运维你的 n8n instance。
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 管理

通过控制 access、保护 credentials、管理 changes 和 monitoring activity 来管理 n8n。

本 section 帮助你在 usage 增长时安全、可靠地运行 n8n。

{% hint style="info" %}
Enterprise teams 通常会在本 section 花更多时间。随着规模扩大，SSO、directory integration、change control 和 centralized logging 会变得更重要。这里覆盖的许多 features 在 Enterprise 之外也很有用，包括 user management 基础、credential security 和 operational monitoring。
{% endhint %}

### 典型 administration workflow

{% stepper %}
{% step %}
### 控制 access

决定谁可以 sign in、他们可以做什么，以及 work 如何组织。请从 [Manage users and access](manage-users-and-access/) 开始。
{% endstep %}

{% step %}
### 保护 secrets

安全地存储和分享 credentials。使用 [Manage credentials](manage-credentials/) 来减少 secret sprawl。
{% endstep %}

{% step %}
### 安全移动 changes

使用 Git-backed workflows 在 environments 之间 promote changes。请参阅 [Use source control and environments](use-source-control-and-environments/)。
{% endstep %}

{% step %}
### Monitor activity

跟踪 usage，并将 signals 发送到你的 logging tools。使用 [Observe and log](observe-and-log/) 提高 visibility。
{% endstep %}
{% endstepper %}
