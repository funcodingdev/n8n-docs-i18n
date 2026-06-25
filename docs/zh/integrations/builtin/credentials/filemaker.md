---
title: FileMaker credentials
description: >-
  FileMaker credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 FileMaker。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: FileMaker credentials
originalFilePath: integrations/builtin/credentials/filemaker.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/filemaker'
url: 'https://docs.n8n.io/integrations/builtin/credentials/filemaker'
layout:
  description:
    visible: false
---

# FileMaker credentials <a href="#filemaker-credentials" id="filemaker-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [FileMaker](../app-nodes/n8n-nodes-base.filemaker.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [FileMaker Server](https://www.claris.com/filemaker/) 上创建一个具有 `fmrest` extended privilege 的 user account，以[访问 FileMaker Data API](https://help.claris.com/en/data-api-guide/content/enable-access.html)。
- 确保 FileMaker Server 可以使用 [FileMaker Data API](https://help.claris.com/en/data-api-guide/content/index.html)：
    1. 使用 FileMaker Pro 为 FileMaker Data API access 准备 database。你可以创建 database 或准备已有 database。
        - 有关更多信息，请参阅 [Prepare databases for FileMaker Data API access](https://help.claris.com/en/data-api-guide/content/prepare-databases-for-access.html)。
    1. 编写调用 FileMaker Data API methods 的代码，以查找、创建、编辑、复制和删除 hosted database 中的 records。
        - 有关更多信息，请参阅 [Write FileMaker Data API calls](https://help.claris.com/en/data-api-guide/content/write-data-api-calls.html)。
    1. 在启用 FileMaker Data API access 的情况下托管你的 solution。
        - 有关更多信息，请参阅 [Host a FileMaker Data API solution](https://help.claris.com/en/data-api-guide/content/host-data-api-app.html)。
    1. 测试 FileMaker Data API access 是否正常工作。
        - 有关更多信息，请参阅 [Test the FileMaker Data API solution](https://help.claris.com/en/data-api-guide/content/test-data-api-app.html)。
    1. 使用 Admin Console 监控你的 hosted solution。
        - 有关更多信息，请参阅 [Monitor FileMaker Data API solutions](https://help.claris.com/en/data-api-guide/content/monitor-data-api-app.html)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [FileMaker Data API Guide](https://help.claris.com/en/data-api-guide/content/index.html)。

## 使用 database connection <a href="#using-database-connection" id="using-database-connection"></a>

配置此 credential：

1. 输入 FileMaker Server 的 **Host** name 或 IP address。
2. 输入 **Database** name。它应与 FileMaker 中 **Databases** 列表显示的 database name 匹配。
3. 输入具备 `fmrest` extended privilege 的账号的 user account **Login**。有关更多信息，请参阅前面的[前置条件](#prerequisites)部分。
4. 输入该 user account 的 **Password**。
