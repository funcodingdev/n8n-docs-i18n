---
title: KoboToolbox node documentation
description: >-
  了解如何在 n8n 中使用 KoboToolbox node。按照技术文档将 KoboToolbox node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: KoboToolbox node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox'
layout:
  description:
    visible: false
---

# KoboToolbox node <a href="#kobotoolbox-node" id="kobotoolbox-node"></a>

使用 KoboToolbox node 自动化 KoboToolbox 中的工作，并将 KoboToolbox 与其他应用集成。n8n 内置支持大量 KoboToolbox 功能，包括创建、更新、删除和获取 file、form、hook 与 submission。

在本页中，你可以找到 KoboToolbox node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [KoboToolbox credentials](../credentials/kobotoolbox.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* File
    * Create
    * Delete
    * Get
    * Get Many
* Form
    * Get
    * Get Many
    * Redeploy
* Hook
    * Get
    * Get Many
    * Logs
    * Retry All
    * Retry One
* Submission
    * Delete
    * Get
    * Get Many
    * Get Validation Status
    * Update Validation Status

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 KoboToolbox node 文档集成模板](https://n8n.io/integrations/kobotoolbox)或[搜索所有模板](https://n8n.io/workflows/)

## 选项 <a href="#options" id="options"></a>

### Query Options <a href="#query-options" id="query-options"></a>

Query Submission 操作支持 query option：

* 在 **Parameters** 面板的主区域中：
    * **Start** 控制开始 query 的 index offset（用于 API pagination 逻辑）。
    * **Limit** 设置要返回的最大 record 数。请注意，无论你提供什么值，API 返回的 record 数上限始终为 30,000。
* 在 **Query Options** 区域中，你可以启用以下参数：
    * **Query** 允许你以 MongoDB JSON query 格式指定 filter predicate。例如：`{"status": "success", "_submission_time": {"$lt": "2021-11-01T01:02:03"}}` 会查询 `status` 字段值为 `success`，且提交时间早于 2021 年 11 月 1 日 01:02:03 的所有 submission。
    * **Fields** 允许你指定要获取的 field 列表，让 response 更轻量。
    * **Sort** 允许你以 MongoDB JSON 格式提供排序条件列表。例如，`{"status": 1, "_submission_time": -1}` 指定按 status 升序排序，然后按 submission time 降序排序。

有关这些选项的更多详细信息，请参阅 [Formhub API 文档](https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters)。

### Submission options <a href="#submission-options" id="submission-options"></a>

所有返回 form submission 数据的操作都提供用于调整 response 的选项。这些选项包括：

- Download option 允许你下载链接到每个特定 form submission 的任何 attachment，例如图片和视频。它还允许你选择命名模式，以及要下载的文件大小（如果可用，通常用于图片）。
- Formatting option 会执行一些重新格式化，如[关于重新格式化](#about-reformatting)所述。

#### 关于重新格式化 <a href="#about-reformatting" id="about-reformatting"></a>

KoboToolbox submission 数据的默认 JSON 格式有时难以处理，因为它不了解 schema，因此所有字段都会以字符串返回。

此 node 提供一种轻量且带有明确取向的重新格式化逻辑，通过 **Reformat?** 参数启用。该参数适用于所有返回 form submission 的操作：submission query、get 和 attachment download 操作。

启用后，重新格式化会：

- 按照 form 的 group 将 JSON 重组为多层级结构。默认情况下，question grouping hierarchy 通过 field name 中的 `/` 字符体现，例如 `Group1/Question1`。启用重新格式化后，n8n 会将其重组为 `Group1.Question1`，即嵌套 JSON 对象。
- 重命名 field，去除 `_`（很多下游系统不支持）。
- 将所有 geospatial field（Point、Line 和 Area question type）解析为标准 GeoJSON 等价结构。
- 将所有匹配任意 **Multiselect Mask** wildcard mask 的 field 拆分为 array。由于 multi-select field 以空格分隔的字符串形式出现，无法通过算法猜测，因此你必须提供 field naming mask。mask 格式为逗号分隔列表。列表支持 `*` wildcard。
- 将所有匹配任意 **Number Mask** wildcard mask 的 field 转换为 JSON float。

下面是一个 JSON 详细示例：

```json
{
  "_id": 471987,
  "formhub/uuid": "189436bb09a54957bfcc798e338b54d6",
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details/Field_Name": "Test Fields",
  "Field_Details/Field_Location": "-1.932914 30.078211 1421 165",
  "Field_Details/Field_Shape": "-1.932914 30.078211 1421 165;-1.933011 30.078085 0 0;-1.933257 30.078004 0 0;-1.933338 30.078197 0 0;-1.933107 30.078299 0 0;-1.932914 30.078211 1421 165",
  "Field_Details/Crops_Grown": "maize beans avocado",
  "Field_Details/Field_Size_sqm": "2300",
  "__version__": "veGcULpqP6JNFKRJbbMvMs",
  "meta/instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "_uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_attachments": [],
  "_status": "submitted_via_web",
  "_geolocation": [
    -1.932914,
    30.078211
  ],
  "_submission_time": "2021-12-05T14:15:44",
  "_tags": [],
  "_notes": [],
  "_validation_status": {},
  "_submitted_by": null
}
```

启用重新格式化，并分别为 multi-select 和 number formatting 提供合适的 mask（例如 `Crops_*` 和 `*_sqm`）后，n8n 会将其解析为：

```json
{
  "id": 471987,
  "formhub": {
    "uuid": "189436bb09a54957bfcc798e338b54d6"
  },
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details": {
    "Field_Name": "Test Fields",
    "Field_Location": {
      "lat": -1.932914,
      "lon": 30.078211
    },
    "Field_Shape": {
      "type": "polygon",
      "coordinates": [
        {
          "lat": -1.932914,
          "lon": 30.078211
        },
        {
          "lat": -1.933011,
          "lon": 30.078085
        },
        {
          "lat": -1.933257,
          "lon": 30.078004
        },
        {
          "lat": -1.933338,
          "lon": 30.078197
        },
        {
          "lat": -1.933107,
          "lon": 30.078299
        },
        {
          "lat": -1.932914,
          "lon": 30.078211
        }
      ]
    },
    "Crops_Grown": [
      "maize",
      "beans",
      "avocado"
    ],
    "Field_Size_sqm": 2300
  },
  "version": "veGcULpqP6JNFKRJbbMvMs",
  "meta": {
    "instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a"
  },
  "xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "attachments": [],
  "status": "submitted_via_web",
  "geolocation": {
    "lat": -1.932914,
    "lon": 30.078211
  },
  "submission_time": "2021-12-05T14:15:44",
  "tags": [],
  "notes": [],
  "validation_status": {},
  "submitted_by": null
}
```

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}
