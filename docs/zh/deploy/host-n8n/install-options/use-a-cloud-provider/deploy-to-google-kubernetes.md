---
contentType: tutorial
nodeTitle: Deploy to Google Kubernetes
originalFilePath: hosting/installation/server-setups/google-kubernetes-engine.md
originalUrl: >-
  https://docs.n8n.io/hosting/installation/server-setups/google-kubernetes-engine
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes
layout:
  description:
    visible: false
---

# 在 Google Kubernetes Engine 上托管 n8n <a href="#hosting-n8n-on-google-kubernetes-engine" id="hosting-n8n-on-google-kubernetes-engine"></a>

Google Cloud 提供多种适合托管 n8n 的选项，包括 Cloud Run（针对运行 containers 优化）、Compute Engine（VMs）和 Kubernetes Engine（使用 Kubernetes 运行 containers）。

本指南使用 Google Kubernetes Engine (GKE) 作为托管选项。如果你想使用 Cloud Run，请参阅[这些说明](deploy-to-google-cloud-run.md)。

本指南中的大多数步骤使用 Google Cloud UI，但你也可以改用 [gcloud command line tool](https://cloud.google.com/sdk/gcloud/) 完成所有步骤。

## 先决条件 <a href="#prerequisites" id="prerequisites"></a>

- [gcloud command line tool](https://cloud.google.com/sdk/gcloud/)
- [gke-gcloud-auth-plugin](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke)（先安装 gcloud CLI）

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 创建项目 <a href="#create-project" id="create-project"></a>

GCP 鼓励你创建 projects，以便对 resources 和 configuration 进行逻辑组织。从 Google Cloud Console 为你的 n8n 部署创建新项目：选择 project dropdown menu，然后选择 **NEW PROJECT** 按钮。然后选择新创建的项目。执行本指南中的其他步骤时，请确保你已选择正确项目。

## 启用 Kubernetes Engine API <a href="#enable-the-kubernetes-engine-api" id="enable-the-kubernetes-engine-api"></a>

GKE 默认未启用。在顶部搜索栏中搜索 "Kubernetes"，并从结果中选择 "Kubernetes Engine"。

选择 **ENABLE**，为此项目启用 Kubernetes Engine API。

## 创建 cluster <a href="#create-a-cluster" id="create-a-cluster"></a>

从 [GKE service page](https://console.cloud.google.com/kubernetes/list/overview)，选择 **Clusters** > **CREATE**。请确保选择 "Standard" cluster 选项，n8n 不适用于 "Autopilot" cluster。除非有需要专门更改的内容（例如 location），否则可以保留 cluster configuration 默认值。

## 设置 Kubectl context <a href="#set-kubectl-context" id="set-kubectl-context"></a>

本指南后续步骤要求你将 GCP instance 设置为 Kubectl context。你可以打开 cluster instance 的详情页并选择 **CONNECT**，找到连接详情。显示的 code snippet 会展示 gcloud CLI tool 的 connection string。将 code snippet 粘贴到 gcloud CLI 并运行，以更改你的本地 Kubernetes settings，使其使用新的 gcloud cluster。

## Clone 配置 repository <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Kubernetes 和 n8n 需要一系列 configuration files。你可以从[此 repository](https://github.com/n8n-io/n8n-hosting) 将它们 clone 到本地。以下步骤说明 file configuration 以及如何添加你的信息。

使用以下命令 clone repository：

```shell
git clone https://github.com/n8n-io/n8n-hosting.git
```

然后切换目录：

```shell
cd n8n-hosting/kubernetes
```

## 配置 Postgres <a href="#configure-postgres" id="configure-postgres"></a>

对于较大规模的 n8n 部署，Postgres 提供比 SQLite 更稳健的 database backend。

### 为持久存储创建 volume <a href="#create-a-volume-for-persistent-storage" id="create-a-volume-for-persistent-storage"></a>

要在 pod 重启之间保留数据，Postgres deployment 需要 persistent volume。在 GCP 上运行 Postgres 需要特定的 Kubernetes Storage Class。你可以阅读[此指南](https://cloud.google.com/architecture/deploying-highly-available-postgresql-with-gke)了解具体信息，但 `storage.yaml` manifest 会为你创建它。你可能需要在 `allowedTopologies` > `matchedLabelExpressions` > `values` key 下更改创建 storage 的 regions。默认情况下，它们设置为 `us-central`。

```yaml
…
allowedTopologies:
  - matchLabelExpressions:
      - key: failure-domain.beta.kubernetes.io/zone
        values:
          - us-central1-b
          - us-central1-c
```

### Postgres 环境变量 <a href="#postgres-environment-variables" id="postgres-environment-variables"></a>

Postgres 需要设置一些环境变量，传递给 containers 中运行的应用。

示例 `postgres-secret.yaml` 文件包含 placeholders，你需要将它们替换为自己的值。Postgres 会在创建 database 时使用这些详情。

`postgres-deployment.yaml` manifest 随后会使用此 manifest 文件中的值，将它们发送给 application pods。

## 配置 n8n <a href="#configure-n8n" id="configure-n8n"></a>

### 为 file storage 创建 volume <a href="#create-a-volume-for-file-storage" id="create-a-volume-for-file-storage"></a>

虽然运行 n8n 并非必须使用 persistent volumes，但以下场景需要它：

* 使用与 files 交互的 nodes，例如 binary data node。
* 如果你希望在重启之间持久化[手动 n8n encryption keys](../../configure-n8n/basic-configuration/use-environment-variables/deployment.md)。这会在启动期间将包含 key 的文件保存到 file storage。

`n8n-claim0-persistentvolumeclaim.yaml` manifest 会创建它，n8n Deployment 会在 `n8n-deployment.yaml` manifest 的 `volumes` 部分挂载该 claim。

```yaml
…
volumes:
  - name: n8n-claim0
    persistentVolumeClaim:
      claimName: n8n-claim0
…
```

### Pod resources <a href="#pod-resources" id="pod-resources"></a>

[Kubernetes 允许你](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)可选地指定 application containers 所需的最小资源以及它们可运行到的限制。上面 clone 的示例 YAML files 在 `n8n-deployment.yaml` 和 `postgres-deployment.yaml` 文件的 `resources` 部分包含以下内容：

```yaml
…
resources:
  requests:
    memory: "250Mi"
  limits:
    memory: "500Mi"
…
```

这定义了每个 container 最少 250mb、最多 500mb，并让 Kubernetes 处理 CPU。你可以按自己的需求更改这些值。作为参考，下面是 n8n cloud offerings 的 resources values：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/I9ftZ1V1rwx3OrFOh0bT/" %}

### 可选：环境变量 <a href="#optional-environment-variables" id="optional-environment-variables"></a>

你可以使用环境变量配置 n8n settings 和 behaviors。

创建一个 `n8n-secret.yaml` 文件。有关 n8n environment variables 的详细信息，请参阅 [Environment variables](../../configure-n8n/basic-configuration/use-environment-variables/README.md)。

## Deployments <a href="#deployments" id="deployments"></a>

两个 deployment manifests（`n8n-deployment.yaml` 和 `postgres-deployment.yaml`）会向 Kubernetes 定义 n8n 和 Postgres 应用。

这些 manifests 定义以下内容：

- 将定义的 environment variables 发送给每个 application pod
- 定义要使用的 container image
- 使用 `resources` object 设置 resource consumption limits
- 之前定义的 `volumes`，以及用于定义 container 中挂载 volumes 路径的 `volumeMounts`
- Scaling 和 restart policies。示例 manifests 为每个 pod 定义一个 instance。你应该按自己的需求更改它。

## Services <a href="#services" id="services"></a>

两个 service manifests（`postgres-service.yaml` 和 `n8n-service.yaml`）使用 Kubernetes load balancer 将 services 暴露给外部世界，分别使用端口 5432 和 5678。

## 发送到 Kubernetes cluster <a href="#send-to-kubernetes-cluster" id="send-to-kubernetes-cluster"></a>

使用以下命令将所有 manifests 发送到 cluster：

```shell
kubectl apply -f .
```

{% hint style="info" %}
**Namespace error**

你可能会看到关于找不到 "n8n" namespace 的错误消息，因为该 resource 尚未准备好。你可以再次运行同一个命令，或先使用以下命令应用 namespace manifest：

```shell
kubectl apply -f namespace.yaml
```
{% endhint %}


## 设置 DNS <a href="#set-up-dns" id="set-up-dns"></a>

n8n 通常运行在 subdomain 上。请在你的 provider 中为 subdomain 创建 DNS record，并将它指向 n8n service 的 IP address。在你要使用的 cluster 的 **Services & Ingress** 菜单项中，从 **Endpoints** 列查找 n8n service 的 IP address。

{% hint style="info" %}
**GKE 和 IP addresses**

[阅读此 GKE tutorial](https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip#configuring_your_domain_name_records)，了解 reserved IP addresses 如何与 GKE 和 Kubernetes resources 配合工作的更多详情。
{% endhint %}
## 删除资源 <a href="#delete-resources" id="delete-resources"></a>

使用以下命令移除 manifests 创建的 resources：

```shell
kubectl delete -f .
```

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
