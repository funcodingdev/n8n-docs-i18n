---
title: External hooks
description: >-
  使用 external hooks，在 n8n 运行特定 operation 时执行自定义代码。
contentType: howto
nodeTitle: External hooks
originalFilePath: hosting/configuration/external-hooks.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/external-hooks'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/external-hooks'
layout:
  description:
    visible: false
---

# External hooks <a href="#external-hooks" id="external-hooks"></a>

External hooks 允许你在 n8n 执行特定 operation 时运行自定义代码。你可以用它们记录数据、修改数据，或通过抛出错误来禁止某个 action。

有两种类型：

- **Backend hooks**：在 server-side 运行，使用 `EXTERNAL_HOOK_FILES` 环境变量注册。
- **Frontend hooks**：在 browser 中运行，通过 script tag 加载。

有关用于注册 hooks 的环境变量，请参阅 [External hooks environment variables](basic-configuration/use-environment-variables/external-hooks.md)。

## Backend hooks <a href="#backend-hooks" id="backend-hooks"></a>

### 可用 hooks <a href="#available-hooks" id="available-hooks"></a>

| Hook | Arguments | Description |
| :------- | :---------| :---------- |
| `credentials.create` | `[credentialData: ICredentialsDb]` | 在创建新 credentials 前调用。可用于限制 credentials 数量。 |
| `credentials.delete` | `[id: credentialId]` | 在删除 credentials 前调用。 |
| `credentials.update` | `[credentialData: ICredentialsDb]` | 在 n8n 保存现有 credentials 前调用。 |
| `frontend.settings` | `[frontendSettings: IN8nUISettings]` | 在 n8n 启动时调用。例如，可用于覆盖显示的 OAuth URL 等 frontend data。 |
| `n8n.ready` | `[app: App]` | 在 n8n ready 后调用一次。例如，可用于注册自定义 API endpoints。 |
| `n8n.stop` |  | 在 n8n process 停止时调用。可用于保存一些 process data。 |
| `oauth1.authenticate` | `[oAuthOptions: clientOAuth1.Options, oauthRequestData: {oauth_callback: string}]` | 在 OAuth1 authentication 前调用。可用于覆盖 OAuth callback URL。 |
| `oauth2.callback` | `[oAuth2Parameters: {clientId: string, clientSecret: string \| undefined, accessTokenUri: string, authorizationUri: string, redirectUri: string, scopes: string[]}]` | 在 OAuth2 callback 中调用。可用于覆盖 OAuth callback URL。 |
| `workflow.activate` | `[workflowData: IWorkflowDb]` | 在 workflow 激活前调用。可用于限制 active workflows 数量。 |
| `workflow.afterCreate` | `[workflowId: string]` | 在创建 workflow 后调用。 |
| `workflow.afterDelete` | `[workflowId: string]` | 在删除 workflow 后调用。 |
| `workflow.afterUpdate` | `[workflowData: IWorkflowBase]` | 在保存现有 workflow 后调用。 |
| `workflow.create` | `[workflowData: IWorkflowBase]` | 在创建 workflow 前调用。可用于限制已保存 workflows 数量。 |
| `workflow.delete` | `[workflowId: string]` | 在删除 workflow 前调用。 |
| `workflow.postExecute` | `[run: IRun, workflowData: IWorkflowBase]` | 在执行 workflow 后调用。 |
| `workflow.preExecute` | `[workflow: Workflow, mode: WorkflowExecuteMode, workflowContext: WorkflowHookContextService]` | 在执行 workflow 前调用。可用于计数或限制 workflow executions 数量。使用 `workflowContext` 参数的示例请参阅 [Hook examples](#hook-examples)（仅从 2.23.0 版本起可用）。 |
| `workflow.update` | `[workflowData: IWorkflowBase]` | 在保存现有 workflow 前调用。 |
| `workflow.afterArchive` | `[workflowId: string]` | 在你 archive workflow 后调用。 |
| `workflow.afterUnarchive` | `[workflowId: string]` | 在你从 archive 恢复 workflow 后调用。 |

### 注册 hooks <a href="#registering-hooks" id="registering-hooks"></a>

通过注册包含 hook functions 的 hook file 来设置 hooks。要注册 hook，请设置环境变量 `EXTERNAL_HOOK_FILES`。

你可以将该变量设置为单个文件：

`EXTERNAL_HOOK_FILES=/data/hook.js`

或设置为由冒号分隔的多个文件：

`EXTERNAL_HOOK_FILES=/data/hook1.js:/data/hook2.js`

### Hook files <a href="#hook-files" id="hook-files"></a>

Hook files 是常规 JavaScript files，格式如下：

```js
module.exports = {
    "frontend": {
        "settings": [
            async function (settings) {
                settings.oauthCallbackUrls.oauth1 = 'https://n8n.example.com/oauth1/callback';
                settings.oauthCallbackUrls.oauth2 = 'https://n8n.example.com/oauth2/callback';
            }
        ]
    },
    "workflow": {
        "activate": [
            async function (workflowData) {
                const activeWorkflows = await this.dbCollections.Workflow.count({ active: true });

                if (activeWorkflows > 1) {
                    throw new Error(
                        'Active workflow limit reached.'
                    );
                }
            }
        ]
    }
}
```

### Hook examples <a href="#hook-examples" id="hook-examples"></a>

#### 缺少必需 tag 时阻止 workflow execution <a href="#block-workflow-execution-if-a-required-tag-is-missing" id="block-workflow-execution-if-a-required-tag-is-missing"></a>

请注意：`workflowContext` 参数仅从 n8n 版本 `2.23.0` 起提供给 `workflow.preExecute` hooks。

使用 `workflow.preExecute` 在 workflow 没有必需 tag 时中止 execution：

```js
module.exports = {
	workflow: {
		preExecute: [
			async function (workflow, mode, workflowContext) {
				const requiredTag = 'exampleTag';
				const workflowTags = await workflowContext.getWorkflowTags(workflow.id);
				if (!workflowTags.includes(requiredTag)) {
					throw new Error(`Workflow is missing required tag "${requiredTag}", aborting`);
				}
			},
		],
	},
};
```

### Hook functions <a href="#hook-functions" id="hook-functions"></a>

一个 hook 或 hook file 可以包含多个 hook functions，所有 functions 会依次执行。

如果 hook function 的参数是 objects，可以修改该参数的数据来改变 n8n 的行为。

你还可以在任何 hook function 中使用 `this.dbCollections` 访问 database（请参阅上面 [Hook files](#hook-files) 中的代码示例）。

## 前端 external hooks <a href="#frontend-external-hooks" id="frontend-external-hooks"></a>

和 backend external hooks 一样，你可以在 frontend code 中定义 external hooks，让 n8n 在用户执行特定 operation 时执行。你可以用它们记录数据、修改数据等。

### 可用 hooks <a href="#available-hooks" id="available-hooks"></a>

| Hook | Description |
| :------- | :---------- |
| `credentialsEdit.credentialTypeChanged` | 现有 credential type 变化时调用。 |
| `credentials.create` | 有人创建新 credential 时调用。 |
| `credentialsList.dialogVisibleChanged` |  |
| `dataDisplay.nodeTypeChanged` |  |
| `dataDisplay.onDocumentationUrlClick` | 有人选择帮助文档链接时调用。 |
| `execution.open` | 打开现有 execution 时调用。 |
| `executionsList.openDialog` | 有人从现有 Workflow Executions 中选择 execution 时调用。 |
| `expressionEdit.itemSelected` |  |
| `expressionEdit.dialogVisibleChanged` |  |
| `nodeCreateList.filteredNodeTypesComputed` |  |
| `nodeCreateList.nodeFilterChanged` | 有人对 node panel filter 做任何更改时调用。 |
| `nodeCreateList.selectedTypeChanged` |  |
| `nodeCreateList.mounted` |  |
| `nodeCreateList.destroyed` |  |
| `nodeSettings.credentialSelected` |  |
| `nodeSettings.valueChanged` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.addNodeButton` |  |
| `nodeView.mount` |  |
| `pushConnection.executionFinished` |  |
| `showMessage.showError` |  |
| `runData.displayModeChanged` |  |
| `workflow.activeChange` |  |
| `workflow.activeChangeCurrent` |  |
| `workflow.afterUpdate` | 有人更新现有 workflow 时调用。 |
| `workflow.open` |  |
| `workflowRun.runError` |  |
| `workflowRun.runWorkflow` | workflow 执行时调用。 |
| `workflowSettings.dialogVisibleChanged` |  |
| `workflowSettings.saveSettings` | 有人保存 workflow settings 时调用。 |

### 注册 frontend hooks <a href="#registering-frontend-hooks" id="registering-frontend-hooks"></a>

你可以通过在页面上加载 hooks script 来设置 hooks。一种方式是在项目中创建 hooks file，并在 `editor-ui/public/index.html` 文件中添加 script tag：

```html
<script src="frontend-hooks.js"></script>
```

### Frontend hook files <a href="#frontend-hook-files" id="frontend-hook-files"></a>

前端 external hook files 是常规 JavaScript files，格式如下：

```js
window.n8nExternalHooks = {
  nodeView: {
    mount: [
      function (store, meta) {
        // do something
      },
    ],
    createNodeActiveChanged: [
      function (store, meta) {
        // do something
      },
      function (store, meta) {
        // do something else
      },
    ],
    addNodeButton: [
      function (store, meta) {
        // do something
      },
    ],
  },
};
```

### Frontend hook functions <a href="#frontend-hook-functions" id="frontend-hook-functions"></a>

你可以为每个 hook 定义多个 hook functions。n8n 会使用以下 arguments 调用每个 hook function：

* `store`：Vuex store object。你可以用它更改或获取 store 中的数据。
* `metadata`：包含 hook 提供的任何数据的 object。要查看传入内容，请在 `editor-ui` package 中搜索该 hook。
