---
title: Evaluation node 文档
description: >-
  n8n 中 Evaluation node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
nodeTitle: Evaluation node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.evaluation.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation'
layout:
  description:
    visible: false
---

# Evaluation node <a href="#evaluation-node" id="evaluation-node"></a>

Evaluation node 会执行与 [evaluation](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test) 相关的多种操作，用于验证你的 AI workflow 可靠性。

在以下场景中使用 Evaluation node：

* 根据 workflow 是否处于 evaluation 状态，有条件地执行逻辑
* 将 evaluation 结果写回 Google Sheet dataset
* 将 evaluation 性能的评分指标记录到 n8n 的 evaluations 标签页

{% hint style="info" %}
**Google Sheets credentials**

Evaluation node 的 **Set Outputs** 操作会将 evaluation 结果记录到 data table 或 Google Sheets。要使用 Google Sheets 作为记录位置，请配置 [Google Sheets credential](../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

Evaluation node 提供以下操作：

* [**Set Outputs**](#set-outputs)：将 evaluation 结果写回 data table 或 Google Sheet dataset。
* [**Set Metrics**](#set-metrics)：将 evaluation 性能的评分指标记录到 n8n 的 **Evaluations** 标签页。
* [**Check If Evaluating**](#check-if-evaluating)：根据当前 execution 是否为 evaluation，对 workflow 执行逻辑进行分支。

可用参数和选项取决于你选择的操作。

### Set Outputs <a href="#set-outputs" id="set-outputs"></a>

**Set Outputs** 操作包含以下参数：

- **Source:** 选择要输出 evaluation 结果的位置。默认值为 **Data table**。

   Source 设置会根据 **Source** 选择而不同。

    * 当 **Source** 为 **Data table** 时：
        * **Data table:** 按名称或 ID 选择一个 data table
    * 当 **Source** 为 **Google Sheets** 时：
        * **Credential to connect with**：创建或选择已有的 [Google Sheets credentials](../credentials/google/README.md)。
        * **Document Containing Dataset**：选择要写入 evaluation 结果的电子表格文档。通常这与你在 [Evaluation Trigger](n8n-nodes-base.evaluationtrigger.md) node 中选择的文档相同。
        * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 可输入 `spreadsheetId`。
            * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
        * **Sheet Containing Dataset**：选择要写入 evaluation 结果的 sheet。通常这与你在 [Evaluation Trigger](n8n-nodes-base.evaluationtrigger.md) node 中选择的 sheet 相同。
            * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 可输入 sheet 标题。
            * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。

你可以在 **Outputs** 部分定义要写入 data table 或 Google Sheet 的 item。对于每个输出，需要设置以下内容：

* **Name**：要写入 evaluation 结果的 Google Sheet 列名。
* **Value**：要写入 Google Sheet 的值。

### Set Metrics <a href="#set-metrics" id="set-metrics"></a>

**Set Metrics** 操作包含 **Metrics to Return** 部分，你可以在其中定义要为 evaluation 记录和跟踪的指标。你可以在 workflow 的 **Evaluations** 标签页中查看指标结果。

对于每个要记录的指标，需要设置以下详细信息：

* **Name**：用于该指标的名称。
* **Value**：要记录的数值。运行 evaluation 后，你可以从之前的 node 拖放值到这里。指标值必须是数字。

### Check If Evaluating <a href="#check-if-evaluating" id="check-if-evaluating"></a>

**Check If Evaluating** 操作没有任何参数。此操作提供分支输出 connector，让你可以根据当前 execution 是否为 evaluation 有条件地执行逻辑。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Evaluation node 集成模板](https://n8n.io/integrations/evaluation)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要进一步了解 n8n evaluations，请查看 [evaluations 文档](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test)

n8n 为 evaluations 提供了一个 trigger node。你可以在[这里](n8n-nodes-base.evaluationtrigger.md)找到该 node 文档。

对于常见问题或故障以及建议解决方案，请参阅 evaluations 的 [tips and common issues](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/fix-common-issues) 页面。
