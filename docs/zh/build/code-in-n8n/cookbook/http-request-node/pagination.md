---
description: HTTP Request node 的 pagination 示例。
contentType: howto
nodeTitle: Pagination
originalFilePath: code/cookbook/http-node/pagination.md
originalUrl: 'https://docs.n8n.io/code/cookbook/http-node/pagination'
url: 'https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination'
layout:
  description:
    visible: false
---

# HTTP Request node 中的 pagination <a href="#pagination-in-the-http-request-node" id="pagination-in-the-http-request-node"></a>

HTTP Request node 支持 pagination。此页面提供一些配置示例，包括使用 [HTTP node 变量](../../use-built-in-shortcuts/http-node.md)。

关于该 node 的更多信息，请参阅 [HTTP Request](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.httprequest)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/91KTZVqkKv8rY72iELNl/" %}


## 启用 pagination <a href="#enable-pagination" id="enable-pagination"></a>

在 HTTP Request node 中，选择 **Add Option** > **Pagination**。

## 使用 `$response` 从 response 获取下一页 URL <a href="#use-a-url-from-the-response-to-get-the-next-page-using-dollarresponse" id="use-a-url-from-the-response-to-get-the-next-page-using-dollarresponse"></a>

如果 API 在其 response 中返回下一页的 URL：

1. 将 **Pagination Mode** 设置为 **Response Contains Next URL**。n8n 会显示此选项的参数。
1. 在 **Next URL** 中，使用 expression[^1] 设置 URL。具体 expression 取决于你的 API 返回的数据。例如，如果 API 在 response body 中包含名为 `next-page` 的参数：
	```javascript
	{{ $response.body["next-page"] }}
	```

## 使用 `$pageCount` 按页码获取下一页 <a href="#get-the-next-page-by-number-using-dollarpagecount" id="get-the-next-page-by-number-using-dollarpagecount"></a>

如果你使用的 API 支持按页码定位特定页面：

1. 将 **Pagination Mode** 设置为 **Update a Parameter in Each Request**。
1. 将 **Type** 设置为 **Query**。
1. 输入 query 参数的 **Name**。这取决于你的 API，通常会在其文档中说明。例如，一些 API 使用名为 `page` 的 query 参数设置页码。因此 **Name** 应为 `page`。
1. 将鼠标悬停在 **Value** 上并开启 **Expression**。
1. 输入 `{{ $pageCount + 1 }}`

`$pageCount` 是 HTTP Request node 已获取的页数。它从零开始。大多数 API pagination 从一开始计数（第一页是 page one）。这意味着给 `$pageCount` 加 `+1` 后，该 node 第一次循环会获取第一页，第二次循环会获取第二页，依此类推。

## 通过 body 参数导航 pagination <a href="#navigate-pagination-through-body-parameters" id="navigate-pagination-through-body-parameters"></a>

如果你使用的 API 允许通过 body 参数分页：

1. 将 HTTP Request Method 设置为 **POST**
1. 将 **Pagination Mode** 设置为 **Update a Parameter in Each Request**。
1. 在 **Type** 参数中选择 **Body**。
1. 输入 body 参数的 **Name**。这取决于你使用的 API。`page` 是常见 key 名称。
1. 将鼠标悬停在 **Value** 上并开启 **Expression**。
1. 输入 `{{ $pageCount + 1 }}`

## 在 query 中设置 page size <a href="#set-the-page-size-in-the-query" id="set-the-page-size-in-the-query"></a>

如果你使用的 API 支持在 query 中选择 page size：

1. 在主 node 参数中选择 **Send Query Parameters**（这是你首次打开 node 时看到的参数，不是 options 内的设置）。
1. 输入 query 参数的 **Name**。这取决于你的 API。例如，很多 API 使用名为 `limit` 的 query 参数设置 page size。因此 **Name** 应为 `limit`。
1. 在 **Value** 中输入你的 page size。

[^1]: 在 n8n 中，expression 允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n expression 语法，通过前序 node、其他 workflow 或 n8n 环境中的数据来定义值。
