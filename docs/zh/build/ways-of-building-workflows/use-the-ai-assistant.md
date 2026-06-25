---
contentType: explanation
nodeTitle: Use the AI assistant
originalFilePath: manage-cloud/ai-assistant.md
originalUrl: https://docs.n8n.io/manage-cloud/ai-assistant
url: https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant
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

# 使用 AI assistant

n8n AI Assistant 可帮助你顺畅地构建、调试和优化工作流。从回答 n8n 相关问题，到提供编码和表达式[^1]帮助，AI Assistant 可以简化你的工作流构建过程，并在你探索 n8n 功能时提供支持。

## 当前能力 <a href="#current-capabilities" id="current-capabilities"></a>

AI Assistant 提供了一系列支持工具：

* **Debug helper**：识别并排查工作流中的 node execution 问题，让工作流稳定运行。
* **Answer n8n questions**：即时回答你的 n8n 相关问题，无论是特定功能还是通用功能。
* **Coding support**：提供编码指导，包括 SQL 和 JSON，帮助优化 node 和数据处理。
* **Expression assistance**：了解如何创建和优化[表达式](../work-with-data/expressions-versus-data-nodes.md)，充分发挥工作流能力。
* **Credential setup tips**：了解如何安全高效地设置和管理 node [credentials](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials)。

## 充分利用 Assistant 的技巧 <a href="#tips-for-getting-the-most-out-of-the-assistant" id="tips-for-getting-the-most-out-of-the-assistant"></a>

1. **进行对话**：AI Assistant 可以与你逐步协作。如果某个建议不符合你的需要，直接告诉它。你提供的上下文越多，推荐效果越好。
2. **提出具体问题**：为获得最佳效果，请提出聚焦的问题（例如，“How do I set up credentials for Google Sheets?”）。问题越清晰，assistant 的效果越好。
3. **基于建议迭代**：可以继续基于 assistant 的回答扩展。尝试不同方法，并根据 assistant 的反馈持续优化，逐步接近理想方案。
4. **可以尝试的事项**：
   * 调试你看到的任何错误
   * 询问如何设置 credential
   * "Explain what this workflow does."
   * "I need your help to write code: \[Explain your code here]"
   * "How can I build X in n8n?"

## AI 使用设置 <a href="#ai-usage-settings" id="ai-usage-settings"></a>

{% hint style="info" %}
适用于 n8n v2.7.0 及以上版本。
{% endhint %}

你可以在 n8n 实例中进入 **Settings** > **AI Usage** 管理 AI 使用设置。在这里，你可以控制与 AI Assistant 共享哪些数据。

这些设置仅对实例 owner 和管理员可用，并会应用于该实例上的所有用户。

![ai\_usage\_settings.png](../../../build/.gitbook/assets/ai_usage_settings.png)

切换是否与 AI Assistant 共享实际工作流数据（例如 node 名称、参数和结构）。禁用此选项会限制 assistant 基于你的工作流提供上下文感知帮助的能力。

由于访问工作流数据是 AI Workflow builder 正常工作的必要条件，**禁用此选项也会禁用 AI Workflow builder 功能**。

### 禁用发送数据 <a href="#disable-sending-data" id="disable-sending-data"></a>

如需停止向 AI Assistant 发送实际数据值，请在 **AI Usage** 设置页面关闭 **Send actual data values** 复选框。

## 常见问题 <a href="#faqs" id="faqs"></a>

### Assistant 有哪些上下文？ <a href="#what-context-does-the-assistant-have" id="what-context-does-the-assistant-have"></a>

AI Assistant 可以访问 n8n 屏幕上显示的所有元素，但不包括实际输入和输出数据值（例如客户信息）。如需了解 n8n 与 Assistant 共享哪些数据，请参阅 [AI in n8n](https://app.gitbook.com/s/ukPPOMQ6NId4gpAIkPXa/#ai-in-n8n)。

### 谁可以使用 Assistant？ <a href="#who-can-use-the-assistant" id="who-can-use-the-assistant"></a>

Cloud 计划中的任何用户都可以使用 assistant。

### Assistant 如何工作？ <a href="#how-does-the-assistant-work" id="how-does-the-assistant-work"></a>

Assistant 的底层逻辑基于 n8n 的高级 AI 能力构建。它结合了多个专门处理 n8n 不同领域的 agent[^2]、用于从文档和社区论坛收集知识的 RAG，以及自定义 prompt、memory[^3] 和上下文。

[^1]: 在 n8n 中，表达式允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n 表达式语法，基于前序 node、其他 workflow 或 n8n 环境中的数据来定义值。
[^2]: AI agent 是能够响应请求、做出决策并为用户执行真实任务的人工智能系统。它们使用大语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^3]: 在 AI 上下文中，memory 允许 AI 工具在交互之间保留消息上下文。例如，这样你可以与 AI agent 持续对话，而无需每条消息都提交持续上下文。在 n8n 中，AI agent node 可以使用 memory，但 AI chain 不能。
