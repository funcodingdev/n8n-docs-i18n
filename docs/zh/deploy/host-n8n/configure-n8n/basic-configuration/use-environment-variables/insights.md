---
title: Insights environment variables
description: >-
  使用环境变量为你的 self-hosted n8n 实例配置 insights metrics collection。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Insights
originalFilePath: hosting/configuration/environment-variables/insights.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/insights'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights
layout:
  description:
    visible: false
---

# Insights 环境变量 <a href="#insights-environment-variables" id="insights-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

Insights 让实例 owner 和 admin 能看到 workflows 随时间变化的性能表现。详情请参考 [Insights](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/track-usage-with-insights)。

{% hint style="warning" %}
**存储和压缩阈值**

`N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` 和 `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` 设置 n8n 在每个 compaction 步骤前保留高分辨率 insights 的天数（metrics 存储在一小时 buckets 中），也就是从 hour bucket 压缩到 day bucket，再从 day bucket 压缩到 week bucket。你可以在实例上配置这些天数。

提高这些值会延迟 compaction。这会给 `insights_by_period` 增加更多 rows，并提高数据库用量。关于它与 retention 的关系，请参阅 [Insights](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/track-usage-with-insights#disable-or-configure-insights-metrics-collection)。
{% endhint %}

如果在 compaction 期间遇到数据库负载问题，请调整 compaction 运行频率以及 n8n 每次运行处理的工作量：

- 减小 `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES`，让 compaction 更频繁运行。这可以减少两次运行之间堆积的数据量。
- 增大 `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS`，让 batches 之间等待更久。
- 减小 `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN`，让每次运行处理更少 batches。
- 减小 `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS`，让每次运行更早停止。

这些设置只控制 compaction workload 和调度。它们不会改变 retention，也不会改变每个 compaction 步骤的 age thresholds。

 | Variable                                                 | Type   | Default | Description                                                                             |
 |:---------------------------------------------------------|:-------|:--------|:----------------------------------------------------------------------------------------|
 | `N8N_DISABLED_MODULES`                                   | String | -       | 设为 `insights` 可为实例禁用该功能和 metrics collection。        |
 | `N8N_INSIGHTS_COMPACTION_BATCH_SIZE`                     | Number | 500     | 单个 batch 中要 compact 的 raw insights data 数量。                           |
 | `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS`       | Number | 100     | 完整 compaction batches 之间的延迟，单位为毫秒。增大此值可在 batches 之间等待更久。设为 `0` 可跳过延迟。 |
 | `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | Number | 180     | n8n 将 daily insights rows compact 到 weekly 前的 age，单位为天。 |
 | `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | Number | 90      | n8n 将 hourly insights rows compact 到 daily 前的 age，单位为天。 |
 | `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES`               | Number | 60      | compaction 应运行的间隔，单位为分钟。减小此值可让 compaction 更频繁运行，并减少两次运行之间堆积的数据量。 |
 | `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN`            | Number | 1000    | 单次运行中要处理的最大 compaction batches 数量。减小此值可让每次运行处理更少 batches。设为 `0` 可禁用此限制。 |
 | `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS`            | Number | 300     | 单次 compaction 运行的最长运行时间，单位为秒。减小此值可让每次运行更早停止。设为 `0` 可禁用此限制。 |
 | `N8N_INSIGHTS_FLUSH_BATCH_SIZE`                          | Number | 1000    | flush 前 buffer 中保留的 insights data 最大数量。              |
 | `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS`                    | Number | 30      | n8n 将 insights data flush 到数据库的间隔，单位为秒。 |
 | `N8N_INSIGHTS_MAX_AGE_DAYS`                              | Number | 365     | n8n 在 pruning 前保留 compacted insights data 的天数。最大值为 730（两年）。 |
 | `N8N_INSIGHTS_PRUNE_CHECK_INTERVAL_HOURS`                | Number | 24      | 实例检查是否有超过有效 max age 的 insights data 并删除它的频率，单位为小时。 |
