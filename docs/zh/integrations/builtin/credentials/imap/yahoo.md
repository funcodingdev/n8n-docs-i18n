---
title: Yahoo
description: >-
  Yahoo IMAP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Yahoo IMAP 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Yahoo
originalFilePath: integrations/builtin/credentials/imap/yahoo.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo'
url: 'https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo'
layout:
  description:
    visible: false
---

# Yahoo IMAP credentials <a href="#yahoo-imap-credentials" id="yahoo-imap-credentials"></a>

按照以下步骤使用 Yahoo account 配置 IMAP credentials。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

要按这些说明操作，你必须先生成 app password：

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/2ZBcW11hezK8c3JZNsKm/" %}

## 设置 credential <a href="#set-up-the-credential" id="set-up-the-credential"></a>

要使用 Yahoo Mail account 设置 IMAP credential，请使用这些设置：

1. 将你的 Yahoo email address 输入为 **User**。
2. 将上方生成的 app password 输入为 **Password**。
3. 将 `imap.mail.yahoo.com` 输入为 **Host**。
4. 保留默认 **Port** number `993`。如果此端口不可用，请向 email administrator 确认。
5. 开启 **SSL/TLS** toggle。
6. 向 email administrator 确认是否需要 **Allow Self-Signed Certificates**。

更多信息请参考 [Set up IMAP for Yahoo mail account](https://help.yahoo.com/kb/sln4075.html)。
