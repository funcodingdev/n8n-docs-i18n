---
contentType: howto
nodeTitle: Manage execution data
originalFilePath: hosting/scaling/execution-data.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/execution-data'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data
layout:
  description:
    visible: false
---

# Execution data <a href="#execution-data" id="execution-data"></a>

根据你的 executions 设置和数量，n8n database 可能会增长并耗尽存储空间。

为避免这种情况，n8n 建议不要保存不必要的数据，并启用旧 executions data 的 pruning。

要做到这一点，请配置对应的[环境变量](../basic-configuration/use-environment-variables/executions.md)。

## 减少保存的数据 <a href="#reduce-saved-data" id="reduce-saved-data"></a>

{% hint style="info" %}
**Workflow 级别配置**

你也可以使用 [workflow settings](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/configure-workflow-settings)，按单个 workflow 配置这些设置。
{% endhint %}

你可以选择 n8n 保存哪些 executions data。例如，你可以只保存结果为 `Error` 的 executions。

```sh
# npm <a href="#npm" id="npm"></a>
# Save executions ending in errors <a href="#save-executions-ending-in-errors" id="save-executions-ending-in-errors"></a>
export EXECUTIONS_DATA_SAVE_ON_ERROR=all

# Don't save successful executions <a href="#dont-save-successful-executions" id="dont-save-successful-executions"></a>
export EXECUTIONS_DATA_SAVE_ON_SUCCESS=none

# Don't save node progress for each execution <a href="#dont-save-node-progress-for-each-execution" id="dont-save-node-progress-for-each-execution"></a>
export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false

# Don't save manually launched executions <a href="#dont-save-manually-launched-executions" id="dont-save-manually-launched-executions"></a>
export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false

```

```sh
# Docker <a href="#docker" id="docker"></a>
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_SAVE_ON_ERROR=all \
 -e EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \
 -e EXECUTIONS_DATA_SAVE_ON_PROGRESS=true \
 -e EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \
 docker.n8n.io/n8nio/n8n
```

```yaml
# Docker Compose <a href="#docker-compose" id="docker-compose"></a>
n8n:
    environment:
      - EXECUTIONS_DATA_SAVE_ON_ERROR=all
      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=none
      - EXECUTIONS_DATA_SAVE_ON_PROGRESS=true
      - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
```

## 启用 executions pruning <a href="#enable-executions-pruning" id="enable-executions-pruning"></a>

执行数据 pruning 会按固定计划删除已完成 executions 及其 execution data 和 binary data。n8n 默认启用 pruning。出于性能原因，pruning 会先标记要删除的目标，之后再永久移除它们。

只要满足以下任一条件，n8n 就会 prune executions：

- **Age**：execution 已在 `EXECUTIONS_DATA_MAX_AGE` 小时前完成（默认：336 小时 -> 14 天）。
- **Count**：executions 总数超过 `EXECUTIONS_DATA_PRUNE_MAX_COUNT`（默认：10,000）。发生这种情况时，n8n 会从最旧到最新删除 executions。

注意：

- 状态为 `new`、`running` 或 `waiting` 的 executions 不符合 pruning 条件。
- Annotated executions（例如带有 tags 或 ratings 的 executions）永远不会被 pruned。
- Pruning 会遵守 `EXECUTIONS_DATA_HARD_DELETE_BUFFER` 小时的 safety buffer period（默认：1h），以确保用户构建或调试 workflow 时最近的数据仍可用。

```sh
# 启用 executions pruning <a href="#enable-executions-pruning" id="enable-executions-pruning"></a>
export EXECUTIONS_DATA_PRUNE=true

# How old (hours) a finished execution must be to qualify for soft-deletion <a href="#how-old-hours-a-finished-execution-must-be-to-qualify-for-soft-deletion" id="how-old-hours-a-finished-execution-must-be-to-qualify-for-soft-deletion"></a>
export EXECUTIONS_DATA_MAX_AGE=168

# Max number of finished executions to keep. May not strictly prune back down to the exact max count. Set to `0` for unlimited. <a href="#max-number-of-finished-executions-to-keep-may-not-strictly-prune-back-down-to-the-exact-max-count-set-to-0-for-unlimited" id="max-number-of-finished-executions-to-keep-may-not-strictly-prune-back-down-to-the-exact-max-count-set-to-0-for-unlimited"></a>
export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

```sh
# Docker <a href="#docker" id="docker"></a>
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_PRUNE=true \
 -e EXECUTIONS_DATA_MAX_AGE=168 \
 docker.n8n.io/n8nio/n8n
```

```yaml
# Docker Compose <a href="#docker-compose" id="docker-compose"></a>
n8n:
    environment:
      - EXECUTIONS_DATA_PRUNE=true
      - EXECUTIONS_DATA_MAX_AGE=168
      - EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

{% hint style="info" %}
**SQLite**

如果你使用默认 SQLite database 运行 n8n，任何被 pruned 的数据所占用的磁盘空间不会自动释放，而是会被后续 executions data 复用。要释放这些空间，请配置 `DB_SQLITE_VACUUM_ON_STARTUP` [环境变量](../basic-configuration/use-environment-variables/database.md#sqlite)，或手动运行 [VACUUM](https://www.sqlite.org/lang_vacuum.html) 操作。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/kct3MUrE5xSbDyeytQIX/" %}
