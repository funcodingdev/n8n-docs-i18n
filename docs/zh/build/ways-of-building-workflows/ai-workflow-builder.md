---
title: AI Workflow Builder
description: >-
  使用自然语言描述目标，创建、优化和调试工作流。
status: beta
nodeTitle: AI Workflow Builder
originalFilePath: advanced-ai/ai-workflow-builder.md
originalUrl: 'https://docs.n8n.io/advanced-ai/ai-workflow-builder'
url: 'https://docs.n8n.io/build/ways-of-building-workflows/ai-workflow-builder'
layout:
  description:
    visible: false
---

# AI Workflow Builder <a href="#ai-workflow-builder" id="ai-workflow-builder"></a>

AI Workflow Builder 允许你使用自然语言描述目标，创建、优化和调试工作流。

它会处理整个工作流构建过程，包括 node 选择、放置和配置，从而减少构建可用工作流所需的时间。

有关 AI Workflow Builder 的价格和可用性详情，请参阅 [n8n Plans and Pricing](https://n8n.io/pricing/)。

## 使用 builder <a href="#working-with-the-builder" id="working-with-the-builder"></a>

1. **描述你的工作流：** 选择示例 prompt，或用自然语言描述你的需求。
2. **监控构建过程：** builder 会在多个阶段提供实时反馈。
3. **审查并优化生成的工作流：** 检查所需 credential 和其他参数。使用 prompt 优化工作流。

    ![ai-workflow-builder.png](../../../build/.gitbook/assets/ai-workflow-builder.png)


### 可在 builder 中运行的命令 <a href="#commands-you-can-run-in-the-builder" id="commands-you-can-run-in-the-builder"></a>

- `/clear`：清除 LLM 的上下文，让你从头开始

## 了解 credits <a href="#understanding-credits" id="understanding-credits"></a>

### Credits 工作方式 <a href="#how-credits-work" id="how-credits-work"></a>

每当你向 builder 发送消息，请它创建或修改工作流时，就会计为一次 **interaction**，相当于一个 **credit**。

✅ **计为 interaction**

- 发送消息创建新工作流
- 请求 builder 修改现有工作流
- 工作流构建完成后，点击 builder 窗口中的 **Execute and refine** 按钮

❌ **不计为 interaction**

- 失败或产生生成错误的消息
- 你点击停止按钮手动停止的请求

### 获取更多 credits <a href="#getting-more-credits" id="getting-more-credits"></a>

如果你已用完月度限额，可以升级到更高计划。

有关计划和价格详情，请参阅 [n8n Plans and Pricing](https://n8n.io/pricing/)。

## AI 模型和数据处理 <a href="#ai-model-and-data-handling" id="ai-model-and-data-handling"></a>

以下数据会发送给 LLM：

- 你为创建、优化或调试工作流而提供的文本 prompt
- Node 定义、参数、connection 以及当前工作流定义
- 使用 builder 时加载的任何 mock execution 数据

以下数据不会发送：

- 你使用的任何 credential 详情
- 工作流过去的 execution
