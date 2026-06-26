---
title: Okta Workforce Identity SAML setup
description: 将 Okta Workforce Identity 与 n8n 搭配使用。
contentType: tutorial
nodeTitle: Set up Okta Workforce Identity SAML
originalFilePath: user-management/saml/okta.md
originalUrl: 'https://docs.n8n.io/user-management/saml/okta'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml
layout:
  description:
    visible: false
---

# Okta Workforce Identity SAML setup <a href="#okta-workforce-identity-saml-setup" id="okta-workforce-identity-saml-setup"></a>

使用 Okta 在 n8n 中设置 SAML SSO。

{% hint style="info" %}
**Workforce Identity 和 Customer Identity**

本指南覆盖 Workforce Identity setup。这是原始 Okta product。Customer Identity 是 Okta 对其收购的 Auth0 的命名。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

你需要一个 Okta Workforce Identity account，以及来自 n8n SAML settings 的 redirect URL 和 entity ID。

根据你的 Okta configuration，Okta Workforce 可能会对 users 强制执行 two factor authentication。

请先阅读 [Set up SAML](set-up-saml.md) guide。

## Setup <a href="#setup" id="setup"></a>

除以下说明外，[this PDF](n8n-saml-with-okta.pdf) 还提供了如何使用 Okta 在 n8n 中 setup SAML 的 visual step-by-step guide。

1. 在 Okta admin panel 中，选择 **Applications** > **Applications**。
1. 选择 **Create App Integration**。Okta 会打开 app creation modal。
1. 选择 **SAML 2.0**，然后选择 **Next**。
1. 在 **General Settings** tab 中，输入 `n8n` 作为 **App name**。
1. 选择 **Next**。
1. 在 **Configure SAML** tab 中，完成以下 **General** fields：
	* **Single sign-on URL**：来自 n8n 的 **Redirect URL**。
	* **Audience URI (SP Entity ID)**：来自 n8n 的 **Entity ID**。
	* **Default RelayState**：留空。
	* **Name ID format**：`EmailAddress`。
	* **Application username**：`Okta username`。
	* **Update application username on**：`Create and update`。
1. 创建 **Attribute Statements**：

	| **Name** | **Name format** | **Value** |
	| -------- | --------------- | --------- |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname` | URI Reference | user.firstName |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname` | URI Reference | user.lastName |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` | URI Reference | user.login |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | URI Reference | user.email |

1. 选择 **Next**。Okta 可能会提示你完成 marketing form，也可能直接带你进入 new n8n Okta app。
1. 将 n8n app 分配给 people：
	1. 在 Okta 中的 n8n app dashboard 上，选择 **Assignments**。
	1. 选择 **Assign** > **Assign to People**。Okta 会显示一个包含 available people 列表的 modal。
	1. 选择要添加 person 旁边的 **Assign**。Okta 会显示 prompt 确认 username。
	1. 保持 username 为 email address。选择 **Save and Go Back**。
	1. 选择 **Done**。
1. 获取 metadata XML：在 **Sign On** tab 上，复制 Metadata URL。打开它并复制 XML。将其粘贴到 n8n 中的 **Identity Provider Settings**。
1. 选择 **Save settings**。
1. 选择 **Test settings**。n8n 会打开 new tab。如果你当前未 logged in，Okta 会提示你 sign in。随后 n8n 会显示 success message，确认 Okta 返回的 attributes。

### Instance 和 project access provisioning <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持两种通过 SSO provision instance 和 project roles 的方式。请根据你希望 mapping logic 位于哪里来选择：

- **Map rules on your IdP**：在 Okta 中配置 n8n-specific attributes（`n8n_instance_role` 和 `n8n_projects`），n8n 直接从 SAML response 读取它们。步骤如下。
- **Map rules inside n8n**：从 Okta 以 SAML attribute 发送 group membership，并在 n8n 内定义 mapping expressions。除 group attribute 外，不需要在 Okta 中进行 n8n-specific configuration。请参阅主 SAML setup 页面中的 [Map rules inside n8n](set-up-saml.md#map-rules-inside-n8n)。

在 n8n 中，将 **Role assignment** 设置为 **Instance roles via SSO** 或 **Instance and project roles via SSO**，然后选择你偏好的 **Role mapping method**。

#### 在 IdP 上映射 rules <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

**添加所需 attributes**

1. 在 Okta admin panel 中，选择 **Applications** > **Applications**。
2. 前往 n8n application 的 configuration。
3. 在 **General** tab 上，点击 **SAML Settings** 旁的 **Edit**。
4. 在打开的页面中，继续到 step 2：**Configure SAML**。
5. 添加以下两个 **Attribute Statements**：

	| **Name** | **Name format** | **Value** |
	| -------- | --------------- | --------- |
	| n8n_instance_role | Basic | appuser.n8n_instance_role |
	| n8n_projects | Basic | appuser.n8n_projects |

6. 点击 **Next**。
7. 点击 **Finish**。

**更新 app profile**

1. 在 Okta admin panel 中，选择 **Directory** > **Profile Editor**。
2. 前往 n8n application 的 profile。
3. 点击 **Add Attribute**。
4. 添加 **n8n_instance_role** attribute：
	* **Data type**：string
	* **Display name**：n8n_instance_role
	* **Variable name**：n8n_instance_role
	* **Attribute type**：Group
4. 添加 **n8n_projects** attribute：
	* **Data type**：string array
	* **Display name**：n8n_projects
	* **Variable name**：n8n_projects
	* **Attribute type**：Group
	* **Group priority**：Combine values across groups

现在，当你前往 **Directory** > **Groups** 并编辑已分配的 n8n application 时，就可以配置 login via SAML 时发送到 n8n 的 **n8n_instance_role** 和 **n8n_projects**。
