---
contentType: howto
nodeTitle: Connect nodes together
originalFilePath: workflows/components/connections.md
originalUrl: https://docs.n8n.io/workflows/components/connections
url: >-
  https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together
description: >-
  Connection 会在 node 之间建立链接，用于在工作流中路由数据。
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

# 将 node 连接在一起

Connection 会在 node 之间建立链接，用于在工作流中路由数据。两个 node 之间的 connection 会把一个 node 的输出数据传递给另一个 node 的输入。

![创建和删除 connection 的示例](../../../../build/.gitbook/assets/example.gif)

## 创建 connection <a href="#create-a-connection" id="create-a-connection"></a>

如需在两个 node 之间创建 connection，选择某个 node 右侧的灰点或 **Add node** <img src="../../../../build/.gitbook/assets/add-node-small (1).png" alt="Add node icon" data-size="line">，然后将箭头拖到后续 node 左侧的灰色矩形上。

## 删除 connection <a href="#delete-a-connection" id="delete-a-connection"></a>

将鼠标悬停在 connection 上，然后选择 **Delete** <img src="../../../../build/.gitbook/assets/delete-connector.png" alt="Delete connector icon" data-size="line">。
