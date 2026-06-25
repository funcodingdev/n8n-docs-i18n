---
description: 在用户之间共享工作流。
contentType: howto
nodeTitle: Share with others
originalFilePath: workflows/sharing.md
originalUrl: 'https://docs.n8n.io/workflows/sharing'
url: 'https://docs.n8n.io/build/manage-workflows/share-with-others'
layout:
  description:
    visible: false
---

# 工作流共享 <a href="#workflow-sharing" id="workflow-sharing"></a>

{% hint style="info" %}
**功能可用性**

适用于 Pro 和 Enterprise Cloud 方案，以及 Enterprise 自托管方案。
{% endhint %}

Workflow sharing 允许你在同一个 n8n 实例的用户之间共享工作流。

用户可以共享自己创建的工作流。实例所有者和拥有 admin 角色的用户可以查看并共享实例中的所有工作流。关于 owners 和 admins 的更多信息，请参阅 [Account types](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/understand-account-types)。

## 共享工作流 <a href="#share-a-workflow" id="share-a-workflow"></a>

1. 打开要共享的工作流。
2. 选择 **Share**。
3. 在 **Add users** 中查找并选择要共享给的用户。
4. 选择 **Save**。

**注意：** 此选项仅在共享位于 **Personal** workspace 内的工作流时可用。如果尝试对 **project 内** 的工作流使用 "Add users" 选项，会看到以下弹窗：

![项目内共享选项的截图](../../../build/.gitbook/assets/sharing-within-projects.png)

这是预期行为，表示该工作流已与该特定 project 内的所有人共享。你不需要直接将用户添加到工作流，而是需要将用户添加到工作流所在的 project。

## 查看共享工作流 <a href="#view-shared-workflows" id="view-shared-workflows"></a>

你可以在 **Workflows** 列表中浏览和搜索工作流。列表中的工作流取决于 project：

* **Overview** 会列出你可以访问的所有工作流，包括：
	* 你自己的工作流。
	* 共享给你的工作流。
	* 你所属 projects 中的工作流。
	* 如果你以实例所有者或 admin 身份登录：实例中的所有工作流。
* 其他 projects：该 project 中的所有工作流。

## 工作流角色和权限 <a href="#workflow-roles-and-permissions" id="workflow-roles-and-permissions"></a>

工作流有两个角色：creator 和 editor。Creator 是创建工作流的用户。Editors 是可以访问该工作流的其他用户。

除了删除用户时，你不能更改工作流所有者。

{% hint style="info" %}
**凭据**

Workflow sharing 允许 editors 使用工作流中用到的所有 credentials[^1]。这也包括没有通过 [credential sharing](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/share-credentials-securely) 显式共享给他们的 credentials。
{% endhint %}
### 权限 <a href="#permissions" id="permissions"></a>

| 权限 | Creator | Editor |
| ----------- | ------- | ------ |
| 查看工作流（只读） | ✅ | ✅ |
| 查看执行 | ✅ | ✅ |
| 更新（包括标签） | ✅ | ✅ |
| 运行 | ✅ | ✅ |
| 共享 | ✅ | ❌ |
| 导出 | ✅ | ✅ |
| 删除 | ✅ | ❌ |

## 使用未共享凭据时的节点编辑限制 <a href="#node-editing-restrictions-with-unshared-credentials" id="node-editing-restrictions-with-unshared-credentials"></a>

n8n 中的共享遵循最小权限原则。这意味着，如果某个用户与你共享了工作流，但没有共享他们的凭据，你就不能编辑工作流中使用这些凭据的节点。你可以查看并运行该工作流，也可以编辑不使用未共享凭据的节点。

关于共享凭据的指南，请参阅 [Credential sharing](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/share-credentials-securely)。

[^1]: 在 n8n 中，credentials 用于存储连接特定应用和服务所需的身份验证信息。使用你的身份验证信息（用户名和密码、API key、OAuth secrets 等）创建凭据后，就可以使用关联的 app node 与该服务交互。
