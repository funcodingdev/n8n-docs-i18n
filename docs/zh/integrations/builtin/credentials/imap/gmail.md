---
title: Gmail
description: >-
  Gmail IMAP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Gmail IMAP 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Gmail
originalFilePath: integrations/builtin/credentials/imap/gmail.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/imap/gmail'
url: 'https://docs.n8n.io/integrations/builtin/credentials/imap/gmail'
layout:
  description:
    visible: false
---

# Gmail IMAP credentials <a href="#gmail-imap-credentials" id="gmail-imap-credentials"></a>

按照以下步骤使用 Gmail account 配置 IMAP credentials。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

要按这些说明操作，你必须先：

1. 在 Gmail account 上[启用 2-step Verification](#enable-2-step-verification)。
2. [生成 app password](#generate-an-app-password)。

### 启用 2-step Verification <a href="#enable-2-step-verification" id="enable-2-step-verification"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ysY7mHC9pN3kCUPncSi8/" %}

### 生成 app password <a href="#generate-an-app-password" id="generate-an-app-password"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/rJn9WooD0IwP7abKawNZ/" %}

## 设置 credential <a href="#set-up-the-credential" id="set-up-the-credential"></a>

要使用 Gmail account 设置 IMAP credential，请使用这些设置：

1. 将你的 Gmail email address 输入为 **User**。
2. 将上方生成的 app password 输入为 **Password**。
3. 将 `imap.gmail.com` 输入为 **Host**。
4. 对于 **Port**，保留默认端口号 `993`。如果此端口不可用，请向 email administrator 确认。
5. 开启 **SSL/TLS** toggle。
6. 向 email administrator 确认是否需要 **Allow Self-Signed Certificates**。

更多信息请参考 [Add Gmail to another client](https://support.google.com/mail/answer/7126229?hl=en)。如果你是在 2024 年 6 月之前使用个人 Google account，可能需要 **Enable IMAP**。
