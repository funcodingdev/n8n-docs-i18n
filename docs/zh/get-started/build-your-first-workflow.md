---
contentType: tutorial
nodeTitle: Build your first workflow
originalFilePath: try-it-out/tutorial-first-workflow.md
originalUrl: https://docs.n8n.io/try-it-out/tutorial-first-workflow
url: https://docs.n8n.io/get-started/build-your-first-workflow
description: 在 n8n 中创建你的第一个工作流，并学习一些关键概念。
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

# 构建你的第一个工作流

本指南会展示如何在 n8n 中构建一个工作流[^1]，并在过程中解释关键概念。你将会：

* 从零创建一个工作流。
* 理解关键概念和技能，包括：
  * 使用 trigger node 启动工作流
  * 配置凭据[^2]
  * 处理数据
  * 在 n8n 工作流中表达逻辑
  * 使用表达式[^3]

!["已完成工作流的截图"](../../get-started/.gitbook/assets/tutorial-first.png)

本快速入门使用 [n8n Cloud](../../manage-cloud/overview.md)，这是推荐给新用户的方式。你可以免费试用。如果还没有账号，请现在[注册](https://app.n8n.cloud/register)。

## 第一步：创建新工作流 <a href="#step-one-create-a-new-workflow" id="step-one-create-a-new-workflow"></a>

打开 n8n 后，你会看到以下其中一种界面：

* 一个带欢迎信息和两个大按钮的窗口：选择 **Start from Scratch** 创建新工作流。
* **Overview** 页面上的 **Workflows** 列表。选择 **Create Workflow** 创建新工作流。

## 第二步：添加 trigger node <a href="#step-two-add-a-trigger-node" id="step-two-add-a-trigger-node"></a>

n8n 提供两种启动工作流的方式：

* 手动启动：选择 **Execute Workflow**。
* 自动启动：将 trigger node 作为第一个节点。trigger node 会响应外部事件，或根据你的设置运行工作流。

在本教程中，我们会使用 [Schedule trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.scheduletrigger)。它可以让你按计划运行工作流：

1. 选择 **Add first step**。
2. 搜索 **Schedule**。n8n 会显示匹配搜索的节点列表。
3. 选择 **Schedule Trigger**，将节点添加到画布。n8n 会打开该节点。
4. 在 **Trigger Interval** 中选择 **Weeks**。
5. 在 **Weeks Between Triggers** 中输入 `1`。
6. 输入时间和日期。本示例中，在 **Trigger on Weekdays** 中选择 **Monday**，在 **Trigger at Hour** 中选择 **9am**，并在 **Trigger at Minute** 中输入 `0`。
7. 关闭节点详情视图，返回画布。

## 第三步：添加 NASA 节点并设置凭据 <a href="#step-three-add-the-nasa-node-and-set-up-credentials" id="step-three-add-the-nasa-node-and-set-up-credentials"></a>

[NASA node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.nasa) 会与 NASA 的[公共 API](https://api.nasa.gov/) 交互，以获取有用数据。我们会使用 API 中的实时数据查找太阳活动事件。

<details>

<summary>凭据</summary>

凭据是应用和服务签发的私密信息，用于验证你的用户身份，并允许你在应用或服务与 n8n 节点之间连接和共享信息。所需信息类型取决于对应的应用或服务。请谨慎处理凭据，不要在 n8n 之外共享或泄露。

</details>

1. 在 Schedule Trigger 节点上，选择 **Add node** <img src="../../get-started/.gitbook/assets/add-node-small (1).png" alt="Add node icon" data-size="line"> 连接器。
2. 搜索 **NASA**。n8n 会显示匹配搜索的节点列表。
3. 选择 **NASA** 查看操作列表。
4. 搜索并选择 **Get a DONKI solar flare**。此操作会返回近期太阳耀斑的报告。选择该操作后，n8n 会将节点添加到画布并打开它。
5. 要访问 NASA API，需要设置凭据：
   1. 选择 **Credential for NASA API** 下拉菜单。
   2. 选择 **Create new credential**。n8n 会打开凭据视图。
   3. 前往 [NASA APIs](https://api.nasa.gov/)，通过 **Generate API Key** 链接填写表单。NASA 网站会生成密钥，并通过邮件发送到你填写的地址。
   4. 在邮箱中查收 API key。如果没有看到邮件，请检查垃圾邮件文件夹。复制该密钥，并粘贴到 n8n 的 **API Key** 中。
   5. 选择 **Save**。
   6. 关闭凭据页面。n8n 会回到节点。新凭据应该会在 **Credential for NASA API** 中自动选中。
6.  默认情况下，DONKI Solar Flare 会提供过去 30 天的数据。要将范围限制为最近一周，请使用 **Additional Fields**：<br>

    1. 选择 **Add field**。
    2. 选择 **Start date**。
    3. 要获取从一周前开始的报告，可以使用表达式：在 **Start date** 旁选择 **Expression** 选项卡，然后选择展开按钮 <img src="../../get-started/.gitbook/assets/open-expression-editor.png" alt="Add node icon" data-size="line"> 打开完整表达式编辑器。
    4. 在 **Expression** 字段中输入以下表达式：

    ```js
    {{ $today.minus(7, 'days') }}
    ```

    这会生成一个格式正确的日期，表示当前日期前 7 天。

    ![上方表达式生成日期的截图](../../get-started/.gitbook/assets/tutorial-date.png)
7. 关闭 **Edit Expression** 弹窗，返回 NASA 节点。
8. 现在可以检查该节点是否正常工作并返回预期数据：选择 **Execute step** 手动运行节点。n8n 会调用 NASA API，并在 **OUTPUT** 区域显示过去 7 天太阳耀斑的详细信息。
9. 关闭 NASA 节点，返回工作流画布。

## 第四步：使用 If 节点添加逻辑 <a href="#step-four-add-logic-with-the-if-node" id="step-four-add-logic-with-the-if-node"></a>

n8n 支持在工作流中使用复杂逻辑。本教程会使用 [If node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 创建两个分支，每个分支都会基于 NASA 数据生成一份报告。太阳耀斑有五种可能的分类；我们会添加逻辑，将较低分类的报告发送到一个输出，将较高分类的报告发送到另一个输出。

添加 If 节点：

1. 在 NASA 节点上，选择 **Add node** <img src="../../get-started/.gitbook/assets/add-node-small (1).png" alt="Add node icon" data-size="line"> 连接器。
2. 搜索 **If**。n8n 会显示匹配搜索的节点列表。
3. 选择 **If**，将节点添加到画布。n8n 会打开该节点。
4. 你需要检查 NASA 数据中 `classType` 属性的值。操作如下：
   1.  将 **classType** 拖入 **Value 1**。<br>

       <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>确保你已经在上一节运行过 NASA 节点</strong></p><p>如果没有按照上一节步骤运行 NASA 节点，这一步将看不到可用数据。</p></div>
   2. 将比较操作改为 **String > Contains**。
   3. 在 **Value 2** 中输入 **X**。这是太阳耀斑的最高分类。下一步中，你会创建两份报告：一份用于 X 级太阳耀斑，另一份用于所有较小级别的太阳耀斑。
5.  现在可以检查该节点是否正常工作并返回预期数据：选择 **Execute step** 手动运行节点。n8n 会根据条件测试数据，并在 **OUTPUT** 面板中显示哪些结果匹配 true 或 false。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>某些周可能没有大型太阳耀斑</strong></p><p>本教程使用实时数据。如果运行工作流时没有任何 X 级太阳耀斑，可以尝试将 <strong>Value 2</strong> 中的 <strong>X</strong> 替换为 <strong>A</strong>、<strong>B</strong>、<strong>C</strong> 或 <strong>M</strong>。</p></div>
6. 确认节点会返回一些事件后，关闭节点并返回画布。

## 第五步：从工作流输出数据 <a href="#step-five-output-data-from-your-workflow" id="step-five-output-data-from-your-workflow"></a>

工作流的最后一步是发送两份关于太阳耀斑的报告。本示例中，你会把数据发送到 [Postbin](https://www.toptal.com/developers/postbin/)。Postbin 是一种接收数据并在临时网页上显示数据的服务。

1. 在 If 节点上，选择标记为 **true** 的 **Add node** <img src="../../get-started/.gitbook/assets/add-node-small (1).png" alt="Add node icon" data-size="line"> 连接器。
2. 搜索 **PostBin**。n8n 会显示匹配搜索的节点列表。
3. 选择 **PostBin**。
4. 选择 **Send a request**。n8n 会将节点添加到画布并打开它。
5. 前往 [Postbin](https://www.toptal.com/developers/postbin/)，并选择 **Create Bin**。保持该标签页打开，方便测试工作流时返回查看。
6. 复制 bin ID。它看起来类似 `1651063625300-2016451240051`。
7. 在 n8n 中，将你的 Postbin ID 粘贴到 **Bin ID**。
8. 现在，配置要发送到 Postbin 的数据。在 **Bin Content** 旁边选择 **Expression** 选项卡（需要将鼠标悬停在 **Bin Content** 上才会显示该选项卡），然后选择展开按钮 <img src="../../get-started/.gitbook/assets/open-expression-editor.png" alt="Add node icon" data-size="line"> 打开完整表达式编辑器。
9. 现在可以从 If Node 输出中点击并拖动正确字段到表达式编辑器，从而自动为该标签创建引用。这里我们需要的输入是 `classType`。
10. 拖入表达式编辑器后，它会变成这个引用：`{{$json["classType"]}}`。给它添加一段消息，使完整表达式如下：

    ```js
    There was a solar flare of class {{$json["classType"]}}
    ```

    ![上方表达式生成输出的截图](../../get-started/.gitbook/assets/tutorial-expression.png)
11. 关闭表达式编辑器，返回节点。
12. 关闭 Postbin 节点，返回画布。
13. 再添加一个 Postbin 节点，用于处理 If 节点的 **false** 输出路径：
    1. 将鼠标悬停在 Postbin 节点上，然后选择 **Node context menu** <img src="../../get-started/.gitbook/assets/node-context-menu (1).png" alt="Node context menu icon" data-size="line"> > **Duplicate node**，复制第一个 Postbin 节点。
    2. 将 If 节点的 **false** 连接器拖到新 Postbin 节点的左侧。

## 第六步：测试工作流 <a href="#step-six-test-the-workflow" id="step-six-test-the-workflow"></a>

1. 现在可以测试整个工作流。选择 **Execute Workflow**。n8n 会运行工作流，并显示每个阶段的进度。
2. 返回你的 Postbin bin。刷新页面以查看输出。
3. 如果想使用这个工作流（也就是让它每周自动运行一次），需要点击 **Publish** 发布它。

{% hint style="info" %}
**时间限制**

Postbin 的 bin 创建后会保留 30 分钟。如果超过这个时间限制，可能需要创建新的 bin，并更新 Postbin 节点中的 ID。
{% endhint %}

## 恭喜 <a href="#congratulations" id="congratulations"></a>

现在你已经有了一个功能完整、能完成实际工作的工作流！它看起来应该类似这样：

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22name%22%3A%20%22Tutorial-workflow%22%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22rule%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22interval%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22field%22%3A%20%22weeks%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22triggerAtDay%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22triggerAtHour%22%3A%209%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.scheduleTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201.2%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-680%2C%0A%20%20%20%20%20%20%20%20100%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22ef14445c-2f5f-4c78-96c8-66732feb7a8f%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Schedule%20Trigger%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22resource%22%3A%20%22donkiSolarFlare%22%2C%0A%20%20%20%20%20%20%20%20%22additionalFields%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22startDate%22%3A%20%22%3D%7B%7B%20%24today.minus%287%2C%20%27days%27%29%20%7D%7D%22%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.nasa%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-460%2C%0A%20%20%20%20%20%20%20%20100%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2252c58b93-c780-4aff-a216-d67b28195a45%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%22credentials%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22nasaApi%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22id%22%3A%20%22sSVnxV9AcBmBOYn8%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22name%22%3A%20%22NASA%20account%22%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22conditions%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22caseSensitive%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22leftValue%22%3A%20%22%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22typeValidation%22%3A%20%22strict%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22version%22%3A%202%0A%20%20%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%20%20%22conditions%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22id%22%3A%20%222f469c8e-12b3-4ee5-95fc-ff81508d0b43%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22leftValue%22%3A%20%22%3D%7B%7B%20%24json.classType%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22rightValue%22%3A%20%22C%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22operator%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22string%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22operation%22%3A%20%22contains%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%22combinator%22%3A%20%22and%22%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.if%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202.2%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-240%2C%0A%20%20%20%20%20%20%20%20100%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22b54e3289-9ebb-451f-8bac-87edeeeced13%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22If%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22resource%22%3A%20%22request%22%2C%0A%20%20%20%20%20%20%20%20%22operation%22%3A%20%22send%22%2C%0A%20%20%20%20%20%20%20%20%22binId%22%3A%20%221741914338605-0907339996192%22%2C%0A%20%20%20%20%20%20%20%20%22binContent%22%3A%20%22%3DThere%20was%20a%20solar%20flare%20of%20class%20%7B%7B%24json%5B%5C%22classType%5C%22%5D%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22requestOptions%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.postBin%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-20%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22a8b602b6-17b1-4274-8d33-73344b6bb8fb%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22PostBin%28true%29%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22resource%22%3A%20%22request%22%2C%0A%20%20%20%20%20%20%20%20%22operation%22%3A%20%22send%22%2C%0A%20%20%20%20%20%20%20%20%22binId%22%3A%20%221741914338605-0907339996192%22%2C%0A%20%20%20%20%20%20%20%20%22binContent%22%3A%20%22%3DThere%20was%20a%20solar%20flare%20of%20class%20%7B%7B%24json%5B%5C%22classType%5C%22%5D%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22requestOptions%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.postBin%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-20%2C%0A%20%20%20%20%20%20%20%20200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2209c2c7a4-c229-430d-a5b0-8d7491515d9f%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22PostBin%28false%29%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22%23%23%20Setup%20required%5Cn%5CnYou%20need%20to%20create%20a%20NASA%20account%20and%20create%20credentials%2C%20and%20create%20a%20bin%20with%20Postbin%20and%20enter%20the%20ID%20-%20see%20%5Bthe%20documentation%5D%28https%3A%2F%2Fdocs.n8n.io%2Ftry-it-out%2Flonger-introduction%2F%29%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20120%2C%0A%20%20%20%20%20%20%20%20%22width%22%3A%20600%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-720%2C%0A%20%20%20%20%20%20%20%20-60%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2208e0b8f9-c90e-4c9c-a663-01aca805b9be%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22Schedule%20Trigger%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22NASA%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22If%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22If%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22PostBin%28true%29%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22PostBin%28false%29%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22active%22%3A%20false%2C%0A%20%20%22settings%22%3A%20%7B%0A%20%20%20%20%22executionOrder%22%3A%20%22v1%22%0A%20%20%7D%2C%0A%20%20%22versionId%22%3A%20%2237de4877-e4f6-4b9a-b6f0-9b7e7aea0163%22%2C%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22templateCredsSetupCompleted%22%3A%20true%2C%0A%20%20%20%20%22instanceId%22%3A%20%22cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7%22%0A%20%20%7D%2C%0A%20%20%22id%22%3A%20%22DPzMzTIyDrYohiw4%22%2C%0A%20%20%22tags%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22createdAt%22%3A%20%222021-06-25T07%3A47%3A07.640Z%22%2C%0A%20%20%20%20%20%20%22updatedAt%22%3A%20%222021-06-25T07%3A47%3A07.640Z%22%2C%0A%20%20%20%20%20%20%22id%22%3A%20%221%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22docs%22%0A%20%20%20%20%7D%0A%20%20%5D%0A%7D" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/try-it-out/quickstart/tutorial.json" %}

在这个过程中，你已经了解了：

* 如何找到所需节点并将它们连接在一起
* 如何使用表达式处理数据
* 如何创建凭据并将其关联到节点
* 如何在工作流中使用逻辑

你还可以在此基础上添加很多内容（例如添加更多凭据和一个节点，把结果通过邮件发送给你），也可能已经有了具体项目想法。无论下一步是什么，下面的资源都能提供帮助。

## 下一步 <a href="#next-steps" id="next-steps"></a>

* 对 AI 能做什么感兴趣？了解[如何使用 n8n 构建 AI chat agent](../../advanced-ai/intro-tutorial.md)。
* 学习 [n8n Academy](https://learn.n8n.io) 课程。
* 在 [workflow templates](https://n8n.io/workflows/) 中探索更多示例。

[^1]: n8n workflow 是一组用于自动化某个流程的节点。触发条件发生时，工作流开始执行，并按顺序运行以完成复杂任务。

[^2]: 在 n8n 中，credentials 用于存储连接特定应用和服务所需的身份验证信息。使用你的身份验证信息（用户名和密码、API key、OAuth secrets 等）创建凭据后，就可以使用关联的 app node 与该服务交互。

[^3]: 在 n8n 中，expressions 可以通过执行 JavaScript 代码动态填充节点参数。你不必提供静态值，而是可以使用 n8n expression 语法，基于前置节点、其他工作流或 n8n 环境中的数据定义该值。
