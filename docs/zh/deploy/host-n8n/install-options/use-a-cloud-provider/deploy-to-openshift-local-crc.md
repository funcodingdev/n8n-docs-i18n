---
contentType: tutorial
nodeTitle: Deploy to OpenShift Local (CRC)
originalFilePath: hosting/installation/server-setups/openshift-crc.md
originalUrl: 'https://docs.n8n.io/hosting/installation/server-setups/openshift-crc'
url: >-
  https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc
layout:
  description:
    visible: false
---

# 在 OpenShift Local (CRC) 上托管 n8n <a href="#hosting-n8n-on-openshift-local-crc" id="hosting-n8n-on-openshift-local-crc"></a>

本指南会带你在 OpenShift Local (CRC) 上部署 n8n。OpenShift Local (CRC) 是 Red Hat 用来运行本地 OpenShift cluster 的工具。它模拟 AWS/EKS 部署，但完全运行在你的本地机器上。它适合在本地 OpenShift environment 中测试 n8n，且不会产生 cloud 成本。

OpenShift 本身会消耗大量资源，因此你需要一台可用资源较充足的机器。

## OpenShift concepts 与标准 Kubernetes 对比 <a href="#openshift-concepts-vs-standard-kubernetes" id="openshift-concepts-vs-standard-kubernetes"></a>

OpenShift 构建在 Kubernetes 之上，但使用不同术语，并且默认安全策略更严格。如果你熟悉标准 Kubernetes，或者熟悉面向 EKS 等 managed Kubernetes service 的指南，下表会映射等价概念，帮助你了解预期行为。

| Standard Kubernetes / EKS | OpenShift Local (CRC) |
| --- | --- |
| `kubectl` | `oc`（OpenShift CLI；也理解 `kubectl` commands） |
| Namespace | Project（同一概念，不同命令） |
| Ingress / LoadBalancer | Route（OpenShift 内置，不需要 controller） |
| EBS StorageClass (gp3) | CRC built-in storage provisioner（不需要设置） |
| RDS PostgreSQL | 通过 Helm 部署的 in-cluster PostgreSQL (Bitnami) |
| ElastiCache Redis | 通过 Helm 部署的 in-cluster Redis (Bitnami) |
| AWS S3 | Cluster 内 MinIO（S3-compatible） |
| Pod Identity / IRSA | 通过 Kubernetes Secret 提供 access keys |
| AWS Load Balancer Controller | 不需要（Routes 内置） |
| OIDC / IAM | 不需要 |
| ~$135-400/month | 免费（在你的机器上运行） |

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

开始前，确认你的机器具备：

- **CPU**：4 个或更多 physical cores（不只是 threads），并支持 virtualization
- **RAM**：至少 32+ GB 可用内存（CRC 会为它的 VM 保留 9 GB）
- **Disk**：100 GB 可用空间
- **OS**：Ubuntu（22.04 LTS 或更新版本）

## 准备 Ubuntu <a href="#prepare-ubuntu" id="prepare-ubuntu"></a>

### 打开 terminal <a href="#open-a-terminal" id="open-a-terminal"></a>

按 `Ctrl+Alt+T`，或在 Applications menu 中搜索 **Terminal**。

本指南中的每条命令都在 terminal 中输入，并通过按 **Enter** 执行。

### 更新系统 <a href="#update-your-system" id="update-your-system"></a>

先更新系统，避免 dependency 问题：

```shell
sudo apt update && sudo apt upgrade -y
```

{% hint style="info" %}
**sudo**

`sudo` 表示“以管理员身份运行”。系统会提示你输入密码。你输入的字符不会显示在屏幕上，这是正常现象。
{% endhint %}

### 检查 CPU virtualization 支持 <a href="#check-cpu-virtualization-support" id="check-cpu-virtualization-support"></a>

CRC 会运行一个 virtual machine。你的 CPU 必须支持 hardware virtualization：

```shell
egrep -c '(vmx|svm)' /proc/cpuinfo
```

- **输出 `0`**：Virtualization 已禁用。进入 BIOS/UEFI 设置并启用 VT-x (Intel) 或 AMD-V (AMD)，然后 reboot 并重试。
- **输出 `1` 或更高**：可以继续。

### 安装 KVM 和 libvirt <a href="#install-kvm-and-libvirt" id="install-kvm-and-libvirt"></a>

KVM 是 Linux 内置 hypervisor。CRC 使用它运行 OpenShift cluster VM：

```shell
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
```

安装 CRC 共享 filesystem 给 cluster VM 所需的 `virtiofsd`：

```shell
sudo apt install -y virtiofsd
```

启动 libvirt service，并配置为 boot 时自动启动：

```shell
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
```

验证它正在运行：

```shell
sudo systemctl status libvirtd
```

查找绿色的 `Active: active (running)`。按 `q` 退出。

### 将用户加入所需 groups <a href="#add-user-to-required-groups" id="add-user-to-required-groups"></a>

这样你就能使用 KVM 和 libvirt，而不必每条命令都输入 `sudo`：

```shell
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
```

{% hint style="info" %}
**Warning**

**你必须 log out 后重新 log in（或 reboot）才能生效。** 如果跳过此步骤，CRC 会因 “permission denied” error 失败。
{% endhint %}

现在 reboot：

```shell
sudo reboot
```

重新登录后，打开 terminal 并验证 group membership：

```shell
groups
```

你应该能看到 `libvirt` 和 `kvm`。

### 安装 NetworkManager <a href="#install-networkmanager" id="install-networkmanager"></a>

CRC 需要 NetworkManager 来管理 cluster internal domains（`*.apps-crc.testing`、`api.crc.testing`）的 DNS entries：

```shell
sudo apt install -y network-manager
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```

验证它已连接：

```shell
nmcli general status
```

`STATE` column 应显示 `connected`。

## 安装工具 <a href="#install-tools" id="install-tools"></a>

### 获取 Red Hat account 和 pull secret <a href="#get-a-red-hat-account-and-pull-secret" id="get-a-red-hat-account-and-pull-secret"></a>

CRC 需要一个免费的 Red Hat account 来 pull container images。

1. 如果你还没有 account，请[创建免费的 Red Hat account](https://console.redhat.com/)。
2. 在 [console.redhat.com/openshift/create/local](https://console.redhat.com/openshift/create/local) 中，点击 **Download OpenShift Local**。
3. 选择 **Linux**，并将 `.tar.xz` 文件下载到 `~/Downloads`。
4. 在 Red Hat console 的同一页面中，点击 **Copy pull secret**。把它粘贴到文本文件中并保存，稍后使用。

### 安装 CRC <a href="#install-crc" id="install-crc"></a>

在 Downloads folder 中打开 terminal。

```shell
cd ~/Downloads
```

解压 archive。

```shell
tar xf crc-linux-amd64.tar.xz
```

将 `crc` binary 移到 system-wide location，这样任何 terminal 都可以使用：

```shell
sudo mv crc-*-linux-amd64/crc /usr/local/bin/
```

验证安装：

```shell
crc version
```

Terminal 中应打印 version number。

### 安装 Helm <a href="#install-helm" id="install-helm"></a>

Helm 会把 n8n 和 supporting services 安装到 cluster 中：

```shell
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

验证：

```shell
helm version
```

### 设置环境变量 <a href="#set-environment-variables" id="set-environment-variables"></a>

```shell
export NAMESPACE=n8n-$(date +%Y%m%d)
echo "Namespace:$NAMESPACE"
```

{% hint style="info" %}
**变量持久性**

这些变量只在当前 terminal session 中有效。每次打开新 terminal 后，请在继续前重新运行这一行。
{% endhint %}

## 启动 OpenShift Local <a href="#start-openshift-local" id="start-openshift-local"></a>

### 运行 CRC setup <a href="#run-crc-setup" id="run-crc-setup"></a>

你只需要运行一次。它会配置 KVM networking、检查 system requirements，并下载 CRC bundle（约 2.5 GB）：

```shell
crc setup
```

这需要几分钟。如果它报告缺少 package，请使用 `sudo apt install -y <package-name>` 安装，然后重新运行。

### 配置 CRC memory 并启动 cluster <a href="#configure-crc-memory-and-start-the-cluster" id="configure-crc-memory-and-start-the-cluster"></a>

CRC 默认给它的 VM 分配 9 GB RAM。n8n 和 supporting services 需要更多 headroom。启动前将 memory 设置为 14 GB：

```shell
crc config set memory 14336
```

你只需要运行一次。此设置会在 `crc stop` / `crc start` cycles 之间保留。

**推荐：** 先把 pull secret 保存到文件中，这样就不必每次都粘贴：

```shell
# Open the file, paste your pull secret (from earlier), then Ctrl+O to save, Ctrl+X to exit <a href="#open-the-file-paste-your-pull-secret-from-earlier-then-ctrlo-to-save-ctrlx-to-exit" id="open-the-file-paste-your-pull-secret-from-earlier-then-ctrlo-to-save-ctrlx-to-exit"></a>
nano ~/pull-secret.txt

# Restrict permissions so only you can read it <a href="#restrict-permissions-so-only-you-can-read-it" id="restrict-permissions-so-only-you-can-read-it"></a>
chmod 600 ~/pull-secret.txt
```

使用文件启动 CRC：

```shell
crc start --pull-secret-file ~/pull-secret.txt
```

或者不带 flag 运行 `crc start`，并在提示时粘贴 secret。

**这需要 10-15 分钟。** 完成后你会看到类似输出：

```
Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: <generated-password>

Log in as user:
  Username: developer
  Password: developer
```

**现在保存 `kubeadmin` password。** 下一步会用到它。你也可以稍后使用 `crc console --credentials` 取回。

### 验证 DNS resolution <a href="#verify-dns-resolution" id="verify-dns-resolution"></a>

在 Ubuntu 上，CRC 会通过 NetworkManager 和 systemd-resolved 自动配置 system resolver。不需要手动添加 `/etc/hosts` entries。

验证 API 可访问：

```shell
sudo ss -tlnp | grep 6443
```

你应该看到某个 process 绑定到 `127.0.0.1:6443`。如果没有任何输出，请重新运行 `crc start`。如果 DNS 无法解析 `*.apps-crc.testing`，请查看 troubleshooting section。

### 配置 shell <a href="#configure-your-shell" id="configure-your-shell"></a>

CRC 在 VM 内附带 `oc` CLI。此命令会让它在你的 terminal 中可用：

```shell
eval $(crc oc-env)
```

如果要让设置永久生效，避免每次打开 terminal 都运行它：

```shell
echo 'eval $(crc oc-env)' >> ~/.bashrc
source ~/.bashrc
```

验证 `oc` 可用：

```shell
oc version
```

### 登录 cluster <a href="#log-in-to-the-cluster" id="log-in-to-the-cluster"></a>

```shell
oc login -u kubeadmin -p <your-kubeadmin-password> https://api.crc.testing:6443
```

将 `<your-kubeadmin-password>` 替换为你[配置 CRC memory 并启动 cluster](#configure-crc-memory-and-start-the-cluster) 时打印的 password。

验证你已登录：

```shell
oc whoami
```

屏幕上应打印 `kubeadmin`。

## Standalone 部署 <a href="#standalone-deployment" id="standalone-deployment"></a>

Standalone mode 会以单个 pod 和 SQLite 运行 n8n。不需要 external database 或 Redis。这很适合在本地探索 n8n 并测试 workflows。

### 创建 project <a href="#create-the-project" id="create-the-project"></a>

在 OpenShift 中，**project** 等同于 Kubernetes namespace：它是资源的隔离空间：

```shell
oc new-project $NAMESPACE
```

### 授予所需 security permission <a href="#grant-the-required-security-permission" id="grant-the-required-security-permission"></a>

OpenShift 会强制执行严格的 security policies，称为 **Security Context Constraints (SCCs)**。默认情况下，pods 不能以特定 user ID 运行。n8n chart 以 user ID `1000` 运行，因此你必须显式允许它。

使用完整显式形式。`-z` shorthand flag 在某些 OpenShift versions 中可能 silent fail：

```shell
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n
```

验证 binding 已创建：

```shell
oc get rolebindings -n $NAMESPACE
```

你应该看到引用 `system:openshift:scc:anyuid` 的 binding。

### 创建所需 secret <a href="#create-the-required-secret" id="create-the-required-secret"></a>

```shell
oc create secret generic n8n-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$(openssl rand -hex 32)" \
  --from-literal=N8N_HOST="localhost" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http"
```

**立即备份 encryption key：**

```shell
oc get secret n8n-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode
```

复制该输出并安全保存。丢失它意味着 workflows 中所有已存储 credentials 将永久不可读。

### 创建 values 文件 <a href="#create-your-values-file" id="create-your-values-file"></a>

创建名为 `n8n-standalone-values.yaml` 的文件。你可以使用 `nano`（一个简单的 text editor）：

```shell
nano n8n-standalone-values.yaml
```

粘贴以下内容，然后按 `Ctrl+O` 保存，按 `Ctrl+X` 退出：

```yaml
# n8n-standalone-values.yaml <a href="#n8n-standalone-valuesyaml" id="n8n-standalone-valuesyaml"></a>
# Single pod, SQLite database, no external dependencies. <a href="#single-pod-sqlite-database-no-external-dependencies" id="single-pod-sqlite-database-no-external-dependencies"></a>

queueMode:
  enabled: false

database:
  type: sqlite
  useExternal: false

redis:
  enabled: false

# PVC stores the SQLite database file. <a href="#pvc-stores-the-sqlite-database-file" id="pvc-stores-the-sqlite-database-file"></a>
persistence:
  enabled: true
  size: 5Gi
  # No storageClassName needed — CRC provides a default storage provisioner.

secretRefs:
  existingSecret: "n8n-secrets"

service:
  type: ClusterIP
  port: 5678

# OpenShift: securityContext must be enabled so the pod runs as UID 1000 (node user) <a href="#openshift-securitycontext-must-be-enabled-so-the-pod-runs-as-uid-1000-node-user" id="openshift-securitycontext-must-be-enabled-so-the-pod-runs-as-uid-1000-node-user"></a>
# with fsGroup 1000 (so the PVC is writable). The anyuid SCC granted above <a href="#with-fsgroup-1000-so-the-pvc-is-writable-the-anyuid-scc-granted-above" id="with-fsgroup-1000-so-the-pvc-is-writable-the-anyuid-scc-granted-above"></a>
# allows this. The seccompProfile line is removed from the chart template in <a href="#allows-this-the-seccompprofile-line-is-removed-from-the-chart-template-in" id="allows-this-the-seccompprofile-line-is-removed-from-the-chart-template-in"></a>
# "Deploy n8n" because OpenShift 4.14+ rejects it even with anyuid. <a href="#deploy-n8n-because-openshift-414-rejects-it-even-with-anyuid" id="deploy-n8n-because-openshift-414-rejects-it-even-with-anyuid"></a>
securityContext:
  enabled: true

resources:
  main:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: "1"
      memory: 1Gi

config:
  timezone: UTC
```

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

n8n Helm chart 在 pod spec 中 hard codes `seccompProfile: RuntimeDefault`。OpenShift 4.14+ 会把它转换为 deprecated alpha annotation，即使已授予 `anyuid` SCC，也会在 admission 时被拒绝。修复方法是把 chart pull 到本地，移除这两行，然后从 patched copy 安装。

**Pull 并 patch chart：**

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Confirm the lines are gone (should return no output) <a href="#confirm-the-lines-are-gone-should-return-no-output" id="confirm-the-lines-are-gone-should-return-no-output"></a>
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml
```

**从 patched chart 安装：**

```shell
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml \
  --wait \
  --timeout 10m
```

### 使用 port forward 访问 n8n <a href="#access-n8n-using-port-forward" id="access-n8n-using-port-forward"></a>

OpenShift Routes 需要 hostname，这会增加 standalone local access 的复杂度。Port-forward 更简单：

```shell
oc port-forward service/n8n-main --namespace $NAMESPACE 5678:5678
```

保持此命令运行，然后在 browser 中打开：

```
http://localhost:5678
```

n8n 会提示你创建 owner account。

{% hint style="info" %}
**停止 tunnel**

按 `Ctrl+C` 停止 tunnel。之后如需再次访问 n8n，请重新运行 `port-forward` command。
{% endhint %}

### 检查 deployment status <a href="#check-deployment-status" id="check-deployment-status"></a>

```shell
oc get pods -n $NAMESPACE
```

预期：

```
NAME                       READY   STATUS    RESTARTS   AGE
n8n-main-7d9f8b-xxxx       1/1     Running   0          3m
```

**Standalone deployment 完成。**

## Multi-instance queue mode <a href="#multi-instance-queue-mode" id="multi-instance-queue-mode"></a>

Multi-instance queue mode 使用 shared database、message queue 和 object storage 运行多个 n8n pods。它需要 [n8n Enterprise license](https://n8n.io/pricing/)。

本指南不使用 AWS managed services，而是使用 cluster 内等价服务，模拟 on-premises 或客户 OpenShift environment 中会见到的内容：

| AWS Service | 本地等价服务 |
| --- | --- |
| RDS PostgreSQL | PostgreSQL (Bitnami Helm chart) |
| ElastiCache Redis | Redis (Bitnami Helm chart) |
| S3 | MinIO（S3-compatible, Bitnami Helm chart） |

### 安装 in-cluster services <a href="#install-in-cluster-services" id="install-in-cluster-services"></a>

#### 创建 Project 并添加 Bitnami Helm repo <a href="#create-the-project-and-add-bitnami-helm-repo" id="create-the-project-and-add-bitnami-helm-repo"></a>

```shell
oc new-project $NAMESPACE
```

添加 Bitnami chart repository（只需要一次）：

```shell
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

#### 安装 PostgreSQL <a href="#install-postgresql" id="install-postgresql"></a>

在下面的命令中，将 `YourStrongPassword123` 替换为合适的复杂 password。

```shell
helm install postgresql bitnami/postgresql \
  --namespace $NAMESPACE \
  --set auth.username=n8n \
  --set auth.password='YourStrongPassword123' \
  --set auth.database=n8n_enterprise \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

{% hint style="info" %}
**Flag**

`global.compatibility.openshift.adaptSecurityContext=auto` flag 会告诉 Bitnami 让 OpenShift 自动分配正确 user ID（避免 SCC errors）。
{% endhint %}

保存 endpoint，因为 in-cluster services 的 endpoint 是固定的：

```
postgresql.YOUR_NAMESPACE.svc.cluster.local
```

将 `YOUR_NAMESPACE` 替换为你的实际 `$NAMESPACE` 值（例如 `n8n-20260306`）。

#### 安装 Redis <a href="#install-redis" id="install-redis"></a>

```shell
helm install redis bitnami/redis \
  --namespace $NAMESPACE \
  --set auth.enabled=false \
  --set architecture=standalone \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

Redis endpoint：`redis-master.$NAMESPACE.svc.cluster.local`

#### 安装 MinIO（S3-compatible storage） <a href="#install-minio-s3-compatible-storage" id="install-minio-s3-compatible-storage"></a>

在下面的命令中，将 `MinioStrongPassword123` 替换为合适的复杂 password。

```shell
helm install minio bitnami/minio \
  --namespace $NAMESPACE \
  --set auth.rootUser=minioadmin \
  --set auth.rootPassword='MinioStrongPassword123' \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

MinIO endpoint：`http://minio:9000`（在同一 namespace 内，只使用 service name 即可）

#### 在 MinIO 中创建 n8n storage bucket <a href="#create-the-n8n-storage-bucket-in-minio" id="create-the-n8n-storage-bucket-in-minio"></a>

MinIO 需要先创建 bucket，n8n 才能使用。使用 MinIO web console：

**打开 MinIO console：**

```shell
oc port-forward svc/minio 9001:9001 -n $NAMESPACE
```

保持此命令运行，然后在 browser 中打开 `http://localhost:9001`。

使用以下信息登录：
- **Username:** `minioadmin`
- **Password:** `MinioStrongPassword123`

在 console 中：
1. 点击左侧 sidebar 中的 **Buckets** -> **Create Bucket**
2. **Bucket Name:** `n8n-data`
3. 点击 **Create Bucket**

回到 terminal，按 `Ctrl+C` 停止 port-forward。

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

#### 为 n8n 授予 SCC <a href="#grant-scc-for-n8n" id="grant-scc-for-n8n"></a>

```shell
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n-enterprise
```

验证 `oc get rolebindings -n $NAMESPACE` 显示了 `system:openshift:scc:anyuid` 的 binding。

#### 创建所需 secrets <a href="#create-required-secrets" id="create-required-secrets"></a>

```shell
# Core n8n secrets <a href="#core-n8n-secrets" id="core-n8n-secrets"></a>
oc create secret generic n8n-enterprise-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$(openssl rand -hex 32)" \
  --from-literal=N8N_HOST="localhost" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http"
```

**立即备份 encryption key：**

```shell
oc get secret n8n-enterprise-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode
```

将该值安全保存。

在下面的命令中，将 `YourStrongPassword123` 和 `MinioStrongPassword123` 替换为前面步骤中使用的 passwords。

```shell
# Database password (must match what you set when installing PostgreSQL) <a href="#database-password-must-match-what-you-set-when-installing-postgresql" id="database-password-must-match-what-you-set-when-installing-postgresql"></a>
oc create secret generic n8n-enterprise-db-secret \
  --namespace $NAMESPACE \
  --from-literal=password='YourStrongPassword123'

# MinIO credentials <a href="#minio-credentials" id="minio-credentials"></a>
oc create secret generic n8n-minio-secret \
  --namespace $NAMESPACE \
  --from-literal=root-password='MinioStrongPassword123'
```

#### 创建 values 文件 <a href="#create-values-file" id="create-values-file"></a>

创建 `n8n-multimain-ocp-values.yaml`。替换标记为 `# <-- REPLACE` 的 **3 个 placeholder values**：

```shell
nano n8n-multimain-ocp-values.yaml
```

```yaml
# n8n-multimain-ocp-values.yaml <a href="#n8n-multimain-ocp-valuesyaml" id="n8n-multimain-ocp-valuesyaml"></a>
# Multi-instance queue mode for OpenShift Local (CRC). <a href="#multi-instance-queue-mode-for-openshift-local-crc" id="multi-instance-queue-mode-for-openshift-local-crc"></a>
# Uses in-cluster PostgreSQL, Redis, and MinIO instead of AWS services. <a href="#uses-in-cluster-postgresql-redis-and-minio-instead-of-aws-services" id="uses-in-cluster-postgresql-redis-and-minio-instead-of-aws-services"></a>
# Requires Enterprise license. <a href="#requires-enterprise-license" id="requires-enterprise-license"></a>

# --- Enterprise license --- <a href="#enterprise-license" id="enterprise-license"></a>
license:
  enabled: true
  activationKey: "your-enterprise-license-key-here"  # <-- REPLACE

# --- Multi-main: 2 replicas (reduced for local resources) --- <a href="#multi-main-2-replicas-reduced-for-local-resources" id="multi-main-2-replicas-reduced-for-local-resources"></a>
multiMain:
  enabled: true
  replicas: 2

# --- Queue mode: 2 worker pods --- <a href="#queue-mode-2-worker-pods" id="queue-mode-2-worker-pods"></a>
queueMode:
  enabled: true
  workerReplicaCount: 2
  workerConcurrency: 5

# --- Webhook processors --- <a href="#webhook-processors" id="webhook-processors"></a>
webhookProcessor:
  enabled: true
  replicaCount: 1
  disableProductionWebhooksOnMainProcess: true

# --- PostgreSQL (in-cluster) --- <a href="#postgresql-in-cluster" id="postgresql-in-cluster"></a>
database:
  type: postgresdb
  useExternal: true
  host: "postgresql.YOUR_NAMESPACE.svc.cluster.local"   # <-- REPLACE YOUR_NAMESPACE
  port: 5432
  database: n8n_enterprise
  schema: "public"
  user: n8n
  passwordSecret:
    name: "n8n-enterprise-db-secret"
    key: "password"

# --- Redis (in-cluster, no TLS) --- <a href="#redis-in-cluster-no-tls" id="redis-in-cluster-no-tls"></a>
redis:
  enabled: true
  useExternal: true
  host: "redis-master.YOUR_NAMESPACE.svc.cluster.local"  # <-- REPLACE YOUR_NAMESPACE
  port: 6379
  tls: false

# --- MinIO (S3-compatible, in-cluster) --- <a href="#minio-s3-compatible-in-cluster" id="minio-s3-compatible-in-cluster"></a>
s3:
  enabled: true
  bucket:
    name: "n8n-data"
    region: "us-east-1"
  host: "http://minio:9000"
  auth:
    autoDetect: false
    accessKeyId: "minioadmin"
    secretAccessKeySecret:
      name: "n8n-minio-secret"
      key: "root-password"
  storage:
    mode: "s3"
    availableModes: "filesystem,s3"
  forcePathStyle: true

# --- Service account --- <a href="#service-account" id="service-account"></a>
serviceAccount:
  create: true
  name: n8n
```

保存并退出 nano（`Ctrl+O`、`Ctrl+X`）。

**部署前**，将两个 `YOUR_NAMESPACE` placeholders 替换为你的实际 namespace 值：

```shell
# Check your namespace value <a href="#check-your-namespace-value" id="check-your-namespace-value"></a>
echo $NAMESPACE

# Replace in the file (this edits it automatically) <a href="#replace-in-the-file-this-edits-it-automatically" id="replace-in-the-file-this-edits-it-automatically"></a>
sed -i "s/YOUR_NAMESPACE/$NAMESPACE/g" n8n-multimain-ocp-values.yaml
```

验证替换：

```shell
grep "svc.cluster.local" n8n-multimain-ocp-values.yaml
```

两行都应显示你的实际 namespace name，而不是 `YOUR_NAMESPACE`。

#### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

如果你之前没有 patch chart，现在 pull 并 patch：

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml  # should return nothing
```

从 patched chart 安装：

```shell
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-multimain-ocp-values.yaml \
  --wait \
  --timeout 15m
```

#### 创建 external access route <a href="#create-a-route-for-external-access" id="create-a-route-for-external-access"></a>

在 OpenShift 中，**Route** 会把 service 暴露给外部世界。它等价于 Kubernetes Ingress 或 LoadBalancer，并且不需要额外 controller：

```shell
oc expose svc/n8n-main -n $NAMESPACE
```

获取 URL：

```shell
export ROUTE=$(oc get route n8n-main -n $NAMESPACE -o jsonpath='{.spec.host}')
echo "n8n URL: http://$ROUTE"
```

URL 看起来类似：`http://n8n-main-n8n-20260306.apps-crc.testing`

#### 更新 host secret <a href="#update-the-host-secret" id="update-the-host-secret"></a>

n8n 需要知道自己的 public URL。使用 Route hostname 更新 secret，然后重启 pods：

```shell
ENCRYPTION_KEY=$(oc get secret n8n-enterprise-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode)

oc create secret generic n8n-enterprise-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$ENCRYPTION_KEY" \
  --from-literal=N8N_HOST="$ROUTE" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http" \
  --dry-run=client -o yaml | oc apply -f -

oc rollout restart deployment -n $NAMESPACE
```

等待 rollout 完成：

```shell
oc rollout status deployment/n8n-main -n $NAMESPACE
```

#### 验证所有 pods 都在运行 <a href="#verify-all-pods-are-running" id="verify-all-pods-are-running"></a>

```shell
oc get pods -n $NAMESPACE
```

预期（全部为 `Running`）：

```
NAME                                    READY   STATUS    RESTARTS   AGE
n8n-main-xxxx-aaaa                      1/1     Running   0          5m
n8n-main-xxxx-bbbb                      1/1     Running   0          5m
n8n-worker-xxxx-aaaa                    1/1     Running   0          5m
n8n-worker-xxxx-bbbb                    1/1     Running   0          5m
n8n-webhook-processor-xxxx-aaaa         1/1     Running   0          5m
postgresql-0                            1/1     Running   0          15m
redis-master-0                          1/1     Running   0          15m
minio-xxxx-xxxx                         1/1     Running   0          15m
```

在 browser 中打开上面打印的 URL。

**Multi-instance deployment 完成。**

## 更新 n8n <a href="#updating-n8n" id="updating-n8n"></a>

要更改 configuration 或升级 chart version，请 pull 并重新 patch 新 chart version，然后 upgrade：

```shell
# Remove the old local chart copy <a href="#remove-the-old-local-chart-copy" id="remove-the-old-local-chart-copy"></a>
rm -rf ~/n8n/

# Pull and patch the new version <a href="#pull-and-patch-the-new-version" id="pull-and-patch-the-new-version"></a>
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version <new-version> --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Standalone <a href="#standalone" id="standalone"></a>
helm upgrade n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml

# Multi-instance <a href="#multi-instance" id="multi-instance"></a>
helm upgrade n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-multimain-ocp-values.yaml
```

## 停止并恢复 CRC <a href="#stopping-and-resuming-crc" id="stopping-and-resuming-crc"></a>

CRC 不需要在 sessions 之间删除。你可以停止并重新启动它：

```shell
# Stop the cluster (saves state) <a href="#stop-the-cluster-saves-state" id="stop-the-cluster-saves-state"></a>
crc stop

# Start it again later <a href="#start-it-again-later" id="start-it-again-later"></a>
crc start
```

重启后，重新运行：

```shell
eval $(crc oc-env)
export NAMESPACE=n8n-YYYYMMDD   # use your original date
oc login -u kubeadmin -p <password> https://api.crc.testing:6443
```

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### `crc setup` 因 “libvirt not found” 失败 <a href="#crc-setup-fails-with-libvirt-not-found" id="crc-setup-fails-with-libvirt-not-found"></a>

```shell
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients
sudo systemctl start libvirtd
```

然后重新运行 `crc setup`。

### `crc start` 因 “insufficient memory” 失败 <a href="#crc-start-fails-with-insufficient-memory" id="crc-start-fails-with-insufficient-memory"></a>

CRC 至少需要 9 GB 可用 RAM。关闭其他 applications 并重试。如果你[按照说明配置了 CRC memory](#configure-crc-memory-and-start-the-cluster)，CRC 已配置为使用 14 GB。

### n8n pod 卡在 `Pending` 或因 SCC error 从未创建 <a href="#n8n-pod-stuck-in-pending-or-never-created-scc-error" id="n8n-pod-stuck-in-pending-or-never-created-scc-error"></a>

检查 events 中的 error：

```shell
oc get events -n $NAMESPACE --sort-by='.lastTimestamp' | tail -20
```

如果你看到 `unable to validate against any security context constraint` 或 `seccomp may not be set`，说明 chart hard coded 的 `seccompProfile: RuntimeDefault` 被拒绝了。OpenShift 4.14+ 会将它转换为 deprecated alpha annotation，即使已授予 `anyuid` SCC，admission 也会拒绝。

**1. 使用显式形式授予 anyuid**（`-z` shorthand 可能 silent fail）：

```shell
# For standalone <a href="#for-standalone" id="for-standalone"></a>
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n

# For multi-instance <a href="#for-multi-instance" id="for-multi-instance"></a>
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n-enterprise
```

验证：运行 `oc get rolebindings -n $NAMESPACE`。你应该看到 `system:openshift:scc:anyuid` 的 binding。

**2. 将 chart pull 到本地，并移除 `seccompProfile` lines：**

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Confirm they're gone (should return no output) <a href="#confirm-theyre-gone-should-return-no-output" id="confirm-theyre-gone-should-return-no-output"></a>
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml
```

**3. 从 patched chart 卸载并重新安装：**

```shell
helm uninstall n8n -n $NAMESPACE
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml \
  --wait \
  --timeout 10m
```

### Route URL 返回 “Application not available” <a href="#route-url-returns-application-not-available" id="route-url-returns-application-not-available"></a>

Pods 可能仍在启动。检查：

```shell
oc get pods -n $NAMESPACE
oc rollout status deployment/n8n-main -n $NAMESPACE
```

也确认 Route 存在：

```shell
oc get route -n $NAMESPACE
```

### n8n pod 因 `Insufficient memory` 卡在 `Pending` <a href="#n8n-pod-stuck-in-pending-with-insufficient-memory" id="n8n-pod-stuck-in-pending-with-insufficient-memory"></a>

CRC node 没有足够 free memory 来 schedule pod。

**修复：** 增加 CRC VM memory 并重启：

```shell
crc stop
crc config set memory 14336
crc start
```

CRC 重启后，pod 应自动 schedule。如果几分钟后 pod 仍 pending，请删除它以强制重新 schedule：

```shell
oc delete pod -n $NAMESPACE -l app.kubernetes.io/component=main
```

如果你的机器无法腾出 14 GB，也可以降低 `n8n-standalone-values.yaml` 中 pod 的 memory request：

```yaml
resources:
  main:
    requests:
      memory: 256Mi
```

然后 upgrade：`helm upgrade n8n ~/n8n/ -n $NAMESPACE -f n8n-standalone-values.yaml`

### DNS 无法解析 `.apps-crc.testing` 或 `api.crc.testing` <a href="#dns-not-resolving-apps-crctesting-or-apicrctesting" id="dns-not-resolving-apps-crctesting-or-apicrctesting"></a>

在 Ubuntu 上，CRC 会自动配置 DNS。如果失败，请重启 NetworkManager：

```shell
sudo systemctl restart NetworkManager
```

如果仍然异常，请手动添加 entries（CRC 通过 `127.0.0.1` route traffic）：

```shell
sudo tee -a /etc/hosts <<EOF
127.0.0.1 api.crc.testing
127.0.0.1 console-openshift-console.apps-crc.testing
127.0.0.1 oauth-openshift.apps-crc.testing
127.0.0.1 default-route-openshift-image-registry.apps-crc.testing
EOF
```

{% hint style="info" %}
**Subdomains**

当你在 multi-instance section 中 expose Routes 时，会创建新的 `*.apps-crc.testing` subdomains。如果 browser 无法访问，请把它们指向 `127.0.0.1` 并加入 `/etc/hosts`。
{% endhint %}

### n8n pod 写入 `/home/node/.n8n/` 时因 `EACCES: permission denied` crash <a href="#n8n-pod-crashes-with-eacces-permission-denied-writing-to-homenoden8n" id="n8n-pod-crashes-with-eacces-permission-denied-writing-to-homenoden8n"></a>

这表示 pod 以 OpenShift 随机分配的 UID 运行，而不是 UID 1000（n8n image 期望的 `node` user）。当 values 中设置 `securityContext.enabled: false` 且没有设置 `runAsUser: 1000` 和 `fsGroup: 1000` 时会发生这种情况，OpenShift 会分配一个无法写入 PVC 的随机 UID。

**修复：** 确保 values 文件中设置了 `securityContext.enabled: true`，并且 chart 已 patch 以移除 `seccompProfile`（见上面的 SCC error section）。两者都需要。

### 查看 pod logs <a href="#view-pod-logs" id="view-pod-logs"></a>

```shell
# Main process <a href="#main-process" id="main-process"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=main --tail=50

# Workers <a href="#workers" id="workers"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=worker --tail=50

# Webhook processors <a href="#webhook-processors" id="webhook-processors"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=webhook-processor --tail=50
```

### Namespace 中的所有 events <a href="#all-events-in-the-namespace" id="all-events-in-the-namespace"></a>

```shell
oc get events -n $NAMESPACE --sort-by='.lastTimestamp'
```

## 快速参考 <a href="#quick-reference" id="quick-reference"></a>

### 重新打开 terminal 后重新 export variables <a href="#re-export-variables-after-reopening-terminal" id="re-export-variables-after-reopening-terminal"></a>

```shell
eval $(crc oc-env)
export NAMESPACE=n8n-YYYYMMDD   # use the date from your original deployment
oc login -u kubeadmin -p <password> https://api.crc.testing:6443
```

### 检查 cluster status <a href="#check-cluster-status" id="check-cluster-status"></a>

```shell
crc status
```

### 打开 OpenShift web console <a href="#open-the-openshift-web-console" id="open-the-openshift-web-console"></a>

```shell
crc console
```

使用 `kubeadmin` / 你的 password 登录，以图形方式查看所有正在运行的内容。

### 需要保存的内容 <a href="#things-to-save" id="things-to-save"></a>

| 项目 | 为什么重要 |
| --- | --- |
| `kubeadmin` password | 登录 cluster |
| n8n encryption key | 丢失它 = 所有已存储 credentials 不可读 |
| `n8n-standalone-values.yaml` | `helm upgrade` 需要 |
| `n8n-multimain-ocp-values.yaml` | `helm upgrade` 需要 |
| MinIO root password | 访问 MinIO console |
| PostgreSQL password | Database access |

## 下一步 <a href="#next-steps" id="next-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GtC2RL8itCPuNiwv5UUW/" %}
