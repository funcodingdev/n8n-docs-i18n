---
contentType: tutorial
nodeTitle: Deploy to AWS
originalFilePath: hosting/installation/server-setups/aws.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/aws'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws
layout:
  description:
    visible: false
---

# 在 Amazon Web Services 上托管 n8n <a href="#hosting-n8n-on-amazon-web-services" id="hosting-n8n-on-amazon-web-services"></a>

本托管指南展示如何使用 Amazon Web Services (AWS) 自托管 n8n。它使用 n8n，并以 Postgres 作为 database backend，同时使用 Kubernetes 管理必要资源和 reverse proxy。

## 托管选项 <a href="#hosting-options" id="hosting-options"></a>

AWS 提供多种适合托管 n8n 的方式，包括 EC2（virtual machines）和 EKS（使用 Kubernetes 运行 containers）。

本指南使用 [EKS](https://aws.amazon.com/eks/) 作为托管选项。使用 Kubernetes 需要一些额外复杂度和配置，但在需求变化时，它是扩展 n8n 的最佳方法。

## 先决条件 <a href="#prerequisites" id="prerequisites"></a>

本指南中的步骤混合使用 AWS UI 和 [用于 EKS 的 eksctl CLI tool](https://eksctl.io)。

虽然 eksctl 文档中没有提到，但你还需要[安装 AWS CLI tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)，并[配置该工具的身份验证](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/YLv7Cqg70tj1alDgktSX/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iFLUKG9zJaouigaM7IOo/" %}

## 创建 cluster <a href="#create-a-cluster" id="create-a-cluster"></a>

使用 eksctl tool 创建 cluster，并通过以下命令指定 name 和 region：

```shell
eksctl create cluster --name n8n --region <your-aws-region>
```

创建 cluster 可能需要一段时间。


cluster 创建完成后，eksctl 会自动将 kubectl context 设置为该 cluster。

## Clone 配置 repository <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Kubernetes 和 n8n 需要一系列 configuration files。你可以从[此 repository](https://github.com/n8n-io/n8n-hosting) clone 它们。以下步骤会说明每个文件的作用，以及你需要更改哪些设置。

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

要在 pod 重启之间保留数据，Postgres deployment 需要 persistent volume。默认 AWS storage class [gp3](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#gp3-ebs-volume-type) 适合此目的。它定义在 `postgres-claim0-persistentvolumeclaim.yaml` manifest 中。


```yaml
…
spec:
  storageClassName: gp3
  accessModes:
    - ReadWriteOnce
…
```

### Postgres 环境变量 <a href="#postgres-environment-variables" id="postgres-environment-variables"></a>

Postgres 需要设置一些环境变量，传递给 containers 中运行的应用。

示例 `postgres-secret.yaml` 文件包含 placeholders，你需要将它们替换为自己的用户详情和要使用的 database。

PostgreSQL 使用 root user（`POSTGRES_USER`）进行设置和管理，但最佳实践是为 n8n 创建单独的非 root user（`POSTGRES_NON_ROOT_USER`）。root user 拥有完全控制权，而 n8n 运行时只需要非 root user 权限。同时配置两者可提升安全性，并帮助防止意外更改 database system。

`postgres-deployment.yaml` manifest 随后会使用此 manifest 文件中的值，将它们发送给 application pods。

## 配置 n8n <a href="#configure-n8n" id="configure-n8n"></a>

### 为 file storage 创建 volume <a href="#create-a-volume-for-file-storage" id="create-a-volume-for-file-storage"></a>

虽然运行 n8n 并非必须使用 persistent volumes，但它有助于保留使用 n8n 时上传的 files；如果你想在重启之间持久化[手动 n8n encryption keys](../../configure-n8n/basic-configuration/use-environment-variables/deployment.md)，也需要它，因为启动期间会将包含 key 的文件保存到 file storage。

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

[Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) 允许你指定 application containers 所需的最小资源以及它们可运行到的限制。上面 clone 的示例 YAML files 在 `n8n-deployment.yaml` 文件的 `resources` 部分包含以下内容：

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
- 设置 resource consumption limits
- 之前定义的 `volumes`，以及用于定义 container 中挂载 volumes 路径的 `volumeMounts`
- Scaling 和 restart policies。示例 manifests 为每个 pod 定义一个 instance。你应该按自己的需求更改它。

## Services <a href="#services" id="services"></a>

默认情况下，两个 service manifests（`postgres-service.yaml` 和 `n8n-service.yaml`）使用 Kubernetes load balancer 将 services 暴露给外部世界，分别使用端口 5432 和 5678。

## 发送到 Kubernetes cluster <a href="#send-to-kubernetes-cluster" id="send-to-kubernetes-cluster"></a>

在 `n8n-kubernetes-hosting` 目录中运行以下命令，将所有 manifests 发送到 cluster：

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

n8n 通常运行在 subdomain 上。请在你的 provider 中为 subdomain 创建 DNS record，并将它指向 instance 的 static address。

要查找 instance 上运行的 n8n service 地址：

1. 在 AWS console 中打开 **Amazon Elastic Kubernetes Service** 页面的 **Clusters** 部分。
2. 选择 cluster 名称，打开其配置页面。
3. 选择 **Resources** tab，然后选择 **Service and networking** > **Services**。
4. 选择 **n8n** service，并复制 **Load balancer URLs** 值。将此值加上 n8n service port（5678）后用于 DNS。

{% hint style="info" %}
**使用 HTTP**

本指南为它定义的 services 使用 HTTP connections，例如在 `n8n-deployment.yaml` 中。但是，如果你点击 **Load balancer URLs** 值，EKS 会带你进入 "HTTPS" URL，从而导致错误。要解决此问题，打开 n8n subdomain 时请确保使用 HTTP。
{% endhint %}
## 删除资源 <a href="#delete-resources" id="delete-resources"></a>

如果需要删除此设置，你可以使用以下命令移除 manifests 创建的 resources：

```shell
kubectl delete -f .
```

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
