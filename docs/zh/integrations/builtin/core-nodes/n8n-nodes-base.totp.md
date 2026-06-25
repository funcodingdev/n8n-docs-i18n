---
title: TOTP
description: >-
  n8n 中 TOTP node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
nodeTitle: TOTP
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.totp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp'
layout:
  description:
    visible: false
---

# TOTP <a href="#totp" id="totp"></a>

TOTP node 提供了一种生成 TOTP（基于时间的一次性密码）的方式。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [TOTP credentials](../credentials/totp.md)。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

使用这些参数配置此 node。

### Credential to connect with <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建此 node 要使用的 [TOTP credential](../credentials/totp.md)。

### Operation <a href="#operation" id="operation"></a>

**Generate Secret** 是当前唯一支持的操作。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些 **Options** 进一步配置此 node。

### Algorithm <a href="#algorithm" id="algorithm"></a>

选择要使用的 HMAC hashing algorithm。默认值为 SHA1。

### Digits <a href="#digits" id="digits"></a>

输入生成代码中的位数。默认值为 `6`。

### Period <a href="#period" id="period"></a>

输入 TOTP 有效的秒数。默认值为 `30`。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 TOTP 集成模板](https://n8n.io/integrations/totp)或[搜索所有模板](https://n8n.io/workflows/)
