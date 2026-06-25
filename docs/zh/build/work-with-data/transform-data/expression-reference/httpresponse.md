---
nodeTitle: Httpresponse
originalFilePath: data/expression-reference/httpresponse.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/httpresponse'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse
layout:
  description:
    visible: false
---
# HTTPResponse <a href="#httpresponse" id="httpresponse"></a>

## `$response`.**`body`** <a href="#dollarresponsebody" id="dollarresponsebody"></a>

**描述：** 最后一次 HTTP 调用返回的 response object 的 body。仅在 ‘HTTP Request’ node 中可用

**语法：** `$response`.`$response`.**`body`**

**返回：** Object

**来源：** 自定义 n8n 功能

## `$response`.**`headers`** <a href="#dollarresponseheaders" id="dollarresponseheaders"></a>

**描述：** 最后一次 HTTP 调用返回的 headers。仅在 ‘HTTP Request’ node 中可用。

**语法：** `$response`.`$response`.**`headers`**

**返回：** Object

**来源：** 自定义 n8n 功能

## `$response`.**`statusCode`** <a href="#dollarresponsestatuscode" id="dollarresponsestatuscode"></a>

**描述：** 最后一次 HTTP 调用返回的 HTTP status code。仅在 ‘HTTP Request’ node 中可用。

**语法：** `$response`.`$response`.**`statusCode`**

**返回：** Number

**来源：** 自定义 n8n 功能

## `$response`.**`statusMessage`** <a href="#dollarresponsestatusmessage" id="dollarresponsestatusmessage"></a>

**描述：** 关于请求状态的可选消息。仅在 ‘HTTP Request’ node 中可用。

**语法：** `$response`.`$response`.**`statusMessage`**

**返回：** String

**来源：** 自定义 n8n 功能
