---
title: Snowflake credentials
description: >-
  Snowflake credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Snowflake 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Snowflake credentials
originalFilePath: integrations/builtin/credentials/snowflake.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/snowflake'
url: 'https://docs.n8n.io/integrations/builtin/credentials/snowflake'
layout:
  description:
    visible: false
---

# Snowflake credentials <a href="#snowflake-credentials" id="snowflake-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Snowflake](../app-nodes/n8n-nodes-base.snowflake.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Snowflake](https://www.snowflake.com/en/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [Password](#using-password-authentication)
- [Key-pair](#using-key-pair-authentication)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Snowflake's API documentation](https://docs.snowflake.com/en/api-reference) 和 [SQL Command Reference](https://docs.snowflake.com/en/sql-reference-commands)。

## 通用配置字段 <a href="#common-configuration-fields" id="common-configuration-fields"></a>

两种身份验证方式都需要以下字段：

- 一个 **Account** name：你的 account name 是 Snowflake URL 中位于 `https://` 和 `snowflakecomputing.com` 之间的字符串。例如，如果你的 Snowflake account URL 是 `https://abc.eu-central-1.snowflakecomputing.com`，则 account name 是 `abc.eu-central-1`。
- 一个 **Database**：输入 credential 应连接到的 [database](https://docs.snowflake.com/en/sql-reference/sql/use-database) 名称。
- 一个 **Warehouse**：输入连接后 session 使用的默认 virtual [warehouse](https://docs.snowflake.com/en/sql-reference/sql/use-warehouse) 名称。n8n 使用此 warehouse 执行 queries、加载数据等操作。
- 一个 **Schema**：输入连接后要使用的 [schema](https://docs.snowflake.com/en/sql-reference/sql/use-schema)。
- 一个 **Role**：输入连接后要使用的 security [role](https://docs.snowflake.com/en/sql-reference/sql/use-role)。
- **Client Session Keep Alive**：默认情况下，client connections 通常会在最近一次 query execution 后三到四小时超时。打开此设置会将 `clientSessionKeepAlive` 参数设为 true：server 会无限期保持 client 的连接，即使该连接不执行任何 queries。

有关这些设置的更多信息，请参考 [Session Commands](https://docs.snowflake.com/en/sql-reference/commands-session)。

## 使用 password authentication <a href="#using-password-authentication" id="using-password-authentication"></a>

除 [通用配置字段](#common-configuration-fields) 外，password authentication 还需要：

- 一个 **Username**
- 一个 **Password**

## 使用 key-pair authentication <a href="#using-key-pair-authentication" id="using-key-pair-authentication"></a>

Key-pair authentication 是 password-based authentication 的替代方案，可提供更高安全性。此方式使用 public-private key pair 进行身份验证。

除 [通用配置字段](#common-configuration-fields) 外，key-pair authentication 还需要：

- 一个 **Username**：被分配了 public key 的 Snowflake user。
- 一个 **Private Key**：PEM format (PKCS#8) 的 private key。这应是 private key 文件的完整内容，包括 `-----BEGIN ENCRYPTED PRIVATE KEY-----` 和 `-----END ENCRYPTED PRIVATE KEY-----` delimiters（如果是未加密 key，则包括 `-----BEGIN PRIVATE KEY-----` 和 `-----END PRIVATE KEY-----`）。
- 一个 **Passphrase**（可选）：如果你的 private key 已加密，请输入用于加密它的 passphrase。如果你使用未加密的 private key，请将此字段留空。

有关生成和配置 key pairs 的更多信息，请参考 [Snowflake's key-pair authentication documentation](https://docs.snowflake.com/en/user-guide/key-pair-auth)。
