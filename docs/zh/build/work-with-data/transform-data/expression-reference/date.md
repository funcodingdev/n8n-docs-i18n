---
nodeTitle: Date
originalFilePath: data/expression-reference/date.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/date'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date
layout:
  description:
    visible: false
---
# Date <a href="#date" id="date"></a>

## _`Date`_.**`toDateTime()`** <a href="#datetodatetime" id="datetodatetime"></a>

**描述：** 将 JavaScript Date 转换为 Luxon DateTime。DateTime 包含相同信息，但更易操作。

**语法：** _`Date`_.toDateTime()

**返回：** DateTime

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // date = new Date("2024-03-30T18:49")
  date.toDateTime().plus(5, 'days') //=> 2024-04-04T18:49
  ```
