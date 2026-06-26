---
title: Configure n8n to use your own certificate authority
description: >-
  自定义 n8n container，使其在连接服务时可使用 self signed certificates。
contentType: howto
nodeTitle: Configure custom SSL certificate authorities
originalFilePath: hosting/configuration/configuration-examples/custom-certificate-authority.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities
layout:
  description:
    visible: false
---

# 配置 n8n 使用你自己的 certificate authority 或 self-signed certificate <a href="#configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate" id="configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate"></a>

你可以向 n8n 添加自己的 certificate authority (CA) 或 self-signed certificate。这意味着你可以信任某个特定 SSL certificate，而不是信任所有 invalid certificates，因为后者存在潜在安全风险。

{% hint style="info" %}
**1.42.0 版本新增**

此功能可用于 1.42.0 及更高版本。
{% endhint %}

要使用此功能，你需要将 certificates 放入一个 folder，并将该 folder mount 到 container 中的 `/opt/custom-certificates`。映射到 `/opt/custom-certificates` 的外部路径必须可由 container 写入。

## Docker <a href="#docker" id="docker"></a>

以下示例假设你有一个名为 `pki` 的 folder，其中包含 certificates，并且它位于运行命令的目录中，或位于 docker compose file 旁边。

### Docker CLI <a href="#docker-cli" id="docker-cli"></a>
使用 CLI 时，你可以从 command line 使用 `-v` flag：

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -v ./pki:/opt/custom-certificates \
 docker.n8n.io/n8nio/n8n
```

### Docker Compose <a href="#docker-compose" id="docker-compose"></a>

```yaml
name: n8n
services:
    n8n:
        volumes:
            - ./pki:/opt/custom-certificates
        container_name: n8n
        ports:
            - 5678:5678
        image: docker.n8n.io/n8nio/n8n
```

你还应该为导入的 certs 授予正确权限。Container 运行后可以执行此操作（假设 container name 为 n8n）：

```bash
docker exec --user 0 n8n chown -R 1000:1000 /opt/custom-certificates
```

## Custom Trust Store 的 certificate 要求 <a href="#certificate-requirements-for-custom-trust-store" id="certificate-requirements-for-custom-trust-store"></a>

支持的 certificate types：

- Root CA Certificates：由 Certificate Authorities 签发并用于签署其他 certificates 的 certificates。信任这些 certificates 即接受该 CA 签署的所有 certificates。
- Self-Signed Certificates：servers 自行创建并签名的 certificates。信任这些 certificates 只会接受连接到该特定 server。

你必须使用 PEM format：

- 带 BEGIN/END markers 的 text-based format
- 支持的 file extensions：`.pem`、`.crt`、`.cer`
- 包含 public certificate（不需要 private key）

例如：

```
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKoK/heBjcOuMA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV
[base64 encoded data]
-----END CERTIFICATE-----
```

系统不接受：

- DER/binary format files
- PKCS#7 (.p7b) files
- PKCS#12 (.pfx, .p12) files
- Private key files
- 使用前请将这些 formats 转换为 PEM。
