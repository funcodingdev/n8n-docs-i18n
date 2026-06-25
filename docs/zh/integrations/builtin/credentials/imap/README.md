---
title: IMAP credentials
description: >-
  IMAP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  IMAP 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: IMAP
originalFilePath: integrations/builtin/credentials/imap/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/imap'
url: 'https://docs.n8n.io/integrations/builtin/credentials/imap'
layout:
  description:
    visible: false
---

# IMAP credentials <a href="#imap-credentials" id="imap-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [IMAP Email](../../core-nodes/n8n-nodes-base.emailimap.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在支持 IMAP 的服务上创建一个 email account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- User account

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Internet Message Access Protocol (IMAP) 是接收 email 的标准协议。大多数 email providers 都提供使用 IMAP 设置其服务的说明；请参考你的 provider 的 IMAP instructions。

## 使用 user account <a href="#using-user-account" id="using-user-account"></a>

要配置此 credential，你需要：

- **User** name：你要检索 email 的 email address。
- **Password**：用于查看 email 的 password 或 app password。你的 provider 会说明应使用自己的 password，还是生成 app password。
- **Host**：你的 email provider 的 IMAP host address，通常格式为 `imap.<provider>.com`。请向你的 provider 确认。
- **Port** number：默认端口为 `993`。除非 provider 或 email administrator 要求使用其他端口，否则请使用此端口。

选择是否使用 **SSL/TLS**，以及是否 **Allow Self-Signed Certificates**。

### Provider instructions <a href="#provider-instructions" id="provider-instructions"></a>

请参考这些常见 email providers 的 quickstart guides。

#### Gmail <a href="#gmail" id="gmail"></a>

请参考 [Gmail](gmail.md)。

#### Outlook.com <a href="#outlookcom" id="outlookcom"></a>

请参考 [Outlook.com](outlook.md)。

#### Yahoo <a href="#yahoo" id="yahoo"></a>

请参考 [Yahoo](yahoo.md)。

### 我的 provider 未列出 <a href="#my-provider-isnt-listed" id="my-provider-isnt-listed"></a>

如果这里未列出你的 email provider，请搜索其 `IMAP settings` 或 `IMAP instructions`。
