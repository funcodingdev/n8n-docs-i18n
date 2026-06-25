---
title: AI 编码
description: 使用 GPT 在 Code node 中生成代码。
contentType: explanation
nodeTitle: Get coding help from AI
originalFilePath: code/ai-code.md
originalUrl: 'https://docs.n8n.io/code/ai-code'
url: 'https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai'
layout:
  description:
    visible: false
---

# 使用 GPT 进行 AI 编码 <a href="#ai-coding-with-gpt" id="ai-coding-with-gpt"></a>

自托管不可用。

不支持 Python。
///

## 在 Code node 中使用 AI <a href="#use-ai-in-the-code-node" id="use-ai-in-the-code-node"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/1MYzyKWyHTaQMU44vlTt/" %}

## 使用限制 <a href="#usage-limits" id="usage-limits"></a>

在试用阶段没有使用限制。如果 n8n 将该功能转为长期功能，则可能会根据你的 pricing tier 设置使用限制。

## 功能限制 <a href="#feature-limits" id="feature-limits"></a>

n8n 中的 ChatGPT 实现有以下限制：

* AI 会编写用于操作 n8n workflow 数据的代码。你不能要求它从其他来源拉取数据。
* AI 不知道你的数据，只知道 schema，因此你需要告诉它如何找到要提取的数据、如何检查 null 等信息。
* 在运行 AI query 之前，Code node 之前的 node 必须先执行并向 Code node 传递数据。
* 不适用于很大的输入数据 schema。
* 如果 code node 之前有很多 node，可能会出现问题。

## 编写好的 prompt <a href="#writing-good-prompts" id="writing-good-prompts"></a>

写好 prompt 可以提高获得有用代码的概率。

一些通用建议：

* 提供示例：如果可以，给出期望输出示例。这有助于 AI 更好地理解你想要的转换或逻辑。
* 描述处理步骤：如果有特定的处理步骤或逻辑需要应用到数据上，请按顺序列出。例如："First, filter out all users under 18. Then, sort the remaining users by their last name."
* 避免歧义：AI 可以理解多种指令，但清晰、直接的表达可以确保你获得最准确的代码。不要说 "Get the older users"，可以说 "Filter users who are 60 years and above."
* 明确你期望的输出。你想要转换、过滤、聚合还是排序数据？请尽可能提供详细信息。

一些 n8n 特定建议：

* 思考输入数据：确保 ChatGPT 知道你想访问数据中的哪些部分，以及输入数据代表什么。你可能需要告诉 ChatGPT n8n 内置方法和变量可用。
* 声明 node 之间的交互：如果你的逻辑涉及多个 node 的数据，请说明它们应该如何交互。"Merge the output of 'Node A' with 'Node B' based on the 'userID' property"。如果你希望数据来自某些 node 或忽略其他 node，请明确说明："Only consider data from the 'Purchases' node and ignore the 'Refunds' node."
* 确保输出与 n8n 兼容。关于 n8n 所需的数据结构，更多信息请参阅[数据结构](../work-with-data/understand-n8ns-data-structure.md)。

### 示例 prompt <a href="#example-prompts" id="example-prompts"></a>

这些示例展示了一系列可能的 prompt 和任务。

#### 示例 1：在第二个数据集中查找一条数据 <a href="#example-1-find-a-piece-of-data-inside-a-second-dataset" id="example-1-find-a-piece-of-data-inside-a-second-dataset"></a>

要自己尝试该示例，请[下载示例 workflow](/_workflows/ai-code/find-a-piece-of-data.json) 并导入到 n8n。

在第三个 Code node 中输入此 prompt：

> Slack 数据只包含一个 item。输入数据表示所有 Notion 用户。有时保存 email 的 person property 可能为 null。我想找到 Slack 用户的 notionId 并返回它。

查看 AI 生成的代码。

这是你需要的 JavaScript：

```js
const slackUser = $("Mock Slack").all()[0];
const notionUsers = $input.all();
const slackUserEmail = slackUser.json.email;

const notionUser = notionUsers.find(
  (user) => user.json.person && user.json.person.email === slackUserEmail
);

return notionUser ? [{ json: { notionId: notionUser.json.id } }] : [];
```

#### 示例 2：数据转换 <a href="#example-2-data-transformation" id="example-2-data-transformation"></a>

要自己尝试该示例，请[下载示例 workflow](/_workflows/ai-code/data-transformation.json) 并导入到 n8n。

在 **Join items** Code node 中输入此 prompt：

> 返回一行文本，其中所有 username 用逗号列出。每个 username 都应使用双引号包裹。

查看 AI 生成的代码。

这是你需要的 JavaScript：

```js
const items = $input.all();
const usernames = items.map((item) => `"${item.json.username}"`);
const result = usernames.join(", ");
return [{ json: { usernames: result } }];
```

#### 示例 3：汇总数据并创建 Slack 消息 <a href="#example-3-summarize-data-and-create-a-slack-message" id="example-3-summarize-data-and-create-a-slack-message"></a>

要自己尝试该示例，请[下载示例 workflow](/_workflows/ai-code/summarize-data.json) 并导入到 n8n。

在 **Summarize** Code node 中输入此 prompt：

> 创建一段用于 Slack 的 markdown 文本，统计提交了多少 idea、feature 和 bug。提交类型保存在 property_type 字段中。feature 的 property 是 "Feature"，bug 的 property 是 "Bug"，idea 的 property 是 "Bug"。另外，在该消息中列出投票数最高的五个提交。使用 "<url|text>" 作为链接的 markdown。

查看 AI 生成的代码。

这是你需要的 JavaScript：

```js
const submissions = $input.all();

// Count the number of ideas, features, and bugs
let ideaCount = 0;
let featureCount = 0;
let bugCount = 0;

submissions.forEach((submission) => {
  switch (submission.json.property_type[0]) {
    case "Idea":
      ideaCount++;
      break;
    case "Feature":
      featureCount++;
      break;
    case "Bug":
      bugCount++;
      break;
  }
});

// Sort submissions by votes and take the top 5
const topSubmissions = submissions
  .sort((a, b) => b.json.property_votes - a.json.property_votes)
  .slice(0, 5);

let topSubmissionText = "";
topSubmissions.forEach((submission) => {
  topSubmissionText += `<${submission.json.url}|${submission.json.name}> with ${submission.json.property_votes} votes\n`;
});

// Construct the Slack message
const slackMessage = `*Summary of Submissions*\n
Ideas: ${ideaCount}\n
Features: ${featureCount}\n
Bugs: ${bugCount}\n
Top 5 Submissions:\n
${topSubmissionText}`;

return [{ json: { slackMessage } }];
```

### 显式引用输入 node 数据 <a href="#reference-incoming-node-data-explicitly" id="reference-incoming-node-data-explicitly"></a>

如果你的输入数据包含嵌套字段，使用 dot notation 引用它们可以帮助 AI 理解你想要的数据。

!["n8n code node 的截图，突出显示如何在 AI query 中使用 dot notation 引用数据"](../.gitbook/assets/reference-data-dot-notation.png)

要自己尝试该示例，请[下载示例 workflow](/_workflows/ai-code/reference-incoming-data-explicitly.json) 并导入到 n8n。

在第二个 Code node 中输入此 prompt：

> "Mock data" 中的数据表示人员列表。对于每个人，返回一个包含 personal_info.first_name 和 work_info.job_title 的新 item。

这是你需要的 JavaScript：

```js
const items = $input.all();
const newItems = items.map((item) => {
  const firstName = item.json.personal_info.first_name;
  const jobTitle = item.json.work_info.job_title;
  return {
    json: {
      firstName,
      jobTitle,
    },
  };
});
return newItems;
```

### 相关资源 <a href="#related-resources" id="related-resources"></a>

Pluralsight 提供了一篇简短指南：[How to use ChatGPT to write code](https://www.pluralsight.com/blog/software-development/how-use-chatgpt-programming-coding)，其中包含示例 prompt。



## 修复代码 <a href="#fixing-the-code" id="fixing-the-code"></a>

AI 生成的代码可能无需任何修改就能工作，但你也可能需要编辑它。你需要了解 n8n 的[数据结构](../work-with-data/understand-n8ns-data-structure.md)。n8n 的内置方法和变量也可能有帮助。
