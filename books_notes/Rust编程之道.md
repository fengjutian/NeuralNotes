---
doc_type: weread-highlights-reviews
bookId: "25462644"
title: Rust编程之道
reviewCount: 0
noteCount: 14
author: 张汉东
cover: https://cdn.weread.qq.com/weread/cover/89/YueWen_25462644/t6_YueWen_25462644.jpg
readingStatus: "2"
progress: 87%
readingTime: 1小时8分钟
readingDate: 2023-02-24
isbn: 9787121354854
lastReadDate: 2024-12-09

---
# 元数据
> [!abstract] Rust编程之道
> - ![ Rust编程之道|200](https://cdn.weread.qq.com/weread/cover/89/YueWen_25462644/t6_YueWen_25462644.jpg)
> - 书名： Rust编程之道
> - 作者： 张汉东
> - 简介： Rust是一门利用现代化的类型系统，有机地融合了内存管理、所有权语义和混合编程范式的编程语言。它不仅能科学地保证程序的正确性，还能保证内存安全和线程安全。同时，还有能与C/C语言媲美的性能，以及能和动态语言媲美的开发效率。本书并非对语法内容进行简单罗列讲解，而是从四个维度深入全面且通透地介绍了Rust语言。从设计哲学出发，探索Rust语言的内在一致性；从源码分析入手，探索Rust地道的编程风格；从工程角度着手，探索Rust对健壮性的支持；从底层原理开始，探索Rust内存安全的本质。本书涵盖了Rust2018的特性，适合有一定编程经验且想要学习Rust的初学者，以及对Rust有一定的了解，想要继续深入学习的进阶者。
> - 出版时间： 2019-01-01 00:00:00
> - ISBN： 9787121354854
> - 分类： 计算机-编程设计
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/0303203071848774030b9d6

# 高亮划线
### 2.2 语句与表达式
> 📌 [语句又分为两种：声明语句（ Declaration statement）和表达式语句（ Expression statement）​。](<weread://bestbookmark?bookId=25462644&chapterUid=16&rangeStart=593&rangeEnd=688>)
> ⏱ 2024-12-09 10:31:46 ^25462644-16-593-688
### 2.3 变量与绑定
> 📌 [顾名思义，位置表达式就是表示内存位置的表达式。](<weread://bestbookmark?bookId=25462644&chapterUid=17&rangeStart=819&rangeEnd=842>)
> ⏱ 2024-12-09 10:40:44 ^25462644-17-819-842
> 📌 [从语义角度来说，位置表达式代表了持久性数据，值表达式代表了临时数据。](<weread://bestbookmark?bookId=25462644&chapterUid=17&rangeStart=1287&rangeEnd=1325>)
> ⏱ 2024-12-09 10:41:06 ^25462644-17-1287-1325
### 2.4 函数与闭包
> 📌 [Rust 语言的作用域是静态作用域，即词法作用域（Lexical Scope）。](<weread://bestbookmark?bookId=25462644&chapterUid=18&rangeStart=1934&rangeEnd=1978>)
> ⏱ 2024-12-09 10:44:04 ^25462644-18-1934-1978
> 📌 [这种连续用 let定义同名变量的做法叫变量遮蔽（Variable Shadow）​。但是最终的变量v的值是由第二个变量定义所决定的。变量遮蔽可以为日常开发提供诸多方便。](<weread://bestbookmark?bookId=25462644&chapterUid=18&rangeStart=2391&rangeEnd=2488>)
> ⏱ 2024-12-09 10:44:35 ^25462644-18-2391-2488
> 📌 [闭包也叫匿名函数。闭包有以下几个特点：· 可以像函数一样被调用。· 可以捕获上下文环境中的自由变量。· 可以自动推断输入和返回的类型。](<weread://bestbookmark?bookId=25462644&chapterUid=18&rangeStart=5527&rangeEnd=5681>)
> ⏱ 2024-12-09 10:46:34 ^25462644-18-5527-5681
> 📌 [但是闭包和函数有一个重要的区别，那就是闭包可以捕获外部变量，而函数不可以。](<weread://bestbookmark?bookId=25462644&chapterUid=18&rangeStart=6132&rangeEnd=6173>)
> ⏱ 2024-12-09 10:48:41 ^25462644-18-6132-6173
### 2.6 基本数据类型
> 📌 [Rust提供的基本数字类型大致可以分为三类：固定大小的类型、动态大小的类型和浮点数，分别介绍如下。](<weread://bestbookmark?bookId=25462644&chapterUid=20&rangeStart=1215&rangeEnd=1264>)
> ⏱ 2024-12-09 10:52:58 ^25462644-20-1215-1264
> 📌 [数组的类型签名为[T；N]。T是一个泛型标记，后面会具体介绍，它代表数组中元素的某个具体类型。N代表数组的长度，是一个编译时常量，必须在编译时确定其值。](<weread://bestbookmark?bookId=25462644&chapterUid=20&rangeStart=4689&rangeEnd=4769>)
> ⏱ 2024-12-09 10:53:48 ^25462644-20-4689-4769
> 📌 [Rust提供了原始的字符串类型str，也叫作字符串切片。它通常以不可变借用的形式存在，即&str。](<weread://bestbookmark?bookId=25462644&chapterUid=20&rangeStart=7442&rangeEnd=7502>)
> ⏱ 2024-12-09 10:57:25 ^25462644-20-7442-7502
> 📌 [我们将可以表示内存地址的类型称为指针。Rust 提供了多种类型的指针，包括引用（Reference）​、原生指针（Raw Pointer）​、函数指针（fn Pointer）和智能指针（Smart Pointer）​。](<weread://bestbookmark?bookId=25462644&chapterUid=20&rangeStart=8533&rangeEnd=8647>)
> ⏱ 2024-12-09 10:59:32 ^25462644-20-8533-8647
> 📌 [Rust中提供了一种特殊数据类型，never类型，即！。该类型用于表示永远不可能有返回值的计算类型](<weread://bestbookmark?bookId=25462644&chapterUid=20&rangeStart=9708&rangeEnd=9760>)
> ⏱ 2024-12-09 11:00:08 ^25462644-20-9708-9760
### 2.7 复合数据类型
> 📌 [元组（Tuple）是一种异构有限序列，形如（T，U，M，N）​。所谓异构，就是指元组内的元素可以是不同类型的；所谓有限，是指元组有固定的长度](<weread://bestbookmark?bookId=25462644&chapterUid=21&rangeStart=849&rangeEnd=918>)
> ⏱ 2024-12-09 11:25:38 ^25462644-21-849-918
> 📌 [Rust提供三种结构体：· 具名结构体（Named-Field Struct）· 元组结构体（Tuple-Like Struct）· 单元结构体（Unit-Like Struct）](<weread://bestbookmark?bookId=25462644&chapterUid=21&rangeStart=1893&rangeEnd=2070>)
> ⏱ 2024-12-09 11:27:15 ^25462644-21-1893-2070

# 读书笔记

# 本书评论
