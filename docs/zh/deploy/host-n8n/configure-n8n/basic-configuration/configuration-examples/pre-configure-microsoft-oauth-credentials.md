---
title: Pre-configure Microsoft OAuth credentials
description: >-
  使用 credential overwrites 在 n8n 中预配置 Microsoft OAuth2 credentials，让用户无需自行注册
  app 即可连接。
contentType: howto
nodeTitle: Pre-configure Microsoft OAuth credentials
originalFilePath: >-
  hosting/configuration/configuration-examples/microsoft-oauth-credential-overwrites.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/microsoft-oauth-credential-overwrites
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials
layout:
  description:
    visible: false
---

# 预配置 Microsoft OAuth credentials <a href="#pre-configure-microsoft-oauth-credentials" id="pre-configure-microsoft-oauth-credentials"></a>

在[设置带委派访问权限的 Microsoft Entra ID app registration](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/microsoftentra#delegated-access-for-organisation-wide-microsoft-integrations)后，你可以使用 [credential overwrites](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/credential-overwrites)，在 n8n 启动时注入 Client ID 和 Client Secret。这意味着你的组织用户无需完成自己的 OAuth app registration，就可以连接 Microsoft 服务。

n8n 支持三个用于 credential overwrites 的环境变量。本指南使用 `CREDENTIALS_OVERWRITE_DATA_FILE`。完整变量参考见 [Credentials environment variables](../use-environment-variables/credentials.md)。

## 创建 credentials file <a href="#create-the-credentials-file" id="create-the-credentials-file"></a>

在运行 n8n 的主机上，在 `docker-compose.yaml` 所在目录创建一个名为 `credentials-overwrite.json` 的文件。

该文件包含一个 JSON 对象，以 n8n credential type name 作为键。例如，要预配置 Microsoft Outlook：

```json
{
  "microsoftOutlookOAuth2Api": {
    "clientId": "YOUR_CLIENT_ID",
    "clientSecret": "YOUR_CLIENT_SECRET"
  }
}
```

要一次预配置多个 Microsoft 服务，请把每个 credential type 作为单独的键添加：

```json
{
  "microsoftOutlookOAuth2Api": {
    "clientId": "YOUR_CLIENT_ID",
    "clientSecret": "YOUR_CLIENT_SECRET"
  },
  "microsoftOneDriveOAuth2Api": {
    "clientId": "YOUR_CLIENT_ID",
    "clientSecret": "YOUR_CLIENT_SECRET"
  }
}
```

{% hint style="info" %}
**压缩 JSON**

n8n 要求 JSON 必须是 minified 格式（没有空格或换行）。上面的示例为了便于阅读做了格式化。请确保实际文件不包含额外空白：

```json
{"microsoftOutlookOAuth2Api":{"clientId":"YOUR_CLIENT_ID","clientSecret":"YOUR_CLIENT_SECRET"}}
```
{% endhint %}

每个 Microsoft 服务对应的 credential type name，请参考 [Required scopes by integration](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/microsoftentra#required-scopes-by-integration)。

## Docker Compose <a href="#docker-compose" id="docker-compose"></a>

将 credentials file 挂载为只读 volume，并在 `compose.yaml` 中设置环境变量：

```yaml
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:latest
    container_name: n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - GENERIC_TIMEZONE=America/New_York
      - TZ=America/New_York
      - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
      - N8N_LOG_LEVEL=debug
      - N8N_LOG_OUTPUT=file,console
      - N8N_LOG_FILE_COUNT_MAX=5
      - CREDENTIALS_OVERWRITE_DATA_FILE=/run/secrets/credentials-overwrite.json
    volumes:
      - n8n_data:/home/node/.n8n
      - ./credentials-overwrite.json:/run/secrets/credentials-overwrite.json:ro
    networks:
      - default
volumes:
  n8n_data:
    name: ${N8N_VOLUME:-n8n_data}
    external: true
```

重启容器以应用更改：

```bash
docker compose up -d
```

## 验证 overwrite 已生效 <a href="#verify-the-overwrite-is-applied" id="verify-the-overwrite-is-applied"></a>

n8n 启动后，让用户为某个已预配置的服务（例如 Microsoft Outlook）创建新的 credential。他们应该会在 credential 选择中看到 **Managed OAuth2 (recommended)** 选项。

![Microsoft Entra credentials screen](../../../../.gitbook/assets/microsoft-entra-oauth.png)

用户可以点击 **Connect to Microsoft Outlook**，无需额外授权。随后应显示 **Account connected** 消息。

如果没有出现 **Managed OAuth 2** 选项，说明环境变量没有正确应用。请检查 volume mount 中的文件路径是否与 `CREDENTIALS_OVERWRITE_DATA_FILE` 的值一致。

## Kubernetes <a href="#kubernetes" id="kubernetes"></a>

对于 Kubernetes 部署，请用 Kubernetes 原生机制替换 Docker volume mount。具体方式会因云服务商不同而不同。请选择与你环境匹配的章节。

### Plain Kubernetes Secret (EKS / AKS / GKE) <a href="#plain-kubernetes-secret-eks-aks-gke" id="plain-kubernetes-secret-eks-aks-gke"></a>

这种方式无需额外依赖，可在三个托管 Kubernetes provider 中通用。

**1. 创建 Secret：**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: n8n-credentials-overwrite
  namespace: your-namespace
type: Opaque
stringData:
  credentials-overwrite.json: '{"microsoftOutlookOAuth2Api":{"clientId":"YOUR_CLIENT_ID","clientSecret":"YOUR_CLIENT_SECRET"}}'
```

**2. 在 Deployment 中挂载 Secret：**

```yaml
spec:
  containers:
    - name: n8n
      image: docker.n8n.io/n8nio/n8n:latest
      env:
        - name: CREDENTIALS_OVERWRITE_DATA_FILE
          value: /run/secrets/credentials-overwrite.json
        # ...your other env vars
      volumeMounts:
        - name: credentials-overwrite
          mountPath: /run/secrets/credentials-overwrite.json
          subPath: credentials-overwrite.json
          readOnly: true
  volumes:
    - name: credentials-overwrite
      secret:
        secretName: n8n-credentials-overwrite
```

`subPath` 字段很重要。没有它时，Kubernetes 会替换整个 `/run/secrets/` 目录，而不是只挂载单个文件。

{% hint style="info" %}
**替代方案：内联环境变量**

如果想完全跳过 volume mount，可以直接把 Secret 作为环境变量引用：

```yaml
env:
  - name: CREDENTIALS_OVERWRITE_DATA
    valueFrom:
      secretKeyRef:
        name: n8n-credentials-overwrite
        key: credentials-overwrite.json
```

```yaml
stringData:
  credentials-json: '{"microsoftOutlookOAuth2Api":{"clientId":"...","clientSecret":"..."}}'
```

对于单一服务配置，这种方式更简洁。但要注意，某些 Kubernetes 环境会限制环境变量大小（例如每个变量 128KB）。如果有很多 credential overwrites，基于文件的方式更稳妥。
{% endhint %}

### AWS Secrets Manager (EKS) <a href="#aws-secrets-manager-eks" id="aws-secrets-manager-eks"></a>

这种方式使用 [AWS Secrets Store CSI Driver](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_csi_driver.html)，将 AWS Secrets Manager 中的 secret 直接挂载到 pod。它增加了轮换支持、CloudTrail 审计日志和集中式 secret 管理。

**前提条件：**

- 集群中已安装 Secrets Store CSI Driver 和 ASCP（AWS Secrets and Configuration Provider）
- 已为集群配置 IAM OIDC provider（IRSA 需要）
- 拥有 `secretsmanager:GetSecretValue` 和 `secretsmanager:DescribeSecret` 权限的 IAM role

**1. 在 AWS Secrets Manager 中创建 secret：**

```bash
aws secretsmanager create-secret \
  --name n8n/credentials-overwrite \
  --description "n8n credential overwrites for Microsoft OAuth" \
  --secret-string '{"microsoftOutlookOAuth2Api":{"clientId":"YOUR_CLIENT_ID","clientSecret":"YOUR_CLIENT_SECRET"}}'
```

**2. 创建 IAM policy：**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:REGION:ACCOUNT_ID:secret:n8n/credentials-overwrite-*"
    }
  ]
}
```

```bash
aws iam create-policy \
  --policy-name n8n-credentials-overwrite-read \
  --policy-document file://policy.json
```

**3. 使用 IRSA 创建 service account：**

```bash
eksctl create iamserviceaccount \
  --name n8n-sa \
  --namespace your-namespace \
  --cluster your-cluster \
  --attach-policy-arn arn:aws:iam::ACCOUNT_ID:policy/n8n-credentials-overwrite-read \
  --approve
```

**4. 创建 SecretProviderClass：**

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: n8n-credentials-overwrite
  namespace: your-namespace
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "n8n/credentials-overwrite"
        objectType: "secretsmanager"
        objectAlias: "credentials-overwrite.json"
```

**5. 更新 n8n Deployment：**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: your-namespace
spec:
  template:
    spec:
      serviceAccountName: n8n-sa
      containers:
        - name: n8n
          image: docker.n8n.io/n8nio/n8n:latest
          env:
            - name: CREDENTIALS_OVERWRITE_DATA_FILE
              value: /run/secrets/credentials-overwrite.json
          volumeMounts:
            - name: credentials-overwrite
              mountPath: /run/secrets/credentials-overwrite.json
              subPath: credentials-overwrite.json
              readOnly: true
      volumes:
        - name: credentials-overwrite
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: n8n-credentials-overwrite
```

**轮换 secret：**

要更新 credentials，请更新 Secrets Manager 中的值：

```bash
aws secretsmanager update-secret \
  --secret-id n8n/credentials-overwrite \
  --secret-string '{"microsoftOutlookOAuth2Api":{"clientId":"NEW_CLIENT_ID","clientSecret":"NEW_CLIENT_SECRET"}}'
```

CSI driver 会按轮询间隔同步更新后的值（默认两分钟）。请重启 n8n pod，让 n8n 读取更新后的文件，因为 n8n 会在启动时读取 credentials file。

### Azure Key Vault (AKS) <a href="#azure-key-vault-aks" id="azure-key-vault-aks"></a>

这种方式使用 [Azure Key Vault Provider for the Secrets Store CSI Driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)，将 Azure Key Vault 中的 secrets 挂载到 pod。

**前提条件：**

- AKS 集群已启用 Secrets Store CSI Driver 和 Azure Key Vault Provider addon
- 一个 Azure Key Vault 实例
- 对该 vault 拥有访问权限的 managed identity 或 service principal
- 集群已启用 Workload Identity（相比 pod identity 更推荐）

**1. 创建或使用现有 Key Vault：**

```bash
az keyvault create \
  --name n8n-credentials-vault \
  --resource-group your-resource-group \
  --location your-region
```

**2. 在 Key Vault 中创建 secret：**

```bash
az keyvault secret set \
  --vault-name n8n-credentials-vault \
  --name n8n-credentials-overwrite \
  --value '{"microsoftOutlookOAuth2Api":{"clientId":"YOUR_CLIENT_ID","clientSecret":"YOUR_CLIENT_SECRET"}}'
```

**3. 设置 Workload Identity：**

创建一个 managed identity，并建立 federated credential：

```bash
# 创建 managed identity <a href="#create-a-managed-identity" id="create-a-managed-identity"></a>
az identity create \
  --name n8n-workload-identity \
  --resource-group your-resource-group \
  --location your-region

# 获取 identity client ID <a href="#get-the-identity-client-id" id="get-the-identity-client-id"></a>
CLIENT_ID=$(az identity show \
  --name n8n-workload-identity \
  --resource-group your-resource-group \
  --query clientId -o tsv)

# 授予 identity 访问 Key Vault 的权限 <a href="#grant-the-identity-access-to-the-key-vault" id="grant-the-identity-access-to-the-key-vault"></a>
az keyvault set-policy \
  --name n8n-credentials-vault \
  --secret-permissions get \
  --spn "$CLIENT_ID"

# 获取集群的 OIDC issuer URL <a href="#get-the-oidc-issuer-url-for-your-cluster" id="get-the-oidc-issuer-url-for-your-cluster"></a>
OIDC_ISSUER=$(az aks show \
  --name your-cluster \
  --resource-group your-resource-group \
  --query "oidcIssuerProfile.issuerUrl" -o tsv)

# 创建 federated credential <a href="#create-the-federated-credential" id="create-the-federated-credential"></a>
az identity credential create \
  --name n8n-workload-identity \
  --resource-group your-resource-group \
  --issuer "$OIDC_ISSUER" \
  --subject system:serviceaccount:your-namespace:n8n-sa \
  --audience api://AzureADTokenExchange
```

**4. 创建 Kubernetes ServiceAccount：**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: n8n-sa
  namespace: your-namespace
  annotations:
    azure.workload.identity/client-id: "YOUR_MANAGED_IDENTITY_CLIENT_ID"
  labels:
    azure.workload.identity/use: "true"
```

**5. 创建 SecretProviderClass：**

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: n8n-credentials-overwrite
  namespace: your-namespace
spec:
  provider: azure
  parameters:
    usePodIdentity: "false"
    useWorkloadIdentity: "true"
    clientID: "YOUR_MANAGED_IDENTITY_CLIENT_ID"
    keyvaultName: "n8n-credentials-vault"
    objects: |
      array:
        - |
          objectName: n8n-credentials-overwrite
          objectType: secret
          objectAlias: credentials-overwrite.json
    tenantId: "YOUR_TENANT_ID"
```

**6. 更新 n8n Deployment：**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: your-namespace
spec:
  template:
    spec:
      serviceAccountName: n8n-sa
      containers:
        - name: n8n
          image: docker.n8n.io/n8nio/n8n:latest
          env:
            - name: CREDENTIALS_OVERWRITE_DATA_FILE
              value: /run/secrets/credentials-overwrite.json
          volumeMounts:
            - name: credentials-overwrite
              mountPath: /run/secrets/credentials-overwrite.json
              subPath: credentials-overwrite.json
              readOnly: true
      volumes:
        - name: credentials-overwrite
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: n8n-credentials-overwrite
```

**轮换 secret：**

```bash
az keyvault secret set \
  --vault-name n8n-credentials-vault \
  --name n8n-credentials-overwrite \
  --value '{"microsoftOutlookOAuth2Api":{"clientId":"NEW_CLIENT_ID","clientSecret":"NEW_CLIENT_SECRET"}}'
```

CSI driver 会按轮询间隔同步（默认两分钟）。之后请重启 n8n pod，让 n8n 获取更新后的文件。

### Google Secret Manager (GKE) <a href="#google-secret-manager-gke" id="google-secret-manager-gke"></a>

这种方式使用 [GCP provider for the Secrets Store CSI Driver](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp)，将 Google Secret Manager 中的 secrets 挂载到 pod。

**前提条件：**

- 已启用 Workload Identity Federation 的 GKE 集群
- 项目已启用 Secret Manager API
- 拥有 `secretmanager.secretAccessor` role 的 Google service account

**1. 启用 Secret Manager API：**

```bash
gcloud services enable secretmanager.googleapis.com \
  --project your-project-id
```

**2. 创建 secret：**

```bash
echo -n '{"microsoftOutlookOAuth2Api":{"clientId":"YOUR_CLIENT_ID","clientSecret":"YOUR_CLIENT_SECRET"}}' | \
  gcloud secrets create n8n-credentials-overwrite \
    --data-file=- \
    --project your-project-id
```

**3. 设置 Workload Identity Federation：**

```bash
# 创建 Google service account <a href="#create-a-google-service-account" id="create-a-google-service-account"></a>
gcloud iam service-accounts create n8n-secret-reader \
  --display-name="n8n Secret Reader" \
  --project your-project-id

# 授予它访问 secret 的权限 <a href="#grant-it-access-to-the-secret" id="grant-it-access-to-the-secret"></a>
gcloud secrets add-iam-policy-binding n8n-credentials-overwrite \
  --member="serviceAccount:n8n-secret-reader@your-project-id.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor" \
  --project your-project-id

# 将 Kubernetes service account 绑定到 Google service account <a href="#bind-the-kubernetes-service-account-to-the-google-service-account" id="bind-the-kubernetes-service-account-to-the-google-service-account"></a>
gcloud iam service-accounts add-iam-policy-binding \
  n8n-secret-reader@your-project-id.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:your-project-id.svc.id.goog[your-namespace/n8n-sa]"
```

**4. 创建 Kubernetes ServiceAccount：**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: n8n-sa
  namespace: your-namespace
  annotations:
    iam.gke.io/gcp-service-account: n8n-secret-reader@your-project-id.iam.gserviceaccount.com
```

**5. 安装 CSI Driver 和 GCP provider：**

```bash
# 安装 CSI driver <a href="#install-the-csi-driver" id="install-the-csi-driver"></a>
helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system

# 安装 GCP provider <a href="#install-the-gcp-provider" id="install-the-gcp-provider"></a>
kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/main/deploy/provider-gcp-plugin.yaml
```

**6. 创建 SecretProviderClass：**

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: n8n-credentials-overwrite
  namespace: your-namespace
spec:
  provider: gcp
  parameters:
    secrets: |
      - resourceName: "projects/your-project-id/secrets/n8n-credentials-overwrite/versions/latest"
        path: "credentials-overwrite.json"
```

**7. 更新 n8n Deployment：**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: your-namespace
spec:
  template:
    spec:
      serviceAccountName: n8n-sa
      containers:
        - name: n8n
          image: docker.n8n.io/n8nio/n8n:latest
          env:
            - name: CREDENTIALS_OVERWRITE_DATA_FILE
              value: /run/secrets/credentials-overwrite.json
          volumeMounts:
            - name: credentials-overwrite
              mountPath: /run/secrets/credentials-overwrite.json
              subPath: credentials-overwrite.json
              readOnly: true
      volumes:
        - name: credentials-overwrite
          csi:
            driver: secrets-store.csi.k8s.io
            readOnly: true
            volumeAttributes:
              secretProviderClass: n8n-credentials-overwrite
```

**轮换 secret：**

创建 secret 的新版本：

```bash
echo -n '{"microsoftOutlookOAuth2Api":{"clientId":"NEW_CLIENT_ID","clientSecret":"NEW_CLIENT_SECRET"}}' | \
  gcloud secrets versions add n8n-credentials-overwrite \
    --data-file=- \
    --project your-project-id
```

由于 SecretProviderClass 引用 `versions/latest`，CSI driver 会在下一次同步时获取新版本。请重启 n8n pod，让 n8n 读取更新后的文件。
