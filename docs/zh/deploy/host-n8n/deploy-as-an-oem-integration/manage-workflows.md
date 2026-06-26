---
title: 管理 workflows
description: >-
  n8n OEM deployment 中跨多个 users 或 organizations 管理 workflows 的 patterns。
contentType: howto
nodeTitle: Manage workflows
originalFilePath: hosting/oem-deployment/managing-workflows.md
originalUrl: 'https://docs.n8n.io/hosting/oem-deployment/managing-workflows'
url: >-
  https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/manage-workflows
layout:
  description:
    visible: false
---

# 管理 workflows <a href="#managing-workflows" id="managing-workflows"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6kdIvlPPl0XWVn5z8UJh/" %}

管理跨 teams 或 organizations 的 n8n OEM deployment 时，你很可能需要为多个 users 运行相同（或相似）的 workflows。可以使用两种选项：

| 方案 | 优点 | 缺点 |
| -------- | ---- | ---- |
| 为每个 user 创建一个 workflow | 不限制 workflow 的启动方式（可以使用任何 trigger） | 需要管理多个 workflows。 |
| 创建单个 workflow，并在执行时传入 user credentials | workflow management 更简单（只需更改一个 workflow）。 | 要运行 workflow，你的产品必须调用它 |

{% hint style="warning" %}
本文档中引用的 APIs 可能随时变化。请务必在每次 version upgrade 后检查功能是否仍然可用。
{% endhint %}

## 每个 user 一个 workflow <a href="#workflow-per-user" id="workflow-per-user"></a>

通常需要遵循三个步骤：

* 获取每个 user 的 credentials，以及基于 workflow 可能需要的任何 additional parameters。
* 为该 user 创建 [n8n credentials](#user-content-fn-1)[^1]。
* 创建 workflow。

### 1. 获取 user credentials <a href="#1-obtain-user-credentials" id="1-obtain-user-credentials"></a>

在这里，你需要捕获该 user 必须进行 authentication 的任何 node/service 的所有 credentials，以及特定 workflow 所需的任何 additional parameters。所需 credentials 和 parameters 取决于你的 workflow 以及你要实现的目标。

### 2. 创建 user credentials <a href="#2-create-user-credentials" id="2-create-user-credentials"></a>

获取所有相关 credential details 后，你可以继续在 n8n 中创建相关 service credentials。这可以通过 Editor UI 或 API call 完成。

#### 使用 Editor UI <a href="#using-the-editor-ui" id="using-the-editor-ui"></a>

1. 从 menu 中选择 **Credentials** > **New**。
1. 使用 drop-down 选择要创建的 **Credential type**，例如 *Airtable*。
    ![Create New Credentials drop-down](../../.gitbook/assets/create_new_credentials.png)
1. 在 **Create New Credentials** modal 中，输入该 user 对应的 credentials details，并选择可以访问这些 credentials 的 nodes。
    ![Create New Credentials modal](../../.gitbook/assets/create_new_credentials2.png)
1. 点击 **Create** 完成并保存。

#### 使用 API <a href="#using-the-api" id="using-the-api"></a>

Editor UI 使用的 frontend API 也可以被调用来实现相同结果。API endpoint format 为：`https://<n8n-domain>/rest/credentials`。

例如，要创建上面 Editor UI 示例中的 credentials，请求为：
```
POST https://<n8n-domain>/rest/credentials
```

请求 body：
```json
{
   "name":"MyAirtable",
   "type":"airtableApi",
   "nodesAccess":[
      {
         "nodeType":"n8n-nodes-base.airtable"
      }
   ],
   "data":{
      "apiKey":"q12we34r5t67yu"
   }
}
```

Response 会包含 new credentials 的 ID，创建此 user 的 workflow 时会用到它：
```json
{
   "data":{
      "name":"MyAirtable",
      "type":"airtableApi",
      "data":{
         "apiKey":"q12we34r5t67yu"
      },
      "nodesAccess":[
         {
            "nodeType":"n8n-nodes-base.airtable",
            "date":"2021-09-10T07:41:27.770Z"
         }
      ],
      "id":"29",
      "createdAt":"2021-09-10T07:41:27.777Z",
      "updatedAt":"2021-09-10T07:41:27.777Z"
   }
}
```

### 3. 创建 workflow <a href="#3-create-the-workflow" id="3-create-the-workflow"></a>

Best practice 是准备一个 “base” workflow，然后为每个新 user duplicate 并使用其 credentials（以及任何其他 details）进行 customize。

你可以使用 Editor UI 或 API call duplicate 并 customize template workflow。

#### 使用 Editor UI <a href="#using-the-editor-ui" id="using-the-editor-ui"></a>

1. 从 menu 中选择 **Workflows** > **Open**，打开要 duplicate 的 template workflow。

1. 选择 **Workflows** > **Duplicate**，然后为这个新 workflow 输入 name，并点击 **Save**。
    ![Duplicate workflow](../../.gitbook/assets/duplicate_workflow.png)

1. 更新所有相关 nodes，让它们使用此 user 的 credentials（上面已创建）。

1. **Save** 此 workflow，并使用右上角的 toggle 将它设为 **Active**。

#### 使用 API <a href="#using-the-api" id="using-the-api"></a>

1. 使用 endpoint 获取 template workflow 的 JSON：`https://<n8n-domain>/rest/workflows/<workflow_id>`
```
GET https://<n8n-domain>/rest/workflows/1012
```

Response 会包含所选 workflow 的 JSON data：
```json
{
  "data": {
    "id": "1012",
    "name": "Nathan's Workflow",
    "active": false,
    "nodes": [
      {
        "parameters": {},
        "name": "Start",
        "type": "n8n-nodes-base.start",
        "typeVersion": 1,
        "position": [
          130,
          640
        ]
      },
      {
        "parameters": {
          "authentication": "headerAuth",
          "url": "https://internal.users.n8n.cloud/webhook/custom-erp",
          "options": {
            "splitIntoItems": true
          },
          "headerParametersUi": {
            "parameter": [
              {
                "name": "unique_id",
                "value": "recLhLYQbzNSFtHNq"
              }
            ]
          }
        },
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 1,
        "position": [
          430,
          300
        ],
        "credentials": {
          "httpHeaderAuth": "beginner_course"
        }
      },
      {
        "parameters": {
          "operation": "append",
          "application": "appKBGQfbm6NfW6bv",
          "table": "processingOrders",
          "options": {}
        },
        "name": "Airtable",
        "type": "n8n-nodes-base.airtable",
        "typeVersion": 1,
        "position": [
          990,
          210
        ],
        "credentials": {
          "airtableApi": "Airtable"
        }
      },
      {
        "parameters": {
          "conditions": {
            "string": [
              {
                "value1": "={{$json[\"orderStatus\"]}}",
                "value2": "processing"
              }
            ]
          }
        },
        "name": "IF",
        "type": "n8n-nodes-base.if",
        "typeVersion": 1,
        "position": [
          630,
          300
        ]
      },
      {
        "parameters": {
          "keepOnlySet": true,
          "values": {
            "number": [
              {
                "name": "=orderId",
                "value": "={{$json[\"orderID\"]}}"
              }
            ],
            "string": [
              {
                "name": "employeeName",
                "value": "={{$json[\"employeeName\"]}}"
              }
            ]
          },
          "options": {}
        },
        "name": "Set",
        "type": "n8n-nodes-base.set",
        "typeVersion": 1,
        "position": [
          800,
          210
        ]
      },
      {
        "parameters": {
          "functionCode": "let totalBooked = items.length;\nlet bookedSum = 0;\n\nfor(let i=0; i < items.length; i++) {\n  bookedSum = bookedSum + items[i].json.orderPrice;\n}\nreturn [{json:{totalBooked, bookedSum}}]\n"
        },
        "name": "Function",
        "type": "n8n-nodes-base.function",
        "typeVersion": 1,
        "position": [
          800,
          400
        ]
      },
      {
        "parameters": {
          "webhookUri": "https://discord.com/api/webhooks/865213348202151968/oD5_WPDQwtr22Vjd_82QP3-_4b_lGhAeM7RynQ8Js5DzyXrQEnj0zeAQIA6fki1JLtXE",
          "text": "=This week we have {{$json[\"totalBooked\"]}} booked orders with a total value of {{$json[\"bookedSum\"]}}. My Unique ID: {{ $(\"HTTP Request\").params.headerParameters.parameters[0].value }}"
        },
        "name": "Discord",
        "type": "n8n-nodes-base.discord",
        "typeVersion": 1,
        "position": [
          1000,
          400
        ]
      },
      {
        "parameters": {
          "triggerTimes": {
            "item": [
              {
                "mode": "everyWeek",
                "hour": 9
              }
            ]
          }
        },
        "name": "Cron",
        "type": "n8n-nodes-base.cron",
        "typeVersion": 1,
        "position": [
          220,
          300
        ]
      }
    ],
    "connections": {
      "HTTP Request": {
        "main": [
          [
            {
              "node": "IF",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Start": {
        "main": [
          []
        ]
      },
      "IF": {
        "main": [
          [
            {
              "node": "Set",
              "type": "main",
              "index": 0
            }
          ],
          [
            {
              "node": "Function",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Set": {
        "main": [
          [
            {
              "node": "Airtable",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Function": {
        "main": [
          [
            {
              "node": "Discord",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Cron": {
        "main": [
          [
            {
              "node": "HTTP Request",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    },
    "createdAt": "2021-07-16T11:15:46.066Z",
    "updatedAt": "2021-07-16T12:05:44.045Z",
    "settings": {},
    "staticData": null,
    "tags": []
  }
}
```

1. 保存返回的 JSON data，并为新 user 更新所有相关 credentials 和 fields。

1. 使用更新后的 JSON 作为 request body，在 endpoint `https://<n8n-domain>/rest/workflows` 创建 new workflow：
```
POST https://<n8n-domain>/rest/workflows/
```

Response 会包含 new workflow 的 ID，下一步会用到它。

1. 最后，publish new workflow：
```
PATCH https://<n8n-domain>/rest/workflows/1012
```

在你的 JSON payload 中传入额外的 `active` value：
```json
// ...
"active":true,
"settings": {},
"staticData": null,
"tags": []
```

## Single workflow <a href="#single-workflow" id="single-workflow"></a>

要实现此方法，需要遵循四个步骤：

* 获取每个 user 的 credentials，以及基于 workflow 可能需要的任何 additional parameters。请参阅上面的[获取 user credentials](#1-obtain-user-credentials)。
* 为该 user 创建 n8n credentials。请参阅上面的[创建 user credentials](#2-create-user-credentials)。
* 创建 workflow。
* 按需调用 workflow。

### 创建 workflow <a href="#create-the-workflow" id="create-the-workflow"></a>

此 workflow 的 details 和 scope 会因具体 use case 而有很大差异，但有几个 design implementations 需要注意：

* 此 workflow 必须由 [Webhook](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.webhook) node 触发。
* Incoming webhook call 必须包含 user 的 credentials，以及所需的任何其他 workflow parameters。
* 每个需要 user credentials 的 node 都应使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes)，让 node 的 credential field 读取 webhook call 中提供的 credential。
* 保存并 publish workflow，确保 Webhook node 选择 production URL。更多信息请参考 [webhook node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.webhook)。

### 调用 workflow <a href="#call-the-workflow" id="call-the-workflow"></a>

对于每个新 user，或任何现有 user 在需要时，调用定义为 workflow trigger 的 webhook，并提供必要 credentials（以及任何其他 workflow parameters）。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。
