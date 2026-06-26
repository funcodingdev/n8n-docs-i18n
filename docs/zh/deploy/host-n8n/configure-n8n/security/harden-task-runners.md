---
title: 加固 task runners
description: 加固 task runners，为你的 self-hosted n8n 实例提供更好的隔离。
contentType: howto
nodeTitle: Harden task runners
originalFilePath: hosting/securing/hardening-task-runners.md
originalUrl: 'https://docs.n8n.io/hosting/securing/hardening-task-runners'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners'
layout:
  description:
    visible: false
---

# 加固 task runners <a href="#hardening-task-runners" id="hardening-task-runners"></a>

[Task runners](../set-up-task-runners.md) 负责执行 [Code node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 中的代码。虽然 Code node executions 是安全的，但你可以遵循以下建议进一步加固 task runners。

## 以 external mode 将 task runners 作为 sidecars 运行 <a href="#run-task-runners-as-sidecars-in-external-mode" id="run-task-runners-as-sidecars-in-external-mode"></a>

为增加 core n8n process 与 Code node 中代码之间的隔离，请在 [external mode](../set-up-task-runners.md#setting-up-external-mode) 中运行 task runners。External task runners 会作为独立 containers 启动，提供完全隔离的环境来执行 Code node 中定义的 JavaScript。

## 使用 distroless image <a href="#use-the-distroless-image" id="use-the-distroless-image"></a>

为了减少 attack surface，请使用 distroless Docker image variant。Distroless images 只包含 application 及其 runtime dependencies，不包含 package managers、shells 和其他运行时不需要的 utilities。

要使用 distroless image，请在 Docker tag 后追加 `-distroless` suffix。例如：`2.4.6-distroless`。

## 以 nobody user 运行 <a href="#run-as-the-nobody-user" id="run-as-the-nobody-user"></a>

为了提高安全性，请将 task runners 配置为以非特权 `nobody` user 运行，user 和 group ID 为 65532。这会防止 container process 以 root privileges 运行，并限制安全漏洞可能造成的损害。

## 配置 read-only root filesystem <a href="#configure-read-only-root-filesystem" id="configure-read-only-root-filesystem"></a>

配置 [read-only root filesystem](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)，防止运行时修改 container filesystem。这有助于防范可能尝试修改 system files 的恶意代码。

Task runners 运行时仍需要一些临时存储。为此，请将一个最小的 `emptyDir` volume 挂载到 `/tmp`。如果你的 workflows 需要更多临时空间，请相应增加 volume 大小。

## 配置 AppArmor profile <a href="#configure-an-apparmor-profile" id="configure-an-apparmor-profile"></a>

作为 defence-in-depth 措施，请应用 [AppArmor](https://apparmor.net/) profile，防止 task runner container 读取敏感的 `/proc` files，例如 `environ` 和 `mounts`。这些文件可能向 container 内运行的代码暴露环境变量，包括 secrets 和 credentials。关于如何将 profile 应用于 pod，请参考 [Kubernetes AppArmor documentation](https://kubernetes.io/docs/tutorials/security/apparmor/)。

将以下规则添加到你的 AppArmor profile：

```
audit deny @{PROC}/[0-9]*/{environ,mounts} rwl,
```

这会拒绝并记录任何读取、写入或链接到 per-process `environ` 和 `mounts` files 的尝试。
