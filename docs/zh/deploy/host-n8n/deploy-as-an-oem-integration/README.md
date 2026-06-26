---
title: OEM deployment
description: >-
  OEM deployment 概览：在 OEM agreement 下，将 n8n interface 嵌入并呈现在你自己产品的 UI 中。
contentType: overview
nodeTitle: Deploy as an OEM integration
originalFilePath: hosting/oem-deployment/index.md
originalUrl: 'https://docs.n8n.io/hosting/oem-deployment'
url: 'https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration'
layout:
  description:
    visible: false
---

# OEM deployment <a href="#oem-deployment" id="oem-deployment"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6kdIvlPPl0XWVn5z8UJh/" %}

n8n 的 OEM deployment 选项让你可以把 n8n interface embed 并呈现在你自己产品的 UI 中。这让你的 users 无需离开你的产品，就能构建 workflows、配置 connections，并运行 workflow automation。OEM integration 要求包含 n8n branding。

这不同于[将 n8n 作为 backend 使用](../README.md)。在 backend 模式中，workflows 在幕后执行，end users 永远不会看到 n8n。你的产品会使用 webhook 或 [API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api) 调用 n8n 来触发 workflows，n8n 会像 infrastructure 中的任何其他 self-hosted service 一样运行，你的 users 不会看到任何 n8n UI。所有 paid plans 都可以在 standard license 下使用这种模式，不需要单独 agreement。只有当你希望 users 直接与 n8n editor 交互时，才需要 OEM deployment。

## 覆盖内容 <a href="#whats-covered" id="whats-covered"></a>

- [Prerequisites](prerequisites.md)：规划 deployment 时关于 CPU、memory 和 database requirements 的指导。
- [Managing workflows](manage-workflows.md)：在 embedded deployment 中跨多个 users 或 organizations 管理 workflows 的 patterns。
- [Token exchange](/hosting/oem-deployment/token-exchange.md)：通过 iframe SSO 使用你自己的 identity provider 认证 users，并代表他们调用 n8n APIs。
- [Workflow templates](../configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library.md)：为你的 users 配置 custom workflow template library。
- [Credential overwrites](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/credential-overwrites)：全局设置 OAuth credentials，让 users 无需看到或输入 client secrets 即可完成 authentication。

## Support <a href="#support" id="support"></a>

请使用签署 OEM agreement 时提供的 email 联系 [n8n support](mailto:support@n8n.io)。[community forum](https://community.n8n.io/) 也可用于一般问题。
