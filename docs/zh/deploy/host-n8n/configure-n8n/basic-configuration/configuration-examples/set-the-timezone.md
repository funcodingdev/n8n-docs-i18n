---
title: Set the self-hosted instance timezone
description: 更改自托管 n8n instance 的默认时区。
contentType: howto
nodeTitle: Set the timezone
originalFilePath: hosting/configuration/configuration-examples/time-zone.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/time-zone'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone
layout:
  description:
    visible: false
---

# 设置自托管 instance 时区 <a href="#set-the-self-hosted-instance-timezone" id="set-the-self-hosted-instance-timezone"></a>

默认时区是 America/New_York。例如，Schedule node 使用它来确定 workflow 应该在什么时间启动。要设置不同的默认时区，请将 `GENERIC_TIMEZONE` 设置为相应值。例如，如果你想将时区设置为 Berlin (Germany)：

```bash
export GENERIC_TIMEZONE=Europe/Berlin
```

你可以在[这里](https://momentjs.com/timezone/)找到你的时区名称。

有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/timezone-and-localization.md)。
