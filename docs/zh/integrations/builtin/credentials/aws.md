---
title: AWS credentials
description: >-
  AWS credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 AWS。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: AWS credentials
originalFilePath: integrations/builtin/credentials/aws.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/aws'
url: 'https://docs.n8n.io/integrations/builtin/credentials/aws'
layout:
  description:
    visible: false
---

# AWS credentials <a href="#aws-credentials" id="aws-credentials"></a>

## AWS (IAM) credentials <a href="#aws-iam-credentials" id="aws-iam-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [AWS Bedrock Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
- [AWS Certificate Manager](../app-nodes/n8n-nodes-base.awscertificatemanager.md)
- [AWS Cognito](../app-nodes/n8n-nodes-base.awscognito.md)
- [AWS Comprehend](../app-nodes/n8n-nodes-base.awscomprehend.md)
- [AWS DynamoDB](../app-nodes/n8n-nodes-base.awsdynamodb.md)
- [AWS Elastic Load Balancing](../app-nodes/n8n-nodes-base.awselb.md)
- [AWS IAM](../app-nodes/n8n-nodes-base.awsiam.md)
- [AWS Lambda](../app-nodes/n8n-nodes-base.awslambda.md)
- [AWS Rekognition](../app-nodes/n8n-nodes-base.awsrekognition.md)
- [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)
- [AWS SES](../app-nodes/n8n-nodes-base.awsses.md)
- [AWS SNS](../app-nodes/n8n-nodes-base.awssns.md)
- [AWS SNS Trigger](../trigger-nodes/n8n-nodes-base.awssnstrigger.md)
- [AWS SQS](../app-nodes/n8n-nodes-base.awssqs.md)
- [AWS Textract](../app-nodes/n8n-nodes-base.awstextract.md)
- [AWS Transcribe](../app-nodes/n8n-nodes-base.awstranscribe.md)
- [Embeddings AWS Bedrock](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)

### 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access key

### 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AWS Identity and Access Management 文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)。

### 使用 API access key <a href="#using-api-access-key" id="using-api-access-key"></a>

要配置此 credential，你需要一个 [AWS](https://aws.amazon.com/) 账号，以及：

- 你的 AWS **Region**
- **Access Key ID**：创建 access key 时生成。
- **Secret Access Key**：创建 access key 时生成。

创建 access key 并设置 credential：

1. 在 n8n credential 中，选择你的 AWS **Region**。
1. 登录 [IAM console](https://console.aws.amazon.com/iam)。
2. 在右上方导航栏中，选择你的用户名，然后选择 **Security credentials**。
3. 在 **Access keys** 区域中，选择 **Create access key**。
4. 在 **Access key best practices & alternatives page** 上，选择你的使用场景。如果它没有提示你创建 access key，请选择 **Other**。
5. 选择 **Next**。
6. 为 access key 设置一个 **description** tag value，便于识别，例如 `n8n integration`。
7. 选择 **Create access key**。
8. 显示 **Access Key ID** 和 **Secret Access Key**，并将它们输入到 n8n。
10. 如需使用 **Temporary security credential**，打开该选项并添加 **Session token**。有关使用 temporary security credentials 的更多信息，请参阅 [AWS Temporary security credential 文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)。
11. 如果你使用 [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) 托管 n8n，可以在 VPC 和部分 apps 之间建立连接。使用 **Custom Endpoints** 输入此连接的相关 custom endpoint。此设置适用于以下 apps：
    - Rekognition
    - Lambda
    - SNS
    - SES
    - SQS
    - S3

你也可以通过 AWS CLI 和 AWS API 生成 access keys。有关使用这些方法生成 access keys 的说明，请参阅 [AWS Managing Access Keys 文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)。

## AWS (Assume Role) credentials <a href="#aws-assume-role-credentials" id="aws-assume-role-credentials"></a>

你可以使用这些 credentials，通过 IAM role assumption 提供的增强安全性验证以下 nodes：

* [AWS Bedrock Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
* [AWS Certificate Manager](../app-nodes/n8n-nodes-base.awscertificatemanager.md)
* [AWS Cognito](../app-nodes/n8n-nodes-base.awscognito.md)
* [AWS Comprehend](../app-nodes/n8n-nodes-base.awscomprehend.md)
* [AWS DynamoDB](../app-nodes/n8n-nodes-base.awsdynamodb.md)
* [AWS Elastic Load Balancing](../app-nodes/n8n-nodes-base.awselb.md)
* [AWS Rekognition](../app-nodes/n8n-nodes-base.awsrekognition.md)
* [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)
* [AWS SES](../app-nodes/n8n-nodes-base.awsses.md)
* [AWS SQS](../app-nodes/n8n-nodes-base.awssqs.md)
* [AWS Textract](../app-nodes/n8n-nodes-base.awstextract.md)
* [AWS Transcribe](../app-nodes/n8n-nodes-base.awstranscribe.md)
* [Embeddings AWS Bedrock](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)

### 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Role Assumption

### 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 role assumption 的更多信息，请参阅 [AWS IAM Role 文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) 和 [STS AssumeRole 文档](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)。

### 理解 AWS Role Assumption <a href="#understanding-aws-role-assumption" id="understanding-aws-role-assumption"></a>

AWS Role Assumption 允许你通过临时 assume 一个 IAM role 来安全访问 AWS 资源，而不是使用长期有效的 access keys。这符合 AWS 安全最佳实践，并支持：

* **跨账号访问：** 访问不同 AWS 账号中的资源
* **增强安全性：** 使用会自动过期的 temporary credentials
* **最小权限原则：** 只授予特定任务所需的权限
* **审计轨迹：** 更好地追踪谁访问了哪些资源

### 设置 AWS Assume Role credentials <a href="#setting-up-aws-assume-role-credentials" id="setting-up-aws-assume-role-credentials"></a>

要配置此 credential，你需要：

#### 必需参数 <a href="#required-parameters" id="required-parameters"></a>

* **Region:** 调用 STS service 来 assume role 的 AWS region。
* **Role ARN:** 你想要 assume 的 IAM role 的 Amazon Resource Name (ARN)。格式为 `arn:aws:iam::123456789012:role/MyRole`。此 role 必须有允许你的 credentials assume 它的 trust policy。
* **External ID:** role 的 trust policy 所需的唯一标识符，用于防止 "confused deputy" 问题。这应是一个 secret value，由你生成并同时配置到 role 的 trust policy 和此 credential 中。请将此值视为敏感信息。不要与不信任的其他 n8n 用户共享。
* **Role Session Name:** assumed role session 的名称（用于审计）。默认值是 `n8n-session`。此值会出现在 AWS CloudTrail logs 中，方便你识别 session。

#### STS credentials（选择一种方法）<a href="#sts-credentials-choose-one-method" id="sts-credentials-choose-one-method"></a>

你有两种方式提供 credentials，用于发起 STS AssumeRole 调用：

##### 选项 1：使用 system credentials（推荐用于 server 部署）<a href="#option-1-use-system-credentials-recommended-for-server-deployments" id="option-1-use-system-credentials-recommended-for-server-deployments"></a>

如果你的 n8n server 已通过以下方式配置 AWS credentials，请启用此选项：

* Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`)
* EC2 instance profile
* ECS task role
* EKS pod identity

此选项要求 n8n administrator 通过将环境变量 `N8N_AWS_SYSTEM_CREDENTIALS_ACCESS_ENABLED` 设置为 `true` 来启用 system credentials access。

##### 选项 2：Manual STS Credentials <a href="#option-2-manual-sts-credentials" id="option-2-manual-sts-credentials"></a>

如果 system credentials 不可用，请手动提供以下内容：

* **STS Access Key ID:** 有权限 assume 目标 role 的 IAM user 或 role 的 Access Key ID。
* **STS Secret Access Key:** 与 STS Access Key ID 对应的 Secret Access Key。
* **STS Session Token**（可选）：如果 STS 调用使用 temporary credentials，请提供 session token。

#### 可选参数 <a href="#optional-parameters" id="optional-parameters"></a>

* **Custom Endpoints:** 如果使用 Amazon VPC，你可以为 AWS services 指定 custom endpoints：

    * Rekognition Endpoint
    * Lambda Endpoint
    * SNS Endpoint
    * SES Endpoint
    * SQS Endpoint
    * S3 Endpoint
    * SSM Endpoint

### 设置步骤 <a href="#setup-steps" id="setup-steps"></a>

1. 在目标 AWS 账号中创建 IAM Role。

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::SOURCE-ACCOUNT:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "sts:ExternalId": "your-unique-external-id"
           }
         }
       }
     ]
   }

   ```
2. 在 n8n 中配置 credential。
   * 选择你的 AWS **Region**
   * 输入你创建的 role 的 **Role ARN**
   * 设置唯一的 **External ID**（与 trust policy 中一致）
   * 选择你的 **STS credentials method**
   * 输入 **Role Session Name**（或使用默认值）
3. 使用内置测试功能 **Test the credential**，验证 role assumption 是否可用。

### 安全最佳实践 <a href="#security-best-practices" id="security-best-practices"></a>

* 为每个 credential 使用唯一的 External ID，防止未授权访问。
* 轮换用于 role assumption 的 STS credentials。
* 对 assuming credentials 和目标 role 都应用最小权限原则。
