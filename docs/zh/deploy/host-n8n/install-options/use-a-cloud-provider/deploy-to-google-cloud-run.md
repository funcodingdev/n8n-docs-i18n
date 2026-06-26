---
contentType: tutorial
nodeTitle: Deploy to Google Cloud Run
originalFilePath: hosting/installation/server-setups/google-cloud-run.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run
layout:
  description:
    visible: false
---

# 在 Google Cloud Run 上托管 n8n <a href="#hosting-n8n-on-google-cloud-run" id="hosting-n8n-on-google-cloud-run"></a>

本托管指南展示如何在 Google Cloud Run 这个 serverless container runtime 上自托管 n8n。如果你刚开始使用 n8n，并且不需要 production-grade deployment，可以选择下面的 "easy mode" 部署选项。否则，如果你打算大规模使用此 n8n 部署，请参阅后面的 "durable mode" 说明。

你也可以通过 OAuth 启用对 Google Workspace（例如 Gmail 和 Drive）的访问，以便将这些服务用作 n8n workflow tools。本文档末尾提供了授予 n8n 访问这些服务权限的说明。

如果你想改为部署到 Google Kubernetes Engine (GKE)，可以参阅[这些说明](deploy-to-google-kubernetes.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 开始前：获取 Google Cloud project <a href="#before-you-begin-get-a-google-cloud-project" id="before-you-begin-get-a-google-cloud-project"></a>

如果你还没有创建 Google Cloud project，请[先完成此操作](https://developers.google.com/workspace/guides/create-project)（并确保该 project 已启用 billing；即使你的 Cloud Run service 免费运行，也必须激活 billing 才能部署）。否则，请导航到你想部署 n8n 的 project。

## Easy mode <a href="#easy-mode" id="easy-mode"></a>

这是在 Cloud Run 上部署 n8n 的最快方式。对于此部署，n8n 的数据位于 in-memory 中，因此只建议用于 demo。**只要此 Cloud Run service scale to zero 或重新部署，n8n data 就会丢失。** 如果你需要 production-grade deployment，请参阅下面的 durable mode 说明。

如果你还没有创建 Google Cloud project，请[先完成此操作](https://developers.google.com/workspace/guides/create-project)（并确保该 project 已启用 billing；即使你的 Cloud Run service 将免费运行，也必须启用 billing 才能部署）。否则，请导航到你想部署 n8n 的 project。

打开 Cloud Shell Terminal（在 Google Cloud console 中，输入 "G" 然后输入 "S"，或点击右上角的 terminal 图标）。

Session 打开后，你可能需要先运行此命令登录（并按提示完成步骤）：

```sh
gcloud auth login
```

你也可以显式启用 Cloud Run API（即使你不这样做，部署时也会询问是否启用）：

```sh
gcloud services enable run.googleapis.com
```

{% hint style="warning" %}
**必需：自定义 health check endpoint**

Google Cloud Run 保留 `/healthz` 用于自己的 health checks。由于 n8n 默认使用此 path，它可能发生冲突并在 workflow canvas 中导致连接问题。要修复此问题，请将 `N8N_ENDPOINT_HEALTH` 环境变量设置为自定义 path（已包含在下面的部署命令中）。
{% endhint %}

部署 n8n：

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n \
    --region=us-west1 \
    --allow-unauthenticated \
    --port=5678 \
    --no-cpu-throttling \
    --memory=2Gi \
    --set-env-vars="N8N_ENDPOINT_HEALTH=health"
```

（你可以指定自己偏好的任何 region，而不是 "us-west1"）

部署完成后，打开另一个 tab 并导航到 Service URL。n8n 可能仍在加载，你会看到 "n8n is starting up. Please wait" 消息，但稍后应该会看到 n8n login screen。

可选：如果你想尽可能保持此 n8n service 运行以避免数据丢失，也可以将 manual scale 设置为 1，防止它 autoscale to 0。

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n \
    --region=us-west1 \
    --allow-unauthenticated \
    --port=5678 \
    --no-cpu-throttling \
    --memory=2Gi \
    --scaling=1 \
    --set-env-vars="N8N_ENDPOINT_HEALTH=health"
```

这并不能完全防止数据丢失，例如 Cloud Run service 被重新部署或更新时仍会丢失。如果你想要真正持久化的数据，应参阅下面关于如何附加 database 的说明。

## Durable mode <a href="#durable-mode" id="durable-mode"></a>

以下说明适用于在 Cloud Run 上更持久、production-grade 的 n8n 部署。它包含 database 和用于敏感数据的 secret manager 等 resources。

如果你想通过 Terraform 部署以下设置，请参阅此 [example](https://github.com/ryanpei/n8n-hosting/tree/main/google-cloud-run)，它部署的设置与下文相同（不包含 Google Workspace tools 的 OAuth 设置）。

## 启用 APIs 并设置 env vars <a href="#enable-apis-and-set-env-vars" id="enable-apis-and-set-env-vars"></a>

打开 Cloud Shell Terminal（在 Google Cloud console 中，输入 "G" 然后输入 "S"，或点击右上角的 terminal 图标），并在 terminal session 中运行这些命令：

```sh
## You may need to login first <a href="#you-may-need-to-login-first" id="you-may-need-to-login-first"></a>
gcloud auth login

gcloud services enable run.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

你还需要为后续说明设置一些环境变量：

```sh
export PROJECT_ID=your-project
export REGION=region-where-you-want-this-deployed
```

## 设置 Postgres database <a href="#setup-your-postgres-database" id="setup-your-postgres-database"></a>

运行此命令创建 Postgres DB instance（完成需要几分钟；同时请确保将 root-password 字段更新为你想要的密码）：

```sh
gcloud sql instances create n8n-db \
    --database-version=POSTGRES_13 \
    --tier=db-f1-micro \
    --region=$REGION \
    --root-password="change-this-password" \
    --storage-size=10GB \
    --availability-type=ZONAL \
    --no-backup \
    --storage-type=HDD
```

完成后，你可以添加 n8n 将使用的 database：

```sh
gcloud sql databases create n8n --instance=n8n-db
```

为 n8n 创建 DB user（当然，请更改 password 值）：

```sh
gcloud sql users create n8n-user \
    --instance=n8n-db \
    --password="change-this-password"
```

你可以将为此 n8n-user 设置的 password 保存到文件中，用于下一步在 Secret Manager 中保存 password。请务必稍后删除此文件。

## 将敏感数据存储在 Secret Manager 中 <a href="#store-sensitive-data-in-secret-manager" id="store-sensitive-data-in-secret-manager"></a>

虽然不是必需，但强烈建议将敏感数据存储在 Secrets Manager 中。

为 database password 创建 secret（将 "/your/password/file" 替换为你上面为 n8n-user password 创建的文件）：

```sh
gcloud secrets create n8n-db-password \
    --data-file=/your/password/file \
    --replication-policy="automatic"
```

创建 encryption key（你可以使用自己的 key，此示例会生成一个随机 key）：

```sh
openssl rand -base64 -out my-encryption-key 42
```

为此 encryption key 创建 secret（如果你提供自己的 key，请替换 "my-encryption-key"）：

```sh
gcloud secrets create n8n-encryption-key \
    --data-file=my-encryption-key \
    --replication-policy="automatic"
```

现在你可以删除创建的 my-encryption-key 和 database password 文件。这些值现在已安全存储在 Secret Manager 中。

## 为 Cloud Run 创建 service account <a href="#create-a-service-account-for-cloud-run" id="create-a-service-account-for-cloud-run"></a>

你希望此 Cloud Run service 仅限访问它所需的 resources。以下命令会创建 service account，并添加访问 secrets 和 database 所需的权限：

```sh
gcloud iam service-accounts create n8n-service-account \
    --display-name="n8n Service Account"

gcloud secrets add-iam-policy-binding n8n-db-password \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"

gcloud secrets add-iam-policy-binding n8n-encryption-key \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"
```

## 部署 Cloud Run service <a href="#deploy-the-cloud-run-service" id="deploy-the-cloud-run-service"></a>

现在你可以部署 n8n service：

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n:latest \
    --command="/bin/sh" \
    --args="-c,sleep 5;n8n start" \
    --region=$REGION \
    --allow-unauthenticated \
    --port=5678 \
    --memory=2Gi \
    --no-cpu-throttling \
    --set-env-vars="N8N_PORT=5678,N8N_PROTOCOL=https,N8N_ENDPOINT_HEALTH=health,DB_TYPE=postgresdb,DB_POSTGRESDB_DATABASE=n8n,DB_POSTGRESDB_USER=n8n-user,DB_POSTGRESDB_HOST=/cloudsql/$PROJECT_ID:$REGION:n8n-db,DB_POSTGRESDB_PORT=5432,DB_POSTGRESDB_SCHEMA=public,GENERIC_TIMEZONE=UTC,QUEUE_HEALTH_CHECK_ACTIVE=true" \
    --set-secrets="DB_POSTGRESDB_PASSWORD=n8n-db-password:latest,N8N_ENCRYPTION_KEY=n8n-encryption-key:latest" \
    --add-cloudsql-instances=$PROJECT_ID:$REGION:n8n-db \
    --service-account=n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com
```

部署完成后，打开另一个 tab 并导航到 Service URL。你应该会看到 n8n login screen。

## 故障排除 <a href="#troubleshooting" id="troubleshooting"></a>

如果你看到 "Cannot GET /" screen，这通常表示 n8n 仍在启动。你可以刷新页面，它最终应该会加载。

## （可选）将 Google Workspace services 作为 n8n tools 启用 <a href="#optional-enabling-google-workspace-services-as-n8n-tools" id="optional-enabling-google-workspace-services-as-n8n-tools"></a>

如果你想将 Google Workspace services（Gmail、Calendar、Drive 等）作为 n8n 中的 tools 使用，建议设置 OAuth 来访问这些服务。

首先确保已启用你需要的相应 APIs：

```sh
## 启用你需要的 APIs <a href="#enable-whichever-apis-you-need" id="enable-whichever-apis-you-need"></a>
## 注意：如果你需要 Sheets/Docs，仅启用 Drive 并不够；这些服务各自有自己的 API <a href="#note-if-you-want-sheetsdocs-its-not-enough-to-just-enable-drive-these-services-each-have-their-own-api" id="note-if-you-want-sheetsdocs-its-not-enough-to-just-enable-drive-these-services-each-have-their-own-api"></a>
gcloud services enable gmail.googleapis.com
gcloud services enable drive.googleapis.com
gcloud services enable sheets.googleapis.com
gcloud services enable docs.googleapis.com
gcloud services enable calendar-json.googleapis.com
```

使用必要的 OAuth callback URLs 作为环境变量，重新部署 Cloud Run 上的 n8n：

```sh
export SERVICE_URL="your-n8n-service-URL"
## e.g. https://n8n-12345678.us-west1.run.app <a href="#eg-httpsn8n-12345678us-west1runapp" id="eg-httpsn8n-12345678us-west1runapp"></a>

gcloud run services update n8n \
    --region=$REGION \
    --update-env-vars="N8N_HOST=$(echo $SERVICE_URL | sed 's/https:\/\///'),WEBHOOK_URL=$SERVICE_URL,N8N_EDITOR_BASE_URL=$SERVICE_URL"
```

最后，你必须为这些服务设置 OAuth。访问 `https://console.cloud.google.com/auth` 并执行以下步骤：

1. 如果显示 "Get Started" 按钮（当你还没有在此 Cloud project 中设置 OAuth 时），点击它。
1. 对于 "App Information"，输入你偏好的 "App Name" 和 "User Support Email"。
1. 对于 "Audience"，如果你只打算允许同一 Google Workspace 中的用户访问，请选择 "Internal"。否则，你可以选择 "External"。
1. 输入 "Contact Information"。
1. 如果你选择了 "External"，则点击 "Audience" 并添加需要授予访问权限的 test users。
1. 点击 "Clients" > "Create client"，在 "Application type" 中选择 "Web application"，在 "Authorized JavaScript origins" 中输入你的 n8n service URL，并在 "Authorized redirect URIs" 中输入 "<YOUR-N8N-URL>/rest/oauth2-credential/callback"，其中 YOUR-N8N-URL 也是 n8n service URL（例如 `https://n8n-12345678.us-west1.run.app/rest/oauth2-credential/callback`）。请确保下载创建的 client JSON 文件，因为它包含 client secret，之后你无法在 Console 中再次看到它。
1. 点击 "Data Access" 并添加你希望 n8n 拥有访问权限的 scopes（例如，要访问 Google Sheets，你需要 `https://googleapis.com/auth/drive.file` 和 `https://googleapis.com/auth/spreadsheets`）。
1. 现在你应该可以使用这些 workspace services。你可以登录 n8n，添加相应 service 的 Tool，并使用第 6 步中 OAuth client JSON 文件里的信息添加其 credentials，测试它是否正常工作。
