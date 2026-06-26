---
title: Manage instance settings using environment variables
description: >-
  通过环境变量配置自托管 n8n instance owner、SSO、security policy、log
  streaming、MCP 和 community packages。
contentType: overview
nodeTitle: Manage settings using environment variables
originalFilePath: hosting/configuration/settings-env-vars.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/settings-env-vars'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables
layout:
  description:
    visible: false
---

# 使用环境变量管理实例设置 <a href="#manage-instance-settings-using-environment-variables" id="manage-instance-settings-using-environment-variables"></a>

你可以通过环境变量管理部分 instance settings，而不是通过 UI 配置它们。当你通过内部部署流水线等方式自动 provision n8n instances 时，这会很有用。

每个支持的区域都有一个专用环境变量，命名为 `<AREA>_MANAGED_BY_ENV`。将此变量设置为 `true` 即可激活该区域的环境变量管理。随后 n8n 会应用相关环境变量，并锁定匹配的 UI controls。

## 工作方式 <a href="#how-it-works" id="how-it-works"></a>

当你将 `<AREA>_MANAGED_BY_ENV` 设置为 `true` 时：

* n8n 会在 **每次启动时** 从环境变量重新应用 settings。
* 匹配的 UI controls 会变为 **read-only**。

当 `<AREA>_MANAGED_BY_ENV` 为 `false`（默认）时，即使你设置了相关环境变量，n8n 也会忽略它们。

{% hint style="info" %}
**关闭 `*_MANAGED_BY_ENV` 后，值会保留**

将 `*_MANAGED_BY_ENV` 重新设置为 `false` 会恢复 UI 写入权限，但会保留最后应用的值。之后如果想更改它们，请通过 UI 编辑。
{% endhint %}

{% hint style="info" %}
**意外的 read-only UI controls**

如果某个 setting 显示为 read-only 且不符合预期，请检查你的环境中匹配的 `*_MANAGED_BY_ENV` 变量是否为 `true`。
{% endhint %}

支持的区域及其激活变量：

* Instance owner：`N8N_INSTANCE_OWNER_MANAGED_BY_ENV`
* SSO：`N8N_SSO_MANAGED_BY_ENV`
* Security policy：`N8N_SECURITY_POLICY_MANAGED_BY_ENV`
* Log streaming：`N8N_LOG_STREAMING_MANAGED_BY_ENV`
* MCP：`N8N_MCP_MANAGED_BY_ENV`
* Community packages：`N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`

{% hint style="info" %}
**设置 `<AREA>_MANAGED_BY_ENV` 以激活分组**

某个区域中的其他环境变量不会生效，除非 `<AREA>_MANAGED_BY_ENV` 为 `true`。请将其设置为 `true` 来激活该分组。
{% endhint %}

## Instance owner <a href="#instance-owner" id="instance-owner"></a>

{% hint style="info" %}
**自 n8n v2.17.0 起可用**


{% endhint %}

通过环境变量预先 provision [instance owner](user-management.md)，而不是走应用内 setup。要在 setup 后更改 owner email，请参阅[更改自托管 n8n 的 instance owner email](change-instance-owner-email.md)。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须是 bcrypt hash**

此变量需要预先 hash 的 bcrypt 值。设置 plaintext password 会导致无法登录。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/75cM0VtFejV1gnDTFOSV/" %}

## SSO <a href="#sso" id="sso"></a>

{% hint style="info" %}
**自 n8n v2.18.0 起可用**


{% endhint %}

{% hint style="info" %}
**功能可用性**

Single sign-on 可用于 Business 和 Enterprise plans。
{% endhint %}

通过环境变量配置 [single sign-on](security/configure-sso.md)。

### 激活和共享设置 <a href="#activation-and-shared-settings" id="activation-and-shared-settings"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/TJ7IUBpRrfLoXyEn4T4d/" %}

### OIDC <a href="#oidc" id="oidc"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/SBpz79jvy94Y5dKIvxqR/" %}

### SAML <a href="#saml" id="saml"></a>

{% hint style="warning" %}
**SAML metadata variables 互斥**

请设置 `N8N_SSO_SAML_METADATA`（inline XML）或 `N8N_SSO_SAML_METADATA_URL`（URL）其中之一，不要同时设置。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/NnYMdwgkElS7TK37owd0/" %}

## Security policy <a href="#security-policy" id="security-policy"></a>

{% hint style="info" %}
**自 n8n v2.18.0 起可用**


{% endhint %}

通过环境变量管理 instance security policy，包括 MFA enforcement 和 personal space restrictions。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/xVIddGVtWAPFZlRYTrwL/" %}

## Log streaming <a href="#log-streaming" id="log-streaming"></a>

{% hint style="info" %}
**自 n8n v2.19.0 起可用**


{% endhint %}

通过环境变量管理 [log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems) destinations。有关每个 destination 的 JSON 结构，请参阅[使用环境变量配置](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems#configure-using-environment-variables)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/JvN9TDUUWTwpWaT83YrH/" %}

## MCP <a href="#mcp" id="mcp"></a>

{% hint style="info" %}
**自 n8n v2.20.0 起可用**


{% endhint %}

通过环境变量管理 [instance-level MCP access](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/connect-to-n8n-mcp-server)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Gf4nC8Xoy8uJDma1fIYg/" %}

## Community packages <a href="#community-packages" id="community-packages"></a>

{% hint style="info" %}
**自 n8n v2.21.0 起可用**


{% endhint %}

通过环境变量管理已安装的 [community packages](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/community-nodes/installation-and-management) 集合。n8n 会在每次启动时根据列表核对已安装 packages。Managed packages 不能通过 UI uninstall 或 update。

`N8N_COMMUNITY_PACKAGES_ENABLED` 也必须设置为 `true`（默认值）。禁用 community packages 时，n8n 会忽略 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` 并记录 warning。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/w3ftfKhp9KdsaTfUFHE8/" %}

## 组合示例 <a href="#combined-example" id="combined-example"></a>

以下示例配置一个由环境变量管理全部六个区域的实例。它会创建 instance owner、配置 OIDC SSO、强制 MFA、注册 webhook log streaming destination、启用 MCP access，并管理一个 community package。

```bash
# Instance owner <a href="#instance-owner" id="instance-owner"></a>
export N8N_INSTANCE_OWNER_MANAGED_BY_ENV=true
export N8N_INSTANCE_OWNER_EMAIL=<owner-email>
export N8N_INSTANCE_OWNER_FIRST_NAME=<first-name>
export N8N_INSTANCE_OWNER_LAST_NAME=<last-name>
export N8N_INSTANCE_OWNER_PASSWORD_HASH=<bcrypt-hash>

# SSO using OIDC <a href="#sso-using-oidc" id="sso-using-oidc"></a>
export N8N_SSO_MANAGED_BY_ENV=true
export N8N_SSO_USER_ROLE_PROVISIONING=instance_role
export N8N_SSO_OIDC_LOGIN_ENABLED=true
export N8N_SSO_OIDC_CLIENT_ID=<client-id>
export N8N_SSO_OIDC_CLIENT_SECRET=<client-secret>
export N8N_SSO_OIDC_DISCOVERY_ENDPOINT=<discovery-url>

# Security policy <a href="#security-policy" id="security-policy"></a>
export N8N_SECURITY_POLICY_MANAGED_BY_ENV=true
export N8N_MFA_ENFORCED_ENABLED=true
export N8N_PERSONAL_SPACE_PUBLISHING_ENABLED=false
export N8N_PERSONAL_SPACE_SHARING_ENABLED=false

# Log streaming <a href="#log-streaming" id="log-streaming"></a>
export N8N_LOG_STREAMING_MANAGED_BY_ENV=true
export N8N_LOG_STREAMING_DESTINATIONS='[{"type":"webhook","url":"https://logs.example.com/n8n"}]'

# MCP <a href="#mcp" id="mcp"></a>
export N8N_MCP_MANAGED_BY_ENV=true
export N8N_MCP_ACCESS_ENABLED=true

# Community packages <a href="#community-packages" id="community-packages"></a>
export N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true
export N8N_COMMUNITY_PACKAGES='[{"name":"n8n-nodes-foo","version":"1.2.3"}]'
```

## 设置环境变量 <a href="#set-environment-variables" id="set-environment-variables"></a>

有关设置环境变量的受支持方式，请参阅[配置方法](basic-configuration.md)。
