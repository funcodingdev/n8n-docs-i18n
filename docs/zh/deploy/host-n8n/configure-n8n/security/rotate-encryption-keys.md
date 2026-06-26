---
title: Encryption key 轮换
description: >-
  启用并轮换用于保护 self-hosted n8n 实例上 credentials 和其他 sensitive data 的 data encryption key。
contentType: howto
nodeTitle: Rotate encryption keys
originalFilePath: hosting/securing/encryption-key-rotation.md
originalUrl: 'https://docs.n8n.io/hosting/securing/encryption-key-rotation'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys
layout:
  description:
    visible: false
---

# Encryption key 轮换 <a href="#encryption-key-rotation" id="encryption-key-rotation"></a>

{% hint style="info" %}
**功能可用性**

* 仅 self-hosted n8n instances 可用。
* 你需要是 instance owner，才能启用此功能并轮换 keys。
{% endhint %}

Encryption key 轮换让你可以定期替换用于加密 n8n data 的 key，例如 credentials、OAuth tokens 和其他 sensitive content，而不必更改实例的 master encryption key。

## Encryption key 轮换如何工作 <a href="#how-encryption-key-rotation-works" id="how-encryption-key-rotation-works"></a>

n8n 使用两层 key model：

* **Instance encryption key** (`N8N_ENCRYPTION_KEY`)：你的 master key，在部署时设置。此 key 永不更改。n8n 只用它来保护 data encryption keys。
* **Data encryption key**：直接加密 credential data 的 key。这是你要轮换的 key。n8n 将它加密后存储在 database 中，并由 instance key 保护。

轮换时，n8n 会生成新的 data encryption key，并将其用于所有未来写入。使用旧 key 加密的现有数据仍可读取。下次更新每条 record 时，n8n 会静默地将其重新加密到新 key。

## 开始之前 <a href="#before-you-begin" id="before-you-begin"></a>

{% hint style="danger" %}
**启用此功能前，请完整备份 database**

启用 encryption key rotation 是单向更改。没有 rollback path。详情请参阅[向后兼容性和 rollback](#backwards-compatibility-and-rollback)。
{% endhint %}

你还需要确保：

* 所有 n8n instances、main 和所有 workers 都共享相同的 `N8N_ENCRYPTION_KEY` 值。
* 你可以直接控制环境变量和 n8n database。这只有在 self-hosted deployments 中才可能。

## 启用 encryption key rotation <a href="#enable-encryption-key-rotation" id="enable-encryption-key-rotation"></a>

1. 在**所有** n8n instances（main 和 workers）上设置以下环境变量：

    ```sh
    N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true
    ```

2. 重启所有 instances。启动时，n8n 会自动生成初始 data encryption key，并将其加密存储在 database 中。
3. 要确认功能已启用，请前往 **Settings** > **Data Encryption Keys**。你应该能看到 active key。

## 轮换 active key <a href="#rotate-the-active-key" id="rotate-the-active-key"></a>

启用此功能后，你可以随时轮换到新的 data encryption key。

### 使用 UI <a href="#using-the-ui" id="using-the-ui"></a>

前往 **Settings** > **Data Encryption Keys**，然后选择 **Rotate key**。

### 使用 API <a href="#using-the-api" id="using-the-api"></a>

向 `/encryption/keys` endpoint 发起 `POST` 调用。请求需要 `encryptionKey:manage` global scope。n8n 永远不会在 API responses 中返回 key material，只返回 ID、algorithm、status 和 timestamps 等 metadata。

轮换后，n8n 会使用新的 active key 处理所有新写入。使用旧 keys 加密的 records 仍可读取。下次更新每条 record 时，n8n 会将其重新加密到新 key。

## 向后兼容性和 rollback <a href="#backwards-compatibility-and-rollback" id="backwards-compatibility-and-rollback"></a>

{% hint style="danger" %}
**这是单向迁移**

启用 encryption key rotation 前，请仔细阅读本节。
{% endhint %}

启用 encryption key rotation 后，n8n 会开始以包含 key identifier 的新格式写入 credentials 和其他 sensitive data。较旧版本的 n8n，以及未启用 feature flag 的 instances，无法读取此格式。

* 在任何数据以新格式写入后，**不要禁用 feature flag**。移除 `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` 或将其设为 `false`，会让启用该功能后加密的所有数据永久无法访问。
* 启用后**不要降级 n8n 版本**。较旧版本无法解密新格式。

没有自动化工具可以将以新格式加密的数据转换回 legacy format。唯一的恢复路径是从启用此功能前创建的 database backup 恢复。

## 建议步骤 <a href="#recommended-steps" id="recommended-steps"></a>

1. **备份 database**。在任何更改前创建完整 snapshot。
2. **先在 staging 启用**。在非生产环境中设置 `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true`，重启，并验证 credentials 仍可正确解密。
3. **在 production 启用**。仅在验证 staging 行为后执行此操作。
4. **不要禁用或降级**。一旦 production data 已以新格式写入，请保持 flag 启用，并保持相同或更新的 n8n 版本。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [Set a custom encryption key](../basic-configuration/configuration-examples/set-a-custom-encryption-key.md)：设置 instance-level `N8N_ENCRYPTION_KEY` 值。
* [Deployment environment variables](../basic-configuration/use-environment-variables/deployment.md)：`N8N_ENCRYPTION_KEY` 和 `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` 参考。
* [Configuring queue mode](../scaling/enable-queue-mode.md)：确保所有 workers 共享相同的 instance encryption key。
