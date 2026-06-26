---
title: External data storage environment variables
description: >-
  用于为你的 self-hosted n8n 实例配置 external data storage 的环境变量。
contentType: reference
tags:
  - environment variables
  - external storage
  - storage
hide:
  - toc
  - tags
nodeTitle: External data storage
originalFilePath: hosting/configuration/environment-variables/external-data-storage.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/external-data-storage
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage
layout:
  description:
    visible: false
---

# External data storage 环境变量 <a href="#external-data-storage-environment-variables" id="external-data-storage-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

有关为 binary data 使用 external storage 的更多信息，请参考 [External storage](../../scaling/use-external-storage.md)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_STORAGE_S3_HOST` | String | - | S3-compatible external storage 中 n8n bucket 的 host。例如 `s3.us-east-1.amazonaws.com`。 |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME` | String | - | S3-compatible external storage 中 n8n bucket 的名称。 |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` | String | - | S3-compatible external storage 中 n8n bucket 的 region。例如 `us-east-1`。 |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY` | String | - | S3-compatible external storage 中的 access key。 |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET` | String | - | S3-compatible external storage 中的 access secret。 |
| `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` | Boolean | - | 使用自动 credential detection 对 external storage 的 S3 调用进行身份验证。这会忽略 access key 和 access secret，并使用默认的 [credential provider chain](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain)。 |

## Azure Blob Storage <a href="#azure-blob-storage" id="azure-blob-storage"></a>

{% hint style="info" %}
**Enterprise-tier feature**

你需要 [Enterprise license key](../../manage-your-license.md) 才能将 execution data 存储在 Azure Blob Storage 中。
{% endhint %}

要将 execution data 存储在 Azure Blob Storage 中，请将 `N8N_EXECUTION_DATA_STORAGE_MODE` 设为 `azure`，并配置下面的变量。`N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME` 始终为必填。

对于身份验证，请选择以下三个选项之一。n8n 会按此顺序检查：

1. **Connection string**：设置 `N8N_EXTERNAL_STORAGE_AZURE_CONNECTION_STRING`。它优先于其他选项，因此设置后 n8n 会忽略 account name、key 和 auto-detect。这是最简单的选项，也适合使用 Azurite 进行本地测试。
2. **Auto-detect**：设置 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME`，并将 `N8N_EXTERNAL_STORAGE_AZURE_AUTH_AUTO_DETECT` 设为 `true`。n8n 会通过 Azure 的 `DefaultAzureCredential` chain（managed identity、environment 或 Azure CLI）进行身份验证，因此你的 n8n 配置中不会保存 key。最适合 Azure 上的生产环境。
3. **Account name and key**：设置 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME` 和 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_KEY`。

只有在使用 custom endpoint 时才设置 `N8N_EXTERNAL_STORAGE_AZURE_ENDPOINT`，例如 Azurite 或 sovereign cloud。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_STORAGE_AZURE_CONNECTION_STRING` | String | - | Azure Blob Storage 的 connection string。设置后优先于 account name 和 key。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME` | String | - | Storage account name。与 account key 或 managed identity 一起使用。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_KEY` | String | - | Storage account key。与 account name 一起使用。 |
| `N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME` | String | - | 用于存储 execution data 的 blob container 名称。Azure Blob Storage 必填。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ENDPOINT` | String | - | Custom blob endpoint，例如用于 Azurite 或 sovereign clouds。 |
| `N8N_EXTERNAL_STORAGE_AZURE_AUTH_AUTO_DETECT` | Boolean | `false` | 通过 `DefaultAzureCredential`（managed identity、environment 或 Azure CLI）而不是 account key 进行身份验证。启用后会忽略 account key。 |
