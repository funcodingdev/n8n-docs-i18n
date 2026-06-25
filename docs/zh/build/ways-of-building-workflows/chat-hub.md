---
title: Chat Hub
status: beta
nodeTitle: Chat Hub
originalFilePath: advanced-ai/chat-hub.md
originalUrl: https://docs.n8n.io/advanced-ai/chat-hub
url: https://docs.n8n.io/build/ways-of-building-workflows/chat-hub
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

# Chat Hub

## 概览 <a href="#overview" id="overview"></a>

Chat Hub 是一个集中式 AI 聊天界面，你可以在其中访问多个 AI 模型、与 n8n agent 交互，并创建自己的 agent。Chat Hub 还引入了 Chat user 角色，让用户无需访问 n8n 工作流即可与聊天界面交互。

## 如何使用 <a href="#how-to-use" id="how-to-use"></a>

如需使用 Chat Hub，在导航栏中找到 **Chat** 选项，选择模型，然后开始对话。

### 创建简单的个人 agent <a href="#creating-simple-personal-agents" id="creating-simple-personal-agents"></a>

为了让 AI 更可靠地处理简单、重复的任务，你可以创建带有自定义指令的 Custom Agents。如需创建简单的个人 agent：

1. 点击 **Personal Agents**，然后点击 **+New Agent**。
2. 定义名称、描述、system prompt、首选模型和 tool 访问权限。
3. 选择 **Save**。

创建后，你可以从模型选择器中选择该 personal agent。

### 使用 n8n workflow agents <a href="#using-n8n-workflows-agents" id="using-n8n-workflows-agents"></a>

对于更复杂的场景，可以使用 n8n workflow agents（由你或同事构建）让工作流可在 Chat Hub 中使用。目前，你只能使用带有 **Chat Trigger** 且在 **Agent** node 中启用 streaming 的工作流。如需让工作流可用：

1. 打开选中的工作流。
2.  Open the **Chat Trigger**.<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>只有最新版本的 chat trigger 才能工作。如需获得最新 chat trigger 版本，请删除现有 chat trigger 并插入新的。</p></div>
3. 启用 **Make Available in n8n Chat** 选项，并设置 personal agent 的名称和描述。
4. 确保你的 AI Agent node 已启用 **Enable Streaming** 选项。
5. 激活你的工作流。

定义完成后，你可以从 Chat Hub 的模型选择器中选择你的工作流。你的同事需要通过共享获得工作流访问权限，或该工作流位于他们至少拥有 viewer 访问权限的 project 中。

## 管理权限 <a href="#managing-permissions" id="managing-permissions"></a>

你可以通过 n8n 的角色系统定义哪些用户可以执行哪些操作。Chat Hub 还提供更多方式控制谁可以使用什么。

### Chat user 角色 <a href="#chat-user-role" id="chat-user-role"></a>

Chat user 是面向组织中只想使用工作流、而不构建工作流的用户的角色。Chat user 默认只会看到聊天界面，不能添加 credential 或工作流。

Chat user 仅适用于 Starter、Pro、Business 和 Enterprise 计划。

### Provider 设置 <a href="#provider-settings" id="provider-settings"></a>

管理员可以控制用户可在 Chat Hub 中访问哪些模型和 provider。这包括：

* 启用或禁用特定模型和 provider
* 阻止用户添加自己的模型
* 为每个 provider 设置默认 credential
* 限制用户添加自己的 credential（通过 n8n 的权限系统）

如需管理这些设置，前往 **Settings > Chat** 并编辑 providers。

## 注意事项和限制 <a href="#considerations-and-limitations" id="considerations-and-limitations"></a>

1. 创建简单 personal agent 时，不能添加文件知识。
2. Tool 选择仅限少数选项。
3. 只有包含 [Chat Trigger node](/broken/spaces/BKcbOzIWja8NfqKDcqHc/pages/ufgV9cVbZYhO7UuKUvU1) 且 [AI Agent node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent) 已启用 streaming 的工作流，才能作为 workflow agent 使用。你的工作流必须满足特定要求。
