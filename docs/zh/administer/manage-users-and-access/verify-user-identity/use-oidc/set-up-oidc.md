---
title: Set up OIDC
description: 启用 n8n OIDC SSO 的设置说明。
contentType: howto
nodeTitle: Set up OIDC
originalFilePath: user-management/oidc/setup.md
originalUrl: 'https://docs.n8n.io/user-management/oidc/setup'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc
layout:
  description:
    visible: false
---

# Set up OIDC <a href="#set-up-oidc" id="set-up-oidc"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/3sB2Mxc1yXYEg1FeAYjK/" %}

{% hint style="info" %}
**使用 environment variables 配置**

你也可以使用 environment variables 配置 OIDC，而不是通过 UI 配置。此方式从 n8n v2.18.0 起可用。请参阅 [SSO environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso)。
{% endhint %}

## 设置并启用 OIDC <a href="#setting-up-and-enabling-oidc" id="setting-up-and-enabling-oidc"></a>

1. 在 n8n 中，前往 **Settings** > **SSO**。
1. 在 **Select Authentication Protocol** 下，从 dropdown 中选择 **OIDC**。
1. 复制显示的 **redirect URL**（例如 `https://yourworkspace.app.n8n.cloud/rest/sso/oidc/callback`）。<br>

	<div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Load balancers 或 proxies 的额外配置</strong></p><p>如果你在 load balancer 后运行 n8n，请确保设置 <a href="https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment"><code>N8N_EDITOR_BASE_URL</code> environment variable</a>。</p></div>

1. 使用你的 identity provider (IdP) 设置 OIDC。你需要：
	- 在 IdP 中创建 new OIDC client/application。
	- 配置上一步中的 redirect URL。
	- 记录 IdP 提供的 **Client ID** 和 **Client Secret**。
1. 在 IdP 中找到 **Discovery Endpoint**（也称为 well-known configuration endpoint）。它通常采用以下 format：
	```
	https://your-idp-domain/.well-known/openid-configuration
	```
1. 在 n8n 中完成 OIDC 配置：
	- **Discovery Endpoint**：输入 IdP 的 discovery endpoint URL。
	- **Client ID**：输入在 IdP 中注册 application 时获得的 client ID。
	- **Client Secret**：输入在 IdP 中注册 application 时获得的 client secret。
1. 选择 **Save settings**。
1. 将 OIDC 设置为 **Activated**。

### Instance 和 project access provisioning <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持通过 SSO provision instance role 和 project roles。当 user 通过 OIDC sign in 时，n8n 可以基于 IdP response 中的 claims 自动分配其 instance role 和 project access。

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

- **Map rules on your IdP**：n8n 直接从 IdP response 读取 n8n-specific claims（`n8n_instance_role` 和 `n8n_projects`）。你的 IdP admin 配置每个 user 或 group 应获得哪个 n8n role 或 project。
- **Map rules inside n8n**：你在 n8n 中定义 expressions，evaluate user 的 OIDC claims 并返回 role。当你的 IdP 无法 encode n8n-specific role logic，或者 IT governance 导致 IdP-side changes 缓慢时，可使用此方式。

#### 在 IdP 上映射 rules <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

在你的 OIDC authorization server 中添加名为 `n8n` 的 additional scope，并包含以下两个 claims：

| **Name** | **Data type** | **Scope** | **Token type** |
| -------- | ------------- | --------- | -------------- |
| `n8n_instance_role` | string | `n8n` | ID |
| `n8n_projects` | string array | `n8n` | ID |

这两个 claims 必须始终包含在 authorization server 的 ID Token 中。请在 IdP 中有权 access n8n 的 user groups 上配置它们。

**配置 `n8n_instance_role` claim**

`n8n_instance_role` 是在你的 IdP 上为 group 或 user 配置的 string。如果未设置值，n8n 会 fallback 到 `global:member`。

Supported instance roles：

- `global:member`
- `global:admin`
- `global:chatUser`

**配置 `n8n_projects` claim**

`n8n_projects` 是在你的 IdP 上为 group 或 user 配置的 string array。每个 element 必须遵循 `<project-id>:<role>` format。

例如：

- `bHsykgeFirmIhezz:viewer`
- `4K3zrg3DvlMFFTB7:editor`
- `dCjnYuEpYOUBVaNe:admin`

对于启用 project provisioning 时已有的 access，请在下载的 CSV file 中查找 project IDs。

对于 new projects，请在 browser 中查看 project 时从 URL 获取 project ID。在 URL `<your-domain>/projects/VVRWZaq5DRxaf9O1/workflows` 中，project ID 是 `VVRWZaq5DRxaf9O1`。

#### 在 n8n 内映射 rules <a href="#map-rules-inside-n8n" id="map-rules-inside-n8n"></a>

**Map rules inside n8n** 从 version `2.19.0` 起可用。

使用此选项可以在 n8n 内定义 group-to-role mappings，而不是在 IdP 中定义。每条 rule 都是一个 expression，n8n 会用 IdP response 中的 OIDC claims evaluate 它。

**Expressions 如何工作**

- Expressions 通过 `$claims` object access IdP response 中的所有 OIDC claims。
- 如果 expression 返回 `true`，n8n 会分配你在该 rule 上选择的 role。
- Rules 按从上到下顺序 evaluate。第一个 matching rule 生效。
- Rules 会在每次 login 时重新 evaluate，因此 role changes 会在 user 下次 session 生效。
- `$claims` 暴露 raw IdP response。n8n 不会 normalise 它，因此请根据 IdP 实际发送的 structure 编写 expressions。

{% hint style="info" %}
**从 IdP 发送 groups claim**

大多数 group-based rules 需要 OIDC response 中包含 `groups` claim。此 claim 默认不包含，你需要配置 IdP 发送它。例如，在 Okta 中添加 `groups` scope，或在 Azure AD token configuration 中配置 `groups` claim。编写 rules 前，请 inspect IdP response，确认确切 claim name 和 structure。
{% endhint %}

**Example userinfo response**

Authentication 后，n8n 会调用 IdP 的 userinfo endpoint 来获取 user claims。典型 response 如下：

```json
{
  "sub": "00uwyqw9raWrKRJ0Q697",
  "name": "Jane Doe",
  "email": "jane.doe@example.com",
  "email_verified": true,
  "given_name": "Jane",
  "family_name": "Doe",
  "groups": [
    "Everyone",
    "n8n admins",
    "n8n members",
    "Operations"
  ]
}
```

`$claims` 会反映此 payload。因此 `$claims.email` 是 string，`$claims.groups` 是 strings array，你可以对它们使用 standard JavaScript methods。确切 group names 取决于你的 IdP。某些 providers（例如 Azure AD）发送 group UUIDs，而不是 display names，在这种情况下，你的 expressions 需要引用 UUID。

要在 Okta 中 inspect 自己的 userinfo response，请使用 valid access token 直接调用 userinfo endpoint。你可以从 **Security** > **API** > **Authorization Servers** > your server > **Token Preview** tab 获取 test access token，然后运行：

```
curl -H "Authorization: Bearer <access-token>" https://<your-okta-domain>/oauth2/<auth-server-id>/v1/userinfo
```

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

## Provider-specific OIDC setup <a href="#provider-specific-oidc-setup" id="provider-specific-oidc-setup"></a>

### Okta <a href="#okta" id="okta"></a>

在 Okta 中 setup OIDC 的步骤与下面描述的 Auth0 类似。

对于 Okta，你可以下载 PDF 形式的 visual step-by-step guide：

[n8n-oidc-with-okta.pdf](n8n-oidc-with-okta.pdf)

### Auth0 <a href="#auth0" id="auth0"></a>

1. **在 Auth0 中创建 application**：
	- 登录你的 Auth0 Dashboard。
	- 前往 **Applications** > **Applications**。
	- 点击 **Create Application**。
	- 输入 name（例如 "n8n SSO"），并选择 **Regular Web Applications**。
	- 点击 **Create**。
1. **配置 application**：
	- 前往 new application 的 **Settings** tab。
	- **Allowed Callback URLs**：添加来自 **Settings** > **SSO** > **OIDC** 的 n8n redirect URL。
	- **Allowed Web Origins**：添加 n8n base URL（例如 `https://yourworkspace.app.n8n.cloud`）。
	- 点击 **Save Changes**。
1. **获取 credentials**：
	- **Client ID**：可在 **Settings** tab 中找到。
	- **Client Secret**：可在 **Settings** tab 中找到。
	- **Discovery Endpoint**：`https://{your-auth0-domain}.auth0.com/.well-known/openid-configuration`。
1. **在 n8n 中完成 OIDC 配置：**
	- **Discovery Endpoint**：输入 Auth0 的 discovery endpoint URL。
	- **Client ID**：输入在 Auth0 settings 中找到的 client ID。
	- **Client Secret**：输入在 Auth0 settings 中找到的 client secret。
1. 选择 **Save settings**。
1. 将 OIDC 设置为 **Activated**。

## Discovery endpoints 参考 <a href="#discovery-endpoints-reference" id="discovery-endpoints-reference"></a>

- **Google discovery endpoint example**：
```
https://accounts.google.com/.well-known/openid-configuration
```
- **Microsoft Azure AD discovery endpoint example**：
```
https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
```
- **Auth0 discovery endpoint example**：
```
https://{your-domain}.auth0.com/.well-known/openid-configuration
```
- **Okta discovery endpoint example**：
```
https://{your-domain}.okta.com/.well-known/openid-configuration
```
- **Amazon Cognito discovery endpoint example**：
```
https://cognito-idp.{region}.amazonaws.com/{user-pool-id}/.well-known/openid-configuration
```
