---
description: n8n 实例的 binary data external storage。
contentType: howto
tags:
  - external storage
  - storage
hide:
  - tags
search:
  boost: 1.5
nodeTitle: Use external storage
originalFilePath: hosting/scaling/external-storage.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/external-storage'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage'
layout:
  description:
    visible: false
---

# External storage <a href="#external-storage" id="external-storage"></a>

{% hint style="info" %}
**功能可用性**

* Self-hosted Enterprise plans 可用
* 如果你想在 Cloud Enterprise 上访问此功能，请[联系 n8n](https://n8n-community.typeform.com/to/y9X2YuGa)。
{% endhint %}

n8n 可以将 workflow executions 产生的 binary data 存储到外部位置。此功能有助于避免依赖 filesystem 存储大量 binary data。

n8n 将来会为其他数据类型引入 external storage。

## 将 n8n 的 binary data 存储在 S3 中 <a href="#storing-n8ns-binary-data-in-s3" id="storing-n8ns-binary-data-in-s3"></a>

n8n 支持将 [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) 作为 workflow executions 产生的 binary data 的 external store。你可以使用 Cloudflare R2 和 Backblaze B2 等其他 S3-compatible services，但 n8n 不正式支持这些服务。

{% hint style="info" %}
**Enterprise-tier feature**

External storage 需要 [Enterprise license key](../manage-your-license.md)。如果 license key 过期且你仍处于 S3 mode，实例可以从 S3 bucket 读取，但无法写入。
{% endhint %}

### 设置 <a href="#setup" id="setup"></a>

按照 [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) 创建并配置 bucket。你可以使用以下 policy，将 `<bucket-name>` 替换为你创建的 bucket 名称：

```json
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "VisualEditor0",
   "Effect": "Allow",
   "Action": ["s3:*"],
   "Resource": ["arn:aws:s3:::<bucket-name>", "arn:aws:s3:::<bucket-name>/*"]
  }
 ]
}
```

设置 bucket-level lifecycle configuration，让 S3 自动删除旧 binary data。n8n 会将 binary data pruning 委托给 S3，因此除非你想永久保留 binary data，否则必须设置 lifecycle configuration。

创建 bucket 后，你会得到 host、bucket name 和 region，以及 access key ID 和 secret access key。你需要在 n8n 环境中设置它们：

```sh
export N8N_EXTERNAL_STORAGE_S3_HOST=... # example: s3.us-east-1.amazonaws.com
export N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME=...
export N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET=...
```

{% hint style="info" %}
**没有 region**

如果你的 provider 不要求 region，可以将 `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` 设为 `'auto'`。
{% endhint %}

## 验证并更新 S3 bucket region 格式（v2.6.4 起） <a href="#validate-and-update-your-s3-bucket-region-format-v264-onward" id="validate-and-update-your-s3-bucket-region-format-v264-onward"></a>

从 n8n v2.6.4 开始，环境变量 `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` 的值必须满足以下条件：

- 只包含字母数字字符（`a-z`、`A-Z`、`0-9`）和连字符（`-`）。
- 不包含下划线（`_`）或其他特殊字符。

如果不满足这些条件，即使 storage endpoint 可达且在旧版本中曾正常工作，n8n 也会因 connection errors 而启动失败。

如果升级到 n8n v2.6.4 后 S3 connection 失败，请验证你的 region 值是否符合这些条件，并重新部署 n8n。

告诉 n8n 将 binary data 存储在 S3 中：

```sh
export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3
export N8N_DEFAULT_BINARY_DATA_MODE=s3
```

{% hint style="info" %}
**Auth autodetection**

要自动检测用于认证 S3 calls 的 credentials，请将 `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` 设为 `true`。这会使用默认 [credential provider chain](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain)。
{% endhint %}

重启 server 以加载新配置。

### 使用方式 <a href="#usage" id="usage"></a>

启用 S3 后，n8n 会将任何新的 binary data 写入 S3 bucket，并从中读取。n8n 会按以下格式将 binary data 写入你的 S3 bucket：

```
workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}
```

如果 `filesystem` 仍作为选项列在 `N8N_AVAILABLE_BINARY_DATA_MODES` 中，n8n 会继续从 filesystem 读取存储在 filesystem 中的旧 binary data。

如果你将 binary data 存储在 S3 中，之后切换到 filesystem mode，只要 `s3` 仍列在 `N8N_AVAILABLE_BINARY_DATA_MODES` 中且你的 S3 credentials 仍然有效，实例就会继续读取存储在 S3 中的任何数据。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/kct3MUrE5xSbDyeytQIX/" %}

### S3 storage 升级最佳实践 <a href="#upgrade-best-practices-for-s3-storage" id="upgrade-best-practices-for-s3-storage"></a>

使用 S3 或 S3-compatible storage 时：

1. 同时将所有 n8n components（main、worker、runner）升级到相同版本，以避免 protocol incompatibilities。
2. 对于通过 HTTP 使用的 on-premise 或 S3-compatible storage，请设置 `N8N_EXTERNAL_STORAGE_S3_PROTOCOL=http`，并在 host configuration 中包含 protocol。
3. 只使用受支持的环境变量名：access key 使用 `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY`。

较新的 n8n 版本有更严格的 validation 和 protocol handling。较旧配置在升级后可能需要更新。
