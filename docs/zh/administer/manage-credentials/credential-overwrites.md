---
title: Credential overwrites
description: >-
  在 self-hosted n8n instance 上全局设置 credential data，让 users 无需看到或输入 client secrets 即可完成
  authentication。
contentType: howto
nodeTitle: Credential overwrites
originalFilePath: hosting/configuration/credential-overwrites.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/credential-overwrites'
url: 'https://docs.n8n.io/administer/manage-credentials/credential-overwrites'
layout:
  description:
    visible: false
---

# Credential overwrites <a href="#credential-overwrites" id="credential-overwrites"></a>

Credential overwrites 让你可以全局设置 credential data。这些 data 对 users 不可见，但 n8n 会在后台自动使用它们。例如，可以在不暴露 client secrets 的情况下，通过 "Connect" button 启用 OAuth login。

在 Editor UI 中，n8n 默认隐藏所有 overwritten fields，因此 users 可以在 credential 上使用 "Connect" button 通过 OAuth 进行 authentication。

用于配置 credential overwrites 的 environment variables，请参考 [Credentials environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials)。

## 使用 environment variables <a href="#using-environment-variables" id="using-environment-variables"></a>

将 `CREDENTIALS_OVERWRITE_DATA` 设置为 `{ CREDENTIAL_NAME: { PARAMETER: VALUE }}`。

{% hint style="warning" %}
不建议使用此方式。Environment variables 在 n8n 中不受保护，因此 data 可能泄露给 users。
{% endhint %}

## 使用 REST API <a href="#using-the-rest-api" id="using-the-rest-api"></a>

推荐方式是使用 custom REST endpoint 加载 data。

1. 将 `CREDENTIALS_OVERWRITE_ENDPOINT` 设置为 endpoint 应可访问的 path：<br>

    ```sh
    export CREDENTIALS_OVERWRITE_ENDPOINT=send-credentials
    ```

    可选：设置 `CREDENTIALS_OVERWRITE_ENDPOINT_AUTH_TOKEN`，要求访问 endpoint 时使用 bearer token。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>如果没有 auth token，出于安全原因，该 endpoint 只能被调用一次。</p></div>

2. 准备一个包含要 overwrite credentials 的 JSON file。例如，为 Asana 和 GitHub 创建 `oauth-credentials.json`：

    ```json
    {
        "asanaOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        },
        "githubOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        }
    }
    ```

3. 将 file 发送到你的 n8n instance：

    ```sh
    curl -H "Content-Type: application/json" --data @oauth-credentials.json http://localhost:5678/send-credentials
    ```

    如果 `CREDENTIALS_OVERWRITE_ENDPOINT_AUTH_TOKEN` 设置为 `secure-token`：

    ```sh
    curl -H "Content-Type: application/json" -H "Authorization: Bearer secure-token" --data @oauth-credentials.json http://localhost:5678/send-credentials
    ```

{% hint style="info" %}
Credentials 可以 extend other credentials。例如，`googleSheetsOAuth2Api` extends `googleOAuth2Api`。你可以在 parent（`googleOAuth2Api`）上设置 parameters，所有 child credentials 都会使用它们。
{% endhint %}

## Persistence <a href="#persistence" id="persistence"></a>

要将 credential overwrites 存储在 database 中，并在 multi-instance 或 queue mode 中将它们 propagate 到所有 workers，请启用：

```sh
export CREDENTIALS_OVERWRITE_PERSISTENCE=true
```

启用后，n8n 会将 encrypted overwrites 存储在 `settings` table 中，并 broadcast 一个 `reload-overwrite-credentials` event，让 workers reload 最新 values。禁用时，overwrites 会保留在加载它们的 process memory 中，n8n 不会将它们 propagate 到 workers，也不会在 restarts 后保留它们。
