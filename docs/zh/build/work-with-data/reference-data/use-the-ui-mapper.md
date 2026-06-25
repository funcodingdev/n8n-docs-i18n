---
contentType: howto
nodeTitle: Use the UI mapper
originalFilePath: data/data-mapping/data-mapping-ui.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/data-mapping-ui'
url: 'https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper'
layout:
  description:
    visible: false
---

# 在 UI 中引用数据 <a href="#referencing-data-in-the-ui" id="referencing-data-in-the-ui"></a>

Data mapping 指引用前序 node 的数据。它不包括更改（转换）数据，只是引用数据。

当你需要工作流中某个特定 node 的数据时，可以[按名称引用 node](reference-previous-nodes.md)。当工作流有多个分支，或需要访问前面多个步骤的数据时，这很有用。

你可以通过以下方式映射数据：

* 使用 expressions editor。
* 将数据从 **INPUT** 面板拖放到 node 参数中。这会为你生成 expression。

![在 UI 中创建 expressions](../../../../build/.gitbook/assets/expressionEditor.gif)

有关 mapping 和 linking items 的错误信息，请参阅 [Item linking errors](link-data-items/item-linking-errors.md)。

参阅[常见引用方式](reference-previous-nodes.md#common-ways-of-referencing)。
