---
title: External secrets
description: 在 n8n 中使用 external secrets vault。
contentType: howto
nodeTitle: Use external secret stores
originalFilePath: external-secrets.md
originalUrl: 'https://docs.n8n.io/external-secrets'
url: 'https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores'
layout:
  description:
    visible: false
---

# External secrets <a href="#external-secrets" id="external-secrets"></a>

{% hint style="info" %}
**功能可用性**

* External secrets 可用于 Enterprise Self-hosted 和 Enterprise Cloud plans。
* n8n 支持以下 secret providers：1Password（通过 [Connect Server](https://developer.1password.com/docs/connect/get-started/)）、AWS Secrets Manager、Azure Key Vault、GCP Secrets Manager、HashiCorp Vault 和 Infisical。
* 从 n8n version 2.10.0 起，你可以为每个 secret provider 连接多个 vaults。旧版本每个 provider 只支持一个 vault。
* 从 version `2.13.0` 起，如果启用，project editors 可以在其 projects 中使用 external secrets，project admins 也可以管理 project vaults。
* n8n 不支持 [HashiCorp Vault Secrets](https://developer.hashicorp.com/hcp/docs/vault-secrets)。
{% endhint %}

你可以使用 external secrets store 来管理 n8n 的 credentials[^1]。

n8n 会将所有 credentials 加密存储在其 database 中，并默认限制对它们的 access。借助 external secrets feature，你可以把 sensitive credential information 存储在 external vault 中，并让 n8n 在需要时加载它。这提供了额外 security layer，并允许你在一个中心位置管理跨多个 [n8n environments](../use-source-control-and-environments/README.md) 使用的 credentials。

## Global vaults <a href="#global-vaults" id="global-vaults"></a>

默认情况下，secrets vault 是 **global**：instance 中的 users 可以使用引用该 vault 中 secrets 的 credentials。

在 personal projects 中，只有 instance owners 和 admins 可以在 credentials 中使用 global vaults 的 secrets。

## Project vaults <a href="#project-vaults" id="project-vaults"></a>

Instance admins 可以与特定 [project](../manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md) 分享 vault。将 vault 分配给 project 后，只有该 project 的 credentials 可以引用它的 secrets。你可以选择将 vault 绑定到单个 project，也可以保持 global。

更改 vault scope：

1. 在 n8n 中，前往 **Settings** > **External Secrets**。
1. 找到要配置的 vault，并选择 **Edit**。
1. 在 **Share** 下，选择以下选项之一：
    - **Global**：在整个 n8n instance 中分享此 vault。这允许 instance 中的 credentials 引用这些 secrets。
    - **Project**：将此 vault 限制到特定 project。选择 project 会把 secret access 限制为只有该 project 的 credentials 可以使用。
1. **Save** 你的配置。

## 将 n8n 连接到 secrets store <a href="#connect-n8n-to-your-secrets-store" id="connect-n8n-to-your-secrets-store"></a>

{% hint style="info" %}
**Secret values**

n8n 只支持 plaintext values 作为 secrets，不支持 JSON objects。
{% endhint %}

1. 在 n8n 中，前往 **Settings** > **External Secrets**。
1. 点击 **Add secrets vault**。
1. 为你的 vault 输入唯一 name。在 credential 中使用 `{{ $secrets.<vault-name>... }}` expression 引用此 vault 时，它会作为第一个 segment。
1. 选择一个 supported secret provider。
1. 输入 provider 的 credentials。详情请参考下面 provider-specific sections。
1. **Save** 你的配置。

只要此 store 保持 connected，你就可以在 credentials 中引用它的 secrets。

### 1Password <a href="#1password" id="1password"></a>

{% hint style="info" %}
**需要 1Password Connect Server**

n8n 集成的是 [1Password Connect Server](https://developer.1password.com/docs/connect/get-started/)，这是用于 machine access to 1Password 的 self-hosted API。它不同于 personal 或 team 1Password account。要使用此 provider，你必须部署并运行 Connect Server。
{% endhint %}

提供你的 **Connect Server URL** 和 **Access Token**。Connect Server URL 是 server 可访问的地址（例如 `http://localhost:8080`）。Access Token 是你为 Connect Server integration 创建的 token。

n8n 会读取 token 可访问的所有 vaults 和 items。每个 1Password item 都会成为一个 secret，其 fields 可作为 properties 访问。使用 `{{ $secrets.<vault-name>.<item-title>.<field-label> }}` 访问特定 field value。

### AWS Secrets Manager <a href="#aws-secrets-manager" id="aws-secrets-manager"></a>

提供你的 **access key ID**、**secret access key** 和 **region**。IAM user 必须拥有 `secretsmanager:ListSecrets`、`secretsmanager:BatchGetSecretValue` 和 `secretsmanager:GetSecretValue` permissions。

要让 n8n 访问 AWS Secrets Manager 中的所有 secrets，可以将以下 policy 附加到 IAM user：

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AccessAllSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:ListSecrets",
				"secretsmanager:BatchGetSecretValue",
				"secretsmanager:GetResourcePolicy",
				"secretsmanager:GetSecretValue",
				"secretsmanager:DescribeSecret",
				"secretsmanager:ListSecretVersionIds"
			],
			"Resource": "*"
		}
	]
}
```

你也可以更严格，只让 n8n access 特定 AWS Secret Manager secrets。你仍然需要允许 `secretsmanager:ListSecrets` 和 `secretsmanager:BatchGetSecretValue` permissions 来访问所有 resources。这些 permissions 允许 n8n retrieve ARN-scoped secrets，但不会提供对 secret values 的 access。

接下来，你需要将 `secretsmanager:GetSecretValue` permission 的 scope 设置为你希望与 n8n 分享的 secrets 的特定 Amazon Resource Names (ARNs)。确保在每个 resource ARN 中使用正确 region 和 account ID。你可以在 AWS dashboard 中找到 secrets 的 ARN details。

例如，以下 IAM policy 只允许 access 你指定 AWS account 和 region 中 name 以 `n8n` 开头的 secrets：

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "ListingSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:ListSecrets",
				"secretsmanager:BatchGetSecretValue"
			],
			"Resource": "*"
		},
		{
			"Sid": "RetrievingSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:GetSecretValue",
				"secretsmanager:DescribeSecret"
			],
			"Resource": [
				"arn:aws:secretsmanager:us-west-2:123456789000:secret:n8n*"
			]
		}
	]
}
```

更多 IAM permission policy examples，请参阅 [AWS documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_iam-policies.html#auth-and-access_examples_batch)。

### Azure Key Vault <a href="#azure-key-vault" id="azure-key-vault"></a>

提供你的 **vault name**、**tenant ID**、**client ID** 和 **client secret**。请参考 Azure 文档来[注册 Microsoft Entra ID app 并创建 service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)。n8n 只支持 single-line values 作为 secrets。

### GCP Secrets Manager <a href="#gcp-secrets-manager" id="gcp-secrets-manager"></a>

为至少具有以下 roles 的 service account 提供 **Service Account Key** (JSON)：`Secret Manager Secret Accessor` 和 `Secret Manager Secret Viewer`。更多信息请参考 Google 的 [service account documentation](https://cloud.google.com/iam/docs/service-account-overview)。

### HashiCorp Vault <a href="#hashicorp-vault" id="hashicorp-vault"></a>

提供 vault instance 的 **Vault URL**，并选择 **Authentication Method**。输入 authentication details。也可以选择提供 namespace。

- 请参考你的 authentication method 对应的 HashiCorp documentation：
	- [Token auth method](https://developer.hashicorp.com/vault/docs/auth/token)
	- [AppRole auth method](https://developer.hashicorp.com/vault/docs/auth/approle)
	- [Userpass auth method](https://developer.hashicorp.com/vault/docs/auth/userpass)
- 如果你使用 vault namespaces，可以输入 n8n 应连接的 namespace。有关 HashiCorp Vault namespaces 的更多信息，请参考 [Vault Enterprise namespaces](https://developer.hashicorp.com/vault/docs/enterprise/namespaces)。

#### Manual KV mount configuration <a href="#manual-kv-mount-configuration" id="manual-kv-mount-configuration"></a>

默认情况下，n8n 会通过读取 `sys/mounts` autodiscover KV secret engines。如果你的 Vault token 无法访问 `sys/mounts`，可以手动指定 KV engine mount path 和 version：

- **KV Mount Path**：KV secret engine 的 mount path（例如 `secret/`）。设置后，n8n 会跳过 `sys/mounts` autodiscovery 并直接使用此 path。留空则使用 autodiscovery。
- **KV Version**：KV engine version（`v1` 或 `v2`）。默认值为 `v2`。仅当指定 **KV Mount Path** 时适用。

你的 Vault token 仍然需要对 KV path 本身具备 read 和 list access。以下 example 展示了 `secret/` 中 KV v2 mount 的最小 Vault policy：

```hcl
# Read and list secrets at the "secret/" KV v2 mount <a href="#read-and-list-secrets-at-the-secret-kv-v2-mount" id="read-and-list-secrets-at-the-secret-kv-v2-mount"></a>
path "secret/data/*" {
  capabilities = ["read"]
}
path "secret/metadata/*" {
  capabilities = ["read", "list"]
}
```

对于 KV v1，你只需要一个 policy path：

```hcl
# Read and list secrets at the "kv/" KV v1 mount <a href="#read-and-list-secrets-at-the-kv-kv-v1-mount" id="read-and-list-secrets-at-the-kv-kv-v1-mount"></a>
path "kv/*" {
  capabilities = ["read", "list"]
}
```

### Infisical <a href="#infisical" id="infisical"></a>

{% hint style="info" %}
**Version `2.26.0` 及更高版本**

Infisical secrets management support 仅从 version `2.26.0` 起可用。
{% endhint %}

要连接 Infisical，请提供以下内容：

- **Site URL**：Infisical instance 的 base URL。默认值为 `https://app.infisical.com`。只有在 self-hosting Infisical 时才需要更改。
- **Project ID**：要读取 secrets 的 Infisical project ID。
- **Environment**：environment slug，例如 `dev`、`staging` 或 `prod`。
- **Secret Path**：project 内要读取 secrets 的 path。默认值为 `/`。
- **Authentication Method**：选择 **Universal Auth**（推荐）或 **Access Token**。

n8n 推荐 Universal Auth，它使用 Infisical [Machine Identity](https://infisical.com/docs/documentation/platform/identities/machine-identities)。Tokens 会在 expire 前自动 refresh。

在 Infisical 中，为 Machine Identity 授予一个有权读取 target project 中 secrets 的 role。内置 **Viewer** role 可用，或者你也可以创建 custom role，在 target environment 和 secret path 上授予 `secrets` permissions **Read Value** 和 **Describe Secret**。请参阅 Infisical 的 [project role docs](https://infisical.com/docs/documentation/platform/access-controls/role-based-access-controls)。

{% tabs %}
{% tab title="Universal Auth" %}
提供：

- **Client ID**：machine identity 的 Client ID。
- **Client Secret**：machine identity 的 Client Secret。

在 Infisical 中，创建 machine identity，将其附加到 project 并赋予上述 role，然后复制 Client ID 和 Client Secret。请参阅 Infisical 的 [Universal Auth docs](https://infisical.com/docs/documentation/platform/identities/universal-auth)。
{% endtab %}

{% tab title="Access Token" %}
提供：

- **Access Token**：machine identity 中签发的 token。

在 Infisical 中，创建 machine identity，将其附加到 project 并赋予上述 role，然后点击 `Add Auth Method` 并选择 `Token Auth`。请参阅 Infisical 的 [Token auth docs](https://infisical.com/docs/documentation/platform/identities/token-auth)。
{% endtab %}
{% endtabs %}

## 在 n8n credentials 中使用 secrets <a href="#use-secrets-in-n8n-credentials" id="use-secrets-in-n8n-credentials"></a>

要在 n8n credential 中使用来自 store 的 secret：

1. 创建 new credential，或打开现有 credential。
1. 在你想使用 secret 的 field 上：
	1. Hover over the field。
	1. 选择 **Expression**。
1. 在你想使用 secret 的 field 中，输入引用 secret name 的 expression[^2]：
	```js
	{{ $secrets.<vault-name>.<secret-name> }}
	```
	`<vault-name>` 是你添加 store 时输入的值。将 `<secret-name>` 替换为它在 vault 中显示的 name。

## 在 n8n environments 中使用 external secrets <a href="#using-external-secrets-with-n8n-environments" id="using-external-secrets-with-n8n-environments"></a>

n8n 的 [Source control and environments](../use-source-control-and-environments/README.md) feature 允许你创建由 Git 支持的不同 n8n environments。该 feature 不支持在不同 instances 中使用不同 credentials。你可以通过将每个 n8n instance 连接到不同 vault 或 project environment，使用 external secrets vault 为不同 environments 提供不同 credentials。

例如，你有两个 n8n instances，一个用于 development，一个用于 production。在你的 secrets provider 中，创建一个包含 development 和 production 两个 environments 的 project。为 secrets provider 的每个 environment 生成一个 token。使用 development environment 的 token 连接 development n8n instance，使用 production environment 的 token 连接 production n8n instance。

## 在 projects 中使用 external secrets <a href="#using-external-secrets-in-projects" id="using-external-secrets-in-projects"></a>

你可以与 project 分享 vault，让只有该 project 的 credentials 可以引用它的 secrets。Setup steps 请参考 [Project vaults](#project-vaults)。Project-scoped vaults 从 version `2.11.0` 起可用。

### Project roles 的 access <a href="#access-for-project-roles" id="access-for-project-roles"></a>

{% hint style="info" %}
**Version `2.13.0` 及更高版本**

在 version `2.13.0` 之前，在 [RBAC project](../manage-users-and-access/set-permissions-and-roles-rbac/README.md) 中使用 external secrets，需要一个 [instance owner 或 instance admin](../manage-users-and-access/understand-account-types.md) 作为 project member。
{% endhint %}

从 version `2.13.0` 起，instance owners 和 admins 可以授予 [project editors](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md#project-editor) 与 [project admins](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md#project-admin) external secrets access。

启用此功能：

1. 前往 **Settings** > **External Secrets**。
1. 打开 **Enable external secrets for project roles**。

启用后，**Project Editors** 可以：

- 查看与 project 分享的 available external secret vaults（在 **Project** > **Settings** 中）。
- 在 credentials 中使用 project vaults 的 secrets。

**Project Admins** 拥有相同 access，此外还可以：

- 为 project 创建 new vaults（在 **Project** > **Settings** 中）。
- 更新和删除分配给 project 的 vaults。

{% hint style="info" %}
**Global vault access**

在 **Settings** > **External Secrets** 中创建的 Global vaults 会显示在 **Project** > **Settings** 中，但对 project roles 是 read-only。只有 instance admins 可以修改或删除 global vaults。
{% endhint %}

### Custom roles <a href="#custom-roles" id="custom-roles"></a>

为了更细粒度的 access control，instance owners 和 admins 可以创建 [custom project role](../manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md)。前往 **Settings** > **Project roles** > **Create role**。在 permissions 列表中，配置：

- **Secrets vaults**：控制 vault management（view、create、edit、delete 和 sync vaults）。
- **Secrets**：控制该 role 是否可以在 credential expressions 中使用 secrets。

这两个 permissions 相互独立。例如，某个 role 可能只需要 **Secrets** permission，即可在 credentials 中使用 secrets，而不需要管理 vaults。可用 scopes 的完整列表请参考 [Secret vault scopes](../manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md#secret-vault-scopes)。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Secrets 在 production 中无法 resolve <a href="#secrets-dont-resolve-in-production" id="secrets-dont-resolve-in-production"></a>

{% hint style="info" %}
**Version `2.13.0` 及更高版本**

从 version `2.13.0` 起，拥有 [secrets access enabled](#access-for-project-roles) 的 project editors 和 admins 可以在自己的 credentials 中使用 external secrets。下面的限制只适用于旧版本，或 opt-in toggle 关闭时。
{% endhint %}

在 `2.13.0` 之前的 versions 中（或 **Enable external secrets for project roles** 关闭时），只有 instance owners 和 admins 可以在 runtime resolve secrets。如果 owner 或 admin 使用 secrets expression 更新另一个 user 的 credential，它在 preview 中可能看起来可用，但在 production 中会失败。

在这种情况下，只在 instance owner 或 admin 拥有的 credentials 中使用 external secrets。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。
[^2]: 在 n8n 中，expressions 允许你通过执行 JavaScript code 动态填充 node parameters。你可以使用 n8n expression syntax 基于 previous nodes、other workflows 或 n8n environment 中的数据定义值，而不是提供 static value。
