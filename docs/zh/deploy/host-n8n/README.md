---
title: n8n Hosting Documentation and Guides
description: >-
  访问 n8n 托管文档和指南。查找全面的资源，帮助你设置和管理自托管 n8n 实例。
contentType: overview
hide:
  - toc
  - feedback
  - kapaButton
nodeTitle: Host n8n
originalFilePath: hosting/index.md
originalUrl: 'https://docs.n8n.io/hosting'
url: 'https://docs.n8n.io/deploy/'
layout:
  description:
    visible: false
---

# 自托管 n8n <a href="#self-hosting-n8n" id="self-hosting-n8n"></a>

所有自托管安装都使用同一个核心产品。没有 license key 时，n8n 会以免费的 [Community edition](community-edition-features.md) 运行。添加 Business 或 Enterprise license key 后会启用对应版本。

## 选择安装方法 <a href="#choose-your-installation-method" id="choose-your-installation-method"></a>

选择最适合你的技术要求和基础设施的安装方法：

- __npm__

	**最适合：** 本地开发、测试或简单的单服务器部署。

	**要求：** 系统中已安装 Node.js。

	使用 Node Package Manager 直接安装 n8n。设置很快，但需要你自行管理 Node.js 版本和依赖。

	[npm 安装指南](install-options/install-with-npm.md)

- __Docker__

	**最适合：** 隔离环境、便捷更新和一致部署。

	**要求：** 系统中已安装 Docker。

	在包含所有依赖的 container 中运行 n8n。可简化安装和更新。

	[Docker 安装指南](install-options/install-with-docker.md)

- __AWS__

	使用 EC2、ECS 或其他 AWS 服务部署到 Amazon Web Services。

	[AWS 设置指南](install-options/use-a-cloud-provider/deploy-to-aws.md)

- __Azure__

	使用 container instances 或 virtual machines 在 Microsoft Azure 上托管 n8n。

	[Azure 设置指南](install-options/use-a-cloud-provider/deploy-to-azure.md)

- __Google Cloud__

	使用 Cloud Run 或 Kubernetes Engine 在 Google Cloud 上运行 n8n。

	[Google Cloud Run](install-options/use-a-cloud-provider/deploy-to-google-cloud-run.md) | [Kubernetes Engine](install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md)

- __DigitalOcean__

	基于 droplet 的简单托管方式，适合中小型部署。

	[DigitalOcean 设置指南](install-options/use-a-cloud-provider/deploy-to-digital-ocean.md)

- __Hetzner__

	高性价比的欧洲托管选项，性能出色。

	[Hetzner 设置指南](install-options/use-a-cloud-provider/deploy-to-hetzner.md)

- __Heroku__

	Platform-as-a-service 选项，适合以最少配置快速部署。

	[Heroku 设置指南](install-options/use-a-cloud-provider/deploy-to-heroku.md)

- __OpenShift__

	用于 containerized applications 的企业级 Kubernetes 平台。

	[OpenShift 设置指南](install-options/use-a-cloud-provider/deploy-to-openshift-local-crc.md)

- __Docker Compose__

	多 container 设置，适合包含数据库和额外服务的生产部署。

	[Docker Compose 指南](install-options/use-a-cloud-provider/use-docker-compose.md)
