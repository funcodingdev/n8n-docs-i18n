---
title: n8n
contentType:
  - integration
  - reference
priority: medium
nodeTitle: n8n
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.n8n.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n
description: >-
  n8n 中 n8n node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
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

# n8n

这是一个用于与 n8n 自身集成的 node。此 node 允许你在 workflow 中使用 [n8n API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)。

有关使用 n8n API 的更多信息，请参阅 [n8n REST API 文档](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)。有关直接使用 API endpoint 的信息，请参阅 [API endpoint reference](/broken/spaces/r7wKI4I1BgdBCuq5Cvcx/pages/NjbdMwHH3QGuRDWQrwJY)。

{% hint style="info" %}
**Credentials**

你可以在 [API authentication](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api/authentication) 文档中找到该 node 的身份验证信息。
{% endhint %}

{% hint style="warning" %}
**SSL**

此 node 不支持 SSL。如果你的 server 要求 SSL 连接，请使用 [HTTP Request node](n8n-nodes-base.httprequest/) 调用 [n8n API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)。HTTP Request node 提供了[提供 SSL certificate](../credentials/httprequest.md#provide-an-ssl-certificate) 的选项。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Audit
  * [**Generate** security audit](n8n-nodes-base.n8n.md#generate-audit)
* Credential
  * [**Create** credential](n8n-nodes-base.n8n.md#create-credential)
  * [**Delete** credential](n8n-nodes-base.n8n.md#delete-credential)
  * [**Get Schema**](n8n-nodes-base.n8n.md#get-credential-schema)：使用此操作获取类型的 credential data schema
* Execution
  * [**Get** execution](n8n-nodes-base.n8n.md#get-execution)
  * [**Get Many** executions](n8n-nodes-base.n8n.md#get-many-executions)
  * [**Delete** execution](n8n-nodes-base.n8n.md#delete-execution)
* Workflow
  * [**Publish** workflow](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Create** workflow](n8n-nodes-base.n8n.md#create-workflow)
  * [**Deactivate** workflow](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Delete** workflow](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Get** workflow](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Get Many** workflows](n8n-nodes-base.n8n.md#get-many-workflows)
  * [**Update** workflow](n8n-nodes-base.n8n.md#update-workflow)

## Generate audit <a href="#generate-audit" id="generate-audit"></a>

此操作没有参数。使用这些选项配置它：

* **Categories**：选择希望 audit 包含的风险类别。选项包括：
  * **Credentials**
  * **Database**
  * **Filesystem**
  * **Instance**
  * **Nodes**
* **Days Abandoned Workflow**：使用此选项设置 workflow 在多少天未执行后应被视为 abandoned。输入天数。默认值为 `90`。

## Create credential <a href="#create-credential" id="create-credential"></a>

使用这些参数配置该操作：

* **Name**：输入要创建的 credential 名称。
* **Credential Type**：输入 credential 的类型。可用类型取决于 n8n instance 上安装的 node。一些内置类型包括 `githubApi`、`notionApi` 和 `slackApi`。
* **Data**：输入包含此 **Credential Type** 所需属性的有效 JSON object。要查看预期格式，请使用 **Get Schema** 操作。

## Delete credential <a href="#delete-credential" id="delete-credential"></a>

使用此参数配置该操作：

* **Credential ID**：输入要删除的 credential ID。

## Get credential schema <a href="#get-credential-schema" id="get-credential-schema"></a>

使用此参数配置该操作：

* **Credential Type**：输入 credential 的类型。可用类型取决于 n8n instance 上安装的 node。一些内置类型包括 `githubApi`、`notionApi` 和 `slackApi`。

## Get execution <a href="#get-execution" id="get-execution"></a>

使用此参数配置该操作：

* **Execution ID**：输入要检索的 execution ID。

### Get execution 选项 <a href="#get-execution-option" id="get-execution-option"></a>

你可以使用此 **Option** 进一步配置该操作：

* **Include Execution Details**：使用此控制项设置是否包含详细 execution data（开启）或不包含（关闭）。

## Get many executions <a href="#get-many-executions" id="get-many-executions"></a>

使用这些参数配置该操作：

* **Return All**：设置是否返回所有结果（开启），或是否将结果限制为输入的 **Limit**（关闭）。
* **Limit**：如果关闭 **Return All** 控制项，设置要返回的结果数。

### Get many executions filter <a href="#get-many-executions-filters" id="get-many-executions-filters"></a>

你可以使用这些 **Filters** 进一步配置该操作：

* **Workflow**：按 workflow 过滤 execution。选项包括：
  * **From list**：选择一个 workflow 作为 filter。
  * **By URL**：输入一个 workflow URL 作为 filter。
  * **By ID**：输入一个 workflow ID 作为 filter。
* **Status**：按 status 过滤 execution。选项包括：
  * **Error**
  * **Success**
  * **Waiting**

### Get many execution 选项 <a href="#get-many-execution-options" id="get-many-execution-options"></a>

你可以使用此 **Option** 进一步配置该操作：

* **Include Execution Details**：使用此控制项设置是否包含详细 execution data（开启）或不包含（关闭）。

## Delete execution <a href="#delete-execution" id="delete-execution"></a>

使用此参数配置该操作：

* **Execution ID**：输入要删除的 execution ID。

## Activate、deactivate、delete 和 get workflow <a href="#activate-deactivate-delete-and-get-workflow" id="activate-deactivate-delete-and-get-workflow"></a>

**Activate**、**Deactivate**、**Delete** 和 **Get** workflow 操作都包含相同参数，可用于选择要执行操作的 **Workflow**。选项包括：

* **From list**：从列表中选择 workflow。
* **By URL**：输入 workflow 的 URL。
* **By ID**：输入 workflow 的 ID。

## Create workflow <a href="#create-workflow" id="create-workflow"></a>

使用此参数配置该操作：

* **Workflow Object**：输入包含新 workflow 详细信息的有效 JSON object。该 object 需要这些字段：
  * `name`
  * `nodes`
  * `connections`
  * `settings`

更多信息请参阅 [n8n API reference](/broken/spaces/r7wKI4I1BgdBCuq5Cvcx/pages/NjbdMwHH3QGuRDWQrwJY)。

## Get many workflows <a href="#get-many-workflows" id="get-many-workflows"></a>

使用这些参数配置该操作：

* **Return All**：设置是否返回所有结果（开启），或是否将结果限制为输入的 **Limit**（关闭）。
* **Limit**：如果关闭 **Return All** 控制项，设置要返回的结果数。

### Get many workflows filter <a href="#get-many-workflows-filters" id="get-many-workflows-filters"></a>

你可以使用这些 **Filters** 进一步配置该操作：

* **Return Only Active Workflows**：选择是否只返回 active workflow（开启），或返回 active 和 inactive workflow（关闭）。
* **Tags**：输入返回的 workflow 必须具有的逗号分隔 tag 列表。

## Update workflow <a href="#update-workflow" id="update-workflow"></a>

使用这些参数配置该操作：

* **Workflow**：选择要更新的 workflow。选项包括：
  * **From list**：从列表中选择 workflow。
  * **By URL**：输入 workflow 的 URL。
  * **By ID**：输入 workflow 的 ID。
* **Workflow Object**：输入用于更新 workflow 的有效 JSON object。该 object 需要这些字段：
  * `name`
  * `nodes`
  * `connections`
  * `settings`

更多信息请参阅 [n8n API | Update a workflow documentation](https://docs.n8n.io/api/api-reference/#tag/Workflow/paths/~1workflows~1%7Bid%7D/put)。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n 集成模板](https://n8n.io/integrations/n8n)或[搜索所有模板](https://n8n.io/workflows/)
