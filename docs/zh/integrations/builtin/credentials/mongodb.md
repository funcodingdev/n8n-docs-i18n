---
title: MongoDB credentials
description: >-
  MongoDB credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MongoDB 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: MongoDB credentials
originalFilePath: integrations/builtin/credentials/mongodb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mongodb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mongodb'
layout:
  description:
    visible: false
---

# MongoDB credentials <a href="#mongodb-credentials" id="mongodb-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [MongoDB](../app-nodes/n8n-nodes-base.mongodb.md)
- [MongoDB Atlas Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md)
- [MongoDB Chat Memory](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [MongoDB](https://www.mongodb.com/) server 上创建一个具备适当权限的 user account。
- 作为 Project Owner，将所有 [n8n IP addresses](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/use-n8n-cloud/configure-cloud/find-your-ip-addresses) 添加到项目 **Network Access** 中的 IP Access List Entries。详细说明请参考 [Add IP Access List entries](https://www.mongodb.com/docs/atlas/security/ip-access-list/#add-ip-access-list-entries)。

如果你要从头设置 MongoDB，请创建 cluster 和 database。有关这些步骤的更详细说明，请参考 [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection - Connection string
- Database connection - Values

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MongoDBs Atlas documentation](https://www.mongodb.com/docs/atlas/)。

## 使用 database connection - Connection string <a href="#using-database-connection-connection-string" id="using-database-connection-connection-string"></a>

要配置此 credential，你需要满足上面列出的[前提条件](#prerequisites)。然后：

1. 选择 **Connection String** 作为 **Configuration Type**。
2. 输入你的 MongoDB **Connection String**。要在 MongoDB 中获取 connection string，请前往 **Database > Connect**。
    1. 选择 **Drivers**。
    2. 复制你在 **Add your connection string into your application code** 中看到的 code。它会类似于：`mongodb+srv://yourName:yourPassword@clusterName.mongodb.net/?retryWrites=true&w=majority`。
    3. 将 connection string 中的 `<password>` 和 `<username>` 替换为你将使用的 database user credentials。
    4. 将该 connection string 输入到 n8n。
    5. 有关查找和格式化 connection string 的信息，请参考 [Connection String](https://www.mongodb.com/docs/manual/reference/connection-string/)。
3. 输入你的 **Database** name。这是 connection string 中已添加详情的 user 将登录的 database 名称。
4. 选择是否 **Use TLS**：启用后使用 TLS。你的 MongoDB database 必须已配置为使用 TLS，并且已生成 x.509 certificate。在 n8n 中添加这些 certificate 字段的信息：
    - **CA Certificate**
    - **Public Client Certificate**
    - **Private Client Key**
    - **Passphrase**

有关使用 x.509 certificates 的更多信息，请参考 [MongoDB's x.509 documentation](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements)。

## 使用 database connection - Values <a href="#using-database-connection-values" id="using-database-connection-values"></a>

要配置此 credential，你需要满足上面列出的[前提条件](#prerequisites)。然后：

1. 选择 **Values** 作为 **Configuration Type**。
2. 输入 database **Host** name 或 address。
3. 输入 **Database** name。
4. 输入你想要登录使用的 **User**。
5. 输入该 user 的 **Password**。
6. 输入用于连接的 **Port**。这是你的 server 用于侦听传入连接的 port number。
7. 选择是否 **Use TLS**：启用后使用 TLS。你的 MongoDB database 必须已配置为使用 TLS，并且已生成 x.509 certificate。在 n8n 中添加这些 certificate 字段的信息：
    - **CA Certificate**
    - **Public Client Certificate**
    - **Private Client Key**
    - **Passphrase**

有关使用 x.509 certificates 的更多信息，请参考 [MongoDB's x.509 documentation](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements)。
