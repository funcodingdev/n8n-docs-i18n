---
title: SSH credentials
description: >-
  SSH credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SSH 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: SSH credentials
originalFilePath: integrations/builtin/credentials/ssh.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ssh'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ssh'
layout:
  description:
    visible: false
---

# SSH credentials <a href="#ssh-credentials" id="ssh-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SSH](../core-nodes/n8n-nodes-base.ssh.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个启用了 SSH 的 remote server。
- 创建一个可以通过以下任一方式 `ssh` 到 server 的 user account：
    - 用户自己的 [password](#using-password)
    - SSH [private key](#using-private-key)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [Password](#using-password)：如果你有一个可以使用自己 password `ssh` 到 server 的 user account，请使用此方式。
- [Private key](#using-private-key)：如果你有一个为该 server 或 service 使用 SSH key 的 user account，请使用此方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Secure Shell (SSH) protocol 是一种通过网络安全发送命令的方法。SSH 设置示例请参考 [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)。


## 使用 password <a href="#using-password" id="using-password"></a>

如果你有一个可以使用自己 password `ssh` 到 server 的 user account，请使用此方式。

要配置此 credential，你需要：

1. 将要连接的 server IP address 输入为 **Host**。
2. 输入连接要使用的 **Port**。SSH 默认使用 port `22`。
3. 输入在该 server 上拥有 `ssh` 访问权限的 user account 的 **Username**。
4. 输入该 user account 的 **Password**。

## 使用 private key <a href="#using-private-key" id="using-private-key"></a>

如果你有一个为该 server 或 service 使用 SSH key 的 user account，请使用此方式。

要配置此 credential，你需要：

1. 将要连接的 server IP address 输入为 **Host**。
2. 输入连接要使用的 **Port**。SSH 默认使用 port `22`。
3. 输入生成 private key 的 account 的 **Username**。
4. 输入你的 SSH **Private Key** 的完整内容。
5. 如果你为 **Private Key** 创建了 **Passphrase**，请输入该 passphrase。
    - 如果你没有为 key 创建 passphrase，请留空。
