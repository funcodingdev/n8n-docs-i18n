# n8n 文档简体中文翻译计划

## 目标

将 `docs/` 下的英文 Markdown 文档分批翻译为简体中文，并在 `docs/zh/` 中保持与英文文档一致的相对路径，方便后续同步 n8n 官方上游仓库。

当前基线：

- 英文 Markdown 文件数：1402
- 已创建中文 Markdown 文件数：724
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
| 3.5.9 | `integrations/builtin/app-nodes/` 第九批 | 已完成 | Bitly、Bitwarden、Box、Brandfetch |
| 3.5.10 | `integrations/builtin/app-nodes/` 第十批 | 已完成 | Brevo、Bubble、Chargebee、CircleCI |
| 3.5.11 | `integrations/builtin/app-nodes/` 第十一批 | 已完成 | Webex by Cisco、Clearbit、ClickUp、Clockify |
| 3.5.12 | `integrations/builtin/app-nodes/` 第十二批 | 已完成 | Cloudflare、Cockpit、Coda、CoinGecko |
| 3.5.13 | `integrations/builtin/app-nodes/` 第十三批 | 已完成 | Contentful、ConvertKit、Copper、Cortex |
| 3.5.14 | `integrations/builtin/app-nodes/` 第十四批 | 已完成 | CrateDB、crowd.dev、Customer.io、Databricks |
| 3.5.15 | `integrations/builtin/app-nodes/` 第十五批 | 已完成 | DeepL、Demio、DHL、Discourse |
| 3.5.16 | `integrations/builtin/app-nodes/` 第十六批 | 已完成 | Disqus、Drift、Dropbox、Dropcontact |
| 3.5.17 | `integrations/builtin/app-nodes/` 第十七批 | 已完成 | E-goi、Elasticsearch、Elastic Security、Emelia |
| 3.5.18 | `integrations/builtin/app-nodes/` 第十八批 | 已完成 | ERPNext、Facebook Graph API、FileMaker、Flow |
| 3.5.19 | `integrations/builtin/app-nodes/` 第十九批 | 已完成 | Freshdesk、Freshservice、Freshworks CRM、GetResponse |
| 3.5.20 | `integrations/builtin/app-nodes/` 第二十批 | 已完成 | Ghost、GitHub、GitLab、Gong |
| 3.5.21 | `integrations/builtin/app-nodes/` 第二十一批 | 已完成 | Google Ads、Google Analytics、Google BigQuery、Google Books |
| 3.5.22 | `integrations/builtin/app-nodes/` 第二十二批 | 已完成 | Google Business Profile、Google Chat、Google Cloud Firestore、Google Cloud Natural Language |
| 3.5.23 | `integrations/builtin/app-nodes/` 第二十三批 | 已完成 | Google Cloud Realtime Database、Google Cloud Storage、Google Contacts、Google Docs |
| 3.5.24 | `integrations/builtin/app-nodes/` 第二十四批 | 已完成 | Google Perspective、Google Slides、Google Tasks、Google Translate |
| 3.5.25 | `integrations/builtin/app-nodes/` 第二十五批 | 已完成 | Gotify、GoToWebinar、Grafana、Grist |
| 3.5.26 | `integrations/builtin/app-nodes/` 第二十六批 | 已完成 | Google Workspace Admin、Hacker News、HaloPSA、Harvest |
| 3.5.27 | `integrations/builtin/app-nodes/` 第二十七批 | 已完成 | Help Scout、HighLevel、Home Assistant、HubSpot |
| 3.5.28 | `integrations/builtin/app-nodes/` 第二十八批 | 已完成 | Humantic AI、Hunter、Intercom、Invoice Ninja |
| 3.5.29 | `integrations/builtin/app-nodes/` 第二十九批 | 已完成 | Iterable、Jenkins、Jina AI、Jira Software |
| 3.5.30 | `integrations/builtin/app-nodes/` 第三十批 | 已完成 | Kafka、Keap、Kitemaker、KoboToolbox |
| 3.5.31 | `integrations/builtin/app-nodes/` 第三十一批 | 已完成 | Lemlist、Line、Linear、LingvaNex |
| 3.5.32 | `integrations/builtin/app-nodes/` 第三十二批 | 已完成 | LinkedIn、LoneScale、Magento 2、Mailcheck |
| 3.5.33 | `integrations/builtin/app-nodes/` 第三十三批 | 已完成 | Mailchimp、MailerLite、Mailgun、Mailjet |
| 3.5.34 | `integrations/builtin/app-nodes/` 第三十四批 | 已完成 | Mandrill、marketstack、Matrix、Mattermost |
| 3.5.35 | `integrations/builtin/app-nodes/` 第三十五批 | 已完成 | Mautic、Medium、MessageBird、Metabase |
| 3.5.36 | `integrations/builtin/app-nodes/` 第三十六批 | 已完成 | Microsoft Dynamics CRM、Microsoft Entra ID、Microsoft Excel 365、Microsoft Graph Security |
| 3.5.37 | `integrations/builtin/app-nodes/` 第三十七批 | 已完成 | Microsoft OneDrive、Microsoft Outlook、Microsoft SharePoint、Microsoft SQL |
| 3.5.38 | `integrations/builtin/app-nodes/` 第三十八批 | 已完成 | Microsoft Teams、Microsoft To Do、Mindee、MISP |
| 3.5.39 | `integrations/builtin/app-nodes/` 第三十九批 | 已完成 | Mistral AI、Mocean、monday.com、MongoDB |
| 3.5.40 | `integrations/builtin/app-nodes/` 第四十批 | 已完成 | Monica CRM、MQTT、MSG91、Customer Datastore (n8n Training) |
| 3.5.41 | `integrations/builtin/app-nodes/` 第四十一批 | 已完成 | Customer Messenger (n8n Training)、NASA、Netlify、Netscaler ADC |
| 3.5.42 | `integrations/builtin/app-nodes/` 第四十二批 | 已完成 | Nextcloud、NocoDB、npm、Odoo |
| 3.5.43 | `integrations/builtin/app-nodes/` 第四十三批 | 已完成 | Okta、One Simple API、Onfleet、OpenThesaurus |
| 3.5.44 | `integrations/builtin/app-nodes/` 第四十四批 | 已完成 | OpenWeatherMap、Oracle Database、Oura、Paddle |
| 3.5.45 | `integrations/builtin/app-nodes/` 第四十五批 | 已完成 | PagerDuty、PayPal、Peekalink、PhantomBuster |
| 3.5.46 | `integrations/builtin/app-nodes/` 第四十六批 | 已完成 | Philips Hue、Pipedrive、Plivo、PostBin |
| 3.5.47 | `integrations/builtin/app-nodes/` 第四十七批 | 已完成 | PostHog、ProfitWell、Pushbullet、Pushcut |
| 3.5.48 | `integrations/builtin/app-nodes/` 第四十八批 | 已完成 | Pushover、QuestDB、Quick Base、QuickBooks Online |
| 3.5.49 | `integrations/builtin/app-nodes/` 第四十九批 | 已完成 | QuickChart、RabbitMQ、Raindrop、Reddit |
| 3.5.50 | `integrations/builtin/app-nodes/` 第五十批 | 已完成 | Redis、Rocket.Chat、Rundeck、S3 |
| 3.5.51 | `integrations/builtin/app-nodes/` 第五十一批 | 已完成 | Salesforce、Salesmate、SeaTable、SecurityScorecard |
| 3.5.52 | `integrations/builtin/app-nodes/` 第五十二批 | 已完成 | Segment、SendGrid、Sendy、Sentry.io |
| 3.5.53 | `integrations/builtin/app-nodes/` 第五十三批 | 已完成 | ServiceNow、Shopify、SIGNL4、Slack |
| 3.5.54 | `integrations/builtin/app-nodes/` 第五十四批 | 已完成 | seven、Snowflake、Splunk、Spotify |
| 3.5.55 | `integrations/builtin/app-nodes/` 第五十五批 | 已完成 | Stackby、Storyblok、Strapi、Strava |
| 3.5.56 | `integrations/builtin/app-nodes/` 第五十六批 | 已完成 | Stripe、SyncroMSP、Taiga、Tapfiliate |
| 3.5.57 | `integrations/builtin/app-nodes/` 第五十七批 | 已完成 | TheHive、TheHive 5、TimescaleDB、Todoist |
| 3.5.58 | `integrations/builtin/app-nodes/` 第五十八批 | 已完成 | Travis CI、Trello、Twake、Twilio |
| 3.5.59 | `integrations/builtin/app-nodes/` 第五十九批 | 已完成 | Twist、X (Formerly Twitter)、Unleashed Software、UpLead |
| 3.5.60 | `integrations/builtin/app-nodes/` 第六十批 | 已完成 | uProc、UptimeRobot、urlscan.io、Venafi TLS Protect Cloud |
| 3.5.61 | `integrations/builtin/app-nodes/` 第六十一批 | 已完成 | Venafi TLS Protect Datacenter、Vero、Vonage、Webflow |
| 3.5.62 | `integrations/builtin/app-nodes/` 第六十二批 | 已完成 | Wekan、Wise、WooCommerce、WordPress |
| 3.5.63 | `integrations/builtin/app-nodes/` 第六十三批 | 已完成 | Xero、Yourls、YouTube、Zammad |
| 3.5.64 | `integrations/builtin/app-nodes/` 第六十四批 | 已完成 | Zendesk、Zoho CRM、Zoom、Zulip |
| 3.5.65 | `integrations/builtin/app-nodes/` 第六十五批 | 已完成 | Alibaba Cloud Model Studio、Anthropic、Google Gemini、MiniMax、Moonshot Kimi、Perplexity |
| 3.6.1 | `integrations/builtin/trigger-nodes/` 第一批 | 已完成 | README、ActiveCampaign Trigger、Acuity Scheduling Trigger、Affinity Trigger |
| 3.6.2 | `integrations/builtin/trigger-nodes/` 第二批 | 已完成 | Airtable Trigger、AMQP Trigger、Asana Trigger、Autopilot Trigger |
| 3.6.3 | `integrations/builtin/trigger-nodes/` 第三批 | 已完成 | AWS SNS Trigger、Bitbucket Trigger、Box Trigger、Brevo Trigger |
| 3.6.4 | `integrations/builtin/trigger-nodes/` 第四批 | 已完成 | Calendly Trigger、Cal Trigger、Chargebee Trigger、Webex by Cisco Trigger |
| 3.6.5 | `integrations/builtin/trigger-nodes/` 第五批 | 已完成 | ClickUp Trigger、Clockify Trigger、ConvertKit Trigger、Copper Trigger |
| 3.6.6 | `integrations/builtin/trigger-nodes/` 第六批 | 已完成 | crowd.dev Trigger、Customer.io Trigger、Emelia Trigger、Eventbrite Trigger |
| 3.6.7 | `integrations/builtin/trigger-nodes/` 第七批 | 已完成 | Facebook Lead Ads Trigger、Figma Trigger、Flow Trigger、Form.io Trigger |
| 3.6.8 | `integrations/builtin/trigger-nodes/` 第八批 | 已完成 | Formstack Trigger、GetResponse Trigger、GitHub Trigger、GitLab Trigger |
| 3.6.9 | `integrations/builtin/trigger-nodes/` 第九批 | 已完成 | Google Business Profile Trigger、Google Calendar Trigger、Gumroad Trigger、Help Scout Trigger |
| 3.6.10 | `integrations/builtin/trigger-nodes/` 第十批 | 已完成 | HubSpot Trigger、Invoice Ninja Trigger、Jira Trigger、Jotform Trigger |
| 3.6.11 | `integrations/builtin/trigger-nodes/` 第十一批 | 已完成 | Kafka Trigger、Keap Trigger、KoboToolbox Trigger、Lemlist Trigger |
| 3.6.12 | `integrations/builtin/trigger-nodes/` 第十二批 | 已完成 | Linear Trigger、LoneScale Trigger、Mailchimp Trigger、MailerLite Trigger |
| 3.6.13 | `integrations/builtin/trigger-nodes/` 第十三批 | 已完成 | Mailjet Trigger、Mautic Trigger、Microsoft OneDrive Trigger、Microsoft Outlook Trigger |
| 3.6.14 | `integrations/builtin/trigger-nodes/` 第十四批 | 已完成 | Microsoft Teams Trigger、MQTT Trigger、Netlify Trigger、Notion Trigger |
| 3.6.15 | `integrations/builtin/trigger-nodes/` 第十五批 | 已完成 | Onfleet Trigger、PayPal Trigger、Pipedrive Trigger、Postgres Trigger |
| 3.6.16 | `integrations/builtin/trigger-nodes/` 第十六批 | 已完成 | Postmark Trigger、Pushcut Trigger、RabbitMQ Trigger、Redis Trigger |
| 3.6.17 | `integrations/builtin/trigger-nodes/` 第十七批 | 已完成 | Salesforce Trigger、SeaTable Trigger、Shopify Trigger、Slack Trigger |
| 3.6.18 | `integrations/builtin/trigger-nodes/` 第十八批 | 已完成 | Strava Trigger、Stripe Trigger、SurveyMonkey Trigger、Taiga Trigger |
| 3.6.19 | `integrations/builtin/trigger-nodes/` 第十九批 | 已完成 | TheHive 5 Trigger、TheHive Trigger、Toggl Trigger、Trello Trigger |
| 3.6.20 | `integrations/builtin/trigger-nodes/` 第二十批 | 已完成 | Twilio Trigger、Typeform Trigger、Venafi TLS Protect Cloud Trigger、Webflow Trigger |
| 3.6.21 | `integrations/builtin/trigger-nodes/` 第二十一批 | 已完成 | WhatsApp Trigger、Wise Trigger、WooCommerce Trigger、Workable Trigger、Wufoo Trigger、Zendesk Trigger；trigger-nodes 已完成 |
| 3.7.1 | `integrations/builtin/cluster-nodes/` 第一批 | 已完成 | Cluster nodes、Root nodes、AI Agent、AI Agent common issues |
| 3.7.2 | `integrations/builtin/cluster-nodes/` 第二批 | 已完成 | Conversational Agent、OpenAI Functions Agent、Plan and Execute Agent、ReAct Agent、SQL Agent、Tools Agent |
| 3.7.3 | `integrations/builtin/cluster-nodes/` 第三批 | 已完成 | Basic LLM Chain、Question and Answer Chain、Q&A common issues、Summarization Chain、LangChain Code、Information Extractor |
| 3.7.4 | `integrations/builtin/cluster-nodes/` 第四批 | 已完成 | Microsoft Agent 365 Trigger、Sentiment Analysis、Text Classifier |
| 3.7.5 | `integrations/builtin/cluster-nodes/` 第五批 | 已完成 | Chroma Vector Store、Simple Vector Store |
| 3.7.6 | `integrations/builtin/cluster-nodes/` 第六批 | 已完成 | Milvus Vector Store、MongoDB Atlas Vector Store、PGVector Vector Store |
| 3.7.7 | `integrations/builtin/cluster-nodes/` 第七批 | 已完成 | Pinecone Vector Store、Qdrant Vector Store |
| 3.7.8 | `integrations/builtin/cluster-nodes/` 第八批 | 已完成 | Redis Vector Store、Supabase Vector Store |
| 3.7.9 | `integrations/builtin/cluster-nodes/` 第九批 | 已完成 | Weaviate Vector Store、Zep Vector Store |
| 3.7.10 | `integrations/builtin/cluster-nodes/` 第十批 | 已完成 | Azure AI Search Vector Store；root vector stores 已完成 |
| 3.7.11 | `integrations/builtin/cluster-nodes/sub-nodes/` 第一批 | 已完成 | README、Default Data Loader、GitHub Document Loader |
| 3.7.12 | `integrations/builtin/cluster-nodes/sub-nodes/` 第二批 | 已完成 | Embeddings AWS Bedrock、Azure OpenAI、Cohere、Google Gemini |
| 3.7.13 | `integrations/builtin/cluster-nodes/sub-nodes/` 第三批 | 已完成 | Google PaLM、Google Vertex、HuggingFace Inference、Lemonade、Mistral Cloud、Ollama、OpenAI embeddings；embeddings sub-nodes 已完成 |
| 3.7.14 | `integrations/builtin/cluster-nodes/sub-nodes/` 第四批 | 已完成 | Alibaba Cloud、Anthropic、AWS Bedrock、Azure OpenAI Chat Model |
| 3.7.15 | `integrations/builtin/cluster-nodes/sub-nodes/` 第五批 | 已完成 | Cohere、DeepSeek、Google Gemini、Google Vertex、Groq Chat Model |
| 3.7.16 | `integrations/builtin/cluster-nodes/sub-nodes/` 第六批 | 已完成 | Lemonade、MiniMax、Mistral Cloud、Moonshot Kimi、NVIDIA Nemotron Chat Model |
| 3.7.17 | `integrations/builtin/cluster-nodes/sub-nodes/` 第七批 | 已完成 | OpenRouter、Vercel AI Gateway、xAI Grok Chat Model |
| 3.7.18 | `integrations/builtin/cluster-nodes/sub-nodes/` 第八批 | 已完成 | Ollama、OpenAI Chat Model README 和 common issues；chat model sub-nodes 已完成 |
| 3.7.19 | `integrations/builtin/cluster-nodes/sub-nodes/` 第九批 | 已完成 | Cohere、Lemonade、Ollama、Hugging Face Inference Model |
| 3.7.20 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十批 | 已完成 | Simple Memory README/common issues、Chat Memory Manager |
| 3.7.21 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十一批 | 已完成 | MongoDB、Motorhead、Postgres、Redis、Xata、Zep memory；memory sub-nodes 已完成 |
| 3.7.22 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十二批 | 已完成 | Model Selector、Auto-fixing/Item List/Structured Output Parser |
| 3.7.23 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十三批 | 已完成 | Reranker Cohere、Contextual Compression/MultiQuery/Vector Store/Workflow Retriever |
| 3.7.24 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十四批 | 已完成 | Character、Recursive Character、Token Text Splitter |
| 3.7.25 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十五批 | 已完成 | AI Agent Tool、Calculator、Custom Code、MCP Client、SearXNG、SerpApi |
| 3.7.26 | `integrations/builtin/cluster-nodes/sub-nodes/` 第十六批 | 已完成 | Think、Vector Store Question Answer、Wikipedia、Wolfram|Alpha、Call n8n Workflow Tool；cluster sub-nodes 已完成 |
| 3.8.1 | `integrations/builtin/credentials/` 第一批 | 已完成 | README、Action Network、ActiveCampaign、Acuity Scheduling、Adalo、Affinity、Agile CRM |
| 3.8.2 | `integrations/builtin/credentials/` 第二批 | 已完成 | Airtable、Airtop、Alibaba Cloud、AlienVault、AMQP、Anthropic |
| 3.8.3 | `integrations/builtin/credentials/` 第三批 | 已完成 | APITemplate.io、Asana、Auth0 Management、Autopilot、AWS、Azure AI Search |
| 3.8.4 | `integrations/builtin/credentials/` 第四批 | 已完成 | Azure Cosmos DB、Azure OpenAI、Azure Storage、BambooHR、Bannerbear、Baserow |
| 3.8.5 | `integrations/builtin/credentials/` 第五批 | 已完成 | Beeminder、Bitbucket、Bitly、Bitwarden、Box、Brandfetch |
| 3.8.6 | `integrations/builtin/credentials/` 第六批 | 已完成 | Brevo、Bubble、Cal.com、Calendly、Carbon Black、Chargebee |
| 3.8.7 | `integrations/builtin/credentials/` 第七批 | 已完成 | Chroma、CircleCI、Cisco Meraki、Cisco Secure Endpoint、Cisco Umbrella、Webex by Cisco |
| 3.8.8 | `integrations/builtin/credentials/` 第八批 | 已完成 | Clearbit、ClickUp、Clockify、Cloudflare、Cockpit、Coda |
| 3.8.9 | `integrations/builtin/credentials/` 第九批 | 已完成 | Cohere、Contentful、ConvertAPI、ConvertKit、Copper、Cortex、CrateDB、crowd.dev |
| 3.8.10 | `integrations/builtin/credentials/` 第十批 | 已完成 | CrowdStrike、Customer.io、Databricks、Datadog |
| 3.8.11 | `integrations/builtin/credentials/` 后续批次 | 未开始 | 继续 credentials 文档 |
| 4 | `deploy/` | 未开始 | 部署与配置 |
| 5 | `administer/` | 未开始 | 管理与运维 |
| 6 | `connect/` | 未开始 | API、MCP、节点开发 |
| 7 | `privacy-and-security/`、`release-notes/`、`contribute/` | 未开始 | 政策、版本和贡献 |

## 每批完成标准

- 本批英文文件都有对应的 `docs/zh/` 中文镜像文件。
- 中文文件保留原始 front matter 中机器可读字段。
- 本批页面的标题和正文已翻译，不留下大段未处理英文正文。
- 运行 `git diff --check` 无错误。
