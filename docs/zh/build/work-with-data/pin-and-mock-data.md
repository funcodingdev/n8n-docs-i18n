---
title: Data mocking and pinning
description: 开发期间在 n8n 工作流中 mock 和 pin 数据的方式。
contentType: howto
nodeTitle: Pin and mock data
originalFilePath: data/data-pinning.md
originalUrl: 'https://docs.n8n.io/data/data-pinning'
url: 'https://docs.n8n.io/build/work-with-data/pin-and-mock-data'
layout:
  description:
    visible: false
---

# Pin 和 mock 数据 <a href="#pinning-and-mocking-data" id="pinning-and-mocking-data"></a>

开发工作流时，你可能希望测试逻辑，而不必反复调用外部系统或使用实时数据。n8n 提供了两个相关功能来帮助你：

* **Data mocking**：无需连接真实数据源即可创建或模拟测试数据
* **Data pinning**：保存测试数据（mock 或真实数据），并在未来 workflow execution 中复用，而不是获取新数据

这两种方式都可以在开发期间节省时间和资源，帮助你使用一致的数据集，并保护线上系统免受重复测试调用影响。

{% hint style="info" %}
**仅用于开发**

Data pinning 和 mocking 是帮助你在开发期间测试工作流的功能。Data pinning 不适用于 production workflow execution。
{% endhint %}

## Data mocking 方式 <a href="#data-mocking-approaches" id="data-mocking-approaches"></a>

创建开发期间使用的测试数据。你可以通过多种方式创建 mock data：

### 使用 Code 或 Edit Fields node 生成自定义数据 <a href="#generate-custom-data-using-the-code-or-edit-fields-nodes" id="generate-custom-data-using-the-code-or-edit-fields-nodes"></a>

你可以在工作流中使用 [Code node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 或 [Edit Fields (Set) node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.set) 创建自定义数据集。

在 Code node 中，你可以创建任意数据集，并将其作为 node 输出返回。在 Edit Fields node 中，选择 **Add fields** 添加自定义数据。

Edit Fields node 适合小型测试。如需创建更复杂的数据集，请使用 Code node。

**适用场景**：你需要完全控制测试数据结构和值，或希望使用特定数据模式测试边界情况。

### 从 Customer Datastore node 输出示例数据集 <a href="#output-a-sample-data-set-from-the-customer-datastore-node" id="output-a-sample-data-set-from-the-customer-datastore-node"></a>

Customer Datastore node 提供了一个可供使用的假数据集。添加并执行该 node 即可探索数据。

**适用场景**：你在探索 n8n 时需要一些测试数据，但还没有真实 use case 可用。

创建或获取想在多次 workflow execution 中复用的测试数据后，使用 [Data pinning](#data-pinning) 保存它，以便进行一致的测试。

## Data pinning <a href="#data-pinning" id="data-pinning"></a>

你可以在工作流开发期间“pin”数据。Data pinning 指保存某个 node 的输出数据，并在未来 workflow execution 中使用保存的数据，而不是获取新数据。

处理来自外部来源的数据时，你可以使用此功能，避免重复请求外部系统。这可以节省时间和资源：

* 如果你的工作流依赖外部系统触发，例如 webhook 调用，pin 数据意味着你不必每次测试工作流都使用外部系统。
* 如果外部资源有数据或使用限制，在测试期间 pin 数据可以避免消耗资源限额。
* 你可以获取并 pin 想测试的数据，然后确信所有工作流测试中的数据一致。
* 你可以使用上述方式 mock 测试数据，然后 pin 它，以便跨 execution 复用。

你只能为具有单个主输出的 node pin 数据（“error” 输出不计入此用途）。

### Pin 数据 <a href="#pin-data" id="pin-data"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/3EMfTKLe60rEZQ4dBdBw/" %}

### 取消 pin 数据 <a href="#unpin-data" id="unpin-data"></a>

启用 data pinning 后，node 输出面板顶部会出现横幅，表示 n8n 已 pin 数据。如需取消 pin 并在下次 execution 中获取新数据，选择横幅中的 **Unpin** 链接。

### 编辑已 pin 数据 <a href="#edit-pinned-data" id="edit-pinned-data"></a>

n8n 允许你编辑已 pin 数据。这意味着你可以检查不同场景，而无需设置每个场景并从外部系统发送相关数据。它让边界情况测试更容易。

{% hint style="info" %}
**仅用于开发**

Data editing 不适用于 production workflow execution。它是帮助你在开发期间测试工作流的功能。
{% endhint %}

#### 编辑输出数据 <a href="#edit-output-data" id="edit-output-data"></a>

如需编辑输出数据：

1. 运行 node 以加载数据。
2. 在 **OUTPUT** 视图中，选择 **JSON** 切换到 JSON 视图。
3. 选择 **Edit** <img src="../../../build/.gitbook/assets/edit-data.png" alt="Edit data icon" data-size="line">。
4. 编辑数据。
5. 选择 **Save**。n8n 会保存数据更改并 pin 数据。

#### 使用先前 execution 的数据 <a href="#use-data-from-previous-executions" id="use-data-from-previous-executions"></a>

你可以从先前 workflow execution 的 node 中复制数据：

1. 打开左侧菜单。
2. 选择 **Executions**。
3. 浏览 workflow executions 列表，找到包含要复制数据的 execution。
4. 选择 **Open Past Execution** <img src="../../../build/.gitbook/assets/open-execution.png" alt="Open past execution icon" data-size="line">。
5. 双击要复制其数据的 node。
6. 如果是表格布局，选择 **JSON** 切换到 JSON 视图。
7. 有两种方式复制 JSON：
  1. 像选择文本一样高亮选择所需 JSON。然后使用 `ctrl` + `c` 复制。
  2. 点击某个参数来选择要复制的 JSON。然后：
    1. 将鼠标悬停在 JSON 上。n8n 会显示 **Copy** <img src="../../../build/.gitbook/assets/copy-data.png" alt="Copy data icon" data-size="line"> 按钮。
    2. 选择 **Copy** <img src="../../../build/.gitbook/assets/copy-data.png" alt="Copy data icon" data-size="line">。
    3. 你可以选择复制内容：
        * **Copy Item Path** 和 **Copy Parameter Path** 会给出访问 JSON 部分内容的 expression。
        * **Copy Value**：复制整个选中的 JSON。
8. 返回正在处理的工作流：
    1. 打开左侧菜单。
    2. 选择 **Workflows**。
    3. 选择 **Open**。
    4. 选择要打开的工作流。
9. 打开要使用已复制数据的 node。
10. 如果没有数据，运行该 node 以加载数据。
11. 在 **OUTPUT** 视图中，选择 **JSON** 切换到 JSON 视图。
12. 选择 **Edit** <img src="../../../build/.gitbook/assets/edit-data.png" alt="Edit data icon" data-size="line">。
15. 粘贴来自先前 execution 的数据。
16. 选择 **Save**。n8n 会保存数据更改并 pin 数据。

### 结合 mocking 和 pinning <a href="#combine-mocking-with-pinning" id="combine-mocking-with-pinning"></a>

为获得最贴近真实情况的测试体验，你可以结合 mocking 和 pinning：

1. 使用其中一种 mocking 方式创建测试数据（Code node、Edit Fields node 或 Customer Datastore）
2. 编辑测试数据以创建特定测试场景或边界情况
3. Pin 编辑后的数据，以便在多次 workflow execution 中复用
4. 使用这个已编辑且已 pin 的数据集继续开发

这种方式让你完全控制测试数据，同时确保多次运行之间的测试保持一致。
