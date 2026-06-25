---
title: Evaluation
description: >-
  使用 n8n evaluation 构建可靠的 AI 工作流。通过比较已知测试用例的输出，增强你对 LLM 工作流的信心。
contentType: overview
nodeTitle: 理解为什么要测试
originalFilePath: advanced-ai/evaluations/overview.md
originalUrl: 'https://docs.n8n.io/advanced-ai/evaluations/overview'
url: >-
  https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test
layout:
  description:
    visible: false
---

# 概览 <a href="#overview" id="overview"></a>


## 什么是 evaluation？ <a href="#what-are-evaluations" id="what-are-evaluations"></a>

Evaluation 是检查 AI 工作流是否可靠的关键技术。它可能决定你的成果只是一个不稳定的概念验证，还是一个稳固的生产工作流。无论在构建阶段，还是部署到生产环境之后，它都很重要。

Evaluation 的基础是让测试数据集通过你的工作流运行。这个数据集包含多个测试用例。每个测试用例都包含工作流的示例输入，并且通常也包含预期输出。

Evaluation 允许你：

* **用一系列输入测试工作流**，从而了解它在边界场景中的表现
* **更有信心地做改动**，避免无意中让其他地方变差
* **比较不同模型或 prompt 的性能**

以下视频解释了 evaluation 是什么、为什么有用，以及它们如何工作：

{% embed url="https://www.youtube.com/embed/5LlF196PKaE" %}


## 为什么需要 evaluation？ <a href="#why-is-evaluation-needed" id="why-is-evaluation-needed"></a>

AI 模型与代码有根本区别。代码是确定性的，你可以对它进行推理。但 LLM 很难这样做，因为它们是黑盒。因此，你必须通过让数据经过 LLM 并观察输出来*衡量* LLM 输出。

只有当你用多个输入运行模型，并且这些输入准确反映它在生产中必须处理的所有边界场景后，你才能建立对模型可靠性的信心。

## 两种 evaluation <a href="#two-types-of-evaluation" id="two-types-of-evaluation"></a>

### 轻量 evaluation（部署前） <a href="#light-evaluation-pre-deployment" id="light-evaluation-pre-deployment"></a>

构建干净、全面的数据集很难。在初始构建阶段，通常只生成少量示例就很合理。这些示例可能足以将工作流迭代到可发布状态（或概念验证）。你可以通过视觉方式比较结果，了解工作流质量，而无需设置正式 metric。

### 基于 metric 的 evaluation（部署后） <a href="#metric-based-evaluation-post-deployment" id="metric-based-evaluation-post-deployment"></a>

部署工作流后，你可以更容易地从生产执行中构建更大、更具代表性的数据集。当发现 bug 时，可以将触发它的输入添加到数据集中。修复 bug 时，重要的是再次让整个数据集通过工作流运行，作为[回归测试](https://en.wikipedia.org/wiki/Regression_testing)，检查修复是否无意中让其他地方变差。

由于测试用例太多，无法逐个检查，evaluation 会使用 metric 来衡量输出质量。metric 是表示某个特定特征的数值。这也允许你跟踪不同运行之间的质量变化。

### evaluation 类型对比 <a href="#comparison-of-evaluation-types" id="comparison-of-evaluation-types"></a>

|                                                     | 轻量 evaluation（部署前）       | 基于 metric 的 evaluation（部署后）      |
|-----------------------------------------------------|-----------------------------------------|------------------------------------------------|
| **每次迭代带来的<br>性能改进** | 大                                   | 小                                          |
| **数据集规模**                                    | 小                                   | 大                                          |
| **数据集来源**                                 | 手动生成<br>AI 生成<br>其他 | 生产执行<br>AI 生成<br>其他 |
| **实际输出**                                  | 必需                                | 必需                                       |
| **预期输出**                                | 可选                                | 通常必需                             |
| **Evaluation metric**                           | 可选                                | 必需                                       |

## 了解更多 <a href="#learn-more" id="learn-more"></a>

* [轻量 evaluation](run-quick-evaluations.md)：非常适合在开发期间使用手动选择的测试用例评估 AI 工作流。
* [基于 metric 的 evaluation](use-metrics-to-measure-quality.md)：高级 evaluation，通过对大型数据集使用评分和 metric，帮助在生产中保持性能和正确性。
* [提示和常见问题](fix-common-issues.md)：了解如何设置特定 evaluation 用例并绕过常见问题。
