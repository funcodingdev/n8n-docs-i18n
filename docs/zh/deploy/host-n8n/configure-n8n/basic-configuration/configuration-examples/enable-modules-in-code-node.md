---
title: Enable modules in Code node
description: 允许在 Code node 中使用 built-in 和 external modules。
contentType: howto
nodeTitle: Enable modules in Code node
originalFilePath: hosting/configuration/configuration-examples/modules-in-code-node.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node
layout:
  description:
    visible: false
---

# 在 Code node 中启用 modules <a href="#enable-modules-in-code-node" id="enable-modules-in-code-node"></a>

出于安全原因，Code node 会限制 importing modules。可以通过设置以下环境变量解除 built-in 和 external modules 的限制：

- `NODE_FUNCTION_ALLOW_BUILTIN`：用于 built-in modules
- `NODE_FUNCTION_ALLOW_EXTERNAL`：用于来自 n8n/node_modules directory 的 external modules。未设置环境变量时，external module support 会被禁用。

```bash
# Allows usage of all builtin modules <a href="#allows-usage-of-all-builtin-modules" id="allows-usage-of-all-builtin-modules"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=*

# Allows usage of only crypto <a href="#allows-usage-of-only-crypto" id="allows-usage-of-only-crypto"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=crypto

# Allows usage of only crypto and fs <a href="#allows-usage-of-only-crypto-and-fs" id="allows-usage-of-only-crypto-and-fs"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=crypto,fs

# Allow usage of external npm modules. <a href="#allow-usage-of-external-npm-modules" id="allow-usage-of-external-npm-modules"></a>
export NODE_FUNCTION_ALLOW_EXTERNAL=moment,lodash
```
{% hint style="info" %}
**如果使用 Task Runners**

如果 n8n instance 已设置 [Task Runners](../../set-up-task-runners.md)，请将环境变量添加到 Task Runners，而不是 main n8n node。
{% endhint %}

有关这些变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/nodes.md)。
