---
title: Guardrails node documentation
description: >-
  n8n 中 Guardrails node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
nodeTitle: Guardrails node documentation
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails
layout:
  description:
    visible: false
---

# Guardrails node <a href="#guardrails-node" id="guardrails-node"></a>

使用 Guardrails node 对文本执行安全、安全性和内容策略。你可以用它在将用户输入发送给 AI model _之前_ 进行验证，或在 workflow 中使用 AI model _输出_ 之前进行检查。

{% hint style="info" %}
**基于 LLM 的 Guardrails 需要 Chat Model 连接**

使用带有基于 LLM 的 guardrails 的 **Check Text for Violations** 操作时，此 node 需要将 Chat Model node 连接到其 Model 输入。许多 guardrail 检查（例如 Jailbreak、NSFW 和 Topical Alignment）都基于 LLM，并使用此连接评估输入文本。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用这些参数配置 Guardrails node。

### Operation <a href="#operation" id="operation"></a>

此 node 的操作 mode，用于定义其行为。

- **Check Text for Violations**：提供完整的 guardrails 集合。任何 violation 都会将 item 发送到 **Fail** 分支。
- **Sanitize Text**：提供 guardrails 子集，可检测 URL、正则表达式、secret key 或个人身份信息（PII），例如电话号码和信用卡号。此 node 会用 placeholder 替换检测到的 violation。

### Text To Check <a href="#text-to-check" id="text-to-check"></a>

guardrails 要评估的文本。通常，你会使用 expression 从前一个 node 映射此文本，例如来自用户查询或 AI model 响应的文本。

### Guardrails <a href="#guardrails" id="guardrails"></a>

选择一个或多个 guardrail，应用到 **Text To Check**。从列表添加 guardrail 后，其特定配置选项会显示在下方。

- **Keywords:** 检查输入文本中是否出现指定关键词。
    - **Keywords**：要阻止的词，使用逗号分隔。
- **Jailbreak:** 检测绕过 AI 安全措施或利用 model 的尝试。
    - **Customize Prompt**：（Boolean）如果开启，会出现一个文本输入框，其中包含 jailbreak detection model 的默认 prompt。你可以更改此 prompt 来微调 guardrail。
    - **Threshold**：介于 0.0 和 1.0 之间的值。表示 AI model 将输入标记为 jailbreak attempt 所需的置信度。阈值越高越严格。
- **NSFW:** 检测生成 Not Safe For Work（NSFW）内容的尝试。
    - **Customize Prompt**：（Boolean）如果开启，会出现一个文本输入框，其中包含 NSFW detection model 的默认 prompt。你可以更改此 prompt 来微调 guardrail。
    - **Threshold**：介于 0.0 和 1.0 之间的值，表示将内容标记为 NSFW 所需的置信度。
- **PII:** 检测文本中的个人身份信息（PII）。
    - **Type**：选择要扫描的 PII entity：
        - **All**：扫描所有可用 entity type。
        - **Selected**：允许你从列表中选择特定 entity。
    - **Entities**：（当 **Type** 为 **Selected** 时显示）要检测的 PII 类型 multi-select 列表（例如 `CREDIT_CARD`、`EMAIL_ADDRESS`、`PHONE_NUMBER` 和 `US_SSN`）。
- **Secret Keys:** 检测文本中是否存在 secret key 或 API credential。
    - **Permissiveness**：标记 secret key 时检测应有多严格或多宽松：
        - **Strict**
        - **Permissive**
        - **Balanced**
- **Topical Alignment:** 确保对话保持在预定义范围或主题内（也称为 "business scope"）。
    - **Prompt**：定义 _允许_ 主题的预设 prompt。guardrail 会检查 **Text To Check** 是否与此 prompt 对齐。
    - **Threshold**：介于 0.0 和 1.0 之间的值，表示将输入标记为 _off-topic_ 所需的置信度。
- **URLs:** 管理此 node 在输入文本中找到的 URL。除非你在 **Block All URLs Except** 中指定允许的 URL，否则它会将所有 URL 检测为 violation。
    - **Block All URLs Except**：（可选）你允许的 URL 列表，以逗号分隔。
    - **Allowed Schemes**：选择允许的 URL scheme（例如 `https`、`http`、`ftp` 和 `mailto`）。
    - **Block userinfo**：（Boolean）如果开启，此 node 会阻止包含用户 credential 的 URL（例如 `user:pass@example.com`），以防止 credential injection。
    - **Allow subdomain**：（Boolean）如果开启，此 node 会自动允许 **Block All URLs Except** 列表中任何 URL 的子域名（例如，如果列表中有 `example.com`，则允许 `sub.example.com`）。
- **Custom:** 定义你自己的基于 LLM 的自定义 guardrail。
    - **Name**：自定义 guardrail 的描述性名称（例如 "Check for rude language"）。
    - **Prompt**：指示 AI model 检查内容的 prompt。
    - **Threshold**：介于 0.0 和 1.0 之间的值，表示将输入标记为 violation 所需的置信度。
- **Custom Regex**：定义你自己的自定义正则表达式 pattern。
    - **Name**：自定义 pattern 的名称。此 node 在 **Sanitize Text** mode 中将此名称用作 placeholder。
    - **Regex**：你的正则表达式 pattern。

### Customize System Message <a href="#customize-system-message" id="customize-system-message"></a>

如果开启，会出现一个文本输入框，其中包含 guardrail 用来根据 schema 强制执行 threshold 和 JSON output 的消息。修改它可更改全局 guardrails 行为。
