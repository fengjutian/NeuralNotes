---
doc_type: weread-highlights-reviews
bookId: "22987515"
title: 深入浅出Rust
reviewCount: 0
noteCount: 45
author: 范长春
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/515/22987515/t6_22987515.jpg
readingStatus: "4"
progress: 99%
readingTime: 5小时46分钟
readingDate: 2021-11-08
finishedDate: 2024-12-05
isbn: 9787111606420
lastReadDate: 2024-12-05

---
# 元数据
> [!abstract] 深入浅出Rust
> - ![ 深入浅出Rust|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/515/22987515/t6_22987515.jpg)
> - 书名： 深入浅出Rust
> - 作者： 范长春
> - 简介： 本书详细描述了Rust语言的基本语法，穿插讲解一部分高级使用技巧，并以更容易理解的方式解释其背后的设计思想。全书总共分五个部分。第一部分介绍Rust基本语法。第二部分介绍属于Rust独一无二的内存管理方式。这部分是本书的重点和核心所在，也是Rust语言的思想内核精髓之处。第三部分介绍Rust的抽象表达能力。第四部分介绍并发模型。在目前这个阶段，对并行编程的支持是新一代编程语言不可绕过的重要话题。第五部分介绍一些实用设施。Rust语言有许多创新，但它绝不是高高在上孤芳自赏的类型，设计者在设计过程中充分考虑了语言的工程实用性。
> - 出版时间： 2018-08-01 00:00:00
> - ISBN： 9787111606420
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/97d324d0715ec2fb97d76a6

# 高亮划线
### 第1章 与君初相见
> 📌 [Rust语言是一门系统编程语言，它有三大特点：运行快、防止段错误、保证线程安全。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=766&rangeEnd=832>)
> ⏱ 2021-08-08 15:51:40 ^22987515-5-766-832
> 📌 [系统级编程语言一般具有以下特点：❏ 可以在资源非常受限的环境下执行；❏ 运行时开销很小，非常高效；❏ 很小的运行库，甚至于没有；❏ 可以允许直接的内存操作。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=922&rangeEnd=1120>)
> ⏱ 2021-11-13 15:56:12 ^22987515-5-922-1120
> 📌 [Rust编译器的版本号采用了“语义化版本号”（Semantic Versioning）规划。在这个规则之下，版本格式为：主版本号．次版本号．修订号。版本号递增规则如下。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=1784&rangeEnd=1868>)
> ⏱ 2022-09-10 23:55:35 ^22987515-5-1784-1868
> 📌 [兼](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=2011&rangeEnd=2012>)
> ⏱ 2022-09-10 23:56:19 ^22987515-5-2011-2012
> 📌 [Rust的第一个正式版本号是1.0，是2015年5月发布的。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=2047&rangeEnd=2077>)
> ⏱ 2022-09-10 23:56:25 ^22987515-5-2047-2077
> 📌 [RLS（Rust Language Server）是官方提供的一个标准化的编辑器增强工具。它也是开源的，项目地址在https://github.com/rust-lang-nursery/rls。它是一个单独的进程，通过进程间通信给编辑器或者集成开发环境提供一些信息，实现比较复杂的功能，比如代码自动提示、跳转到定义、显示函数签名等。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=7496&rangeEnd=7663>)
> ⏱ 2022-09-11 00:02:14 ^22987515-5-7496-7663
> 📌 [Rust中的宏与C/C++中的宏是完全不一样的东西。简单点说，可以把它理解为一种安全版的编译期语法扩展。这里之所以使用宏，而不是函数，是因为标准输出宏可以完成编译期格式检查，更加安全。](<weread://bestbookmark?bookId=22987515&chapterUid=5&rangeStart=10400&rangeEnd=10492>)
> ⏱ 2022-09-15 13:16:12 ^22987515-5-10400-10492
### 第2章 变量和类型
> 📌 [局部变量声明一定是以关键字let开头，类型一定是跟在冒号：的后面。语法歧义更少，语法分析器更容易编写。](<weread://bestbookmark?bookId=22987515&chapterUid=6&rangeStart=763&rangeEnd=814>)
> ⏱ 2022-09-15 13:20:54 ^22987515-6-763-814
> 📌 [如果我们需要让变量是可写的，那么需要使用mut关键字](<weread://bestbookmark?bookId=22987515&chapterUid=6&rangeStart=1535&rangeEnd=1561>)
> ⏱ 2022-09-15 13:21:46 ^22987515-6-1535-1561
> 📌 [下划线表达的含义是“忽略这个变量绑定，后面不会再用到了”。](<weread://bestbookmark?bookId=22987515&chapterUid=6&rangeStart=3601&rangeEnd=3630>)
> ⏱ 2022-09-15 13:24:43 ^22987515-6-3601-3630
> 📌 [变量遮蔽在某些情况下非常有用，比如，我们需要在同一个函数内部把一个变量转换为另一个类型的变量，但又不想给它们起不同的名字。](<weread://bestbookmark?bookId=22987515&chapterUid=6&rangeStart=4266&rangeEnd=4327>)
> ⏱ 2022-09-15 13:25:25 ^22987515-6-4266-4327
### 第3章 语句和表达式
> 📌 [一个Rust程序，是从main函数开始执行的。](<weread://bestbookmark?bookId=22987515&chapterUid=7&rangeStart=557&rangeEnd=580>)
> ⏱ 2024-11-29 18:08:58 ^22987515-7-557-580
### 第4章 函数
> 📌 [在Rust中，有以下这些情况永远不会返回，它们的类型就是！。❏ panic！以及基于它实现的各种函数/宏，比如unimplemented! 、unreachable!；❏ 死循环loop {}；❏ 进程退出函数std::process::exit以及类似的libc中的exec一类函数。](<weread://bestbookmark?bookId=22987515&chapterUid=8&rangeStart=4438&rangeEnd=4671>)
> ⏱ 2022-10-16 20:57:33 ^22987515-8-4438-4671
### 第5章 trait
> 📌 [所有的trait中都有一个隐藏的类型Self（大写S）​，代表当前这个实现了此trait的具体类型。trait中定义的函数，也可以称作关联函数（associated function）​。函数的第一个参数如果是Self相关的类型，且命名为self（小写s）​，这个参数可以被称为“receiver”​（接收者）​。具有receiver参数的函数，我们称为“方法”​（method）​，可以通过变量实例使用小数点来调用。没有receiver参数的函数，我们称为“静态函数”​（static function）​，可以通过类型加双冒号：:的方式来调用。在Rust中，函数和方法没有本质区别。](<weread://bestbookmark?bookId=22987515&chapterUid=9&rangeStart=917&rangeEnd=1201>)
> ⏱ 2024-11-29 18:10:47 ^22987515-9-917-1201
> 📌 [没有receiver参数的方法（第一个参数不是self参数的方法）称作“静态方法”​。静](<weread://bestbookmark?bookId=22987515&chapterUid=9&rangeStart=5927&rangeEnd=5970>)
> ⏱ 2024-11-29 18:47:21 ^22987515-9-5927-5970
### 第6章 数组和字符串
> 📌 [数组中元素的占用空间大小必须是编译期确定的。数组本身所容纳的元素个数也必须是编译期确定的，执行阶段不可变](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=590&rangeEnd=642>)
> ⏱ 2022-11-05 23:45:16 ^22987515-10-590-642
> 📌 [对于两个数组类型，只有元素类型和元素个数都完全相同，这两个数组才是同类型的。数组与指针之间不能隐式转换。同类型的数组之间可以互相赋值](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=1020&rangeEnd=1086>)
> ⏱ 2024-11-30 23:06:11 ^22987515-10-1020-1086
> 📌 [把数组xs作为参数传给一个函数，这个数组并不会退化成一个指针。而是会将这个数组完整复制进这个函数。函数体内对数组的改动不会影响到外面的数组。](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=1321&rangeEnd=1391>)
> ⏱ 2024-11-30 23:06:22 ^22987515-10-1321-1391
> 📌 [在目前的标准库中，数组本身没有实现IntoIterator trait，但是数组切片是实现了的。所以我们可以直接在for in循环中使用数组切片，而不能直接使用数组本身。](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=2209&rangeEnd=2294>)
> ⏱ 2024-11-30 23:08:03 ^22987515-10-2209-2294
> 📌 [对数组取借用borrow操作，可以生成一个“数组切片”（Slice）。数组切片对数组没有“所有权”，我们可以把数组切片看作专门用于指向数组的指针，是对数组的另外一个“视图”。](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=2752&rangeEnd=2839>)
> ⏱ 2022-11-06 17:49:16 ^22987515-10-2752-2839
> 📌 [Slice与普通的指针是不同的，它有一个非常形象的名字：胖指针（fat pointer）。与这个概念相对应的概念是“动态大小类型”（Dynamic Sized Type, DST）。所谓的DST指的是编译阶段无法确定占用空间大小的类型。为了安全性，指向DST的指针一般是胖指针。](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=3822&rangeEnd=3961>)
> ⏱ 2022-11-06 18:40:54 ^22987515-10-3822-3961
> 📌 [str是Rust的内置类型。&str是对str的借用。Rust的字符串内部默认是使用utf-8编码格式的。而内置的char类型是4字节长度的，存储的内容是Unicode Scalar Value。所以，Rust里面的字符串不能视为char类型的数组，而更接近u8类型的数组](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=13270&rangeEnd=13410>)
> ⏱ 2022-11-06 21:02:59 ^22987515-10-13270-13410
> 📌 [String类型。它跟&str类型的主要区别是，它有管理内存空间的权力。](<weread://bestbookmark?bookId=22987515&chapterUid=10&rangeStart=14978&rangeEnd=15018>)
> ⏱ 2022-11-06 21:13:34 ^22987515-10-14978-15018
### 第7章 模式解构
> 📌 [Rust中模式解构功能设计得非常美观，它的原则是：构造和解构遵循类似的语法，我们怎么把一个数据结构组合起来的，我们就怎么把它拆解开来。](<weread://bestbookmark?bookId=22987515&chapterUid=11&rangeStart=1103&rangeEnd=1170>)
> ⏱ 2022-11-06 21:19:29 ^22987515-11-1103-1170
### 第11章 所有权和移动语义
> 📌 [“所有权”代表着以下意义：❏ 每个值在Rust中都有一个变量来管理它，这个变量就是这个值、这块内存的所有者；❏ 每个值在一个时间点上只有一个管理者；❏ 当变量所在的作用域结束的时候，变量以及它代表的值将会被销毁。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=1042&rangeEnd=1238>)
> ⏱ 2023-11-16 11:27:44 ^22987515-16-1042-1238
> 📌 [Rust中所有权转移的重要特点是，它是所有类型的默认语义。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=4723&rangeEnd=4778>)
> ⏱ 2023-11-16 15:15:35 ^22987515-16-4723-4778
> 📌 [Rust中，在普通变量绑定、函数传参、模式匹配等场景下，凡是实现了std::marker::Copy trait的类型，都会执行copy语义。基本类型，比如数字、字符、bool等，都实现了Copy trait，因此具备copy语义。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=6806&rangeEnd=6922>)
> ⏱ 2023-11-16 15:19:55 ^22987515-16-6806-6922
> 📌 [Copy这个trait在编译器的眼里代表的是什么意思呢？简单点总结就是，如果一个类型impl了Copy trait，意味着任何时候，我们都可以通过简单的内存复制（在C语言里按字节复制memcpy）实现该类型的复制，并且不会产生任何内存安全问题。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=10000&rangeEnd=10122>)
> ⏱ 2023-11-17 10:49:30 ^22987515-16-10000-10122
> 📌 [常见的数字类型、bool类型、共享借用指针&，都是具有Copy属性的类型。而Box、Vec、可写借用指针&mut等类型都是不具备Copy属性的类型。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=10965&rangeEnd=11047>)
> ⏱ 2023-11-17 10:53:54 ^22987515-16-10965-11047
> 📌 [我们可以认为，Rust中只有POD（C++语言中的Plain Old Data）类型才有资格实现Copy trait。在Rust中，如果一个类型只包含POD数据类型的成员，并且没有自定义析构函数，那它就是POD类型。比如：整数、浮点数、只包含POD类型的数组等，都属于POD类型；而Box String Vec等不能按字节复制的类型，都不属于POD类型。但是，反过来讲，也并不是所有满足POD的类型都应该实现Copy trait，是否实现Copy取决于业务需求。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=11630&rangeEnd=11861>)
> ⏱ 2023-11-17 10:55:17 ^22987515-16-11630-11861
> 📌 [所谓“析构函数”（destructor），是与“构造函数”（constructor）相对应的概念。“构造函数”是对象被创建的时候调用的函数，“析构函数”是对象被销毁的时候调用的函数。](<weread://bestbookmark?bookId=22987515&chapterUid=16&rangeStart=14515&rangeEnd=14606>)
> ⏱ 2023-11-17 10:59:12 ^22987515-16-14515-14606
### 第12章 借用和生命周期
> 📌 [变量对其管理的内存拥有所有权。这个所有权不仅可以被转移（move），还可以被借用（borrow）。](<weread://bestbookmark?bookId=22987515&chapterUid=17&rangeStart=1201&rangeEnd=1250>)
> ⏱ 2023-11-17 11:13:53 ^22987515-17-1201-1250
> 📌 [关于借用指针，有以下几个规则：❏ 借用指针不能比它指向的变量存在的时间更长。❏ &mut型借用只能指向本身具有mut修饰的变量，对于只读变量，不可以有&mut型借用。❏ &mut型借用指针存在的时候，被借用的变量本身会处于“冻结”状态。❏ 如果只有&型借用指针，那么能同时存在多个；如果存在&mut型借用指针，那么只能存在一个；如果同时有其他的&或者&mut型借用指针存在，那么会出现编译错误。](<weread://bestbookmark?bookId=22987515&chapterUid=17&rangeStart=3692&rangeEnd=4037>)
> ⏱ 2023-11-27 10:52:19 ^22987515-17-3692-4037
### 第13章 借用检查
> 📌 [Rust语言的核心特点是：在没有放弃对内存的直接控制力的情况下，实现了内存安全。](<weread://bestbookmark?bookId=22987515&chapterUid=18&rangeStart=519&rangeEnd=559>)
> ⏱ 2023-11-27 10:55:04 ^22987515-18-519-559
> 📌 [总的来说，Rust的设计者们在一系列的“内存不安全”的问题中观察到了这样的一个结论：Danger arises from Aliasing + Mutation](<weread://bestbookmark?bookId=22987515&chapterUid=18&rangeStart=883&rangeEnd=1037>)
> ⏱ 2023-11-27 10:56:44 ^22987515-18-883-1037
### 第14章 NLL（Non-Lexical-Lifetime）
> 📌 [Rust防范“内存不安全”代码的原则极其清晰明了。如果你对同一块内存存在多个引用，就不要试图对这块内存做修改；如果你需要对一块内存做修改，就不要同时保留多个引用。](<weread://bestbookmark?bookId=22987515&chapterUid=19&rangeStart=477&rangeEnd=558>)
> ⏱ 2024-11-27 14:30:30 ^22987515-19-477-558
### 第15章 内部可变性
> 📌 [Rust的borrow checker的核心思想是“共享不可变，可变不共享”​。但是只有这个规则是不够的，在某些情况下，我们的确需要在存在共享的情况下可变。为了让这种情况是可控的、安全的，Rust还设计了一种“内部可变性”​（interior mutability）​。](<weread://bestbookmark?bookId=22987515&chapterUid=20&rangeStart=436&rangeEnd=569>)
> ⏱ 2024-11-27 14:35:17 ^22987515-20-436-569
### 第18章 Panic
> 📌 [在Rust中，正常的错误处理应该尽量使用Result类型。Panic则是作为一种“fail fast”机制，处理那种万不得已的情况。](<weread://bestbookmark?bookId=22987515&chapterUid=23&rangeStart=2725&rangeEnd=2791>)
> ⏱ 2024-11-27 14:51:59 ^22987515-23-2725-2791
> 📌 [在Rust中，Panic的实现机制有两种方式：unwind和abort。❏ unwind方式在发生panic的时候，会一层一层地退出函数调用栈，在此过程中，当前栈内的局部变量还可以正常析构。❏ abort方式在发生panic的时候，会直接退出整个程序。](<weread://bestbookmark?bookId=22987515&chapterUid=23&rangeStart=3049&rangeEnd=3235>)
> ⏱ 2024-11-27 14:52:55 ^22987515-23-3049-3235
> 📌 [Rust中，通过unwind方式实现的panic，其内部的实现方式基本与C++的异常是一样的。而且，Rust提供了一些工具函数，可以让用户在代码中终止栈展开。示例如下：](<weread://bestbookmark?bookId=22987515&chapterUid=23&rangeStart=3753&rangeEnd=3837>)
> ⏱ 2024-11-27 15:05:47 ^22987515-23-3753-3837
### 第22章 闭包
> 📌 [闭包（closure）是一种匿名函数，具有“捕获”外部变量的能力。闭包有时候也被称作lambda表达式。它有两个特点：​（1）可以像函数一样被调用；​（2）可以捕获当前环境中的变量。](<weread://bestbookmark?bookId=22987515&chapterUid=28&rangeStart=431&rangeEnd=520>)
> ⏱ 2024-11-26 18:02:20 ^22987515-28-431-520
### 第23章 动态分派和静态分派
> 📌 [Rust可以同时支持“静态分派”​（static dispatch）和“动态分派”​（dynamic dispatch）​。](<weread://bestbookmark?bookId=22987515&chapterUid=29&rangeStart=444&rangeEnd=504>)
> ⏱ 2024-11-27 15:23:17 ^22987515-29-444-504
### 第24章 容器与迭代器
> 📌 [一个可以自动扩展容量的动态数组](<weread://bestbookmark?bookId=22987515&chapterUid=30&rangeStart=931&rangeEnd=946>)
> ⏱ 2024-12-05 09:24:17 ^22987515-30-931-946
> 📌 [一个Vec中能存储的元素个数最多为std::usize::MAX个，超过了会发生panic。](<weread://bestbookmark?bookId=22987515&chapterUid=30&rangeStart=2632&rangeEnd=2678>)
> ⏱ 2024-12-05 09:25:33 ^22987515-30-2632-2678
> 📌 [HashMap<K, V, S>是基于hash算法的存储一组键值对（key-value-pair）的容器。其中，泛型参数K是键的类型，V是值的类型，S是哈希算法的类型。](<weread://bestbookmark?bookId=22987515&chapterUid=30&rangeStart=4638&rangeEnd=4728>)
> ⏱ 2024-12-05 14:15:25 ^22987515-30-4638-4728

# 读书笔记

# 本书评论
