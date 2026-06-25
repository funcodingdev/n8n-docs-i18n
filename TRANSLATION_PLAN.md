# n8n 文档简体中文翻译计划

## 目标

将 `docs/` 下的英文 Markdown 文档分批翻译为简体中文，并在 `docs/zh/` 中保持与英文文档一致的相对路径，方便后续同步 n8n 官方上游仓库。

当前基线：

- 英文 Markdown 文件数：1402
- 已创建中文 Markdown 文件数：243
- 中文根目录：`docs/zh/`

## 路径规则

- 英文源文档保留在 `docs/`，尽量不改动，便于合并 upstream。
- 中文翻译文档放在 `docs/zh/`。
- 中文文件路径必须镜像英文文件路径。

示例：

```text
docs/get-started/learning-paths.md
docs/zh/get-started/learning-paths.md
```

## 翻译规则

- 保留 Markdown 结构、front matter 字段、相对链接、代码块、命令、环境变量、文件路径和 API 字段。
- 页面标题、正文、列表、表格说明翻译为简体中文。
- n8n、workflow、node、credential、execution 等核心产品词第一次出现时可保留英文或采用中英混排，避免误译产品概念。
- 外部链接不改目标地址；指向英文站内文档的相对链接保持同路径，依赖 `docs/zh/` 镜像结构逐步补齐。
- 每批翻译后运行轻量检查：
  - `git diff --check`
  - 检查新增中文文件是否位于 `docs/zh/`
  - 抽查关键页面的语言切换路径

## 批次顺序

1. `get-started/`：新用户入口、学习路径、核心概念。
2. `build/`：工作流构建、数据处理、AI 集成、流程逻辑。
3. `integrations/`：内置节点、凭据、触发器、社区节点。
4. `deploy/`：自托管、Cloud、环境变量、部署方式。
5. `administer/`：用户、凭据、安全、日志、源代码控制。
6. `connect/`：API、MCP、节点开发。
7. `privacy-and-security/`、`release-notes/`、`contribute/`：政策、版本说明、贡献指南。
8. 其余散落页面和补漏文件。

## 进度表

| 批次 | 范围 | 状态 | 备注 |
| --- | --- | --- | --- |
| 0 | i18n 基础结构 | 已完成 | 已添加顶部语言切换和 `docs/zh/index.md` |
| 1.1 | `get-started/README.md`、`SUMMARY.md`、`learning-paths.md` | 已完成 | 第一批入口页 |
| 1.2 | `get-started/choose-how-to-use-n8n.md` | 已完成 | 选择使用方式 |
| 1.3 | `get-started/build-your-first-workflow.md` | 已完成 | 首个工作流教程 |
| 1.4 | `get-started/key-concept-glossary.md` | 已完成 | 关键概念术语表 |
| 2.1 | `build/README.md`、`SUMMARY.md`、`keyboard-shortcuts.md` | 已完成 | Build 顶层入口 |
| 2.2 | `build/flow-logic/` | 已完成 | 流程逻辑 |
| 2.3.1 | `build/manage-workflows/` | 已完成 | 工作流管理 |
| 2.3.2 | `build/understand-workflows/` 顶层 | 已完成 | 工作流概念、创建、credential、保存发布 |
| 2.3.3 | `build/understand-workflows/workflow-components/` | 已完成 | 工作流组件 |
| 2.3.4 | `build/understand-workflows/understand-executions/` | 已完成 | 执行概念、列表、调试和重试 |
| 2.3.5 | `build/ways-of-building-workflows/` | 已完成 | 构建工作流的方式、MCP、AI assistant |
| 2.4.1 | `build/work-with-data/` 顶层 | 已完成 | 数据处理概览、data tables、pin/mock、数据结构 |
| 2.4.2 | `build/work-with-data/reference-data/` | 已完成 | 引用数据和 item linking |
| 2.4.3 | `build/work-with-data/transform-data/` 顶层 | 已完成 | 转换数据概览和 expression 转换 |
| 2.4.4.1 | `build/work-with-data/transform-data/expression-reference/` 短参考页 | 已完成 | BinaryFile、Boolean、CustomData、Date、ExecData、HTTPResponse、Item、NodeInputData、NodeOutputData、PrevNodeData、WorkflowData |
| 2.4.4.2 | `build/work-with-data/transform-data/expression-reference/` 长参考页 | 已完成 | README、Array、DateTime、Number、Object、Root、String |
| 2.4.5 | `build/work-with-data/handle-special-data-types/` | 已完成 | 特殊数据类型 |
| 2.5.1 | `build/code-in-n8n/` 顶层 | 已完成 | README、使用 Code node、AI 编码、自定义变量 |
| 2.5.2 | `build/code-in-n8n/use-built-in-shortcuts/` | 已完成 | 内置快捷方式、HTTP node、JMESPath、LangChain Code node、n8n metadata |
| 2.5.3 | `build/code-in-n8n/cookbook/` | 已完成 | Code cookbook、内置变量示例、Code node 示例、HTTP Request 示例 |
| 2.6.1 | `build/integrate-ai/` 顶层 | 已完成 | 集成 AI 入口和 AI 示例概览 |
| 2.6.2 | `build/integrate-ai/understand-ai-components/` | 已完成 | AI 组件概念、agent、chain、memory、tool、vector 和 RAG |
| 2.6.3 | `build/integrate-ai/ai-examples/` | 已完成 | API、Google Sheets、网站内容、人工兜底、HITL、$fromAI() 示例 |
| 2.6.4 | `build/integrate-ai/test-and-improve-ai-workflows/` | 已完成 | AI workflow 测试、轻量 evaluation、metric evaluation 和常见问题 |
| 3.1 | `integrations/` 顶层、`builtin/README.md`、`community-nodes/README.md` | 已完成 | 集成入口、导航骨架、内置 node 和社区 node 索引 |
| 3.2 | `integrations/builtin/` 顶层参考页 | 已完成 | node 类型、自定义 API action、速率限制、弃用/移除/版本化 node |
| 3.3 | `integrations/community-nodes/` | 已完成 | 社区 node 安装、风险、封禁列表、故障排查和构建 |
| 3.4.1 | `integrations/builtin/core-nodes/` 第一批 | 已完成 | README、Activation Trigger、Aggregate、AI Transform、Compare Datasets、Compression |
| 3.4.2 | `integrations/builtin/core-nodes/` 第二批 | 已完成 | Convert to File、Crypto、Date & Time |
| 3.4.3 | `integrations/builtin/core-nodes/` 第三批 | 已完成 | Debug Helper、Email Trigger (IMAP)、Error Trigger、Evaluation |
| 3.4.4 | `integrations/builtin/core-nodes/` 第四批 | 已完成 | Edit Image、Evaluation Trigger、Execute Sub-workflow、Execute Sub-workflow Trigger、Execution Data |
| 3.4.5 | `integrations/builtin/core-nodes/` 第五批 | 已完成 | Extract From File、Filter、FTP |
| 3.4.6 | `integrations/builtin/core-nodes/` 第六批 | 已完成 | Form Trigger、GraphQL、HTML |
| 3.4.7 | `integrations/builtin/core-nodes/` 第七批 | 已完成 | Git、If、JWT、LDAP |
| 3.4.8 | `integrations/builtin/core-nodes/` 第八批 | 已完成 | n8n Form |
| 3.4.9 | `integrations/builtin/core-nodes/` 第九批 | 已完成 | Limit、Local File Trigger、Manual Trigger、Markdown |
| 3.4.10 | `integrations/builtin/core-nodes/` 第十批 | 已完成 | Merge、n8n、n8n Trigger、No Operation、Read/Write Files from Disk |
| 3.4.11 | `integrations/builtin/core-nodes/` 第十一批 | 已完成 | Rename Keys、Respond to Webhook、RSS Read、RSS Feed Trigger、Send Email |
| 3.4.12 | `integrations/builtin/core-nodes/` 第十二批 | 已完成 | Edit Fields (Set)、Sort、Loop Over Items、Split Out、SSE Trigger |
| 3.4.13 | `integrations/builtin/core-nodes/` 第十三批 | 已完成 | SSH、Stop And Error、Summarize、Switch、TOTP |
| 3.4.14 | `integrations/builtin/core-nodes/` 第十四批 | 已完成 | Wait、Workflow Trigger、XML |
| 3.4.15 | `integrations/builtin/core-nodes/` 第十五批 | 已完成 | Chat、Guardrails、MCP Client、MCP Server Trigger；core-nodes 已完成 |
| 3.5.1 | `integrations/builtin/app-nodes/` 第一批 | 已完成 | README、Action Network、ActiveCampaign、Adalo、Affinity |
| 3.5.2 | `integrations/builtin/app-nodes/` 第二批 | 已完成 | Agile CRM、Airtable、Airtable common issues、Airtop |
| 3.5.3 | `integrations/builtin/app-nodes/` 第三批 | 已完成 | AMQP Sender、APITemplate.io、Asana、Autopilot |
| 3.5.4 | `integrations/builtin/app-nodes/` 第四批 | 已完成 | AWS Certificate Manager、AWS Cognito、AWS Comprehend、AWS DynamoDB |
| 3.5.5 | `integrations/builtin/app-nodes/` 第五批 | 已完成 | AWS Elastic Load Balancing、AWS IAM、AWS Lambda、AWS Rekognition |
| 3.5.6 | `integrations/builtin/app-nodes/` 第六批 | 已完成 | AWS S3、AWS SES、AWS SNS、AWS SQS |
| 3.5.7 | `integrations/builtin/app-nodes/` 第七批 | 已完成 | AWS Textract、AWS Transcribe、Azure Cosmos DB、Azure Storage |
| 3.5.8 | `integrations/builtin/app-nodes/` 第八批 | 已完成 | BambooHR、Bannerbear、Baserow、Beeminder |
| 3.5.9 | `integrations/builtin/app-nodes/` 后续批次 | 未开始 | App node 参考，按服务首字母拆分 |
| 3.6 | `integrations/builtin/trigger-nodes/`、`cluster-nodes/`、`credentials/` | 未开始 | Trigger、cluster node 和 credential |
| 4 | `deploy/` | 未开始 | 部署与配置 |
| 5 | `administer/` | 未开始 | 管理与运维 |
| 6 | `connect/` | 未开始 | API、MCP、节点开发 |
| 7 | `privacy-and-security/`、`release-notes/`、`contribute/` | 未开始 | 政策、版本和贡献 |

## 每批完成标准

- 本批英文文件都有对应的 `docs/zh/` 中文镜像文件。
- 中文文件保留原始 front matter 中机器可读字段。
- 本批页面的标题和正文已翻译，不留下大段未处理英文正文。
- 运行 `git diff --check` 无错误。
