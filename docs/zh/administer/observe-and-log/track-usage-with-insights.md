---
description: Insights
contentType: explanation
nodeTitle: Track usage with Insights
originalFilePath: insights.md
originalUrl: 'https://docs.n8n.io/insights'
url: 'https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights'
layout:
  description:
    visible: false
---

# Insights <a href="#insights" id="insights"></a>

Insights 让 instance owners 和 admins 可以查看 workflows 随时间变化的 performance。此 feature 由三部分组成：

- [**Insights summary banner**](#insights-summary-banner)：在 **Overview** space 顶部显示 instance 过去 7 天的 key metrics。
- [**Insights dashboard**](#insights-dashboard)：更详细的 visual breakdown，包含 per-workflow metrics 和 historical comparisons。
- [**Time saved (Workflow ROI)**](#setting-the-time-saved-by-a-workflow)：对于每个 workflow，你可以选择设置每个 workflow 节省的固定时间，或基于特定 workflow 上所采用的 execution path 动态计算节省时间。

{% hint style="info" %}
**功能可用性**

Insights summary banner 会为所有 plans 显示过去 7 天的 activity。Insights dashboard 仅可用于 Pro、Business 和 Enterprise plans。
{% endhint %}

## Insights summary banner <a href="#insights-summary-banner" id="insights-summary-banner"></a>

n8n 会为 insights summary banner 和 dashboard 收集多个 metrics。它们包括：

- Total production executions（不包括 sub-workflow executions 或 manual executions）
- Total failed production executions
- Production execution failure rate
- Time saved（当至少一个或多个 active workflows 上已设置时）
- Run time average（包括任何 wait nodes 的 wait time）

## Insights dashboard <a href="#insights-dashboard" id="insights-dashboard"></a>

从 side navigation 访问 **Insights** section。Summary banner 中的每个 metric 也可以点击，会带你到对应 chart。

Insights dashboard 还有一个 table，显示来自每个 workflow 的 individual insights，包括 total production executions、failed production executions、failure rate、time saved 和 run time average。

## Insights time periods <a href="#insights-time-periods" id="insights-time-periods"></a>

默认情况下，insights summary banner 和 dashboard 显示 rolling 7 day window，并与 previous period 比较，以识别每个 metric 的 increases 或 decreases。在 dashboard 上，paid plans 还会显示其他 date ranges 的 data：

- Pro：7 和 14 天
- Business：24 小时、7 天、14 天、30 天。
- Enterprise：24 小时、7 天、14 天、30 天、90 天、6 个月、1 年

## 设置 workflow 节省的时间 <a href="#setting-the-time-saved-by-a-workflow" id="setting-the-time-saved-by-a-workflow"></a>

对于每个 workflow，你可以 track 它为你节省了多少时间。此 setting 帮助你计算随时间推移，automating a process 相比完成同一 task 或 process 的 manual effort 节省了多少时间。

配置后，n8n 会基于 production executions 数量计算 workflow 为你节省的时间，并显示在 summary banner 和 insights dashboard 上。

你可以选择两种计算 time saved 的方法：

### Fixed time saved <a href="#fixed-time-saved" id="fixed-time-saved"></a>

使用 fixed time saved 时，你设置一个适用于该 workflow 每次 production execution 的单一 time value，无论 execution 采用哪个 path。

配置 fixed time saved：

1. Navigate 到 workflow
2. 选择右上角 three dots menu，并选择 **Settings**
3. 在 **Estimated time saved** dropdown 中，选择 **Fixed**
4. 输入每次 execution 节省的 work minutes 数
5. 保存 settings

### Dynamic time saved <a href="#dynamic-time-saved" id="dynamic-time-saved"></a>

Dynamic time saved 会基于实际采用的 execution path 计算 time savings，适用于不同 execution paths 节省不同时间的 workflows。

配置 dynamic time saved：

1. Navigate 到 workflow
2. 选择右上角 three dots menu，并选择 **Settings**
3. 在 **Estimated time saved** dropdown 中，选择 **Dynamic**
4. 保存 settings
5. 在 workflow 中节省时间的位置添加 **Time Saved** nodes
6. 对每个 Time Saved node，配置：
   - **Time saved**：节省的时间量（minutes）
   - **Calculation mode**：选择每次 execution 对所有 items 只计算一次节省时间，或按 item 计算，这会将节省 minutes 乘以 input items 总数

使用 dynamic time saved 时，n8n 会把 workflow run 期间所有执行的 Time Saved nodes 的时间相加，计算该 execution 的 total time saved。

{% hint style="info" %}
**Subworkflow support**

Time saved tracking 当前只适用于 parent workflows。目前不支持来自 subworkflows 的 time saved，计划在 future release 中支持。
{% endhint %}

## 禁用或配置 insights metrics collection <a href="#disable-or-configure-insights-metrics-collection" id="disable-or-configure-insights-metrics-collection"></a>

如果你 self-host n8n，可以使用 [environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights) 禁用或配置 insights 和 metrics collection。

默认情况下，n8n 会保留 compacted insights data 365 天（`N8N_INSIGHTS_MAX_AGE_DAYS`）。n8n 将 retention 上限设为 730 天（两年）；如果需要更短 window，请使用较小数值。要完全关闭 insights collection，请设置 `N8N_DISABLED_MODULES=insights`（参考 [environment variables page](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights)）。

{% hint style="info" %}
**Self-host upgrade**

在较旧 versions 中，pruning 可能遵循 license-driven defaults（通常为 180 天）。现在 `N8N_INSIGHTS_MAX_AGE_DAYS` 控制 pruning（默认 365）。如果你想要类似 previous default 的 retention window，请设置 `N8N_INSIGHTS_MAX_AGE_DAYS=180`。
{% endhint %}

n8n 会以 one-hour granularity 存储 recent insights，然后将 older data compact 为 day-level 和 week-level summaries。使用 [Insights environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights) 控制 compaction timing、batch limits、runtime 和 delays。

将这些 thresholds 提高到 defaults 之上，会更长时间保留 finer detail。这会向 `insights_by_period` 添加更多 rows，并比单独延长 `N8N_INSIGHTS_MAX_AGE_DAYS` 使用更多 database space。如果你只需要更长 retention window，请先增加 `N8N_INSIGHTS_MAX_AGE_DAYS`。

## Insights FAQs <a href="#insights-faqs" id="insights-faqs"></a>

### n8n 使用哪些 executions 来计算 insights banner 和 dashboard 中的 values？ <a href="#which-executions-do-n8n-use-to-calculate-the-values-in-the-insights-banner-and-dashboard" id="which-executions-do-n8n-use-to-calculate-the-values-in-the-insights-banner-and-dashboard"></a>

n8n insights 只从 main（parent）workflow 的 production executions（例如 active workflows 按 schedule 或 webhook 触发的 executions）收集 data。这意味着它不会计入 manual (test) executions、sub-workflows 或 error workflows 的 executions。

### 升级到支持 insights 的 version 时，n8n 是否使用 historic execution data？ <a href="#does-n8n-use-historic-execution-data-when-upgrading-to-a-version-with-insights" id="does-n8n-use-historic-execution-data-when-upgrading-to-a-version-with-insights"></a>

n8n 只会在你更新到第一个 supported version（1.89.0）后才开始为 insights 收集 data。这意味着它只报告从那时起的 executions，你不会在 insights 中看到 prior periods 的 execution data。
