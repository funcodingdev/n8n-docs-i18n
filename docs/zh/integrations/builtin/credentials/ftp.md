---
title: FTP credentials
description: >-
  FTP credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 FTP。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: FTP credentials
originalFilePath: integrations/builtin/credentials/ftp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ftp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ftp'
layout:
  description:
    visible: false
---

# FTP credentials <a href="#ftp-credentials" id="ftp-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [FTP](../core-nodes/n8n-nodes-base.ftp.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 File Transfer Protocol (FTP) server 上创建账号，例如 [JSCAPE](https://mft.jscape.com/lp/ftp-server)、[OpenSSH](https://www.openssh.com/) 或 [FileZilla Server](https://filezilla-project.org/)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **FTP account**：如果你的 FTP server 不支持 SSH tunneling 或 encrypted connections，请使用此方法。
- **SFTP account**：如果你的 FTP server 支持 SSH tunneling 和 encrypted connections，请使用此方法。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

File Transfer Protocol (FTP) 和 Secure Shell File Transfer Protocol (SFTP) 是用于在 FTP/SFTP client 和 server 之间直接传输 files 的 protocols。

## 使用 FTP account <a href="#using-ftp-account" id="using-ftp-account"></a>

如果你的 FTP server 不支持 SSH tunneling 或 encrypted connections，请使用此方法。

要配置此 credential，你需要：

1. 输入 FTP server 的 **Host** 名称或 IP address。
2. 输入连接应使用的 **Port** number。
3. 输入 credential 应连接为的 **Username**。
4. 输入该 user 的 **Password**。

请查看 FTP server provider 的文档，以了解获取所需信息的说明。

## 使用 SFTP account <a href="#using-sftp-account" id="using-sftp-account"></a>

如果你的 FTP server 支持 SSH tunneling 和 encrypted connections，请使用此方法。

要配置此 credential，你需要：

1. 输入 FTP server 的 **Host** 名称或 IP address。
2. 输入连接应使用的 **Port** number。
3. 输入 credential 应连接为的 **Username**。
4. 输入该 user 的 **Password**。
5. 对于 **Private Key**，输入用于 key-based 或 host-based user authentication 的字符串
    - 以 OpenSSH format 输入你的 Private Key。这通常使用 ssh-keygen 的 `-o` 参数生成，例如：`ssh-keygen -o -a 100 -t ed25519`。
6. 如果 **Private Key** 已加密，请输入用于解密它的 **Passphrase**。
    - 如果 **Private Key** 未使用 passphrase，请将此字段留空。

请查看 FTP server provider 的文档，以了解获取所需信息的说明。
