---
doc_type: weread-highlights-reviews
bookId: "22655635"
title: Linux就该这么学
reviewCount: 3
noteCount: 10
author: 刘遄
cover: https://cdn.weread.qq.com/weread/cover/22/YueWen_22655635/t6_YueWen_22655635.jpg
readingStatus: "2"
progress: 19%
readingTime: 0小时39分钟
readingDate: 2020-01-18
isbn: 9787115470317
lastReadDate: 2020-02-15

---
# 元数据
> [!abstract] Linux就该这么学
> - ![ Linux就该这么学|200](https://cdn.weread.qq.com/weread/cover/22/YueWen_22655635/t6_YueWen_22655635.jpg)
> - 书名： Linux就该这么学
> - 作者： 刘遄
> - 简介： 本书源自日均阅读量近万次火爆的线上同名课程，口碑与影响力俱佳，旨在打造简单易学且实用性强的轻量级Linux入门教程。本书基于zui新的红帽RHEL系统编写，且内容通用于CentOS、Fedora等系统。
> - 出版时间： 2017-12-01 00:00:00
> - ISBN： 9787115470317
> - 分类： 计算机-计算机综合
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/38c323a07159b29338c5755

# 高亮划线
### 2.3 常用系统工作命令
> 📌 [top命令用于动态地监视进程活动与系统负载等信息，其格式为top。](<weread://bestbookmark?bookId=22655635&chapterUid=17&rangeStart=7854&rangeEnd=7887>)
> ⏱ 2020-02-15 18:43:59 ^22655635-17-7684-7717
> 📌 [kill命令用于终止某个指定PID的服务进程，格式为“kill [参数] [进程PID]”。](<weread://bestbookmark?bookId=22655635&chapterUid=17&rangeStart=9879&rangeEnd=9925>)
> ⏱ 2020-02-15 18:45:38 ^22655635-17-9599-9645
> 📌 [killall命令用于终止某个指定名称的服务所对应的全部进程，格式为：“killall [参数] [进程名称]”。](<weread://bestbookmark?bookId=22655635&chapterUid=17&rangeStart=10194&rangeEnd=10251>)
> ⏱ 2020-02-15 18:45:53 ^22655635-17-9914-9971
### 2.4 系统状态检测命令
> 📌 [uname命令用于查看系统内核与系统版本等信息，格式为“uname [-a]”。在使用uname命令时，一般会固定搭配上-a参数来完整地查看当前系统的内核名称、主机名、内核发行版本、节点名、系统时间、硬件名称、硬件平台、处理器类型以及操作系统名称等信息。](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=2091&rangeEnd=2247>)
> ⏱ 2020-02-15 18:48:50 ^22655635-18-2091-2247
> 📌 [uptime用于查看系统的负载信息，格式为uptime。uptime命令真的很棒，它可以显示当前系统时间、系统已运行时间、启用终端数量以及平均负载值等信息。平均负载值指的是系统在最近1分钟、5分钟、15分钟内的压力情况（下面加粗的信息部分）；负载值越低越好，尽量不要长期超过1，在生产环境中不要超过5。](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=2796&rangeEnd=2976>)
> ⏱ 2020-02-15 18:50:27 ^22655635-18-2796-2976
> 📌 [free用于显示当前系统中内存的使用量信息，格式为“free [-h]”。为了保证Linux系统不会因资源耗尽而突然宕机，运维人员需要时刻关注内存的使用量。在使用free命令时，可以结合使用-h参数以更人性化的方式输出当前内存的实时使用量信息。](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=3207&rangeEnd=3358>)
> ⏱ 2020-02-15 18:51:17 ^22655635-18-3207-3358
> 📌 [who用于查看当前登入主机的用户终端信息，格式为“who [参数]”。](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=3838&rangeEnd=3873>)
> ⏱ 2020-02-15 18:52:04 ^22655635-18-3818-3853
> 📌 [last命令用于查看所有系统的登录记录，格式为“last [参数]”。使用last命令可以查看本机的登录记录。但是，由于这些信息都是以日志文件的形式保存在系统中，因此黑客可以很容易地对内容进行篡改。千万不要单纯以该命令的输出信息而判断系统有无被恶意入侵！](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=4356&rangeEnd=4512>)
> ⏱ 2020-02-15 18:52:50 ^22655635-18-4316-4472
> 📌 [history命令用于显示历史执行过的命令，格式为“history [-c]”。history命令应该是作者最喜欢的命令。执行history命令能显示出当前用户在本地计算机中执行过的最近1000条命令记录。如果觉得1000不够用，还可以自定义/etc/profile文件中的HISTSIZE变量值。在使用history命令时，如果使用-c参数则会清空所有的命令历史记录。还可以使用“！编码数字”的方式来重复执行某一次的命令](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=5220&rangeEnd=5460>)
> ⏱ 2020-02-15 18:54:01 ^22655635-18-5180-5420
> 📌 [sosreport命令用于收集系统配置及架构信息并输出诊断文档，格式为sosreport。](<weread://bestbookmark?bookId=22655635&chapterUid=18&rangeStart=6793&rangeEnd=6838>)
> ⏱ 2020-02-15 18:54:31 ^22655635-18-6753-6798

# 读书笔记

# 本书评论
