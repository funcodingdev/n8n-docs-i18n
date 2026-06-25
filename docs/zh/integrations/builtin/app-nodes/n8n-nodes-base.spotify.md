---
title: Spotify node documentation
description: >-
  了解如何在 n8n 中使用 Spotify node。按照技术文档将 Spotify node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Spotify node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.spotify.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify'
layout:
  description:
    visible: false
---

# Spotify node <a href="#spotify-node" id="spotify-node"></a>

使用 Spotify node 自动化 Spotify 中的工作，并将 Spotify 与其他应用集成。n8n 内置支持大量 Spotify 功能，包括获取 album 和 artist 信息。

在本页中，你可以找到 Spotify node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Spotify credentials](../credentials/spotify.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Album
    * 按 URI 或 ID 获取 album。
    * 获取 new album release 列表。
    * 按 URI 或 ID 获取 album 的 track。
    * 按 keyword 搜索 album。
* Artist
    * 按 URI 或 ID 获取 artist。
    * 按 URI 或 ID 获取 artist 的 album。
    * 按 URI 或 ID 获取 artist 的 related artist。
    * 按 URI 或 ID 获取 artist 的 top track。
    * 按 keyword 搜索 artist。
* Library
    * 获取 user 喜欢的 track。
* My Data
    * 获取你关注的 artist。
* Player
    * 将 song 添加到你的 queue。
    * 获取当前正在播放的 track。
    * 跳到下一首 track。
    * 暂停音乐。
    * 跳到上一首 song。
    * 获取最近播放的 track。
    * 在当前 active device 上恢复播放。
    * 设置当前 active device 的音量。
    * 开始播放 playlist、artist 或 album。
* Playlist
    * 按 track 和 playlist URI 或 ID 从 playlist 添加 track。
    * 创建新 playlist。
    * 按 URI 或 ID 获取 playlist。
    * 按 URI 或 ID 获取 playlist 的 track。
    * 获取 user 的 playlist。
    * 按 track 和 playlist URI 或 ID 从 playlist 移除 track。
    * 按 keyword 搜索 playlist。
* Track
    * 按 URI 或 ID 获取 track。
    * 按 URI 或 ID 获取 track 的 audio feature。
    * 按 keyword 搜索 track

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Spotify node 文档集成模板](https://n8n.io/integrations/spotify)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}
