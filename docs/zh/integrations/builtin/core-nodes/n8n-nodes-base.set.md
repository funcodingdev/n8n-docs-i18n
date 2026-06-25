---
title: Edit Fields (Set)
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Edit Fields (Set)
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.set.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set
description: >-
  n8n 中 Edit Fields node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
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

# Edit Fields (Set)

使用 Edit Fields node 设置 workflow 数据。此 node 可以设置新数据，也可以覆盖已经存在的数据。对于需要使用前面 node 传入数据的 workflow，此 node 非常关键，例如向 Google Sheets 或数据库插入值时。

## Node parameters <a href="#node-parameters" id="node-parameters"></a>

这些是 Edit Fields node 中可用的设置和选项。

### Mode <a href="#mode" id="mode"></a>

你可以使用 **Manual Mapping** 通过 GUI 编辑字段，也可以使用 **JSON Output** 编写 JSON，让 n8n 将其添加到输入数据中。

### Fields to Set <a href="#fields-to-set" id="fields-to-set"></a>

如果选择 **Mode** > **Manual Mapping**，你可以从 **INPUT** 拖放值来配置字段。

拖动值时的默认行为是：

* n8n 将该值的名称设置为字段名称。
* 字段值包含一个访问该值的 expression。

如果不想使用 expression：

1. 将鼠标悬停在字段上。n8n 会显示 **Fixed | Expressions** 切换项。
2. 选择 **Fixed**。

字段的名称和值都可以这样设置。

![展示拖放操作以及将字段改为 fixed 的 GIF](<../../.gitbook/assets/drag-drop-fixed-toggle (1).gif>)

### Keep Only Set Fields <a href="#keep-only-set-fields" id="keep-only-set-fields"></a>

启用此项可丢弃未在 **Fields to Set** 中使用的任何输入数据。

### Include in Output <a href="#include-in-output" id="include-in-output"></a>

选择要包含在 node 输出数据中的输入数据。

## Node options <a href="#node-options" id="node-options"></a>

使用这些选项自定义 node 的行为。

### Include Binary Data <a href="#include-binary-data" id="include-binary-data"></a>

如果输入数据包含二进制数据，请选择是否将其包含在 Edit Fields node 的输出数据中。

### Ignore Type Conversion Errors <a href="#ignore-type-conversion-errors" id="ignore-type-conversion-errors"></a>

仅适用于 Manual Mapping。

启用此项后，n8n 在映射字段时可以忽略某些数据类型错误。

### Support Dot Notation <a href="#support-dot-notation" id="support-dot-notation"></a>

默认情况下，n8n 支持 dot notation。

例如，使用 manual mapping 时，此 node 会在 **Name** 字段中遵循 dot notation。这意味着，如果你将 **Name** 字段中的名称设置为 `number.one`，并将 **Value** 字段中的值设置为 `20`，生成的 JSON 为：

```json
{ "number": { "one": 20} }
```

你可以选择 **Add Option** > **Support Dot Notation**，并将 **Dot Notion** 字段设为关闭，从而阻止此行为。此时生成的 JSON 为：

```json
{ "number.one": 20 }
```

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Edit Fields (Set) 集成模板](https://n8n.io/integrations/set)或[搜索所有模板](https://n8n.io/workflows/)

## JSON Output mode 中的数组和 expression <a href="#arrays-and-expressions-in-json-output-mode" id="arrays-and-expressions-in-json-output-mode"></a>

创建 JSON Output 时，可以使用数组和 expression。

例如，给定 Customer Datastore node 生成的以下输入数据：

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10"
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05"
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09"
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12"
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16"
  }
]
```

在 **JSON Output** 字段中添加以下 JSON，并将 **Include in Output** 设置为 **All Input Fields**：

```json
{
  "newKey": "new value",
  "array": [{{ $json.id }},"{{ $json.name }}"],
  "object": {
    "innerKey1": "new value",
    "innerKey2": "{{ $json.id }}",
    "innerKey3": "{{ $json.name }}",
 }
}
```

你会得到以下输出：

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10",
    "newKey": "new value",
    "array": [
      23423532,
      "Jay Gatsby"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423532",
      "innerKey3": "Jay Gatsby"
    }
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05",
    "newKey": "new value",
    "array": [
      23423533,
      "José Arcadio Buendía"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423533",
      "innerKey3": "José Arcadio Buendía"
    }
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09",
    "newKey": "new value",
    "array": [
      23423534,
      "Max Sendak"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423534",
      "innerKey3": "Max Sendak"
    }
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12",
    "newKey": "new value",
    "array": [
      23423535,
      "Zaphod Beeblebrox"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423535",
      "innerKey3": "Zaphod Beeblebrox"
    }
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16",
    "newKey": "new value",
    "array": [
      23423536,
      "Edmund Pevensie"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423536",
      "innerKey3": "Edmund Pevensie"
    }
  }
]
```
