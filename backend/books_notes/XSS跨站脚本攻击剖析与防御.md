---
doc_type: weread-highlights-reviews
bookId: "730671"
title: XSS跨站脚本攻击剖析与防御
reviewCount: 0
noteCount: 7
author: 邱永华编著
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/671/730671/t6_730671.jpg
readingStatus: "2"
progress: 7%
readingTime: 0小时20分钟
readingDate: 2022-01-11
isbn: 9787115311047
lastReadDate: 2022-01-11

---
# 元数据
> [!abstract] XSS跨站脚本攻击剖析与防御
> - ![ XSS跨站脚本攻击剖析与防御|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/671/730671/t6_730671.jpg)
> - 书名： XSS跨站脚本攻击剖析与防御
> - 作者： 邱永华编著
> - 简介： 本书通过讲述有关跨站脚本的知识，读者可以深刻地感受到跨站脚本的强大，并且详尽地了解许多与XSS相关的内容，例如，在什么环境下可以触发XSS，利用XSS漏洞可以做什么，如何防范此类攻击等。自始至终，本书贯穿着许多案例分析，读者可以在实际环境中进行安全测试。
> - 出版时间： 2013-09-01 00:00:00
> - ISBN： 9787115311047
> - 分类： 计算机-计算机综合
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/4fd328f05b262f4fd266794

# 高亮划线
### 1.1 跨站脚本介绍
> 📌 [跨站脚本（Cross-Site Scripting，XSS）是一种经常出现在Web应用程序中的计算机安全漏洞，是由于Web应用程序对用户的输入过滤不足而产生的。攻击者利用网站漏洞把恶意的脚本代码（通常包括HTML代码和客户端Javascript脚本）注入到网页之中，当其他用户浏览这些网页时，就会执行其中的恶意代码，对受害用户可能采取Cookie资料窃取、会话劫持、钓鱼欺骗等各种攻击。](<weread://bestbookmark?bookId=730671&chapterUid=6&rangeStart=949&rangeEnd=1142>)
> ⏱ 2022-01-11 13:07:13 ^730671-6-949-1142
### 1.2 XSS的分类
> 📌 [XSS根据其特性和利用手法的不同，主要分成两大类型：一种是反射型跨站脚本；另一种是持久型跨站脚本。](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=463&rangeEnd=512>)
> ⏱ 2022-01-11 13:15:18 ^730671-7-463-512
> 📌 [反射型跨站脚本（Refected Cross-site Scripting）也称作非持久型、参数型跨站脚本。这种类型的跨站脚本是最常见，也是使用最广的一种，主要用于将恶意脚本附加到URL地址的参数中](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=607&rangeEnd=707>)
> ⏱ 2022-01-11 13:16:01 ^730671-7-607-707
> 📌 [反射型XSS的利用一般是攻击者通过特定手法（比如利用电子邮件），诱使用户去访问一个包含恶意代码的URL，当受害者单击这些专门设计的链接的时候，恶意JavaScript代码会直接在受害者主机上的浏览器执行。它的特点是只在用户单击时触发，而且只执行一次，非持久化，所以称为反射型跨站式脚本。](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=1060&rangeEnd=1203>)
> ⏱ 2022-01-11 13:16:32 ^730671-7-1060-1203
> 📌 [此类 XSS 通常出现在网站的搜索栏、用户登入口等地方，常用来窃取客户端 Cookies 或进行钓鱼欺骗。](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=1515&rangeEnd=1568>)
> ⏱ 2022-01-11 13:17:32 ^730671-7-1515-1568
> 📌 [持久型跨站脚本（Persistent Cross-site Scripting）也等于存储型跨站脚本（Stored Cross-site Scripting）](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=3191&rangeEnd=3270>)
> ⏱ 2022-01-11 13:18:42 ^730671-7-3191-3270
> 📌 [持久型 XSS 一般出现在网站的留言、评论、博客日志等交互处，恶意脚本被存储到客户端或者服务器的数据库中，当其他用户浏览该网页时，站点即从数据库中读取恶意用户存入的非法数据，然后显示在页面中，即在受害者主机上的浏览器执行恶意代码。](<weread://bestbookmark?bookId=730671&chapterUid=7&rangeStart=3741&rangeEnd=3856>)
> ⏱ 2022-01-11 13:20:13 ^730671-7-3741-3856

# 读书笔记

# 本书评论
