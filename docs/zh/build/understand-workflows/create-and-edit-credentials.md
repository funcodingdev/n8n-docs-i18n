---
contentType: howto
nodeTitle: Create and edit credentials
originalFilePath: credentials/add-edit-credentials.md
originalUrl: https://docs.n8n.io/credentials/add-edit-credentials
url: https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials
description: 创建和编辑 credential。
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
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 创建和编辑 credential

Credential 是安全存储的认证信息，用于将 n8n 工作流连接到 API、数据库等外部服务。

## 创建 credential <a href="#create-a-credential" id="create-a-credential"></a>

1. 选择侧边菜单左上角的 <img src="../../../build/.gitbook/assets/universal-resource-button (1).png" alt="universal create resource icon" data-size="line"> **Create** 按钮。选择 credential。
2. 如果你的 n8n 实例支持 project[^1]，还需要选择是在你的 personal space 中创建 credential，还是在你有权访问的特定 project 中创建。如果你使用的是社区版，则会在 personal space 中创建 credential。
3. 选择要连接的 app 或服务。

或者：

1. 在 **Overview** 页面或某个特定 project 中，使用右上角的 <img src="../../../build/.gitbook/assets/universal-resource-button (1).png" alt="universal create resource icon" data-size="line"> **Create** 按钮。选择 Credential。
2. 如果你是在 **Overview** 页面执行此操作，credential 会创建在你的 personal space 中。如果你是在某个 project 中执行此操作，credential 会创建在该 project 中。
3. 选择要连接的 app 或服务。

在工作流编辑器中编辑 node 时，你也可以在 credential 下拉菜单中创建新的 credential。

进入 credential 弹窗后，输入该服务所需的详细信息。相关指引请参考[凭据库](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials)中对应服务的页面。

保存 credential 时，n8n 会测试它以确认可用。

{% hint style="info" %}
**Credential 命名**

n8n 默认将新的 credential 命名为“_node name_ account”。你可以点击名称来重命名 credential，方式类似于重命名 node。建议使用能标识 app 或服务、类型以及用途的名称。命名约定有助于跟踪和识别 credential。
{% endhint %}

## 允许的 HTTP 请求域名 <a href="#allowed-http-request-domains" id="allowed-http-request-domains"></a>

许多用于 Web API 和服务的 n8n credential 都会显示 **Allowed HTTP Request Domains** 字段。当在 **HTTP Request** node 中选择该 credential 时，这个字段控制该 credential 允许用于哪些域名。如果 credential 用在它自己的专用 node 中，此字段不会生效。

该字段有三个选项：

* **All**：credential 可用于任意 URL。
* **Specific Domains**：限制为特定域名（提供逗号分隔列表，例如 `httpbin.org, api.github.com`）。
* **None**：完全禁止在 **HTTP Request** node 中使用该 credential。

此字段可防止 credential 被误用，例如将 credential 发送到预期域名之外的 URL。

## Credential 中的表达式 <a href="#expressions-in-credentials" id="expressions-in-credentials"></a>

你可以使用表达式[^2]在工作流运行时动态设置 credential：

1. 在工作流中找到包含 credential 的数据路径。具体路径取决于数据中的实际参数名称。确保执行到需要 credential 的 node 时，工作流中可以访问包含该 credential 的数据。
2. 创建 credential 时，将鼠标悬停在要使用表达式的字段上。
3. 打开 **Expression**。
4. 输入表达式。

### 示例工作流 <a href="#example-workflow" id="example-workflow"></a>

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22name%22%3A%20%22Dynamic%20credentials%20using%20expressions%22%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22path%22%3A%20%22da4071f2-7550-4dae-aa48-8bced4291643%22%2C%0A%20%20%20%20%20%20%20%20%22formTitle%22%3A%20%22Test%20dynamic%20credentials%22%2C%0A%20%20%20%20%20%20%20%20%22formDescription%22%3A%20%22This%20form%20is%20for%20testing%20an%20n8n%20workflow%20that%20demonstrates%20setting%20credentials%20with%20expressions.%22%2C%0A%20%20%20%20%20%20%20%20%22formFields%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22values%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22fieldLabel%22%3A%20%22Enter%20your%20NASA%20API%20key%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22requiredField%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22responseMode%22%3A%20%22responseNode%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22cc6f2b1e-0ed0-4d22-8a44-d7223ba283b4%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22n8n%20Form%20Trigger%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.formTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20560%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22webhookId%22%3A%20%22da4071f2-7550-4dae-aa48-8bced4291643%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22additionalFields%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22ef336bae-3d4f-419c-ab5c-b9f0de89f170%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.nasa%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20900%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22credentials%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22nasaApi%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22id%22%3A%20%22QDDBOZOD6k3ijL5t%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22name%22%3A%20%22NASA%20account%22%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22respondWith%22%3A%20%22redirect%22%2C%0A%20%20%20%20%20%20%20%20%22redirectURL%22%3A%20%22%3D%7B%7B%20%24json.url%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22143bcdb6-aca0-4dd8-9204-9777271cd230%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Respond%20to%20Webhook%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.respondToWebhook%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201220%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22This%20workflow%20shows%20how%20to%20set%20credentials%20dynamically%20using%20expressions.%5Cn%5Cn%5CnFirst%2C%20set%20up%20your%20NASA%20credential%3A%20%5Cn%5Cn1.%20Create%20a%20new%20NASA%20credential.%5Cn1.%20Hover%20over%20%2A%2AAPI%20Key%2A%2A.%5Cn1.%20Toggle%20%2A%2AExpression%2A%2A%20on.%5Cn1.%20In%20the%20%2A%2AAPI%20Key%2A%2A%20field%2C%20enter%20%60%7B%7B%20%24json%5B%5C%22Enter%20your%20NASA%20API%20key%5C%22%5D%20%7D%7D%60.%5Cn%5Cn%5CnThen%2C%20test%20the%20workflow%3A%5Cn%5Cn1.%20Get%20an%20%5BAPI%20key%20from%20NASA%5D%28https%3A%2F%2Fapi.nasa.gov%2F%29%5Cn2.%20Select%20%2A%2AExecute%20workflow%2A%2A%5Cn3.%20Enter%20your%20key%20using%20the%20form.%5Cn4.%20The%20workflow%20runs%20and%20sends%20you%20to%20the%20NASA%20picture%20of%20the%20day.%5Cn%5Cn%5CnFor%20more%20information%20on%20expressions%2C%20refer%20to%20%5Bn8n%20documentation%20%7C%20Expressions%5D%28https%3A%2F%2Fdocs.n8n.io%2Fcode%2Fexpressions%2F%29.%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20564%2C%0A%20%20%20%20%20%20%20%20%22width%22%3A%20322%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%204%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%220a0dee23-fa16-4f09-b5e0-856f47fb53d0%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20120%2C%0A%20%20%20%20%20%20%20%20140%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22User%20submits%20an%20API%20key%20using%20the%20form%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22dd766e32-334d-4e46-9daa-7800b134a3a5%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note1%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20500%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22The%20workflow%20passes%20the%20key%20to%20the%20NASA%20node.%20You%20can%20reference%20the%20value%20using%20the%20expression%20%60%24json%5B%5C%22Enter%20your%20NASA%20API%20key%5C%22%5D%60.%20This%20is%20also%20available%20to%20the%20node%20credential.%20%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%205%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%223d8f02e6-e029-41dc-89ad-0f5cffe09348%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note2%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20820%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22The%20Respond%20to%20Webhook%20node%20controls%20the%20form%20response%20%28in%20this%20example%2C%20redirecting%20the%20user%20to%20an%20image%29%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22096eb6ab-c276-4687-9dc0-50e16a8f709a%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note3%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201140%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22n8n%20Form%20Trigger%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22NASA%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Respond%20to%20Webhook%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/credentials/dynamic_credentials_using_expressions.json" %}

#### 使用示例 <a href="#using-the-example" id="using-the-example"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/vKIIq31qrlay3ovXTvUj/" %}

[^1]: n8n project 允许你将 workflow、variable 和 credential 分到不同组中，便于管理。通过共享和分隔相关资源，project 可以让团队协作更容易。
[^2]: 在 n8n 中，表达式允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n 表达式语法，基于前序 node、其他 workflow 或 n8n 环境中的数据来定义值。
