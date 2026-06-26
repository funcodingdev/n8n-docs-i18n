---
title: Azure AD SAML setup
description: 将 Azure AD 与 n8n 搭配使用。
contentType: tutorial
nodeTitle: Set up Azure AD SAML
originalFilePath: user-management/saml/azuread.md
originalUrl: 'https://docs.n8n.io/user-management/saml/azuread'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml
layout:
  description:
    visible: false
---

# Azure AD SAML setup <a href="#azure-ad-saml-setup" id="azure-ad-saml-setup"></a>

本文档说明如何配置 Azure AD，通过 SAML attributes 向 n8n 发送 role information。这会根据 Azure AD group membership 启用 automatic role assignment。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

你需要一个可 access Enterprise Applications 的 Azure AD account，以及来自 n8n SAML settings 的 redirect URL 和 entity ID。

请先阅读 [Set up SAML](set-up-saml.md) guide。

## n8n 需要什么 <a href="#what-n8n-requires" id="what-n8n-requires"></a>

n8n 期望 SAML assertion 中包含一个 custom SAML attribute：

| **Attribute Name** | **Data Type** | **Purpose** |
| ------------------- | ------------- | ----------- |
| n8n_instance_role | String | 控制 user 在 n8n 中的 global role |

`n8n_instance_role` 的 valid values：

| **Value** | **Description** |
| --------- | --------------- |
| `global:owner` | 完整 instance owner access |
| `global:admin` | Administrator access |
| `global:member` | 常规 member access（未指定时默认） |
| `global:chatUser` | n8n 中受限的 non-technical role，用于通过 Chat Hub interface 安全地与 AI agents 交互 |

## Setup <a href="#setup" id="setup"></a>

**Step 1：配置 Standard SAML Attributes**

1. 在 Azure AD portal 中，导航到你的 n8n Enterprise Application。
2. 前往 **Single sign-on** > **Attributes & Claims**。
3. 确保已配置这些 standard attributes：

	| **Claim Name** | **Source Attribute** |
	| -------------- | ------------------- |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | user.mail |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname` | user.givenname |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname` | user.surname |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` | user.userprincipalname |

**Step 2：添加 n8n_instance_role Claim**

此 claim 使用 conditional logic，根据 Azure AD group membership 发送不同 role values。

1. 在 **Attributes & Claims** 中，点击 **Add new claim**。
2. 配置 basic settings：
	* **Name**：`n8n_instance_role`
	* **Namespace**：留空
	* **Source**：`Attribute`
3. 展开 **Claim conditions**，并点击 **Add condition**。
4. 为每个 Azure AD group 添加 conditions（按 priority order）：

	| **User Type** | **Scoped Groups** | **Source** | **Value** |
	| ------------- | ----------------- | ---------- | --------- |
	| Members | n8n-chatusers | Attribute | `global:chatUser` |
	| Members | n8n-users | Attribute | `global:member` |
	| Members | n8n-admins | Attribute | `global:admin` |
	| Members | n8n-owners | Attribute | `global:owner` |

{% hint style="info" %}
**Condition order**

Conditions 会按顺序 evaluate。将权限最高的 group（owners）放在最后。
{% endhint %}

5. 点击 **Save**。

### 测试配置 <a href="#testing-the-configuration" id="testing-the-configuration"></a>

1. 在 n8n 中，前往 **Settings** > **SSO**。
1. 将 **Role assignment** 设置为 **Instance roles via SSO**。
1. 将 **Role mapping method** 设置为 **Map rules on your IdP**。
1. 点击 **Test settings**。
1. 验证 SAML response 显示正确的 `n8n_instance_role` value。

### 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

**Claim 未出现在 SAML response 中**

* 验证 user 至少是一个 configured groups 的 member。
* 检查 groups 是否已分配给 Enterprise Application。
* 确保 conditions 使用 `Attribute` 作为 source。
* 使用 'SAML Chrome Panel' 等 browser extension plugin 查看 application SAML response。

**User 获得了错误 role**

* 检查 condition order（权限最高的 group 应该在最后）。

## 使用 app roles 而不是 group-based claims 分配多个 project roles <a href="#assigning-multiple-project-roles-using-app-roles-instead-of-group-based-claims" id="assigning-multiple-project-roles-using-app-roles-instead-of-group-based-claims"></a>

使用 Azure AD group-based claim conditions 为 users 分配多个 project roles 时，通常只会在 SAML assertion 中发送第一个 matching group claim。这意味着 users 虽然属于多个 groups，却可能只看到一个 project 的 access。

要可靠地分配多个 projects 及其各自 roles，请使用 App Registration 中定义的 **App Roles**，而不是 group-based claims：

1. 在 n8n SAML app 的 **App Registration** 中，定义代表每个 project 和 permission combination 的 App Roles（例如 `<projectId>:<role>`）。
2. 保存更新后的 App Manifest。
3. 在 **Enterprise Application** 中，在 **Users and groups** 下将 users 或 groups 分配到这些 App Roles。
4. 在 **Single sign-on > Attributes & Claims** 中更新 `n8n_projects` SAML claim，让它 source from `user.assignedroles`。这会在 SAML response 中以 array 形式发出所有 assigned roles。

此 setup 可确保 n8n 正确接收所有 project assignments，从而在多个 projects 中启用合适 access。虽然定义 App Roles 会增加初始 administrative overhead，但它简化了后续 user-role management，并保证完整的 project role sync。

从 group-based claims 迁移到 App Roles 时，请相应调整 role definitions 和 claims mapping，避免 project access 不完整。

## References <a href="#references" id="references"></a>

* [n8n SAML Setup](https://docs.n8n.io/user-management/saml/setup/)
* [n8n Okta Guide (reference)](https://docs.n8n.io/user-management/saml/okta/)
* [Azure AD Claims Customization](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization)
