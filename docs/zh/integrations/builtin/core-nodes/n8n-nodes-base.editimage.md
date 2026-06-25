---
title: Edit Image
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Edit Image
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.editimage.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage
description: >-
  n8n 中 Edit Image node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Edit Image

使用 Edit Image node 可以处理和编辑图片。

{% hint style="info" %}
**依赖**

1. 如果你不是在 Docker 上运行 n8n，需要安装 [GraphicsMagick](http://www.graphicsmagick.org/README.html)。
2. 你需要使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) node 或 [HTTP Request](n8n-nodes-base.httprequest/) node 等节点，将图片文件作为 data property 传递给 Edit Image node。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 向图片添加 **Blur** 以降低锐度
* 向图片添加 **Border**
* 将一张图片 **Composite** 到另一张图片上方
* **Create** 新图片
* **Crop** 图片
* 在图片上 **Draw**
* **Get Information** 获取图片信息
* **Multi Step** 对图片执行多个操作
* **Resize**：更改图片尺寸
* **Rotate** 图片
* 沿 X 或 Y 轴 **Shear** 图片
* 向图片添加 **Text**
* 让图片中的某种颜色 **Transparent**

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

此 node 的参数取决于你选择的操作。

### Blur 参数 <a href="#blur-parameters" id="blur-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Blur**：输入 0 到 1000 之间的数字，设置模糊强度。数字越大，图片越模糊。
* **Sigma**：输入 0 到 1000 之间的数字，设置模糊的 sigma。数字越大，图片越模糊。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Border 参数 <a href="#border-parameters" id="border-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Border Width**：输入边框宽度。
* **Border Height**：输入边框高度。
* **Border Color**：设置边框颜色。你可以输入 hex，也可以选择色块打开颜色选择器。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Composite 参数 <a href="#composite-parameters" id="composite-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。此图片是你的基础图片。
* **Composite Image Property**：输入存储要叠加到 **Property Name** 图片上方的图片的二进制属性名称。
* **Operator**：选择 composite operator，它决定叠加的工作方式。选项包括：
  * **Add**
  * **Atop**
  * **Bumpmap**
  * **Copy**
  * **Copy Black**
  * **Copy Blue**
  * **Copy Cyan**
  * **Copy Green**
  * **Copy Magenta**
  * **Copy Opacity**
  * **Copy Red**
  * **Copy Yellow**
  * **Difference**
  * **Divide**
  * **In**
  * **Minus**
  * **Multiply**
  * **Out**
  * **Over**
  * **Plus**
  * **Subtract**
  * **Xor**
* **Position X**：输入 composite 图片在 x 轴上的位置（水平）。
* **Position Y**：输入 composite 图片在 y 轴上的位置（垂直）。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Create 参数 <a href="#create-parameters" id="create-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Background Color**：设置图片背景颜色。你可以输入 hex，也可以选择色块打开颜色选择器。
* **Image Width**：输入图片宽度。
* **Image Height**：输入图片高度。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Crop 参数 <a href="#crop-parameters" id="crop-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Width**：输入你想裁剪到的宽度。
* **Height**：输入你想裁剪到的高度。
* **Position X**：输入开始裁剪的 x 轴位置（水平）。
* **Position Y**：输入开始裁剪的 y 轴位置（垂直）。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Draw 参数 <a href="#draw-parameters" id="draw-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Primitive**：选择要绘制的 primitive shape。可选：
  * **Circle**
  * **Line**
  * **Rectangle**
* **Color**：设置 primitive 的颜色。你可以输入 hex，也可以选择色块打开颜色选择器。
* **Start Position X**：输入开始绘制的 x 轴位置（水平）。
* **Start Position Y**：输入开始绘制的 y 轴位置（垂直）。
* **End Position X**：输入停止绘制的 x 轴位置（水平）。
* **End Position Y**：输入停止绘制的 y 轴位置（垂直）。
* **Corner Radius**：输入数字设置圆角半径。添加圆角半径会让绘制出的 primitive 的角变圆。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Get Information 参数 <a href="#get-information-parameters" id="get-information-parameters"></a>

对于此操作，你只需要添加存储图片数据的二进制属性的 **Property Name**。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Multi Step 参数 <a href="#multi-step-parameters" id="multi-step-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Operations**：添加你希望 multi step 操作执行的操作。你可以使用任何其他操作。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Resize 参数 <a href="#resize-parameters" id="resize-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Width**：输入图片的新宽度。
* **Height**：输入图片的新高度。
* **Option**：选择希望如何调整图片大小。可选：
  * **Ignore Aspect Ratio**：忽略宽高比，并调整为你输入的精确高度和宽度。
  * **Maximum Area**：你输入的高度和宽度是图片的最大区域/尺寸。图片会保持宽高比，并且不会大于你输入的高度和/或宽度。
  * **Minimum Area**：你输入的高度和宽度是图片的最小区域/尺寸。图片会保持宽高比，并且不会小于你输入的高度和/或宽度。
  * **Only if Larger**：仅当图片大于你输入的宽度和高度时才调整大小。图片会保持宽高比。
  * **Only if Smaller**：仅当图片小于你输入的宽度和高度时才调整大小。图片会保持宽高比。
  * **Percent**：使用宽度和高度相对于原始图片的百分比来调整图片大小。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Rotate 参数 <a href="#rotate-parameters" id="rotate-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Rotate**：输入图片旋转的度数，范围为 -360 到 360。
* **Background Color**：设置图片背景颜色。你可以输入 hex，也可以选择色块打开颜色选择器。当图片按非 90 度倍数旋转时，此颜色用于填充空白背景。如果 **Rotate** 字段使用的是 90 度倍数，则不会使用背景颜色。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Shear 参数 <a href="#shear-parameters" id="shear-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Degrees X**：输入沿 x 轴剪切的度数。
* **Degrees Y**：输入沿 y 轴剪切的度数。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Text 参数 <a href="#text-parameters" id="text-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Text**：输入要写到图片上的文本。
* **Font Size**：选择文本字号。
* **Font Color**：设置字体颜色。你可以输入 hex，也可以选择色块打开颜色选择器。
* **Position X**：输入文本开始位置的 x 轴坐标（水平）。
* **Position Y**：输入文本开始位置的 y 轴坐标（垂直）。
* **Max Line Length**：输入每行最大字符数，超过后会添加换行。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

### Transparent 参数 <a href="#transparent-parameters" id="transparent-parameters"></a>

* **Property Name**：输入存储图片数据的二进制属性名称。
* **Color**：设置要变为透明的颜色。你可以输入 hex，也可以选择色块打开颜色选择器。

可选配置选项请参阅 [Node 选项](n8n-nodes-base.editimage.md#node-options)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **File Name**：输入输出文件的文件名。
* **Format**：输入输出文件的图片格式。可选：
  * **bmp**
  * **gif**
  * **jpeg**
  * **png**
  * **tiff**
  * **WebP**

**Text** 操作还包含 **Font Name or ID** 选项。可以从下拉列表中选择文本字体，或使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Edit Image 集成模板](https://n8n.io/integrations/edit-image)或[搜索所有模板](https://n8n.io/workflows/)
