---
title: Set up SAML
description: 使用 n8n SAML SSO 的通用设置说明。
contentType: howto
nodeTitle: Set up SAML
originalFilePath: user-management/saml/setup.md
originalUrl: 'https://docs.n8n.io/user-management/saml/setup'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml
layout:
  description:
    visible: false
---

# Set up SAML <a href="#set-up-saml" id="set-up-saml"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/9DXSTQsxYGisAV8xk6p4/" %}

{% hint style="info" %}
**使用 environment variables 配置**

你也可以使用 environment variables 配置 SAML，而不是通过 UI 配置。此方式从 n8n v2.18.0 起可用。请参阅 [SSO environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso)。
{% endhint %}

## 启用 SAML <a href="#enable-saml" id="enable-saml"></a>

1. 在 n8n 中，前往 **Settings** > **SSO**。
1. 记录 n8n **Redirect URL** 和 **Entity ID**。
	* **Optional**：如果你的 IdP 允许从 imported metadata 设置 SAML，请打开 **Entity ID** URL 并保存 XML。
	* **Optional**：如果你在 load balancer 后运行 n8n，请确保已配置 `N8N_EDITOR_BASE_URL`。
1. 使用你的 identity provider (IdP) 设置 SAML。你需要 **Redirect URL** 和 **Entity ID**。你可能还需要 IdP user 的 email address 和 name。
1. 在 IdP 中完成 setup 后，将 metadata XML 加载到 n8n。你可以使用 metadata URL 或 raw XML：
	* **Metadata URL**：从 IdP 复制 metadata URL 到 n8n 的 **Identity Provider Settings** field。
	* **Raw XML**：从 IdP 下载 metadata XML，将 **Identiy Provider Settings** toggle 到 **XML**，然后将 raw XML 复制到 **Identity Provider Settings**。
1. 选择 **Save settings**。
1. 选择 **Test settings** 检查 SAML setup 是否正常工作。
1. 将 SAML 2.0 设置为 **Activated**。

{% hint style="info" %}
**SAML Request Type**

n8n 不支持 `POST` binding。请将 IdP 配置为使用 `HTTP` request binding。
{% endhint %}

## 通用 IdP setup <a href="#generic-idp-setup" id="generic-idp-setup"></a>

配置 IdP 的步骤会因你选择的 IdP 而异。以下是一些常见 setup tasks：

* 在 IdP 中为 n8n 创建 app。
* 将 n8n attributes 映射到 IdP attributes：

| Value (IdP side) | Name format | Name |
| ---------------- | ----------- | ---- |
| User email       | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| User First Name  | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname`    |
| User Last Name   | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname`     |
| User Email       | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn`          |

### Instance 和 project access provisioning <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持通过 SSO provision instance role 和 project roles。当 user 通过 SAML sign in 时，n8n 可以基于 SAML response 中的 attributes 自动分配其 instance role 和 project access。

Role provisioning 在 version `1.122.2` 中引入。

#### 选择 roles 如何分配 <a href="#choose-how-roles-are-assigned" id="choose-how-roles-are-assigned"></a>

在 n8n 中，前往 **Settings** > **SSO**。使用 **Role assignment** dropdown 选择 n8n 如何为通过 SSO sign in 的 users 分配 roles。默认值为 **Assigned manually in n8n**。

选项包括：

- **Assigned manually in n8n**：admins 直接在 n8n 中分配每个 role。不会从 IdP 自动 mapping。
- **Instance roles via SSO**：n8n 在 login 时从 IdP 读取 user 的 instance role。Project access 仍在 n8n 中手动管理。
- **Instance and project roles via SSO**：n8n 在 login 时同时从 IdP 读取 instance role 和 project access。

Roles 会在每次 login 时重新 evaluate，因此 IdP 中的 changes 会在 user 下次 sign-in 时生效。

{% hint style="warning" %}
**Existing access 会被覆盖**

启用任一 SSO provisioning mode 后，任何在 n8n 内授予、但未反映在 IdP response 中的 access，会在 users 下次 login 时被移除。

保存此更改前，n8n 会要求你下载两个包含当前 access settings 的 CSV files。请保留它们以供参考。
{% endhint %}

#### 选择 role mapping method <a href="#choose-a-role-mapping-method" id="choose-a-role-mapping-method"></a>

当 **Role assignment** 设置为 **Instance roles via SSO** 或 **Instance and project roles via SSO** 时，会出现 **Role mapping method** dropdown。你可以选择：

- **Map rules on your IdP**：n8n 直接从 SAML response 读取 n8n-specific attributes（`n8n_instance_role` 和 `n8n_projects`）。你的 IdP admin 配置每个 user 或 group 应获得哪个 n8n role 或 project。
- **Map rules inside n8n**：你在 n8n 中定义 expressions，evaluate user 的 SAML attributes 并返回 role。当你的 IdP 无法 encode n8n-specific role logic，或者 IT governance 导致 IdP-side changes 缓慢时，可使用此方式。

#### 在 IdP 上映射 rules <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

在你的 IdP 中为 groups 或 individual users 配置这些 attributes：

| Value (IdP side) | Data type | Name |
| ---------------- | ----------- | ---- |
| `n8n_instance_role` | string | `n8n_instance_role` |
| `n8n_projects` | array | `n8n_projects` |

**配置 `n8n_instance_role` attribute**

`n8n_instance_role` 是在你的 IdP 上为 group 或 user 配置的 string。如果未设置值，n8n 会 fallback 到 `global:member`。

Supported instance roles：

- `global:member`
- `global:admin`
- `global:chatUser`

**配置 `n8n_projects` attribute**

`n8n_projects` 是在你的 IdP 上为 group 或 user 配置的 string array。每个 element 必须遵循 `<project-id>:<role>` format。

例如：

- `bHsykgeFirmIhezz:viewer`
- `4K3zrg3DvlMFFTB7:editor`
- `dCjnYuEpYOUBVaNe:admin`

对于启用 project provisioning 时已有的 access，请在下载的 CSV file 中查找 project IDs。

对于 new projects，请在 browser 中查看 project 时从 URL 获取 project ID。在 URL `<your-domain>/projects/VVRWZaq5DRxaf9O1/workflows` 中，project ID 是 `VVRWZaq5DRxaf9O1`。

#### 在 n8n 内映射 rules <a href="#map-rules-inside-n8n" id="map-rules-inside-n8n"></a>

**Map rules inside n8n** 从 version `2.19.0` 起可用。

使用此选项可以在 n8n 内定义 group-to-role mappings，而不是在 IdP 中定义。每条 rule 都是一个 expression，n8n 会用 IdP response 中的 SAML attributes evaluate 它。

**Expressions 如何工作**

- Expressions 通过 `$claims` object access IdP response 中的所有 SAML attributes。
- 如果 expression 返回 `true`，n8n 会分配你在该 rule 上选择的 role。
- Rules 按从上到下顺序 evaluate。第一个 matching rule 生效。
- Rules 会在每次 login 时重新 evaluate，因此 role changes 会在 user 下次 session 生效。
- `$claims` 暴露 raw SAML attributes。n8n 不会 normalise 它们，因此请根据 IdP 实际发送的 structure 编写 expressions。SAML group membership 通常以 multi-value attribute 发送，但确切 shape 取决于你的 IdP。

{% hint style="info" %}
**检查你的 SAML response structure**

不同 IdPs 会以不同方式 serialise groups 和其他 attributes。编写 rules 前，请使用 SAML Chrome Panel 等 browser tool（或你的 IdP test tools）inspect SAML response，确认 attribute names 和 structure。
{% endhint %}

**Instance role rules**

在 **Instance role rules** 下，选择 **Add rule** 创建 rule。输入 condition expression，并选择当 condition 返回 `true` 时要分配的 instance role。

例如，要将 **Admin** role 分配给 IdP `admin` group 中的任何 user：

```
{{ $claims.groups.includes('admin') }}
```

**Default condition** row 设置当没有 rule match 时 users 接收的 role。默认是 **Member**。

**Project role rules**

在 **Project role rules** 下，选择 **Add rule** 创建 rule，在一个或多个 projects 中分配 project role。

例如，要给 `operations` group 中的 users 在 **Operations** project 中授予 **Project Editor** role，请将 expression 设置为：

```
{{ $claims.groups.includes('operations') }}
```

在 **assign** field 中选择 role，并在 **in** field 中选择 target projects。不匹配任何 project rule 的 users 不会获得 project access。

{% hint style="warning" %}
**Manual role management 已禁用**

当 **Map rules inside n8n** 处于 active 状态时，手动分配 user roles 的 UI controls 会被禁用。所有 role assignment 都通过 mapping rules 完成。
{% endhint %}

{% hint style="warning" %}
**切换 mapping methods**

从 **Map rules inside n8n** 切换回 **Map rules on your IdP** 会移除所有 in-n8n mappings。如果 IdP 中没有设置 equivalent mappings，users 可能会在下次 login 时失去当前分配的 roles。n8n 会在应用此更改前要求你确认。
{% endhint %}

## 常见 IdPs 的 setup resources <a href="#setup-resources-for-common-idps" id="setup-resources-for-common-idps"></a>

常见 IdPs 的 documentation links。

| IdP | Documentation |
| --- | ------------- |
| Auth0 | [Configure Auth0 as SAML Identity Provider: Manually configure SSO integrations](https://auth0.com/docs/authenticate/protocols/saml/saml-sso-integrations/configure-auth0-saml-identity-provider#manually-configure-sso-integrations) |
| Authentik | [Applications](https://goauthentik.io/docs/applications) 和 [SAML Provider](https://docs.goauthentik.io/add-secure-apps/providers/saml/) |
| Azure AD | [SAML authentication with Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/auth-saml) |
| JumpCloud | [How to setup SAML (SSO) applications with JumpCloud](https://jumpcloud.com/support/integrate-with-zoom#configuring-the-sso-integration)（使用 `Zoom` 作为 example） |
| Keycloak | 根据你的 hosting 选择一个 [Getting Started](https://www.keycloak.org/guides#getting-started) guide。 |
| Okta | n8n 提供 [Workforce Identity setup guide](set-up-okta-workforce-identity-saml.md) 和 [step-by-step PDF guide](n8n-saml-with-okta.pdf) |
| PingIdentity | [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html) |
