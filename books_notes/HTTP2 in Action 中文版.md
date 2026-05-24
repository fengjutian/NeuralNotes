---
doc_type: weread-highlights-reviews
bookId: "32517945"
title: HTTP/2 in Action 中文版
reviewCount: 0
noteCount: 6
author: Barry Pollard
cover: https://cdn.weread.qq.com/weread/cover/50/YueWen_32517945/t6_YueWen_32517945.jpg
readingStatus: "2"
progress: 22%
readingTime: 2小时20分钟
readingDate: 2021-06-05
isbn: 9787121386718
lastReadDate: 2021-07-01

---
# 元数据
> [!abstract] HTTP/2 in Action 中文版
> - ![ HTTP/2 in Action 中文版|200](https://cdn.weread.qq.com/weread/cover/50/YueWen_32517945/t6_YueWen_32517945.jpg)
> - 书名： HTTP/2 in Action 中文版
> - 作者： Barry Pollard
> - 简介： 本书以易于理解、方便上手的方式，使用贴近用户的实例来解释 HTTP/2 协议。本书首先介绍为什么要升级到 HTTP/2 以及升级的方法 ；然后逐步深入，详细解释了 HTTP/2 协议本身及其对Web 开发的影响 ；之后介绍了部分高级内容，如流状态、HPACK 等 ；最后探讨了 HTTP 的未来。本书对于 Web 开发者和运维工程师来说是一本很有价值的参考书。
> - 出版时间： 2020-07-01 00:00:00
> - ISBN： 9787121386718
> - 分类： 计算机-理论知识
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/71f32ba071f02f3971f1284

# 高亮划线
#### 1.3 HTTP的语法和历史
> 📌 [HEAD方法允许客户端获取资源的所有元信息（例如HTTP头）而无须下载资源本身。](<weread://bestbookmark?bookId=32517945&chapterUid=13&rangeStart=3786&rangeEnd=3833>)
> ⏱ 2021-07-01 21:31:08 ^32517945-13-3786-3833
> 📌 [HTTP/1.1的首个规范发布于1997年1月[14]（HTTP/1.0规范发布之后仅仅过了9个月），于1999年6月[15]被新版本替换，然后于2014年6月第3个版本[16]发布。每个新版本的发布都会废除之前的版本。](<weread://bestbookmark?bookId=32517945&chapterUid=13&rangeStart=10640&rangeEnd=11035>)
> ⏱ 2021-07-01 21:56:37 ^32517945-13-10640-11035
> 📌 [HTTP/1.1不仅将持久连接添加到文档标准中，还将其作为默认行为。即使响应中没有Connection:Keep-Alive首部，也可以假定任何HTTP/1.1连接都使用持久连接。](<weread://bestbookmark?bookId=32517945&chapterUid=13&rangeStart=15214&rangeEnd=15329>)
> ⏱ 2021-07-01 21:53:15 ^32517945-13-15214-15329
#### 1.4 HTTPS简介
> 📌 [HTTPS使用公钥加密，服务器在用户首次连接时以数字证书的形式提供公钥。你的浏览器使用此公钥加密消息，只有服务器可以解密，因为只有它拥有配对的私钥。该系统允许你安全地与网站进行通信，而无须事先知道共享密钥。](<weread://bestbookmark?bookId=32517945&chapterUid=14&rangeStart=3046&rangeEnd=3149>)
> ⏱ 2021-07-01 22:15:58 ^32517945-14-3046-3149
> 📌 [HTTPS是基于HTTP构建的，几乎可以与HTTP协议无缝衔接。它默认在不同的端口上服务（使用443端口，而HTTP的默认端口是80）。它有一个不同的URL协议名（https://而不是http://），但除了加密和解密本身以外，它并没有从根本上改变HTTP的语法或消息格式。](<weread://bestbookmark?bookId=32517945&chapterUid=14&rangeStart=4645&rangeEnd=4833>)
> ⏱ 2021-07-01 22:17:18 ^32517945-14-4645-4833
#### 2.2 解决HTTP/1.1性能问题的方案
> 📌 [打包技术叫作精灵图。例如，如果你网站上有很多社交网站图标，则每个网站图标都可以使用一个单独的图片。但这种方式会导致很多低效的HTTP请求排队，因为图片比较小，所以相对于下载这些图片所需要的时间，发送请求的时间可能会较长。所以，可以将它们合并到一张大的图片里面，然后使用CSS来定位图片位置，让它们看起来像是独立的图片，这样更高效。](<weread://bestbookmark?bookId=32517945&chapterUid=19&rangeStart=4607&rangeEnd=4799>)
> ⏱ 2021-07-01 21:15:39 ^32517945-19-4607-4799

# 读书笔记

# 本书评论
