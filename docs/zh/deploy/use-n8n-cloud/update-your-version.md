---
contentType: howto
nodeTitle: Update your version
originalFilePath: manage-cloud/update-cloud-version.md
originalUrl: https://docs.n8n.io/manage-cloud/update-cloud-version
url: https://docs.n8n.io/deploy/use-n8n-cloud/update-your-version
description: 如何更新 Cloud 上的 n8n 版本。
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

# 更新版本

n8n 建议定期更新你的 Cloud 版本。查看 [Release notes](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/) 了解更多变更信息。

{% hint style="info" %}
只有实例所有者可以升级 n8n Cloud 版本。如果你没有更新 n8n Cloud 的权限，请联系实例所有者。
{% endhint %}

1. [登录 n8n Cloud dashboard](https://app.n8n.cloud/manage)
2. 在 dashboard 上选择 **Manage**。
3. 使用 **n8n version** dropdown 选择你偏好的 release version：
   * Latest Stable：推荐给大多数用户。
   * Latest Beta：获取最新的 n8n。它可能不稳定。
4. 选择 **Save Changes** 重启你的 n8n 实例并执行更新。
5. 在 confirmation modal 中选择 **Confirm**。

## 更新最佳实践 <a href="#best-practices-for-updating" id="best-practices-for-updating"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/1Q2X3RjU5o2jnRfcKzuN/" %}

## 自动更新 <a href="#automatic-update" id="automatic-update"></a>

n8n 会自动更新过时的 Cloud 实例。

如果你 120 天没有更新实例，n8n 会向你发送邮件提醒你更新。再过 30 天后，n8n 会自动更新你的实例。
