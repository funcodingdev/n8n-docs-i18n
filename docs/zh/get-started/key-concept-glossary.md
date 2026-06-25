---
title: n8n 术语表
description: 使用 n8n 和相关软件时常见术语的词汇表。
contentType: reference
nodeTitle: Key concept glossary
originalFilePath: glossary.md
originalUrl: 'https://docs.n8n.io/glossary'
url: 'https://docs.n8n.io/get-started/key-concept-glossary'
layout:
  description:
    visible: false
---

#### AI agent <a href="#ai-agent" id="ai-agent"></a>

AI agents 是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。

#### AI chain <a href="#ai-chain" id="ai-chain"></a>

AI chains 允许你通过一系列组件调用，与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久记忆，因此不能用它们引用之前的上下文（这种场景应使用 AI agents）。

#### AI completion <a href="#ai-completion" id="ai-completion"></a>

Completions 是由 GPT 这类模型生成的响应。

#### AI embedding <a href="#ai-embedding" id="ai-embedding"></a>

Embeddings 是使用向量表示数据的数值化形式。AI 会通过在多个维度上映射值来理解复杂数据及其关系。Vector databases 或 vector stores 是专门用于存储和访问 embeddings 的数据库。

#### AI groundedness <a href="#ai-groundedness" id="ai-groundedness"></a>

在 AI 中，尤其是在检索增强生成（RAG）场景中，groundedness 和 ungroundedness 用于衡量模型响应在多大程度上准确反映了来源信息。模型会使用来源文档生成有依据的回答，而无依据回答则包含不受这些来源支持的推测或幻觉。

#### AI hallucination <a href="#ai-hallucination" id="ai-hallucination"></a>

AI hallucination 指大型语言模型（LLM）错误地感知到并不存在的模式或对象。

#### AI reranking <a href="#ai-reranking" id="ai-reranking"></a>

Reranking 是一种重新优化候选文档列表顺序的技术，用于提高搜索结果的相关性。检索增强生成（RAG）和其他应用会使用 reranking，为生成任务或后续任务优先选择最相关的信息。

#### AI memory <a href="#ai-memory" id="ai-memory"></a>

在 AI 场景中，memory 允许 AI 工具在多次交互之间保留消息上下文。例如，这可以让你与 AI agents 持续对话，而不必在每条消息中重复提交上下文。在 n8n 中，AI agent nodes 可以使用 memory，但 AI chains 不能。

#### AI retrieval-augmented generation (RAG) <a href="#ai-retrieval-augmented-generation-rag" id="ai-retrieval-augmented-generation-rag"></a>

Retrieval-augmented generation，简称 RAG，是一种让 LLM 访问外部来源中新信息的技术，用于提升 AI 响应质量。RAG 系统会检索相关文档，将响应建立在最新、特定领域或专有知识之上，以补充模型原始训练数据。RAG 系统通常依赖 vector stores 来高效管理和搜索这些外部数据。

#### AI tool <a href="#ai-tool" id="ai-tool"></a>

在 AI 场景中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI 模型可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

#### AI vector store <a href="#ai-vector-store" id="ai-vector-store"></a>

Vector store 或 vector database 用于存储信息的数学表示。它可以与 embeddings 和 retrievers 配合使用，创建一个 AI 在回答问题时可访问的数据库。

#### API <a href="#api" id="api"></a>

API，即 application programming interface，提供对某个服务的数据和功能的程序化访问。API 让软件更容易与外部系统交互。它们通常作为传统用户界面的替代方式存在，而传统界面一般通过浏览器或 UI 访问。

#### canvas (n8n) <a href="#canvas-n8n" id="canvas-n8n"></a>

Canvas 是 n8n editor UI 中构建工作流的主界面。你可以在 canvas 上添加并连接节点来编排工作流。

#### cluster node (n8n) <a href="#cluster-node-n8n" id="cluster-node-n8n"></a>

在 n8n 中，cluster nodes 是一组协同工作、为工作流提供功能的节点。它们由一个 root node 和一个或多个 sub nodes 组成，sub nodes 会扩展该节点的功能。

#### credential (n8n) <a href="#credential-n8n" id="credential-n8n"></a>

在 n8n 中，credentials 用于存储连接特定应用和服务所需的身份验证信息。使用你的身份验证信息（用户名和密码、API key、OAuth secrets 等）创建凭据后，就可以使用关联的 app node 与该服务交互。

#### data pinning (n8n) <a href="#data-pinning-n8n" id="data-pinning-n8n"></a>

Data pinning 允许你在工作流开发过程中临时冻结某个节点的输出数据。这样可以在不反复请求外部服务的情况下，使用可预测的数据开发工作流。生产工作流会忽略 pinned data，并在每次执行时请求新数据。

#### editor (n8n) <a href="#editor-n8n" id="editor-n8n"></a>

n8n editor UI 允许你创建和管理工作流。主区域是 canvas，你可以在其中通过添加、配置和连接节点来编排工作流。侧边和顶部面板可用于访问 UI 的其他区域，例如 credentials、templates、variables、executions 等。

#### entitlement (n8n) <a href="#entitlement-n8n" id="entitlement-n8n"></a>

在 n8n 中，entitlements 会在特定时间段内授予 n8n 实例访问受方案限制功能的权限。

Floating entitlements 是一组可分配给多个 n8n 实例的 entitlements。你可以重新分配 floating entitlement，将其访问权限转移到不同的 n8n 实例。

#### evaluation (n8n) <a href="#evaluation-n8n" id="evaluation-n8n"></a>

在 n8n 中，evaluation 允许你标记和整理执行历史，并将其与新的执行进行比较。你可以用它了解工作流在修改过程中随时间变化的表现。它在开发以 AI 为中心的工作流时尤其有用。

#### expression (n8n) <a href="#expression-n8n" id="expression-n8n"></a>

在 n8n 中，expressions 可以通过执行 JavaScript 代码动态填充节点参数。你不必提供静态值，而是可以使用 n8n expression 语法，基于前置节点、其他工作流或 n8n 环境中的数据定义该值。

#### LangChain <a href="#langchain" id="langchain"></a>

LangChain 是一个用于处理大型语言模型（LLM）的 AI 开发框架。LangChain 提供标准化系统，用于处理多种模型和其他资源，并将不同组件连接起来以构建复杂应用。

#### Large language model (LLM) <a href="#large-language-model-llm" id="large-language-model-llm"></a>

Large language models，简称 LLM，是专为自然语言处理（NLP）任务设计的 AI 机器学习模型。它们通过大量数据训练而成，用于构建语言和其他数据的概率模型。

#### node (n8n) <a href="#node-n8n" id="node-n8n"></a>

在 n8n 中，nodes 是用于编排和创建工作流的独立组件。Nodes 可以定义工作流何时运行，允许你获取、发送和处理数据，可以定义流程控制逻辑，并可连接外部服务。

#### project (n8n) <a href="#project-n8n" id="project-n8n"></a>

n8n projects 允许你将工作流、变量和凭据拆分到不同分组中，以便管理。Projects 通过共享和隔离相关资源，让团队更容易协作。

#### root node (n8n) <a href="#root-node-n8n" id="root-node-n8n"></a>

每个 n8n cluster node 都包含一个 root node，用于定义该 cluster 的主要功能。一个或多个 sub nodes 会连接到 root node，以扩展其功能。

#### sub node (n8n) <a href="#sub-node-n8n" id="sub-node-n8n"></a>

n8n cluster nodes 由一个或多个连接到 root node 的 sub nodes 组成。Sub nodes 会扩展 root node 的功能，提供对特定服务或资源的访问，或提供某类专用处理能力，例如计算器功能。

#### template (n8n) <a href="#template-n8n" id="template-n8n"></a>

n8n templates 是由 n8n 和社区成员设计的预构建工作流，你可以将它们导入 n8n 实例。使用 templates 时，可能需要填写凭据并调整配置，以适应你的需求。

#### trigger node (n8n) <a href="#trigger-node-n8n" id="trigger-node-n8n"></a>

Trigger node 是一种特殊节点，负责在特定条件发生时执行工作流。所有生产工作流都至少需要一个 trigger，用于决定工作流何时运行。

#### workflow (n8n) <a href="#workflow-n8n" id="workflow-n8n"></a>

n8n workflow 是一组用于自动化某个流程的节点。触发条件发生时，工作流开始执行，并按顺序运行以完成复杂任务。
