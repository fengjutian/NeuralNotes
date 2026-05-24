---
doc_type: weread-highlights-reviews
bookId: "26211825"
title: Linux程序设计（第4版）
reviewCount: 0
noteCount: 8
author: Neil Matthew Richard Stones
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/825/26211825/t6_26211825.jpg
readingStatus: "2"
progress: 58%
readingTime: 1小时56分钟
readingDate: 2021-05-23
isbn: 9787115228215
lastReadDate: 2023-02-11

---
# 元数据
> [!abstract] Linux程序设计（第4版）
> - ![ Linux程序设计（第4版）|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/825/26211825/t6_26211825.jpg)
> - 书名： Linux程序设计（第4版）
> - 作者： Neil Matthew Richard Stones
> - 简介： 本书讲述了Linux 系统及其他UNIX 风格的操作系统上的程序开发，主要内容包括标准Linux C 语言函数库和由不同的Linux 或UNIX 标准指定的各种工具的使用方法，大多数标准Linux 开发工具的使用方法，通过DBM 和MySQL 数据库系统存储Linux 中的数据，为X 视窗系统建立图形化用户界面等。本书通过先介绍程序设计理论，再以适当的例子和清晰的解释来阐明它的方式，帮助读者迅速掌握相关的知识。本书适合Linux 的初学者及希望利用Linux 进行开发的程序人员阅读，也适合作为高等院校计算机相关专业师生的参考教材。
> - 出版时间： 2010-06-08 00:00:00
> - ISBN： 9787115228215
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/0cf329b0718ff5f10cf1c9f

# 高亮划线
### 2.6 shell的语法
> 📌 [shell脚本程序内部执行两类命令。一类是可以在命令提示符中执行的“普通”命令，也称为外部命令（external command），一类是我们前面提到的“内置”命令，也称为内部命令（internal command）。内置命令是在shell内部实现的，它们不能作为外部程序被调用。](<weread://bestbookmark?bookId=26211825&chapterUid=19&rangeStart=28769&rangeEnd=28909>)
> ⏱ 2023-02-07 23:10:11 ^26211825-19-28769-28909
### 3.1 Linux文件结构
> 📌 [目录也是文件，但它是一种特殊类型的文件。在现代的UNIX（包括Linux）版本中，即使是超级用户可能也不再被允许直接对目录进行写操作了。所有用户通常都使用上层的opendir/readdir接口来读取目录，而无需了解特定系统中目录实现的具体细节。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=765&rangeEnd=888>)
> ⏱ 2023-02-07 23:15:26 ^26211825-24-765-888
> 📌 [文件，除了本身包含的内容以外，它还会有一个名字和一些属性，即“管理信息”，包括文件的创建/修改日期和它的访问权限。这些属性被保存在文件的inode（节点）中，它是文件系统中的一个特殊的数据块，它同时还包含文件的长度和文件在磁盘上的存放位置。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=1138&rangeEnd=1258>)
> ⏱ 2023-02-07 23:20:06 ^26211825-24-1138-1258
> 📌 [目录是用于保存其他文件的节点号和名字的文件。目录文件中的每个数据项都是指向某个文件节点的链接，删除文件名就等于删除与之对应的链接（文件的节点号可以通过ls -i命令查看）。你可以通过使用ln命令在不同的目录中创建指向同一个文件的链接。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=1325&rangeEnd=1442>)
> ⏱ 2023-02-07 23:20:58 ^26211825-24-1325-1442
> 📌 [这个设备代表的是系统控制台。错误信息和诊断信息通常会被发送到这个设备。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=3211&rangeEnd=3246>)
> ⏱ 2023-02-11 16:55:27 ^26211825-24-3211-3246
> 📌 [如果一个进程有控制终端的话，那么特殊文件/dev/tty就是这个控制终端（键盘和显示屏，或键盘和窗口）的别名（逻辑设备）。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=3423&rangeEnd=3484>)
> ⏱ 2023-02-11 16:57:21 ^26211825-24-3423-3484
> 📌 [/dev/null文件是空（null）设备。所有写向这个设备的输出都将被丢弃，而读这个设备会立刻返回一个文件尾标志，所以在cp命令里可以把它用做复制空文件的源文件。](<weread://bestbookmark?bookId=26211825&chapterUid=24&rangeStart=3877&rangeEnd=3959>)
> ⏱ 2023-02-11 16:58:09 ^26211825-24-3877-3959
### 3.2 系统调用和设备驱动程序
> 📌 [操作系统的核心部分，即内核，是一组设备驱动程序。它们是一组对系统硬件进行控制的底层接口。](<weread://bestbookmark?bookId=26211825&chapterUid=25&rangeStart=570&rangeEnd=642>)
> ⏱ 2023-02-11 16:59:31 ^26211825-25-570-642

# 读书笔记

# 本书评论
