# n8n 文档简体中文翻译计划

## 目标

将 `docs/` 下的英文 Markdown 文档分批翻译为简体中文，并在 `docs/zh/` 中保持与英文文档一致的相对路径，方便后续同步 n8n 官方上游仓库。

当前基线：

- 英文 Markdown 文件数：1402
- 已创建中文 Markdown 文件数：35
- 中文根目录：`docs/zh/`

## 路径规则

- 英文源文档保留在 `docs/`，尽量不改动，便于合并 upstream。
- 中文翻译文档放在 `docs/zh/`。
- 中文文件路径必须镜像英文文件路径。

示例：

```text
docs/get-started/learning-paths.md
docs/zh/get-started/learning-paths.md
```

## 翻译规则

- 保留 Markdown 结构、front matter 字段、相对链接、代码块、命令、环境变量、文件路径和 API 字段。
- 页面标题、正文、列表、表格说明翻译为简体中文。
- n8n、workflow、node、credential、execution 等核心产品词第一次出现时可保留英文或采用中英混排，避免误译产品概念。
- 外部链接不改目标地址；指向英文站内文档的相对链接保持同路径，依赖 `docs/zh/` 镜像结构逐步补齐。
- 每批翻译后运行轻量检查：
  - `git diff --check`
  - 检查新增中文文件是否位于 `docs/zh/`
  - 抽查关键页面的语言切换路径

## 批次顺序

1. `get-started/`：新用户入口、学习路径、核心概念。
2. `build/`：工作流构建、数据处理、AI 集成、流程逻辑。
3. `integrations/`：内置节点、凭据、触发器、社区节点。
4. `deploy/`：自托管、Cloud、环境变量、部署方式。
5. `administer/`：用户、凭据、安全、日志、源代码控制。
6. `connect/`：API、MCP、节点开发。
7. `privacy-and-security/`、`release-notes/`、`contribute/`：政策、版本说明、贡献指南。
8. 其余散落页面和补漏文件。

## 进度表

| 批次 | 范围 | 状态 | 备注 |
| --- | --- | --- | --- |
| 0 | i18n 基础结构 | 已完成 | 已添加顶部语言切换和 `docs/zh/index.md` |
| 1.1 | `get-started/README.md`、`SUMMARY.md`、`learning-paths.md` | 已完成 | 第一批入口页 |
| 1.2 | `get-started/choose-how-to-use-n8n.md` | 已完成 | 选择使用方式 |
| 1.3 | `get-started/build-your-first-workflow.md` | 已完成 | 首个工作流教程 |
| 1.4 | `get-started/key-concept-glossary.md` | 已完成 | 关键概念术语表 |
| 2.1 | `build/README.md`、`SUMMARY.md`、`keyboard-shortcuts.md` | 已完成 | Build 顶层入口 |
| 2.2 | `build/flow-logic/` | 已完成 | 流程逻辑 |
| 2.3.1 | `build/manage-workflows/` | 已完成 | 工作流管理 |
| 2.3.2 | `build/understand-workflows/` 顶层 | 已完成 | 工作流概念、创建、credential、保存发布 |
| 2.3.3 | `build/understand-workflows/workflow-components/` | 已完成 | 工作流组件 |
| 2.3.4 | `build/understand-workflows/understand-executions/`、`ways-of-building-workflows/` | 未开始 | 执行概念和构建方式 |
| 2.4 | `build/work-with-data/` | 未开始 | 数据处理，文件较多需继续拆分 |
| 2.5 | `build/code-in-n8n/` | 未开始 | Code node 和代码辅助 |
| 2.6 | `build/integrate-ai/` | 未开始 | AI 集成，文件较多需继续拆分 |
| 3 | `integrations/` | 未开始 | 文件最多，需按节点类型拆分 |
| 4 | `deploy/` | 未开始 | 部署与配置 |
| 5 | `administer/` | 未开始 | 管理与运维 |
| 6 | `connect/` | 未开始 | API、MCP、节点开发 |
| 7 | `privacy-and-security/`、`release-notes/`、`contribute/` | 未开始 | 政策、版本和贡献 |

## 每批完成标准

- 本批英文文件都有对应的 `docs/zh/` 中文镜像文件。
- 中文文件保留原始 front matter 中机器可读字段。
- 本批页面的标题和正文已翻译，不留下大段未处理英文正文。
- 运行 `git diff --check` 无错误。
