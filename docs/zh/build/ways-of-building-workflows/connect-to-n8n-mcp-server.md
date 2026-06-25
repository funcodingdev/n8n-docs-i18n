---
title: 设置并使用 n8n MCP server
status: beta
nodeTitle: Connect to n8n MCP server
originalFilePath: advanced-ai/mcp/accessing-n8n-mcp-server.md
originalUrl: https://docs.n8n.io/advanced-ai/mcp/accessing-n8n-mcp-server
url: https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server
description: >-
  连接、认证并集成 MCP client，以编程方式构建和执行 n8n 工作流
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

# 连接到 n8n MCP server

通过 n8n 内置 MCP server，将受支持的 MCP client 连接到你的 n8n 工作流。

该 server 允许 Lovable 或 Claude Desktop 等 client 安全连接到 n8n 实例。连接后，这些 client 可以：

* 搜索你的工作流
* 与标记为可在 MCP 中使用的工作流交互
* 触发和测试已暴露的工作流
* 创建和编辑工作流及数据表

## Instance-level MCP access 与 MCP Server Trigger node 的区别 <a href="#difference-between-instance-level-mcp-access-and-mcp-server-trigger-node" id="difference-between-instance-level-mcp-access-and-mcp-server-trigger-node"></a>

Instance-level MCP access 允许你为每个 n8n 实例创建一个连接，使用集中式认证，并选择要启用访问的工作流。已启用的工作流易于查找和运行，无需为每个工作流额外设置。

相比之下，MCP Server Trigger node 是在单个工作流内部配置的。此 node 只暴露该工作流中的 tool。当你希望在一个工作流内精确定制某种 MCP server 行为时，这种方式很有用。

### 使用 instance-level MCP access 时的关键注意事项 <a href="#key-considerations-when-using-instance-level-mcp-access" id="key-considerations-when-using-instance-level-mcp-access"></a>

* MCP 支持两类工作流交互：使用 workflow execution tools 运行现有工作流，以及构建或编辑工作流（v2.13 起）。
* 它不会把实例中的所有工作流整体暴露出去。你必须先在实例级别启用 MCP，然后逐个启用工作流。唯一例外是 `search_workflows` tool，它可以访问当前用户有权访问的所有工作流，但只能展示预览，不能展示完整工作流数据。
* 它不是按每个 MCP client 单独限定范围。你连接的所有 client（例如 Claude Desktop 和 ChatGPT）都能看到你已启用 MCP 访问的所有工作流。你不能把特定工作流限制给特定 client。在用户级别，可见性仍然按用户权限限定：用户只能看到自己有权访问且已启用 MCP 的工作流。
* 大多数 MCP tool 可用于未发布的工作流。例外是 `execute_workflow`，它默认使用 production 模式并运行工作流的已发布版本。它也支持 `manual` execution 模式，用于运行当前（未发布）版本。

## 启用 MCP access <a href="#enabling-mcp-access" id="enabling-mcp-access"></a>

### Cloud 和自托管实例 <a href="#for-cloud-and-self-hosted-instances" id="for-cloud-and-self-hosted-instances"></a>

1. 前往 **Settings > Instance-level MCP**
2.  打开 **Enable MCP access**（需要实例 owner 或管理员权限）。

    ![enable-mcp-access.png](<../../../build/.gitbook/assets/enable-mcp-access (1).png>)

启用后，你会看到：

1. 暴露给 MCP client 的工作流列表
2. 已连接 OAuth client 的列表
3. 用于启用/禁用 instance-level access 的主 MCP 开关
4.  _Connection details_ 按钮，用于显示连接 MCP client 的详细说明

    ![mcp\_page\_content.png](<../../../build/.gitbook/assets/mcp_page_content (1).png>)

**如需禁用：** 关闭主 MCP 开关。

{% hint style="info" %}
**环境变量（仅自托管）**

在自托管实例上，你也可以使用环境变量管理 MCP 设置。参阅[使用环境变量管理实例设置](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/manage-settings-using-environment-variables#mcp)。
{% endhint %}

### 自托管：完全禁用 <a href="#for-self-hosted-complete-disablement" id="for-self-hosted-complete-disablement"></a>

如需完全移除此功能，设置环境变量：

`N8N_DISABLED_MODULES=mcp`

此操作会移除 MCP endpoint，并隐藏所有相关 UI 元素。

## 设置 MCP authentication <a href="#setting-up-mcp-authentication" id="setting-up-mcp-authentication"></a>

**Connection details** 弹出菜单为 MCP client 提供两种认证选项：

* **OAuth2**
*   **Access Token**

    ![mcp\_connect\_menu.png](<../../../build/.gitbook/assets/mcp_connect_menu (1).png>)

### 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

从 **OAuth** 标签复制实例 server URL，并用它配置 MCP client。连接后，client 会将你重定向到 n8n 以授权访问。

#### 撤销 client access <a href="#revoking-client-access" id="revoking-client-access"></a>

如需撤销已连接 MCP client 的访问权限：

1. 前往 **Settings > Instance-level MCP**。
2. 切换到 **Connected clients** 标签。你应该会看到已连接 OAuth client 的表格。
3.  使用每个 client 行中的操作菜单，撤销特定 client 的访问权限。

    ![mcp\_revoke\_client\_access.png](<../../../build/.gitbook/assets/mcp_revoke_client_access (1).png>)

### 使用 Access Token <a href="#using-access-token" id="using-access-token"></a>

使用 _Connection details_ 菜单中 **Access Token** 标签下的实例 server URL 和你的个人 MCP Access Token。

首次访问 **MCP Access page** 时，n8n 会自动生成一个绑定到你用户账号的个人 MCP Access Token。

{% hint style="info" %}
请立即复制 token。之后再次访问时，你只会看到遮盖后的值，复制按钮也会被禁用。
{% endhint %}

#### 轮换 token <a href="#rotating-your-token" id="rotating-your-token"></a>

如果你丢失 token 或需要轮换 token：

1. 前往 **Settings > Instance-level MCP**。
2. 点击右上角按钮，打开 _Connection details_ 菜单。
3. 切换到 **Access Token** 标签。
4.  使用遮盖后的 token 值旁边的按钮生成新 token。

    生成新 token 时，n8n 会撤销先前的 token。
5.  使用新值更新所有已连接的 MCP client。

    ![mcp\_rotate\_token.png](<../../../build/.gitbook/assets/mcp_rotate_token (1).png>)

## 向 MCP client 暴露工作流 <a href="#exposing-workflows-to-mcp-clients" id="exposing-workflows-to-mcp-clients"></a>

MCP client 可以使用 `search_workflows` 发现当前用户有权访问的所有工作流预览。但是，除非你显式为该工作流启用 MCP access，否则 client 不能访问完整工作流数据，也不能执行或修改工作流。

### 为单个工作流启用 access <a href="#enabling-access-for-individual-workflows" id="enabling-access-for-individual-workflows"></a>

#### 选项 1：从 MCP 设置页面启用（n8n v2.2.0 起可用） <a href="#option-1-from-mcp-settings-page-available-from-n8n-v220" id="option-1-from-mcp-settings-page-available-from-n8n-v220"></a>

1. 点击 **Enable workflows** 按钮（位于 workflows 表头或表格空状态中）
2. 搜索目标工作流（按名称或描述），并从列表中选择
3. 点击 **Enable** 按钮确认

#### 选项 2：从工作流编辑器启用 <a href="#option-2-from-the-workflow-editor" id="option-2-from-the-workflow-editor"></a>

1. 打开工作流。
2. 点击右上角的工作流主菜单（`...`）。
3. 选择 **Settings**。
4. 打开 **Available in MCP**。

#### 选项 3：从工作流列表启用 <a href="#option-3-from-the-workflows-list" id="option-3-from-the-workflows-list"></a>

1. 前往 **Workflows**。
2. 打开工作流卡片上的菜单。
3. 选择 **Enable MCP access**。

### 为 project/folder 启用 access <a href="#enabling-access-for-projectsfolders" id="enabling-access-for-projectsfolders"></a>

{% hint style="info" %}
**n8n v2.24.0 起可用**
{% endhint %}

你可以使用工作流列表中的 **Options** 菜单 <img src="../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options menu" data-size="line">，切换当前 project 或 folder 中所有工作流的 MCP access：

1. 前往目标 project，并从顶部菜单选择 **Workflows**，如有需要再打开子文件夹。
2. 选择 project 或 folder 名称旁边的 **Options** 菜单 <img src="../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options icon" data-size="line">。
3. 选择 **Manage MCP access**，然后选择 **Enable MCP** 或 **Disable MCP**。

![mcp\_bulk\_toggle.png](<../../../build/.gitbook/assets/mcp_bulk_toggle (1).png>)

{% hint style="info" %}
**注意**

这会切换选中 project 或 folder 中**当前**所有工作流的 MCP access（跳过已经处于目标状态的工作流）。对于未来新增的工作流，你仍然需要单独切换 access。
{% endhint %}

### 管理 access <a href="#managing-access" id="managing-access"></a>

**Instance-level MCP** 设置页面会显示所有已允许 MCP client 访问和操作的工作流。你可以在此列表中：

* 直接打开工作流、其所属 project 或父 folder
* 使用操作菜单撤销 access（或从工作流卡片菜单使用 **Disable MCP access**）
* 使用操作菜单更新工作流描述（或使用工作流编辑器中的菜单）
* 使用 **Enable workflows** 按钮为更多工作流启用 access（n8n v2.2.0 起可用）

### 工作流描述 <a href="#workflow-descriptions" id="workflow-descriptions"></a>

为帮助 MCP client 识别工作流，你可以按以下方式添加自由文本描述：

1. 选项 1：从 **Instance-level MCP** 页面
   1. 前往 **Settings > Instance-level MCP**。
   2. 确保当前位于 **Workflows** 标签。
   3. 使用目标工作流所在行的操作菜单，并选择 **Edit description** 操作。
   4. 也可以直接点击描述文本打开编辑对话框。
2.  选项 2：从工作流编辑器

    1. 打开工作流。
    2. 点击右上角的工作流主菜单（`...`）。
    3. 选择 **Edit description**。

    ![mcp\_workflow\_description.png](<../../../build/.gitbook/assets/mcp_workflow_description (1).png>)

## Tools 和资源 <a href="#tools-and-resources" id="tools-and-resources"></a>

{% hint style="info" %}
建议使用 coding agent（例如 Claude Code 或 Google ADK agent）作为 MCP client，而不是聊天 client。Coding agent 针对生成和验证 TypeScript 代码做了优化，非常适合以编程方式构建工作流。
{% endhint %}

n8n MCP server 会暴露用于工作流管理、工作流构建和数据表的 tools。可用 tools 及其参数的完整列表，请参阅 [MCP server tools reference](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/connect-to-n8n-mcp-server/mcp-server-tools-reference)。

## 示例 <a href="#examples" id="examples"></a>

#### 将 Lovable 连接到 n8n MCP server <a href="#connecting-lovable-to-n8n-mcp-server" id="connecting-lovable-to-n8n-mcp-server"></a>

1. 在 Lovable 中配置 MCP Server（OAuth）。
   * 前往你的 workspace **Settings > Integrations**。
   * 在 **MCP Servers** 部分，找到 **n8n** 并点击 **Connect**。
   * 输入你的 n8n server URL（显示在 **MCP Access** 页面）。
   * 保存连接。如果成功，n8n 会将你重定向以授权 Lovable。
2. 验证连接。
   * 连接后，Lovable 可以查询已启用 MCP access 的工作流。
   * **示例：** 请求 Lovable 构建一个列出用户并允许删除用户的工作流 UI。

#### 将 Claude Desktop 连接到 n8n MCP server <a href="#connecting-claude-desktop-to-n8n-mcp-server" id="connecting-claude-desktop-to-n8n-mcp-server"></a>

**使用 OAuth2**

1. 在 Claude Desktop 中前往 **Settings** > **Connectors**。
2. 点击 **Add custom connector**。
3. 输入以下详情：
   * **Name:** n8n MCP
   * **Remote MCP Server URL**：你的 n8n base URL（显示在 **Instance-level MCP** 页面）
4. 保存 connector。
5. 出现提示时，授权 Claude Desktop 访问你的 n8n 实例。

**使用 Access Token**

将以下条目添加到 `claude_desktop_config.json` 文件：

```json
"mcpServers": {
  "n8n-mcp": {
    "type": "http",
    "url": "https://<your-n8n-domain>/mcp-server/http",
    "headers": {
      "Authorization": "Bearer <YOUR_N8N_MCP_TOKEN>"
    }
  }
}
```

在这里，替换：

* `<your-n8n-domain>`：你的 n8n base URL（显示在 **Instance-level MCP** 页面）

#### 将 Claude Code 连接到 n8n MCP server <a href="#connecting-claude-code-to-n8n-mcp-server" id="connecting-claude-code-to-n8n-mcp-server"></a>

**选项 1：使用 OAuth2 认证（推荐）**

使用以下 CLI 命令：

```bash
claude mcp add --transport http n8n-mcp https://<your-n8n-domain>/mcp-server/http
```

或者，将以下条目添加到 `claude.json` 文件：

```json
{
    "mcpServers": {
        "n8n-mcp": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http"
        }
    }
}
```

在这里，替换：

* `<your-n8n-domain>`：你的 n8n base URL（显示在 **Instance-level MCP** 页面）

**选项 2：使用 Access Token 认证**

使用以下 CLI 命令：

```bash
claude mcp add --transport http n8n-mcp https://<your-n8n-domain>/mcp-server/http \
  --header "Authorization: Bearer <YOUR_N8N_MCP_TOKEN>"
```

或者，将以下条目添加到 `claude.json` 文件：

```json
{
    "mcpServers": {
        "n8n-mcp": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http",
            "headers": {
                "Authorization": "Bearer <YOUR_N8N_MCP_TOKEN>"
            }
        }
    }
}
```

在这里，替换：

* `<your-n8n-domain>`：你的 n8n base URL（显示在 **Instance-level MCP** 页面）
* `<YOUR_N8N_MCP_TOKEN>`：你生成的 token

### 将 Codex CLI 连接到 n8n MCP server <a href="#connecting-codex-cli-to-n8n-mcp-server" id="connecting-codex-cli-to-n8n-mcp-server"></a>

**选项 1：使用 OAuth2 认证（推荐）**

使用以下 CLI 命令：

```bash
codex mcp add n8n-mcp --url https://<your-n8n-domain>/mcp-server/http
```

或者，将以下条目添加到 `~/.codex/config.toml` 文件：

```toml
[mcp_servers.n8n-mcp]
url = "http://localhost:5678/mcp-server/http"
```

在这里，替换：

* `<your-n8n-domain>`：你的 n8n base URL（显示在 **Instance-level MCP** 页面）

**选项 2：使用 Access Token 认证**

将以下条目添加到 `~/.codex/config.toml` 文件：

```toml
[mcp_servers.n8n-mcp]
url = "https://<your-n8n-domain>/mcp-server/http"
http_headers = { "authorization" = "Bearer <YOUR_N8N_MCP_TOKEN>" }
```

在这里，替换：

* `<your-n8n-domain>`：你的 n8n base URL（显示在 **Instance-level MCP** 页面）
* `<YOUR_N8N_MCP_TOKEN>`：你生成的 token

### 将 Google ADK agent 连接到 n8n MCP server <a href="#connecting-google-adk-agent-to-n8n-mcp-server" id="connecting-google-adk-agent-to-n8n-mcp-server"></a>

以下示例代码会创建一个连接到远程 n8n MCP server 的 agent：

```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

N8N_INSTANCE_URL = "https://localhost:5678"
N8N_MCP_TOKEN = "YOUR_N8N_MCP_TOKEN"

root_agent = Agent(
    model="gemini-2.5-pro",
    name="n8n_agent",
    instruction="Help users manage and execute workflows in n8n",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"{N8N_INSTANCE_URL}/mcp-server/http",
                headers={
                    "Authorization": f"Bearer {N8N_MCP_TOKEN}",
                },
            ),
        )
    ],
)
```

更多详情，请参阅 [Connect ADK agent to n8n](https://google.github.io/adk-docs/tools/third-party/n8n/)。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

如果在将 MCP client 连接到 n8n 实例时遇到问题，请检查以下事项：

* 如果使用基于云的 MCP client，确保你的 n8n 实例可公开访问。
* 确认已在 n8n 设置中启用 MCP access。
* 检查你要执行或修改的工作流是否标记为 **Available in MCP**。
* 确认 MCP client 中已正确配置认证方式（OAuth2 或 Access Token）。
* 查看 n8n server 日志，检查与 MCP 连接相关的错误消息。
