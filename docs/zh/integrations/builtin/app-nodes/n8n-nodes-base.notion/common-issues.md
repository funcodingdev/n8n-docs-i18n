---
title: Notion node common issues
contentType:
  - integration
  - reference
priority: high
nodeTitle: Notion node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues
description: >-
  n8n 中 Notion node 的常见问题文档。包含问题详情和建议解决方案。
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

# Common issues

这里列出 [Notion node](./) 的一些常见错误和问题，以及解决或排查步骤。

## Relation property not displaying <a href="#relation-property-not-displaying" id="relation-property-not-displaying"></a>

Notion node 只支持显示[双向关系](https://www.notion.com/help/relations-and-rollups)的数据 relation 属性。当你使用双向关系连接两个 Notion 数据库时，可以在使用 Notion node 的 **Database Page** resource 时选择或按 relation 属性过滤。

要启用双向关系，请在 Notion 中编辑 relation 属性，并启用 **Show on \[name of related database]** 选项来创建反向 relation。选择一个名称，用于新上下文中的 relation。之后在 n8n 中进行过滤或选择时，即可访问该 relation。

如果你需要处理单向关系的 Notion 数据库，可以使用 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/) 并复用现有 Notion credentials。例如，要更新单向关系，可以向以下 URL 发送 `PATCH` 请求：

```
https://api.notion.com/v1/pages/<page_id>
```

启用 **Send Body**，将 **Body Content Type** 设置为 **JSON**，并将 **Specify Body** 设置为 **Using JSON**。之后，你可以在 **JSON** 字段中输入如下 JSON 对象：

```json
{
	"properties": {
		"Account": {
			"relation": [
				{
					"id": "<your_relation_ID>"
				}
			]
		}
	}
}
```

## Create toggle heading <a href="#create-toggle-heading" id="create-toggle-heading"></a>

在向 **Page**、**Database Page** 或 **Block** resource 添加 block 时，Notion node 允许你创建 heading 和 toggle。Notion node 本身尚不支持创建可 toggle 的 heading。

你可以通过先创建普通 heading，再修改它以启用 [`is_toggleable` property](https://developers.notion.com/reference/block#headings) 来绕过这个限制：

1. 使用 Notion node 添加 heading。
2. 选择要添加 heading 的 resource：
   * 要创建带 heading 的新页面，请选择 **Page** 或 **Database Page** resource，并使用 **Create** operation。
   * 要向已有页面添加 heading，请选择 **Block** resource，并使用 **Append After** operation。
3. 选择 **Add Block**，并将 **Type Name or ID** 设置为 **Heading 1**、**Heading 2** 或 **Heading 3**。
4. 添加一个连接到 Notion node 的 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/) node，并选择 `GET` method。
5. 将 **URL** 设置为 `https://api.notion.com/v1/blocks/<block_ID>`。例如，如果你把 heading 添加到已有页面，可以使用以下 URL：`https://api.notion.com/v1/blocks/{{ $json.results[0].id }}`。如果你创建的是新页面而不是追加 block，可能需要先查询页面内容来发现 block ID。
6. 选择 **Predefined Credential Type** 并连接现有 Notion credentials。
7. 在 HTTP Request node 后添加一个 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md) node。
8. 添加 `heading_1.is_toggleable` 作为新的 **Boolean** 字段，并设置为 `true`。如有需要，将 `heading_1` 替换为其他 heading 编号。
9. 在 Edit Fields (Set) node 后添加第二个 HTTP Request node。
10. 将 **Method** 设置为 `PATCH`，并使用 `https://api.notion.com/v1/blocks/{{ $json.id }}` 作为 **URL** 值。
11. 选择 **Predefined Credential Type** 并连接现有 Notion credentials。
12. 启用 **Send Body** 并设置一个参数。
13. 将参数 **Name** 设置为 `heading_1`（将 `heading_1` 替换为你正在使用的 heading 级别）。
14. 将参数 **Value** 设置为 `{{ $json.heading_1 }}`（将 `heading_1` 替换为你正在使用的 heading 级别）。

上述序列会创建一个普通 heading block。它会查询新创建的 heading，添加 `is_toggleable` property，并更新 heading block。

## Handle null and empty values <a href="#handle-null-and-empty-values" id="handle-null-and-empty-values"></a>

使用 Notion node 时，如果提交的字段为空值或 null 值，你可能会收到验证错误。只要你从前置 node 填充字段但该数据缺失，就可能发生这种情况。

要绕过此问题，请在将字段数据发送到 Notion 之前检查其是否存在，或使用默认值。

要在执行 Notion node 之前检查数据，请使用 [If](../../core-nodes/n8n-nodes-base.if.md) node 检查字段是否未设置。这样可以让你使用 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md) node，在字段没有有效值时有条件地移除该字段。

作为替代方案，如果传入数据没有提供值，你可以设置默认值。
