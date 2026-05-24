---
doc_type: weread-highlights-reviews
bookId: "3300039608"
title: Rust实战
reviewCount: 0
noteCount: 7
author: 蒂姆·麦克纳马拉
cover: https://cdn.weread.qq.com/weread/cover/48/cpPlatform_5a4QZ7yJotT3mo4L3Bi5bk/t6_cpPlatform_5a4QZ7yJotT3mo4L3Bi5bk.jpg
readingStatus: "2"
progress: 50%
readingTime: 2小时39分钟
readingDate: 2023-02-24
isbn: 9787115591395
lastReadDate: 2025-04-03

---
# 元数据
> [!abstract] Rust实战
> - ![ Rust实战|200](https://cdn.weread.qq.com/weread/cover/48/cpPlatform_5a4QZ7yJotT3mo4L3Bi5bk/t6_cpPlatform_5a4QZ7yJotT3mo4L3Bi5bk.jpg)
> - 书名： Rust实战
> - 作者： 蒂姆·麦克纳马拉
> - 简介： 本书通过探索多种系统编程概念和技术引入Rust编程语言，在深入探索计算机工作原理的同时，帮助读者了解Rust的所有权系统、Trait、包管理、错误处理、条件编译等概念，并通过源自现实的示例来帮助读者了解Rust中的内存模型、文件操作、多线程、网络编程等内容。 本书旨在帮助读者理解如何用Rust进行系统编程，并提供了一些使用Rust编写代码的技巧。本书给出了10余个源自现实的示例，让读者不仅能了解Rust语法，还能了解Rust的实际运用。 本书适合所有对Rust感兴趣的读者阅读。要更好地掌握本书涵盖的内容，读者应具备一定的编程经验，至少应对计算机编程的基本概念有所了解。
> - 出版时间： 2022-09-01 00:00:00
> - ISBN： 9787115591395
> - 分类： 计算机-人工智能
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/ad032cb0813ab75f8g0181c1

# 高亮划线
### 第4章 生命周期、所有权和借用
> 📌 [借用检查依赖于3个紧密关联的概念：所有权、生命周期和借用。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=1082&rangeEnd=1111>)
> ⏱ 2025-04-03 14:47:29 ^3300039608-12-1082-1111
> 📌 [● 所有权(ownership)是一个引申而来的比喻，它与产权是没有关系的。在Rust中，所有权与针对不再需要的值的清理有关。举例来说，当一个函数返回后，在内存中该函数的局部变量需要被释放。再比如，值的所有者并不能阻止程序的其他部分访问它们的值，它们也不会向某些Rust“最高权威”去报告数据的盗用行为。● 值的生命周期是一个时间段，在此时间段内对该值的访问是有效的行为。一个函数的局部变量，在此函数返回前都是存活的。而全局变量，可能在程序的生命期内都是存活的。● 借用一个值意味着要访问它。这个术语会使人有点儿困惑，因为并没有义务将该值返还其所有者。它主要是用来强调，虽然值可能只有一个所有者，但是程序的许多部分都有可能会共享对这些值的访问。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=1140&rangeEnd=1520>)
> ⏱ 2025-04-03 14:48:46 ^3300039608-12-1140-1520
> 📌 [在Rust的世界里，所有权的概念是相当有限的：一个所有者在它的值的生命周期结束时将被清理。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=10008&rangeEnd=10053>)
> ⏱ 2025-04-03 14:49:21 ^3300039608-12-10008-10053
> 📌 [当值超出了作用域，或者由于其他原因它们的生命周期结束了，此时它们的析构器就会被调用。析构器是一个函数，通过删除引用、释放内存来从程序中清除对值的跟踪。在大多数的Rust代码中，你都找不到对任何析构器调用的代码。编译器会自行注入相应代码，并将其作为跟踪每个值生命周期的处理过程的一部分。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=10082&rangeEnd=10224>)
> ⏱ 2025-04-03 14:52:59 ^3300039608-12-10082-10224
> 📌 [所有权系统的意义在于，值不能存活得比它们的所有者更长。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=10390&rangeEnd=10417>)
> ⏱ 2025-04-03 14:53:28 ^3300039608-12-10390-10417
> 📌 [在Rust程序中，要将所有权从一个变量转移到另一个变量，有两种主要的方法。第一种是通过赋值来转移所有权。[插图]第二种方法是通过函数传递数据，](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=10720&rangeEnd=10885>)
> ⏱ 2025-04-03 14:57:36 ^3300039608-12-10720-10885
> 📌 [将其作为参数或返回值。](<weread://bestbookmark?bookId=3300039608&chapterUid=12&rangeStart=10885&rangeEnd=10896>)
> ⏱ 2025-04-03 14:57:53 ^3300039608-12-10885-10896

# 读书笔记

# 本书评论
