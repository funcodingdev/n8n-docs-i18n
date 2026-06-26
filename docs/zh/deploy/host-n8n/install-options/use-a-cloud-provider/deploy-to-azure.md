---
contentType: tutorial
nodeTitle: Deploy to Azure
originalFilePath: hosting/installation/server-setups/azure.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/azure'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure
layout:
  description:
    visible: false
---

# 在 Azure 上托管 n8n <a href="#hosting-n8n-on-azure" id="hosting-n8n-on-azure"></a>

本托管指南展示如何在 Azure 上自托管 n8n。它使用 n8n，并以 Postgres 作为 database backend，同时使用 Kubernetes 管理必要资源和 reverse proxy。

## 先决条件 <a href="#prerequisites" id="prerequisites"></a>

你需要 [Azure command line tool](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 托管选项 <a href="#hosting-options" id="hosting-options"></a>

Azure 提供多种适合托管 n8n 的方式，包括 Azure Container Instances（针对运行 containers 优化）、Linux Virtual Machines 和 Azure Kubernetes Service（使用 Kubernetes 运行 containers）。

本指南使用 Azure Kubernetes Service (AKS) 作为托管选项。使用 Kubernetes 需要一些额外复杂度和配置，但在需求变化时，它是扩展 n8n 的最佳方法。

本指南的步骤混合使用 Azure UI 和 command line tool，但大多数任务你可以任选其中一种方式完成。

## 打开 Azure Kubernetes Service <a href="#open-the-azure-kubernetes-service" id="open-the-azure-kubernetes-service"></a>

从 [Azure portal](https://portal.azure.com/) 选择 **Kubernetes services**。

## 创建 cluster <a href="#create-a-cluster" id="create-a-cluster"></a>

从 Kubernetes services 页面，选择 **Create** > **Create a Kubernetes cluster**。

你可以选择任何符合需求的配置选项，完成后选择 **Create**。

## 设置 Kubectl context <a href="#set-kubectl-context" id="set-kubectl-context"></a>

本指南剩余步骤要求你将 Azure instance 设置为 Kubectl context。你可以打开 cluster instance 的详情页，然后点击 **Connect** 按钮来找到连接详情。生成的 code snippets 会显示需要粘贴并在 terminal 中运行的步骤，用于更改你的本地 Kubernetes settings，使其使用新的 cluster。

## Clone 配置 repository <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Kubernetes 和 n8n 需要一系列 configuration files。你可以从[此 repository](https://github.com/n8n-io/n8n-hosting) clone 它们。以下步骤会说明哪个文件配置什么，以及你需要更改什么。

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

### 为持久存储配置 volume <a href="#configure-volume-for-persistent-storage" id="configure-volume-for-persistent-storage"></a>

要在 pod 重启之间保留数据，Postgres deployment 需要 persistent volume。默认 storage class 适合此目的，并定义在 `postgres-claim0-persistentvolumeclaim.yaml` manifest 中。

{% hint style="info" %}
**专用 storage classes**

如果你对 storage classes 有专门或更高要求，请[阅读文档中 Azure 提供的选项](https://learn.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes)。
{% endhint %}
### Postgres 环境变量 <a href="#postgres-environment-variables" id="postgres-environment-variables"></a>

Postgres 需要设置一些环境变量，传递给 containers 中运行的应用。

示例 `postgres-secret.yaml` 文件包含需要替换为你自己的值的 placeholders。Postgres 会在创建 database 时使用这些详情。

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

[Kubernetes 允许你](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)可选地指定 application containers 所需的最小资源以及它们可运行到的限制。上面 clone 的示例 YAML files 在 `n8n-deployment.yaml` 文件的 `resources` 部分包含以下内容：

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

n8n 通常运行在 subdomain 上。请在你的 provider 中为 subdomain 创建 DNS record，并将它指向 n8n service 的 IP address。在你要使用的 cluster 的 **Services & ingresses** 菜单项中，从 **External IP** 列查找 n8n service 的 IP address。你需要将 n8n 端口 "5678" 添加到 URL。

{% hint style="info" %}
**AKS 中的静态 IP 地址**

[阅读此教程](https://learn.microsoft.com/en-us/azure/aks/static-ip)，了解如何在 AKS 中使用静态 IP 地址的更多详情。
{% endhint %}
## 删除资源 <a href="#delete-resources" id="delete-resources"></a>

使用以下命令移除 manifests 创建的 resources：

```shell
kubectl delete -f .
```

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
