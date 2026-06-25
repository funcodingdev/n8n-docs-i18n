---
title: Tools AI Agent node 文档
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Tools AI Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 Tools Agent。按照技术文档将 Tools Agent
  集成到你的 workflow 中。
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

# Tools Agent

Tools Agent 使用外部 tools[^1] 和 API 执行动作并检索信息。它可以理解不同 tool 的能力，并根据任务决定使用哪个 tool。此 agent 有助于将 LLM 与各种外部服务和数据库集成。

此 agent 具备增强的 tool 使用能力，并可确保标准输出格式。

Tools Agent 实现 [Langchain 的 tool calling](https://js.langchain.com/docs/concepts/tool_calling/) 接口。此接口描述可用 tools 及其 schema。由于它会将 parser 作为格式化 tool 传递给 model，因此此 agent 也具备改进的输出解析能力。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/cHtfs3gewkhPbGP31rjc/" %}

此 agent 支持以下 chat models：

* [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/)
* [Groq Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatgroq.md)
* [Mistral Cloud Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Anthropic Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)
* [Azure OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)

<details>

<summary>Tools Agent 可以使用以下 tools...</summary>

* [Call n8n Workflow](../../sub-nodes/n8n-nodes-langchain.toolworkflow.md)
* [Code](../../sub-nodes/n8n-nodes-langchain.toolcode.md)
* [HTTP Request](../../../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md)
* [Action Network](../../../app-nodes/n8n-nodes-base.actionnetwork.md)
* [ActiveCampaign](../../../app-nodes/n8n-nodes-base.activecampaign.md)
* [Affinity](../../../app-nodes/n8n-nodes-base.affinity.md)
* [Agile CRM](../../../app-nodes/n8n-nodes-base.agilecrm.md)
* [Airtable](../../../app-nodes/n8n-nodes-base.airtable/)
* [APITemplate.io](../../../app-nodes/n8n-nodes-base.apitemplateio.md)
* [Asana](../../../app-nodes/n8n-nodes-base.asana.md)
* [AWS Lambda](../../../app-nodes/n8n-nodes-base.awslambda.md)
* [AWS S3](../../../app-nodes/n8n-nodes-base.awss3.md)
* [AWS SES](../../../app-nodes/n8n-nodes-base.awsses.md)
* [AWS Textract](../../../app-nodes/n8n-nodes-base.awstextract.md)
* [AWS Transcribe](../../../app-nodes/n8n-nodes-base.awstranscribe.md)
* [Baserow](../../../app-nodes/n8n-nodes-base.baserow.md)
* [Bubble](../../../app-nodes/n8n-nodes-base.bubble.md)
* [Calculator](../../sub-nodes/n8n-nodes-langchain.toolcalculator.md)
* [ClickUp](../../../app-nodes/n8n-nodes-base.clickup.md)
* [CoinGecko](../../../app-nodes/n8n-nodes-base.coingecko.md)
* [Compression](../../../core-nodes/n8n-nodes-base.compression.md)
* [Crypto](../../../core-nodes/n8n-nodes-base.crypto.md)
* [DeepL](../../../app-nodes/n8n-nodes-base.deepl.md)
* [DHL](../../../app-nodes/n8n-nodes-base.dhl.md)
* [Discord](../../../app-nodes/n8n-nodes-base.discord/)
* [Dropbox](../../../app-nodes/n8n-nodes-base.dropbox.md)
* [Elasticsearch](../../../app-nodes/n8n-nodes-base.elasticsearch.md)
* [ERPNext](../../../app-nodes/n8n-nodes-base.erpnext.md)
* [Facebook Graph API](../../../app-nodes/n8n-nodes-base.facebookgraphapi.md)
* [FileMaker](../../../app-nodes/n8n-nodes-base.filemaker.md)
* [Ghost](../../../app-nodes/n8n-nodes-base.ghost.md)
* [Git](../../../core-nodes/n8n-nodes-base.git.md)
* [GitHub](../../../app-nodes/n8n-nodes-base.github.md)
* [GitLab](../../../app-nodes/n8n-nodes-base.gitlab.md)
* [Gmail](../../../app-nodes/n8n-nodes-base.gmail/)
* [Google Analytics](../../../app-nodes/n8n-nodes-base.googleanalytics.md)
* [Google BigQuery](../../../app-nodes/n8n-nodes-base.googlebigquery.md)
* [Google Calendar](../../../app-nodes/n8n-nodes-base.googlecalendar/)
* [Google Chat](../../../app-nodes/n8n-nodes-base.googlechat.md)
* [Google Cloud Firestore](../../../app-nodes/n8n-nodes-base.googlecloudfirestore.md)
* [Google Cloud Realtime Database](../../../app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md)
* [Google Contacts](../../../app-nodes/n8n-nodes-base.googlecontacts.md)
* [Google Docs](../../../app-nodes/n8n-nodes-base.googledocs.md)
* [Google Drive](../../../app-nodes/n8n-nodes-base.googledrive/)
* [Google Sheets](../../../app-nodes/n8n-nodes-base.googlesheets/)
* [Google Slides](../../../app-nodes/n8n-nodes-base.googleslides.md)
* [Google Tasks](../../../app-nodes/n8n-nodes-base.googletasks.md)
* [Google Translate](../../../app-nodes/n8n-nodes-base.googletranslate.md)
* [Google Workspace Admin](../../../app-nodes/n8n-nodes-base.gsuiteadmin.md)
* [Gotify](../../../app-nodes/n8n-nodes-base.gotify.md)
* [Grafana](../../../app-nodes/n8n-nodes-base.grafana.md)
* [GraphQL](../../../core-nodes/n8n-nodes-base.graphql.md)
* [Hacker News](../../../app-nodes/n8n-nodes-base.hackernews.md)
* [Home Assistant](../../../app-nodes/n8n-nodes-base.homeassistant.md)
* [HubSpot](../../../app-nodes/n8n-nodes-base.hubspot.md)
* [Jenkins](../../../app-nodes/n8n-nodes-base.jenkins.md)
* [Jira Software](../../../app-nodes/n8n-nodes-base.jira.md)
* [JWT](../../../core-nodes/n8n-nodes-base.jwt.md)
* [Kafka](../../../app-nodes/n8n-nodes-base.kafka.md)
* [LDAP](../../../core-nodes/n8n-nodes-base.ldap.md)
* [Line](../../../app-nodes/n8n-nodes-base.line.md)
* [LinkedIn](../../../app-nodes/n8n-nodes-base.linkedin.md)
* [Mailcheck](../../../app-nodes/n8n-nodes-base.mailcheck.md)
* [Mailgun](../../../app-nodes/n8n-nodes-base.mailgun.md)
* [Mattermost](../../../app-nodes/n8n-nodes-base.mattermost.md)
* [Mautic](../../../app-nodes/n8n-nodes-base.mautic.md)
* [Medium](../../../app-nodes/n8n-nodes-base.medium.md)
* [Microsoft Excel 365](../../../app-nodes/n8n-nodes-base.microsoftexcel.md)
* [Microsoft OneDrive](../../../app-nodes/n8n-nodes-base.microsoftonedrive.md)
* [Microsoft Outlook](../../../app-nodes/n8n-nodes-base.microsoftoutlook.md)
* [Microsoft SQL](../../../app-nodes/n8n-nodes-base.microsoftsql.md)
* [Microsoft Teams](../../../app-nodes/n8n-nodes-base.microsoftteams.md)
* [Microsoft To Do](../../../app-nodes/n8n-nodes-base.microsofttodo.md)
* [Monday.com](../../../app-nodes/n8n-nodes-base.mondaycom.md)
* [MongoDB](../../../app-nodes/n8n-nodes-base.mongodb.md)
* [MQTT](../../../app-nodes/n8n-nodes-base.mqtt.md)
* [MySQL](../../../app-nodes/n8n-nodes-base.mysql/)
* [NASA](../../../app-nodes/n8n-nodes-base.nasa.md)
* [Nextcloud](../../../app-nodes/n8n-nodes-base.nextcloud.md)
* [NocoDB](../../../app-nodes/n8n-nodes-base.nocodb.md)
* [Notion](../../../app-nodes/n8n-nodes-base.notion/)
* [Odoo](../../../app-nodes/n8n-nodes-base.odoo.md)
* [OpenWeatherMap](../../../app-nodes/n8n-nodes-base.openweathermap.md)
* [Pipedrive](../../../app-nodes/n8n-nodes-base.pipedrive.md)
* [Postgres](../../../app-nodes/n8n-nodes-base.postgres/)
* [Pushover](../../../app-nodes/n8n-nodes-base.pushover.md)
* [QuickBooks Online](../../../app-nodes/n8n-nodes-base.quickbooks.md)
* [QuickChart](../../../app-nodes/n8n-nodes-base.quickchart.md)
* [RabbitMQ](../../../app-nodes/n8n-nodes-base.rabbitmq.md)
* [Reddit](../../../app-nodes/n8n-nodes-base.reddit.md)
* [Redis](../../../app-nodes/n8n-nodes-base.redis.md)
* [RocketChat](../../../app-nodes/n8n-nodes-base.rocketchat.md)
* [S3](../../../app-nodes/n8n-nodes-base.s3.md)
* [Salesforce](../../../app-nodes/n8n-nodes-base.salesforce.md)
* [Send Email](../../../core-nodes/n8n-nodes-base.sendemail.md)
* [SendGrid](../../../app-nodes/n8n-nodes-base.sendgrid.md)
* [SerpApi (Google Search)](../../sub-nodes/n8n-nodes-langchain.toolserpapi.md)
* [Shopify](../../../app-nodes/n8n-nodes-base.shopify.md)
* [Slack](../../../app-nodes/n8n-nodes-base.slack.md)
* [Spotify](../../../app-nodes/n8n-nodes-base.spotify.md)
* [Stripe](../../../app-nodes/n8n-nodes-base.stripe.md)
* [Supabase](../../../app-nodes/n8n-nodes-base.supabase/)
* [Telegram](../../../app-nodes/n8n-nodes-base.telegram/)
* [Todoist](../../../app-nodes/n8n-nodes-base.todoist.md)
* [TOTP](../../../core-nodes/n8n-nodes-base.totp.md)
* [Trello](../../../app-nodes/n8n-nodes-base.trello.md)
* [Twilio](../../../app-nodes/n8n-nodes-base.twilio.md)
* [urlscan.io](../../../app-nodes/n8n-nodes-base.urlscanio.md)
* [Vector Store](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)
* [Webflow](../../../app-nodes/n8n-nodes-base.webflow.md)
* [Wikipedia](../../sub-nodes/n8n-nodes-langchain.toolwikipedia.md)
* [Wolfram|Alpha](../../sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)
* [WooCommerce](../../../app-nodes/n8n-nodes-base.woocommerce.md)
* [Wordpress](../../../app-nodes/n8n-nodes-base.wordpress.md)
* [X (Formerly Twitter)](../../../app-nodes/n8n-nodes-base.twitter.md)
* [YouTube](../../../app-nodes/n8n-nodes-base.youtube.md)
* [Zendesk](../../../app-nodes/n8n-nodes-base.zendesk.md)
* [Zoho CRM](../../../app-nodes/n8n-nodes-base.zohocrm.md)
* [Zoom](../../../app-nodes/n8n-nodes-base.zoom.md)

</details>

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Tools Agent。

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 Tools Agent node 的行为：

### System Message <a href="#system-message" id="system-message"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ci5NMdJiVoyT9dtdTE9w/" %}

### Max Iterations <a href="#max-iterations" id="max-iterations"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/8UflrA3Nx8LD5bKQn8Xc/" %}

### Return Intermediate Steps <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/skA96E8hAnMMKG7c4Lta/" %}

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

### Automatically Passthrough Binary Images <a href="#automatically-passthrough-binary-images" id="automatically-passthrough-binary-images"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/2rKQZnqDH1pc3xlyYYdX/" %}

### Enable Streaming <a href="#enable-streaming" id="enable-streaming"></a>

启用后，AI Agent 会在生成答案时实时将数据发回给用户。这对长时间运行的生成很有用。默认情况下此选项已启用。

{% hint style="info" %}
**Streaming 要求**

要让 streaming 工作，你的 workflow 必须使用支持 streaming responses 的 trigger，例如 [Chat Trigger](../../../core-nodes/n8n-nodes-base.compression/n8n-nodes-base.compression.md) 或 [Webhook](../../../core-nodes/n8n-nodes-base.webhook/) node，并将 **Response Mode** 设置为 **Streaming**。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](./#templates-and-examples)部分。

## 使用 `$fromAI()` 为 tools 动态设置参数 <a href="#dynamic-parameters-for-tools-with-dollarfromai" id="dynamic-parameters-for-tools-with-dollarfromai"></a>

要了解如何为 app node tools 动态填充参数，请参阅[让 AI 使用 `$fromAI()` 指定 tool 参数](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/ai-examples/use-ai-for-parameters)。

## Tool calls 的人工审核 <a href="#human-review-for-tool-calls" id="human-review-for-tool-calls"></a>

你可以要求在 AI Agent 执行特定 tools 之前进行人工批准。这对执行敏感操作的 tools 很有用，例如发送消息、修改记录或删除数据。

要添加人工审核步骤：

1. 点击 AI Agent node 上的 tool 连接器。
2. 在 Tools Panel 中，找到 **Human review** 部分。
3. 选择你偏好的审批渠道（Chat、Slack、Telegram 等）并配置它。
4. 将需要批准的 tools 连接到人工审核步骤。

当 AI 想使用受控 tool 时，workflow 会暂停，并通过你选择的渠道发送批准请求。接收者可以批准（执行 tool）或拒绝（取消操作）。

有关详细的设置说明和最佳实践，请参阅 [Human-in-the-loop for AI tool calls](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/ai-examples/human-in-the-loop-for-tools)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。
