---
title: Evaluation Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Evaluation Trigger node。按照技术文档将
  Evaluation Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Evaluation Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger
layout:
  description:
    visible: false
---

# Evaluation Trigger node <a href="#evaluation-trigger-node" id="evaluation-trigger-node"></a>

在设置 [evaluation](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test) 以验证 AI workflow 可靠性时，请使用 Evaluation Trigger node。在 evaluation 期间，Evaluation Trigger node 会从 Google Sheets 读取你的 evaluation dataset，并按顺序一次一个 item 发送到 workflow 中。

在本页中，你可以找到 Evaluation Trigger node 的参数和选项。

{% hint style="info" %}
**Google Sheets credentials**

Evaluation Trigger node 使用 data table 或 Google Sheets 存储测试 dataset。要使用 Google Sheets 作为 dataset 来源，请配置 [Google Sheets credential](../credentials/google/README.md)。
{% endhint %}

## 参数 <a href="#parameters" id="parameters"></a>

- **Source:** 选择测试 dataset 所在的位置。默认值为 **Data table**。

    Source 设置会根据 **Source** 选择而不同。

    * 当 **Source** 为 **Data table** 时：
        * **Data table:** 按名称或 ID 选择一个 data table。
        * **Limit Rows**：是否限制 data table 中要处理的行数。默认状态为 `off`。
            * **Max Rows to Process**：启用 **Limit Rows** 时，evaluation 期间要读取和处理的最大行数。默认值为 10。
            * **Filter Rows:** 是否过滤 data table 中要处理的行。默认状态为 `off`。
     * 当 **Source** 为 **Google Sheets** 时：
        - **Credential to connect with**：创建或选择已有的 [Google Sheets credentials](../credentials/google/README.md)。
        * **Document Containing Dataset**：选择包含测试 dataset 的 sheet 所在的电子表格文档。
            - 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 可输入 `spreadsheetId`。
            - 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
        * **Sheet Containing Dataset**：选择包含测试 dataset 的 sheet。
            - 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 可输入 sheet 标题。
            - 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
        * **Limit Rows**：是否限制 sheet 中要处理的行数。
            * **Max Rows to Process**：启用 **Limit Rows** 时，evaluation 期间要读取和处理的最大行数。
        * **Filters:** 根据列值过滤 evaluation dataset。
            * **Column**：选择要作为过滤依据的 sheet 列。选择 **From list** 可从下拉列表中选择列名，或选择 **By ID** 使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
            * **Value**：要作为过滤条件的列值。Evaluation 只会处理所选列具有给定值的行。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Evaluation Trigger node 集成模板](https://n8n.io/integrations/evaluation-trigger)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要进一步了解 n8n evaluations，请查看 [evaluations 文档](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test)

n8n 为 evaluations 提供了一个 app node。你可以在[这里](n8n-nodes-base.evaluation.md)找到该 node 文档。

对于常见问题或故障以及建议解决方案，请参阅 evaluations 的 [tips and common issues](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/fix-common-issues) 页面。
