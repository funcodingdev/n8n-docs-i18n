---
nodeTitle: Binaryfile
originalFilePath: data/expression-reference/binaryfile.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/binaryfile'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile
layout:
  description:
    visible: false
---
# BinaryFile <a href="#binaryfile" id="binaryfile"></a>

## `binaryFile`.**`directory`** <a href="#binaryfiledirectory" id="binaryfiledirectory"></a>

**描述：** 文件存储目录的路径。用于区分不同目录中同名文件。如果 n8n 配置为将文件存储在数据库中，则不会设置。

**语法：** `binaryFile`.**`directory`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`fileExtension`** <a href="#binaryfilefileextension" id="binaryfilefileextension"></a>

**描述：** 附加在文件名后的后缀（例如 <code>txt</code>）

**语法：** `binaryFile`.**`fileExtension`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`fileName`** <a href="#binaryfilefilename" id="binaryfilefilename"></a>

**描述：** 文件名，包括扩展名

**语法：** `binaryFile`.**`fileName`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`fileSize`** <a href="#binaryfilefilesize" id="binaryfilefilesize"></a>

**描述：** 表示文件大小的字符串

**语法：** `binaryFile`.**`fileSize`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`fileType`** <a href="#binaryfilefiletype" id="binaryfilefiletype"></a>

**描述：** 表示文件类型的字符串，例如 <code>image</code>。对应 MIME type 的第一部分。

**语法：** `binaryFile`.**`fileType`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`id`** <a href="#binaryfileid" id="binaryfileid"></a>

**描述：** 文件的唯一 ID。当文件存储在磁盘或 S3 等存储服务中时，用于识别文件。

**语法：** `binaryFile`.**`id`**

**返回：** String

**来源：** 自定义 n8n 功能

## `binaryFile`.**`mimeType`** <a href="#binaryfilemimetype" id="binaryfilemimetype"></a>

**描述：** 表示文件内容格式的字符串，例如 <code>image/jpeg</code>

**语法：** `binaryFile`.**`mimeType`**

**返回：** String

**来源：** 自定义 n8n 功能
