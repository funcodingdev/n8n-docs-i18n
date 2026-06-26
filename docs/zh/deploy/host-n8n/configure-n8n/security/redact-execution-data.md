---
title: Execution data 脱敏
contentType: howto
nodeTitle: Redact execution data
originalFilePath: workflows/executions/execution-data-redaction.md
originalUrl: https://docs.n8n.io/workflows/executions/execution-data-redaction
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data
description: >-
  控制 workflows 中 execution data 的可见性，以保护敏感信息并满足合规要求。
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

# Execution data 脱敏 <a href="#redact-execution-data" id="redact-execution-data"></a>

{% hint style="info" %}
**功能可用性**

Data redaction 可用于 Enterprise Self-hosted 和 Enterprise Cloud plans。

**可用版本：** n8n version 2.16.0（per-workflow redaction）、n8n version 2.26.0（instance-level enforcement）
{% endhint %}

Execution data redaction 让你隐藏 workflow executions 的 input 和 output data。这有助于保护 personal data、authentication tokens、financial records 等敏感信息，避免让可以查看 workflow 但不需要查看底层数据的用户接触这些内容。

启用 redaction 后，execution metadata（status、timing、node names）仍然可见，但 n8n 会把每个 node 实际处理的数据 payload 替换为 redacted indicator。

你可以按 workflow 配置 redaction，也可以[在整个 instance 范围强制执行](redact-execution-data.md#instance-level-enforcement)，让每个 workflow 都对 execution data 进行脱敏。

## 为什么使用 execution data redaction <a href="#why-use-execution-data-redaction" id="why-use-execution-data-redaction"></a>

Workflows 经常处理 workflow builder 或 viewers 在 n8n 之外不应该访问的数据。常见场景包括：

* **PII 和 compliance**：处理客户 personal data（emails、addresses、financial records）的 workflows 需要满足 GDPR、SOC 2 或内部安全标准。
* **跨部门 workflows**：一个 team 构建的 workflow 会处理另一个 team 的敏感数据，而 builder 原本不应该访问这些数据。
* **最小权限原则**：只让需要数据的人看到数据，而不是让所有拥有 workflow view access 的人都能看到。

在 execution data redaction 之前，唯一选择是在 workflow 级别完全禁用 execution history，这会移除 workflow 成功或失败状态的全部可见性。Execution data redaction 可以保留 execution monitoring，同时隐藏敏感 data payload。

## 配置 redaction 设置 <a href="#configure-redaction-settings" id="configure-redaction-settings"></a>

你可以在 workflow settings 中按 workflow 配置 redaction。你需要 `workflow:enableRedaction` 或 `workflow:disableRedaction` scope（或两者）才能更改这些设置。

配置 redaction：

1. 打开你的 workflow。
2. 选择右上角的 **three dots icon** <img src="../../../.gitbook/assets/three-dots-horizontal (1).png" alt="three dots icon" data-size="line">。
3. 选择 **Settings**。
4. 找到 **Redact production execution data** 和 **Redact manual execution data** 设置。
5. 对每个设置，选择 **Default - Do not redact** 或 **Redact**。
6. 选择 **Save**。

{% hint style="info" %}
**设置被 instance enforcement 锁定**

当 [instance-level enforcement](redact-execution-data.md#instance-level-enforcement) 处于启用状态时，n8n 会把 enforced scope 覆盖的设置锁定为 **Redact**。你无法在 workflow 级别关闭它们。
{% endhint %}

### Redaction 设置说明 <a href="#redaction-settings-explained" id="redaction-settings-explained"></a>

有两个独立 toggle 控制 redaction：

| 设置 | 控制内容 |
| --- | --- |
| **Redact production execution data** | 控制 n8n 是否对 production（非手动触发）executions 的数据进行脱敏。Production executions 包括 workflow 保持 active 时由 webhooks、schedules 或其他 triggers 触发的 executions。 |
| **Redact manual execution data** | 控制 n8n 是否对手动触发的 executions 的数据进行脱敏。Manual executions 包括你在 editor 中选择 **Execute Workflow** 启动的 executions。 |

## Instance-level enforcement <a href="#instance-level-enforcement" id="instance-level-enforcement"></a>

Instance owners 和 admins 可以为 instance 上的所有 workflows 强制执行 redaction，而不是依赖每个 workflow 自己的设置。Enforcement 会设置一个适用于所有位置的最低 redaction policy（一个 "floor"）。

要启用 enforcement，请前往 **Settings** > **Security**，并配置 **Data redaction** section。分步说明请参考 [Security settings](manage-security-policies.md#enforce-execution-data-redaction)。

### Enforcement scope <a href="#enforcement-scope" id="enforcement-scope"></a>

Enforcement scope 控制 n8n 在整个 instance 中会对哪些 executions 脱敏：

| Scope | 强制内容 |
| --- | --- |
| **Production executions** | n8n 会对每个 workflow 中的 production executions 脱敏。Manual executions 遵循每个 workflow 自己的设置。这是推荐设置：它保护 live data，同时保留 manual test runs 以便 debugging。 |
| **Manual and production executions** | n8n 会对每个 workflow 中的所有 executions 脱敏。当 test data 也很敏感时使用此选项。 |

### Enforcement 如何与 workflow settings 交互 <a href="#how-enforcement-interacts-with-workflow-settings" id="how-enforcement-interacts-with-workflow-settings"></a>

* **Enforcement 会在读取 execution data 时生效。** 每当有人查看 execution 时，n8n 都会对 enforcement scope 覆盖的数据进行脱敏，包括那些自身 settings 未启用 redaction 的 workflows 的 executions。
* **Workflow settings 不能弱于 enforced scope。** Workflow settings UI 会锁定受影响的 redaction toggles，[public API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api) 也会拒绝创建或更新 redaction policy 低于 floor 的 workflow。Workflows 仍然可以选择比 floor 更严格的 redaction。
* **新 workflows 会从 floor 开始。** 在 enforcement 启用时创建 workflow，其 redaction policy 默认会设为 enforced scope。如果你通过 public API 创建 workflow 且没有指定 redaction policy，n8n 会把它设为 floor。
* **现有 workflow settings 保持不变。** 启用 enforcement 不会修改现有 workflows 已存储的 settings。它们的 execution data 仍会按 enforced scope 脱敏；如果之后禁用 enforcement，每个 workflow 会回到自己的设置。

## 会脱敏哪些内容 <a href="#what-gets-redacted" id="what-gets-redacted"></a>

当 n8n 对 execution 进行 redaction 时，会脱敏：

* **Item JSON data**：n8n 会把每个 node 的所有 input 和 output data（`item.json`）替换为空对象。
* **Binary data**：n8n 会移除 files、images 等 binary data（`item.binary`）。
* **声明为 sensitive 的 fields**：n8n 始终会脱敏 node authors 使用 `sensitiveOutputFields` 标记为 sensitive 的 fields，并阻止 reveal，即使用户拥有 reveal access 也一样。
* **Error metadata**：n8n 会脱敏 error messages，只保留 error type 和 HTTP status code（针对 API errors），以辅助 troubleshooting。

在 redacted execution 中：

* Execution viewer 会显示带有 shredder icon 的 **"Data redacted"** indicator，而不是常规 data tables。
* Execution metadata 保持可见：node names、execution status（success/failure）、timing information 和 workflow structure。

{% hint style="info" %}
**Error information**

当 n8n 对 execution data 进行 redaction 时，也会脱敏 error details，防止敏感信息通过 error messages 泄露。只保留 error type（例如 `NodeApiError`）和 HTTP status code。这样可以提供足够信息来识别 failure 类别，而不会暴露数据。
{% endhint %}

## Reveal redacted data <a href="#reveal-redacted-data" id="reveal-redacted-data"></a>

拥有 **Reveal execution data**（`execution:reveal`）scope 的用户可以临时查看某个具体 execution 的 redacted execution data。Instance owners 和 admins 默认拥有此 scope。

Reveal data：

1. 在 execution viewer 中打开 execution。
2. 选择 redacted data 区域中显示的 **Reveal data** button。
3. 查看 confirmation dialog。它会说明：
   * 系统会在 audit trail 中记录此操作。
   * 只有在有 legitimate reason 时才应该 reveal data。
   * 不必要的 access 可能违反你组织的 policy。
4. 选择 **Reveal data** 确认。

该 execution data 会在当前 session 中对该 execution 变为可见。

{% hint style="info" %}
**使用 dynamic credentials 的 executions**

对于使用 dynamic credentials 的 executions，无论用户 permissions 或当前 redaction policy 如何，n8n 都会拒绝 reveal requests。这可以防止暴露 execution 在 runtime 解析出的 credentials。
{% endhint %}

## 审计日志 <a href="#audit-logging" id="audit-logging"></a>

[Log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems) 会跟踪 reveal actions 和 enforcement policy changes。以下 audit events 可用：

| Event | Description |
| --- | --- |
| `n8n.audit.execution.data.revealed` | 当用户 reveal redacted execution data 时，n8n 会发出此 event。包含 user、execution ID、workflow ID、timestamp、IP address 和当前生效的 redaction policy。 |
| `n8n.audit.execution.data.reveal_failure` | 当 n8n 拒绝 reveal attempt 时（例如 permissions 不足），会发出此 event。包含相同 fields 以及 rejection reason。 |
| `n8n.audit.redaction-enforcement.updated` | 当用户更改 instance-level enforcement policy 时，n8n 会发出此 event。包含 user 以及变更前后的 policy values。 |

这些 events 会与你现有的 log streaming destinations（syslog、webhooks、Sentry）集成，并支持 compliance reporting 和 access auditing。

## Permission scopes <a href="#permission-scopes" id="permission-scopes"></a>

Execution data redaction 引入以下 permission scopes，你可以通过 [custom project roles](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles) 分配：

| Scope | 用途 |
| --- | --- |
| `workflow:enableRedaction` | 允许在 workflow settings 中开启 redaction。在 role configuration UI 中显示为 **Enable data redaction**。 |
| `workflow:disableRedaction` | 允许在 workflow settings 中关闭 redaction。在 role configuration UI 中显示为 **Disable data redaction**。 |

默认情况下，instance owners、admins 和 project admins 拥有启用或禁用 redaction，以及 reveal redacted data 的权限。你可以创建 custom roles，为 workflow builders 等更多用户独立授予一个或两个 scopes。

## Redaction 不覆盖哪些内容 <a href="#what-redaction-doesnt-cover" id="what-redaction-doesnt-cover"></a>

Redaction 控制的是用户查看 executions 时 execution data 的可见性。它不是 backend access control，某些 data paths 不在它的覆盖范围内。评估 redaction 是否满足合规要求时，请注意以下限制：

* **Code node `console.log` output**：Code node 使用 `console.log` 记录的数据不会被脱敏。在 manual executions 中，output 会出现在 editor 的 Logs panel 中。在 production executions 中，output 会进入 server 的 standard output (stdout) 以及连接到它的任何 logging infrastructure。
* **Nodes 之间流动的数据**：Redaction 不会限制 downstream nodes 接收什么内容。在 execution 期间，数据会在 nodes 之间不受限制地流动，因此 workflow 中的任何 node 都可以把 execution data 发送到 external systems。Redaction 控制用户在 execution viewer 中看到什么，而不是 workflow 本身如何使用数据。
* **Webhook responses**：workflow 返回给 caller 的 response body（例如通过 Respond to Webhook node 或 node 的 respond option）是 raw data，而不是 redacted version。
* **Outbound requests 中的 authentication headers**：Redaction 不会修改 workflows 向 external services 发出的 requests，包括其中包含的任何 authentication headers。
* **不支持 field-level redaction**：Redaction 适用于 node 的整个 data payload。你不能为数据中的单个 fields 配置 redaction。例外是 node authors 声明为 sensitive 的 fields，n8n 始终会脱敏它们。
* **Stored data 保持原样**：Redaction 不会加密或修改 database 中的 execution data。n8n 在通过 API 提供数据时应用 redaction。任何拥有 direct database access 的人都可以读取底层数据。
* **Enforcement 不会通过 source control 传播**：Instance-level enforcement 是 instance policy，当你使用 [source control](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments) push workflows 时不会包含它。从 enforced instance push 到 non-enforced instance 的 workflow，在目标 instance 上不会被 redacted。这与 two-factor authentication enforcement 等其他 instance-level policies 的行为一致。

## 最佳实践 <a href="#best-practices" id="best-practices"></a>

### 选择合适的 redaction policy <a href="#choosing-the-right-redaction-policy" id="choosing-the-right-redaction-policy"></a>

| 场景 | 推荐设置 |
| --- | --- |
| 在 production 中处理 PII、financial data 或 authentication tokens 的 workflows | Redact production execution data |
| test data 也敏感的 workflows（例如使用 production data 的副本） | Redact both production and manual execution data |
| 处理非敏感数据的 workflows，或初始开发阶段 | No redaction |

### 通用建议 <a href="#general-recommendations" id="general-recommendations"></a>

* **从 production redaction 开始**：对于大多数处理敏感数据的 workflows，redacting production executions 同时保持 manual executions 可见，可以在安全性和 debugging 便利性之间取得良好平衡。
* **按需 redacting manual data**：如果你的 test environment 使用真实或接近 production 的数据，也要启用 manual execution redaction。
* **使用 log streaming**：启用 [log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems) 捕获 reveal audit events。这会为 compliance 提供 audit trail，并让你 monitor 谁访问了敏感 execution data。
* **在 workflow reviews 中检查 redaction 设置**：把 redaction policy 纳入 workflow review 或 approval process，特别是对于处理跨部门或 customer-facing data 的 workflows。

## 安全注意事项 <a href="#security-considerations" id="security-considerations"></a>

* n8n 在 API level 应用 redaction，并且绝不会把 redacted data 发送到 browser。
* 当你[创建 custom nodes](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview) 时，可以在 node type definition 中使用 `sensitiveOutputFields` 声明特定 output fields 为 sensitive。n8n 始终会脱敏这些 fields，并阻止 reveal，即使用户拥有 reveal access 也一样。
* 如果 redaction service 无法解析 node 的 type definition（例如卸载 community node 后），n8n 会完整脱敏该 node 的所有 output data。这种 fail-closed approach 可防止 unknown nodes 泄露 sensitive fields。
* 启用 redaction 后，execution data 也会自动从 [log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems) 和 logging output 中脱敏。
