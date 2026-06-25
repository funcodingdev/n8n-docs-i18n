---
title: LDAP
description: >-
  n8n 中 LDAP node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
nodeTitle: LDAP
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ldap.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap'
layout:
  description:
    visible: false
---

# LDAP <a href="#ldap" id="ldap"></a>

此 node 允许你与 LDAP server 交互，以创建、查找和更新对象。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/ldap.md)找到该 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Compare**](#compare) attribute
* [**Create**](#create) 新 entry
* [**Delete**](#delete) entry
* [**Rename**](#rename) 现有 entry 的 DN
* [**Search**](#search) LDAP
* [**Update**](#update) attributes

有关为每个操作配置该 node 的详情，请参阅下面各节。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Compare <a href="#compare" id="compare"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **DN**：输入要比较的 entry 的 Distinguished Name（DN）。
* **Attribute ID**：输入要比较的 attribute ID。
* **Value**：输入要比较的值。

## Create <a href="#create" id="create"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **DN**：输入要创建的 entry 的 Distinguished Name（DN）。
* **Attributes**：添加要创建的 **Attribute ID**/**Value** 对。

## Delete <a href="#delete" id="delete"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **DN**：输入要删除的 entry 的 Distinguished Name（DN）。

## Rename <a href="#rename" id="rename"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **DN**：输入要重命名 entry 当前的 Distinguished Name（DN）。
* **New DN**：在此字段中输入该 entry 新的 Distinguished Name（DN）。

## Search <a href="#search" id="search"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **Base DN**：输入要在其中搜索的 subtree 的 Distinguished Name（DN）。
* **Search For**：选择要搜索的 directory object class。
* **Attribute**：选择要搜索的 attribute。
* **Search Text**：输入要搜索的文本。使用 `*` 作为 wildcard。
* **Return All**：开启后，该 node 会返回所有结果。关闭后，该 node 会返回最多 **Limit** 指定数量的结果。
* **Limit**：仅在关闭 **Return All** 时可用。输入要返回的最大结果数。

### Search 选项 <a href="#search-options" id="search-options"></a>

你还可以使用这些选项配置此操作：

* **Attribute Names or IDs**：输入逗号分隔的要返回 attribute 列表。可从列表中选择，或使用 expression 指定 ID。
* **Page Size**：输入一次请求的最大结果数。设置为 0 可禁用 paging。
* **Scopes**：要在 **Base DN** 处或其下方搜索潜在匹配项的 entry 集合。可选：
    * **Base Tree**：通常称为 subordinateSubtree 或简称 "subordinates"，选择此选项会搜索 **Base DN** entry 的 subordinate，但不会搜索 **Base DN** entry 本身。
    * **Single Level**：通常称为 "one"，选择此选项只会搜索 **Base DN** entry 的直接子项。
    * **Whole Subtree**：通常称为 "sub"，选择此选项会搜索 **Base DN** entry 及其任意深度的所有 subordinate。

有关 search scope 的更多信息，请参阅 [The LDAP Search Operation](https://ldap.com/the-ldap-search-operation/)。

## Update <a href="#update" id="update"></a>

使用这些参数配置该操作：

* **Credential to connect with**：选择或创建用于连接的 [LDAP credential](../credentials/ldap.md)。
* **DN**：输入要更新的 entry 的 Distinguished Name（DN）。
* ***Update Attributes**：选择是 **Add** 新 attribute、**Remove** 现有 attribute，还是 **Replace** 现有 attribute。
* 然后输入要更新的 **Attribute ID**/**Value** 对。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 LDAP 集成模板](https://n8n.io/integrations/ldap)或[搜索所有模板](https://n8n.io/workflows/)
