---
contentType: explanation
nodeTitle: 为现有 node 自定义 API action
originalFilePath: integrations/custom-operations.md
originalUrl: 'https://docs.n8n.io/integrations/custom-operations'
url: 'https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes'
layout:
  description:
    visible: false
---

# 自定义 API operation <a href="#custom-api-operations" id="custom-api-operations"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/k23mQunNshTkLRuOqark/" %}

## 预定义 credential 类型 <a href="#predefined-credential-types" id="predefined-credential-types"></a>

预定义 credential 类型是 n8n 中已经存在的 credential。你可以在 HTTP Request 节点中使用预定义 credential 类型，而不是通用 credential。

例如：你创建了一个 Asana credential，用于 Asana node。之后，你想使用 Asana API 执行一个 Asana node 不支持的 operation。你可以在 HTTP Request 节点中使用现有 Asana credential 执行该 operation，而无需额外设置身份验证。

### 使用预定义 credential 类型 <a href="#using-predefined-credential-types" id="using-predefined-credential-types"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ZmZC9v8B1NG5lgRY44yF/" %}


### Credential scope <a href="#credential-scopes" id="credential-scopes"></a>

一些现有 credential 类型具有特定 scope：也就是它们可使用的 endpoint。选择 credential 类型时，n8n 会对此发出提示。

例如，按照[使用预定义 credential 类型](#using-predefined-credential-types)中的步骤操作，并选择 **Google Calendar OAuth2 API** 作为 **Credential Type**。n8n 会显示一个框，列出你可以与此 credential 类型一起使用的两个 endpoint：

![scope 框](../.gitbook/assets/scopes.png)
