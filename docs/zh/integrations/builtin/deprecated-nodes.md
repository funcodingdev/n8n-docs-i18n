---
contentType: reference
nodeTitle: 已弃用 node
originalFilePath: integrations/builtin/deprecated-and-versioned-nodes.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/deprecated-and-versioned-nodes'
url: 'https://docs.n8n.io/integrations/builtin/deprecated-nodes'
layout:
  description:
    visible: false
---

# 已弃用和版本化 node <a href="#deprecated-and-versioned-nodes" id="deprecated-and-versioned-nodes"></a>

n8n 会随时间改进 node 库。此页面列出已移除 node（完全移除）、已弃用 node（退役但仍可使用）和版本化 node（仍处于活动状态且有多个可用版本）。

## 已弃用 node <a href="#deprecated-nodes" id="deprecated-nodes"></a>

n8n 不会再为已弃用 node 发布更新或 bug 修复。使用这些 node 的现有 workflow 会继续运行，但你应该迁移到受支持的替代方案。

{% hint style="info" %}
**迁移已弃用 node**

在 n8n 于未来版本中移除这些 node 之前，请替换 workflow 中的已弃用 node。
{% endhint %}

| Node | 最终 node 版本 |
|------|:-----------------:|
| Binary Input Loader | 1 |
| Chat Messages Retriever | 1 |
| Convert to/from binary data | 1.1 |
| Cron | 1 |
| Embedding Dimensions | 1 |
| Function | 1 |
| Function Item | 1 |
| GitHub Document Loader | 1.1 |
| HTML Extract | 1 |
| HTTP Request Tool | 1.1 |
| iCalendar | 1 |
| In Memory Vector Store Insert | 1 |
| In Memory Vector Store Load | 1 |
| Interval | 1 |
| JSON Input Loader | 1 |
| Manual Chat Trigger | 1.1 |
| MCP Registry Client (internal) | 1 |
| Message an Agent | 1 |
| Motorhead | 1.4 |
| OpenAI Assistant | 1.1 |
| OpenAI Model | 1 |
| Options | 1 |
| Orbit | 1 |
| Pinecone: Insert | 1 |
| Pinecone: Load | 1 |
| Read Binary File | 1 |
| Read Binary Files | 1 |
| Read PDF | 1 |
| SerpApi (Google Search) | 1 |
| Simulate | 1 |
| Simulate Trigger | 1 |
| Supabase: Insert | 1 |
| Supabase: Load | 1 |
| Tool Executor | 1 |
| Workflow Trigger | 1 |
| Write Binary File | 1 |
| Zep | 1.4 |
| Zep Vector Store: Insert | 1 |
| Zep Vector Store: Load | 1 |

## 已移除 node <a href="#removed-nodes" id="removed-nodes"></a>

当 node 连接的外部服务不再可用时，n8n 会移除这些 node。使用已移除 node 的 workflow 会失败。

{% hint style="warning" %}
**更新或移除受影响的 workflow**

如果你的 workflow 使用了其中任何 node，请更新为使用替代方案，或移除它们以避免错误。
{% endhint %}

| Node | n8n 版本 |
|------|:-----------:|
| Automizy | 2.0 |
| crowd.dev | 2.0 |
| Kitemaker | 2.0 |
| Spontit | 2.0 |

## 版本化 node <a href="#versioned-nodes" id="versioned-nodes"></a>

当 n8n 对某个 node 进行重大改进时，n8n 会发布新的默认版本，并保留旧版本可用。使用旧版本的现有 workflow 会继续不变地工作。

在新的 workflow 中，请始终使用当前版本，以获得最新功能和 bug 修复。

| Node | 当前 node 版本 | 之前的 node 版本 |
|------|:--------------------:|:-----------------------|
| AI Agent | 3.1 | 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 3 |
| AI Agent Tool | 3 | 2.2 |
| Airtable | 2.2 | 1, 2, 2.1 |
| Airtop | 1.1 | 1 |
| Anthropic Chat Model | 1.5 | 1, 1.1, 1.2, 1.3, 1.4 |
| AWS Bedrock Chat Model | 1.1 | 1 |
| AwsS3 | 2 | 1 |
| Baserow | 1.1 | 1 |
| Basic LLM Chain | 1.9 | 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 |
| Bitbucket Trigger | 1.1 | 1 |
| Cal.com Trigger | 2 | 1 |
| Call n8n Sub-Workflow Tool | 2.2 | 1, 1.1, 1.2, 1.3, 2, 2.1 |
| Chat | 1.3 | 1, 1.1, 1.2 |
| Chat Memory Manager | 1.1 | 1 |
| Chat Trigger | 1.4 | 1, 1.1, 1.2, 1.3 |
| Coda | 1.1 | 1 |
| Code | 2 | 1 |
| Code Tool | 1.3 | 1, 1.1, 1.2 |
| Compare Datasets | 2.3 | 1, 2, 2.1, 2.2 |
| Compression | 1.1 | 1 |
| Convert to File | 1.1 | 1 |
| Crypto | 2 | 1 |
| Data table | 1.1 | 1 |
| Date & Time | 2 | 1 |
| Default Data Loader | 1.1 | 1 |
| Discord | 2 | 1 |
| Email Trigger (IMAP) | 2.1 | 1, 2 |
| Embeddings OpenAI | 1.2 | 1, 1.1 |
| Execute Sub-workflow | 1.3 | 1, 1.1, 1.2 |
| Execute Workflow Trigger | 1.1 | 1 |
| Execution Data | 1.1 | 1 |
| Extract from File | 1.1 | 1 |
| Filter | 2.3 | 1, 2, 2.1, 2.2 |
| Git | 1.1 | 1 |
| GitHub | 1.1 | 1 |
| Gmail | 2.2 | 1, 2, 2.1 |
| Gmail Trigger | 1.4 | 1, 1.1, 1.2, 1.3 |
| Google Analytics | 2 | 1 |
| Google BigQuery | 2.1 | 1, 2 |
| Google Books | 2 | 1 |
| Google Calendar | 1.3 | 1, 1.1, 1.2 |
| Google Cloud Firestore | 1.1 | 1 |
| Google Docs | 2 | 1 |
| Google Drive | 3 | 1, 2 |
| Google Gemini Chat Model | 1.1 | 1 |
| Google Sheets | 4.7 | 1, 2, 3, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6 |
| Google Slides | 2 | 1 |
| Google Translate | 2 | 1 |
| GraphQL | 1.1 | 1 |
| Guardrails | 2 | 1 |
| HighLevel | 2 | 1 |
| HTML | 1.2 | 1, 1.1 |
| HTTP Request | 4.4 | 1, 2, 3, 4, 4.1, 4.2, 4.3 |
| HubSpot | 2.2 | 1, 2, 2.1 |
| If | 2.3 | 1, 2, 2.1, 2.2 |
| Information Extractor | 1.2 | 1, 1.1 |
| Invoice Ninja | 2 | 1 |
| Invoice Ninja Trigger | 2 | 1 |
| Item Lists | 3.1 | 1, 2, 2.1, 2.2, 3 |
| Jira Trigger | 1.1 | 1 |
| Kafka Trigger | 1.3 | 1, 1.1, 1.2 |
| Lemlist | 2 | 1 |
| Linear | 1.1 | 1 |
| MailerLite | 2 | 1 |
| MailerLite Trigger | 2 | 1 |
| MCP Client Tool | 1.2 | 1, 1.1 |
| MCP Server Trigger | 2 | 1, 1.1 |
| Merge | 3.2 | 1, 2, 2.1, 3, 3.1 |
| Microsoft Agent 365 Trigger | 1.1 | 1 |
| Microsoft Excel 365 | 2.2 | 1, 2, 2.1 |
| Microsoft OneDrive | 1.1 | 1 |
| Microsoft Outlook | 2 | 1 |
| Microsoft SQL | 1.1 | 1 |
| Microsoft Teams | 2 | 1, 1.1 |
| Mindee | 3 | 1, 2 |
| MongoDB | 1.3 | 1, 1.1, 1.2 |
| MongoDB Chat Memory | 1.1 | 1 |
| Moonshot Kimi Chat Model | 1.1 | 1 |
| MySQL | 2.5 | 1, 2, 2.1, 2.2, 2.3, 2.4 |
| n8n Form | 2.5 | 1, 2.3, 2.4 |
| n8n Form Trigger | 2.5 | 1, 2, 2.1, 2.2, 2.3, 2.4 |
| NocoDB | 4 | 1, 2, 3 |
| Notion | 2.2 | 1, 2, 2.1 |
| OpenAI | 2.3 | 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 2, 2.1, 2.2 |
| OpenAI Chat Model | 1.3 | 1, 1.1, 1.2 |
| Perplexity | 2 | 1 |
| Pipedrive | 2 | 1 |
| Pipedrive Trigger | 1.1 | 1 |
| Postgres | 2.6 | 1, 2, 2.1, 2.2, 2.3, 2.4, 2.5 |
| Postgres Chat Memory | 1.4 | 1, 1.1, 1.2, 1.3 |
| Question and Answer Chain | 1.7 | 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6 |
| RabbitMQ | 1.1 | 1 |
| Read/Write Files from Disk | 1.1 | 1 |
| Redis Chat Memory | 1.6 | 1, 1.1, 1.2, 1.3, 1.4, 1.5 |
| Remove Duplicates | 2 | 1, 1.1 |
| Respond to Webhook | 1.5 | 1, 1.1, 1.2, 1.3, 1.4 |
| RSS Read | 1.2 | 1, 1.1 |
| Schedule Trigger | 1.3 | 1, 1.1, 1.2 |
| SeaTable | 2 | 1 |
| SeaTable Trigger | 2 | 1 |
| Send Email | 2.1 | 1, 2 |
| Sentiment Analysis | 1.1 | 1 |
| Set | 3.4 | 1, 2, 3, 3.1, 3.2, 3.3 |
| Simple Memory | 1.4 | 1, 1.1, 1.2, 1.3 |
| Slack | 2.4 | 1, 2, 2.1, 2.2, 2.3 |
| Split In Batches | 3 | 2 |
| Splunk | 2 | 1 |
| Spreadsheet File | 2 | 1 |
| Strava | 1.1 | 1 |
| Structured Output Parser | 1.3 | 1, 1.1, 1.2 |
| Summarization Chain | 2.1 | 1, 2 |
| Summarize | 1.1 | 1 |
| Switch | 3.4 | 1, 2, 3, 3.1, 3.2, 3.3 |
| Telegram | 1.2 | 1, 1.1 |
| Telegram Trigger | 1.3 | 1, 1.1, 1.2 |
| Text Classifier | 1.1 | 1 |
| TheHive Trigger | 2 | 1 |
| Think Tool | 1.1 | 1 |
| Todoist | 2.2 | 1, 2, 2.1 |
| Typeform Trigger | 1.1 | 1 |
| Vector Store Question Answer Tool | 1.1 | 1 |
| Wait | 1.1 | 1 |
| Webflow | 2 | 1 |
| Webflow Trigger | 2 | 1 |
| Webhook | 2.1 | 1, 1.1, 2 |
| WhatsApp Business Cloud | 1.1 | 1 |
| Workflow Retriever | 1.1 | 1 |
| X (Formerly Twitter) | 2 | 1 |
| Xata | 1.5 | 1, 1.1, 1.2, 1.3, 1.4 |
