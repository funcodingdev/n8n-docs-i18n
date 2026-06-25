---
contentType: howto
nodeTitle: 环境变量安装
originalFilePath: integrations/community-nodes/installation/env-install.md
originalUrl: 'https://docs.n8n.io/integrations/community-nodes/installation/env-install'
url: >-
  https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation
layout:
  description:
    visible: false
---

# 通过环境变量管理社区 package <a href="#manage-community-packages-from-environment-variables" id="manage-community-packages-from-environment-variables"></a>

{% hint style="info" %}
**自 n8n v2.21.0 起可用**


{% endhint %}

在自托管 n8n 中，你可以通过环境变量管理已安装的社区 package 集合。n8n 每次启动时都会根据列表核对已安装 package：安装缺失 package、修正版本，并卸载不在列表中的 package。使用此方法可以用固定 package 集合启动实例，例如通过部署流水线。

{% hint style="warning" %}
**启用后会卸载不在列表中的 package**

首次使用 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true` 启动 n8n 时，n8n 会卸载任何当前已安装但未包含在 `N8N_COMMUNITY_PACKAGES` 中的社区 package。如果你已经通过 UI 管理 package，请先检查 **Community nodes** 设置页，并将要保留的 package 添加到 `N8N_COMMUNITY_PACKAGES`，再启用此变量。
{% endhint %}

## 配置 <a href="#configure" id="configure"></a>

在 n8n 实例上设置以下环境变量，然后重启：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/w3ftfKhp9KdsaTfUFHE8/" %}

{% hint style="info" %}
**必须启用社区 package**

`N8N_COMMUNITY_PACKAGES_ENABLED` 必须为 `true`（默认值）。如果在实例级别禁用了社区 package，n8n 会忽略 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`，并在启动时记录警告。
{% endhint %}

例如：

```bash
export N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true
export N8N_COMMUNITY_PACKAGES='[{"name":"n8n-nodes-foo","version":"1.2.3"}]'
```

当 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` 为 `true` 时，**Community nodes** 设置页是只读的：你无法通过 UI 安装、更新或卸载 package。

### 每个 package 的字段 <a href="#per-package-fields" id="per-package-fields"></a>

| 字段 | 类型 | 是否必需 | 说明 |
| :---- | :--- | :------- | :---------- |
| `name` | string | 是 | npm package 名称。你可以将版本以内联形式写为 `<package-name>@<version>`。如果这样做，请不要再将 `version` 字段设置为其他值，否则 n8n 会拒绝冲突版本。 |
| `version` | string | 否 | 版本说明符。如果省略，n8n 会在 vetted-packages registry 中查找该 package 并使用对应版本；如果该 package 未被审查，n8n 会安装 npm 解析出的版本，并且不会在重启之间核对版本。 |
| `checksum` | string | 否 | 解析出的 tarball 的 SHA-512 校验和（`sha512-...`）。需要设置 `version`。可行时，n8n 会从 vetted registry 自动解析校验和。 |

包含全部三个字段的示例：

```json
[
  { "name": "n8n-nodes-foo", "version": "1.2.3" },
  { "name": "n8n-nodes-bar@0.5.0" },
  { "name": "n8n-nodes-baz", "version": "2.0.0", "checksum": "sha512-..." }
]
```

{% hint style="warning" %}
**未验证 package 需要 checksum**

如果 package 不在 vetted-packages registry 中，且 `N8N_UNVERIFIED_PACKAGES_ENABLED` 为 `false`，n8n 会启动失败。请为该 package 固定 `checksum`，设置 `N8N_UNVERIFIED_PACKAGES_ENABLED=true`，或选择经过审查的 package。
{% endhint %}

有关设置环境变量的受支持方式，请参阅[配置方法](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration)。

## 管理 package <a href="#manage-packages" id="manage-packages"></a>

要添加、移除、升级或降级 package，请编辑 `N8N_COMMUNITY_PACKAGES` 并重启 n8n。n8n 会在下次启动时根据新列表进行核对。

{% hint style="warning" %}
**版本中的 breaking change**

Node 开发者可能会在新版本中引入 breaking change。Breaking change 是会破坏既有功能的更新。更改版本时请谨慎。如果新版本导致问题，请将 `version` 设置回之前的值并重启 n8n 以回滚。
{% endhint %}
