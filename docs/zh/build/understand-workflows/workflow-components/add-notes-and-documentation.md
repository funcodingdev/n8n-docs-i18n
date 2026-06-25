---
contentType: howto
nodeTitle: Add notes and documentation
originalFilePath: workflows/components/sticky-notes.md
originalUrl: https://docs.n8n.io/workflows/components/sticky-notes
url: >-
  https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation
description: 使用 Sticky Note 为工作流添加注释。
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

# 添加备注和文档说明

Sticky Notes 允许你为工作流添加注释和说明。

n8n 建议充分使用 Sticky Notes，尤其是在[模板工作流](#user-content-fn-1)[^1]中，这有助于其他用户理解你的工作流。

![带有示例 Sticky Note 的基础工作流截图](../../../../build/.gitbook/assets/example-sticky-note.png)

## 创建 Sticky Note <a href="#create-a-sticky-note" id="create-a-sticky-note"></a>

Sticky Notes 是一种 core node。如需添加新的 Sticky Note：

1. 打开 nodes 面板。
2. 搜索 `note`。
3. 点击 **Sticky Note** node。n8n 会向画布添加新的 Sticky Note。

## 编辑 Sticky Note <a href="#edit-a-sticky-note" id="edit-a-sticky-note"></a>

1. 双击要编辑的 Sticky Note。
2. 写入备注。[这份指南](https://commonmark.org/help/)说明了如何使用 Markdown 格式化文本。n8n 使用实现 CommonMark 规范的 [markdown-it](https://github.com/markdown-it/markdown-it)。
3. 点击备注以外的位置，或按 `Esc`，停止编辑。

## 更改颜色 <a href="#change-the-color" id="change-the-color"></a>

如需更改 Sticky Note 颜色：

1. 将鼠标悬停在 Sticky Note 上
2. 选择 **Change color** <img src="../../../../build/.gitbook/assets/change-color.png" alt="Change Sticky Note color icon" data-size="line">
3. 从七种预设颜色中选择，或点击彩虹渐变按钮选择自定义颜色

![显示预设颜色和自定义颜色按钮的颜色选择器](../../../../build/.gitbook/assets/color-picker-popover.png)

### 自定义颜色 <a href="#custom-colors" id="custom-colors"></a>

除了七种预设颜色，你还可以为 sticky note 选择任意自定义颜色：

1. 点击带有彩虹渐变和加号图标的按钮
2. 使用颜色选择器选择所需颜色，或输入十六进制颜色代码（例如 `#FF5733`）
3. 点击 **Apply** 设置颜色

最近使用的自定义颜色（最多 8 个）会自动保存并显示在颜色选择器中，方便快速访问。

自定义颜色具有感知主题的边框，会在浅色和深色模式下自动调整，以获得最佳可见性。

## Sticky Note 定位 <a href="#sticky-note-positioning" id="sticky-note-positioning"></a>

你可以：

* 将 Sticky Note 拖到画布上的任意位置。
* 将 Sticky Note 拖到 node 后方。你可以用这种方式在视觉上分组 node。
* 将鼠标悬停在备注边缘并拖拽，调整 Sticky Note 大小。
* 更改颜色：选择 **Options** <img src="../../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options icon" data-size="line"> 打开颜色选择器。

## 使用 Markdown 编写 <a href="#writing-in-markdown" id="writing-in-markdown"></a>

Sticky Notes 支持 Markdown 格式。本节介绍一些常用选项。

```
The text in double asterisks will be **bold**

The text in single asterisks will be *italic*

Use # to indicate headings:
# This is a top-level heading <a href="#this-is-a-top-level-heading" id="this-is-a-top-level-heading"></a>
## This is a sub-heading <a href="#this-is-a-sub-heading" id="this-is-a-sub-heading"></a>
### This is a smaller sub-heading <a href="#this-is-a-smaller-sub-heading" id="this-is-a-smaller-sub-heading"></a>

You can add links:
[Example](https://example.com/)

Create lists with asterisks:

* Item one
* Item two

Or created ordered lists with numbers:

1. Item one
2. Item two
```

更详细的指南请参考 [CommonMark 帮助](https://commonmark.org/help/)。n8n 使用实现 CommonMark 规范的 [markdown-it](https://github.com/markdown-it/markdown-it)。

## 让图片占满宽度 <a href="#make-images-full-width" id="make-images-full-width"></a>

你可以通过在文件名后追加 `#full-width`，强制图片占满 sticky note 的 100% 宽度：

```markdown
![Source example](https://<IMAGE-URL>/<IMAGE-NAME>.png#full-width)
```

## 嵌入 YouTube 视频 <a href="#embed-a-youtube-video" id="embed-a-youtube-video"></a>

如需在备注中显示 YouTube 视频，请使用带视频 ID 的 `@[youtube](<video-id>)` 指令。要使其生效，视频创建者必须允许嵌入。

例如：

```markdown
@[youtube](ZCuL2e4zC_4)
```

如需嵌入你自己的视频，复制上述语法，并将 `ZCuL2e4zC_4` 替换为你的视频 ID。YouTube 视频 ID 是 YouTube URL 中 `v=` 后面的字符串。

[^1]: n8n template 是由 n8n 和社区成员设计的预构建 workflow，你可以将其导入到 n8n 实例中。使用 template 时，你可能需要填写 credential，并根据需要调整配置。
