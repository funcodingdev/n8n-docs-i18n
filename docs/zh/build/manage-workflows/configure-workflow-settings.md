---
contentType: howto
nodeTitle: Configure workflow settings
originalFilePath: workflows/settings.md
originalUrl: https://docs.n8n.io/workflows/settings
url: https://docs.n8n.io/build/manage-workflows/configure-workflow-settings
description: 管理单个工作流的设置。
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

# 配置工作流设置

你可以使用 workflow settings 为单个工作流自定义工作流行为。

## 访问工作流设置 <a href="#access-workflow-settings" id="access-workflow-settings"></a>

要打开设置：

1. 打开你的工作流。
2. 选择右上角的 **three dots icon** <img src="../../../build/.gitbook/assets/three-dots-horizontal (1).png" alt="three dots icon" data-size="line">。
3. 选择 **Settings**。n8n 会打开 **Workflow settings** 弹窗。

## 可用设置 <a href="#available-settings" id="available-settings"></a>

以下设置可用：

### 执行顺序 <a href="#execution-order" id="execution-order"></a>

选择多分支工作流的执行顺序：

**v1（推荐）** 会依次执行每个分支，完成一个分支后再开始另一个分支。n8n 会根据分支在画布[^1]上的位置排序，从最上方到最下方执行。如果两个分支高度相同，则先执行最左侧分支。

**v0（旧版）** 会先执行每个分支的第一个节点，再执行每个分支的第二个节点，以此类推。

### Error Workflow (to notify when this one errors) <a href="#error-workflow-to-notify-when-this-one-errors" id="error-workflow-to-notify-when-this-one-errors"></a>

选择当前工作流失败时要触发的工作流。更多详情请参阅 [error workflows](../flow-logic/handle-errors-gracefully.md)。

### This workflow can be called by <a href="#this-workflow-can-be-called-by" id="this-workflow-can-be-called-by"></a>

选择哪些其他工作流可以调用此工作流。

### Timezone <a href="#timezone" id="timezone"></a>

设置此工作流的时区。时区设置对 Schedule Trigger 节点很重要。

你可以设置 n8n 实例的时区，以配置工作流使用的默认时区：

* [设置 n8n Cloud 实例时区](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/configure-cloud/set-your-timezone)
* [配置自托管实例的时区](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization)

如果没有配置工作流或实例时区，n8n 默认使用 EDT（New York）时区。

### Save failed production executions <a href="#save-failed-production-executions" id="save-failed-production-executions"></a>

n8n 是否应保存活跃工作流的失败执行。

### Save successful production executions <a href="#save-successful-production-executions" id="save-successful-production-executions"></a>

n8n 是否应保存活跃工作流的成功执行。

### Save manual executions <a href="#save-manual-executions" id="save-manual-executions"></a>

n8n 是否应保存用户在编辑器中启动的工作流执行。

### Save execution progress <a href="#save-execution-progress" id="save-execution-progress"></a>

n8n 是否应保存每个节点的执行数据。

如果设置为 **Save**，工作流在发生错误时会从停止位置继续。这可能会增加延迟。

### Timeout Workflow <a href="#timeout-workflow" id="timeout-workflow"></a>

n8n 是否应在经过一定时间后取消当前工作流执行。

启用后，会出现 **Timeout After** 选项。你可以在这里设置工作流超时所需的时间（以小时、分钟和秒为单位）。对于 n8n Cloud 用户，n8n 会根据每个方案强制设置可用的最大超时时间。

### Redact production execution data <a href="#redact-production-execution-data" id="redact-production-execution-data"></a>

控制 n8n 是否从生产（非手动触发）执行中隐藏执行数据。设置为 **Redact** 时，n8n 会隐藏每个节点的输入和输出数据，并用脱敏标记替代。

### Redact manual execution data <a href="#redact-manual-execution-data" id="redact-manual-execution-data"></a>

控制 n8n 是否从手动触发的执行中隐藏执行数据。设置为 **Redact** 时，n8n 会隐藏每个节点的输入和输出数据，并用脱敏标记替代。

如果实例管理员[在实例范围强制执行数据脱敏](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data#instance-level-enforcement)，n8n 会将强制范围覆盖的设置锁定为 **Redact**。你无法在这里关闭它们。

有关脱敏策略、显示数据和权限要求的详情，请参阅 [Execution data redaction](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data)。

### Estimated time saved <a href="#estimated-time-saved" id="estimated-time-saved"></a>

估算该工作流每次执行为你节省的分钟数。

设置此项后，n8n 可以为 [insights](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/track-usage-with-insights) 计算节省的时间。

### Custom span attributes <a href="#custom-span-attributes" id="custom-span-attributes"></a>

向工作流的 OpenTelemetry span 添加自定义键值属性。详情请参阅 [Custom span attributes](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry#custom-span-attributes)。

[^1]: Canvas 是 n8n editor UI 中构建工作流的主界面。你可以在 canvas 上添加并连接节点来编排工作流。
