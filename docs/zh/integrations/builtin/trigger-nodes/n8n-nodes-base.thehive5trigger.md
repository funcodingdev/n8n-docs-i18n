---
title: TheHive 5 Trigger node 文档
description: >-
  了解如何在 n8n 中使用 TheHive 5 Trigger node。按照技术文档将 TheHive 5
  Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: TheHive 5 Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger
layout:
  description:
    visible: false
---

# TheHive 5 Trigger node <a href="#thehive-5-trigger-node" id="thehive-5-trigger-node"></a>

使用 TheHive 5 Trigger node 响应 [TheHive](https://strangebee.com/thehive/) 中的事件，并将 TheHive 与其他应用程序集成。n8n 内置支持多种 TheHive 事件，包括 alert、case、comment、page 和 task。

在本页中，你可以找到 TheHive5 Trigger node 可响应的事件列表，以及更多相关资源链接。

{% hint style="info" %}
**TheHive 和 TheHive 5**

n8n 为 TheHive 提供了两个 node。如果你想使用 TheHive 的版本 5 API，请使用此 node（TheHive 5 Trigger）。如果要使用版本 3 或 4，请使用 [TheHive Trigger](n8n-nodes-base.thehivetrigger.md)。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [TheHive 5 Trigger integrations](https://n8n.io/integrations/thehive-5-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Alert
	* 已创建
	* 已删除
	* 已更新
* Case
	* 已创建
	* 已删除
	* 已更新
* Comment
	* 已创建
	* 已删除
	* 已更新
* Observable
	* 已创建
	* 已删除
	* 已更新
* Page
	* 已创建
	* 已删除
	* 已更新
* Task
	* 已创建
	* 已删除
	* 已更新
* Task log
	* 已创建
	* 已删除
	* 已更新

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 5 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.thehive5.md)找到 node 文档。

有关该服务的更多信息，请参阅 TheHive 的[文档](https://docs.strangebee.com/)。

## 在 TheHive 中配置 webhook <a href="#configure-a-webhook-in-thehive" id="configure-a-webhook-in-thehive"></a>

要为你的 TheHive 实例配置 webhook：

1. 从 TheHive Trigger node 复制测试和生产 webhook URL。
2. 将以下内容添加到 `application.conf` 文件。此文件是 TheHive 配置文件：

	```
	notification.webhook.endpoints = [
		{
			name: TESTING_WEBHOOK_NAME
			url: TESTING_WEBHOOK_URL
			version: 1
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		},
		{
			name: PRODUCTION_WEBHOOK_NAME
			url: PRODUCTION_WEBHOOK_URL
			version: 1
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		}
	]
	```

3. 将 `TESTING_WEBHOOK_URL` 和 `PRODUCTION_WEBHOOK_URL` 替换为你在上一步复制的 URL。
4. 将 `TESTING_WEBHOOK_NAME` 和 `PRODUCTION_WEBHOOK_NAME` 替换为你偏好的 endpoint 名称。
5. 将 `ORGANIZATION_NAME` 替换为你的组织名称。
6. 执行以下 cURL 命令以启用 notifications：
	```sh
	curl -XPUT -uTHEHIVE_USERNAME:THEHIVE_PASSWORD -H 'Content-type: application/json' THEHIVE_URL/api/config/organisation/notification -d '
	{
		"value": [
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "TESTING_WEBHOOK_NAME" }
			},
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "PRODUCTION_WEBHOOK_NAME" }
			}
		]
	}'
	```
