---
title: Data tables
description: 在 project 边界内为工作流管理结构化表格数据
contentType: overview
tags:
  - data tables
hide:
  - tags
nodeTitle: Data tables
originalFilePath: data/data-tables.md
originalUrl: 'https://docs.n8n.io/data/data-tables'
url: 'https://docs.n8n.io/build/work-with-data/data-tables'
layout:
  description:
    visible: false
---

# Data tables <a href="#data-tables" id="data-tables"></a>

## 概览 <a href="#overview" id="overview"></a>

Data tables 将数据存储集成到 n8n 环境中。使用 data tables，你可以直接在工作流中保存、管理并与数据交互，而无需依赖外部数据库系统，适用于以下场景：

- 在同一 project 的多个工作流之间持久化数据
- 存储标记，用于防止重复运行或控制工作流 trigger
- 在多个工作流之间复用 prompt 或消息
- 为 AI 工作流存储评估数据
- 存储 workflow execution 生成的数据
- 组合不同来源的数据，丰富数据集
- 创建 lookup table，作为工作流内的快速参考点

## 使用 data tables <a href="#working-with-data-tables" id="working-with-data-tables"></a>

你可以通过三种方式创建、筛选和管理 data tables 及其数据：使用 **Data Table node**、**DataTable API endpoint**，或 **Data tables tab**。

### Data Table node <a href="#data-table-node" id="data-table-node"></a>

在工作流中使用 data tables 存储和管理数据，让工作流运行时能够自动创建、检索、更新和删除数据。

完整文档请参阅 [Data Table node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.datatable)。

### DataTable API endpoint <a href="#datatable-api-endpoint" id="datatable-api-endpoint"></a>

使用 n8n API 中的 `/datatables` endpoint 以编程方式操作 data tables。

完整文档请参阅 [API reference](https://docs.n8n.io/api/api-reference/#tag/datatable)。

### Data table 标签 <a href="#data-table-tab" id="data-table-tab"></a>

通过可视化界面直接在 UI 中查看和操作 data tables。这样无需构建工作流，就可以浏览和编辑数据并管理表。

1. 在 n8n project 中，选择 **Data tables** 标签。
2. 点击右上角的 split button，并选择 **Create Data table**。

    ![Data table creation](../../../build/.gitbook/assets/create-data-table.png)

3. 为表输入描述性名称。

4. 选择创建表的方式：
    - **From scratch**：通过可视化界面手动定义列并添加行，创建新表。
    - **Import CSV**：上传 CSV 文件，自动创建表结构并用文件中的数据填充。

    在出现的表格视图中，你可以：

    * 重命名或删除 data table 或其列
    * 添加并重新排列列以组织数据
    * 添加、删除和更新行
    * 编辑现有数据

## 导出和导入数据 <a href="#exporting-and-importing-data" id="exporting-and-importing-data"></a>

在 **Data tables** 标签中，你可以：

- 如[上一节](#data-table-tab)所述，将 CSV 数据直接导入 data table
- 下载 data table 的 CSV。点击左上角的三点菜单并选择 **Download CSV**。

## Data tables 的注意事项和限制 <a href="#considerations-and-limitations-of-data-tables" id="considerations-and-limitations-of-data-tables"></a>

- Data tables 适合轻量到中等规模的数据存储。默认情况下，一个实例中所有 data tables 使用的总存储空间限制为 50MB。在自托管环境中，你可以使用环境变量 `N8N_DATA_TABLES_MAX_SIZE_BYTES` 增加这个默认大小限制。
- 当 data tables 接近存储限制的 80% 时，n8n 会显示警告。达到存储限制时，会出现最终警告。超过此限制会禁用向表手动添加内容，并在尝试插入或更新数据时导致 workflow execution 错误。
- 默认情况下，在 project 中创建的 data tables 可供该 project 中的所有团队成员访问。
- Admin 和 Owner 可以看到所有用户的 data tables。
- 不支持从 Code node 直接以编程方式访问 data tables。你不能通过内置方法或变量访问 data table 值。

## Data tables 与 variables 对比 <a href="#data-tables-versus-variables" id="data-tables-versus-variables"></a>

| 功能 | Data tables | Variables |
|---------|-------------|-----------|
| 统一表格视图 | ✓ | ✗ |
| 行列关系 | ✓ | ✗ |
| 跨 project 访问 | ✗ | ✓ |
| 单个值显示 | ✗ | ✓ |
| 针对短值优化 | ✗ | ✓ |
| 结构化数据 | ✓ | ✗ |
| 按 project 限定范围 | ✓ | ✗ |
| 将值用作 expression | ✗ | ✓ |
