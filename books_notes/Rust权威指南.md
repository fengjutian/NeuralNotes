---
doc_type: weread-highlights-reviews
bookId: "32435929"
title: Rust权威指南
reviewCount: 0
noteCount: 50
author: 史蒂夫·克拉伯尼克 卡罗尔·尼科尔斯
cover: https://cdn.weread.qq.com/weread/cover/17/YueWen_32435929/t6_YueWen_32435929.jpg
readingStatus: "4"
progress: 99%
readingTime: 8小时24分钟
readingDate: 2020-08-17
finishedDate: 2024-11-26
isbn: 9787121387067
lastReadDate: 2024-11-26

---
# 元数据
> [!abstract] Rust权威指南
> - ![ Rust权威指南|200](https://cdn.weread.qq.com/weread/cover/17/YueWen_32435929/t6_YueWen_32435929.jpg)
> - 书名： Rust权威指南
> - 作者： 史蒂夫·克拉伯尼克 卡罗尔·尼科尔斯
> - 简介： 本书由Rust核心开发团队编写而成，由浅入深地探讨了Rust语言的方方面面。从学习函数、选择数据结构及绑定变量入手，逐步介绍所有权、trait、生命周期、安全保证等高级概念，模式匹配、错误处理、包管理、函数式特性、并发机制等实用工具，以及两个完整的项目开发实战案例。 作为开源的系统级编程语言，Rust可以帮助你编写出更为快速且更为可靠的软件，在给予开发者底层控制能力的同时，通过深思熟虑的工程设计避免了传统语言带来的诸多麻烦。 本书被视为Rust开发工作的必读书目，适合所有希望评估、入门、提高和研究Rust语言的软件开发人员阅读。
> - 出版时间： 2020-05-01 00:00:00
> - ISBN： 9787121387067
> - 分类： 计算机-计算机综合
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/d733256071eeeed9d7322fd

# 高亮划线
### Hello, Cargo!
> 📌 [Cargo使用TOML（Tom's Obvious, Minimal Language）作为标准的配置格式](<weread://bestbookmark?bookId=32435929&chapterUid=12&rangeStart=2736&rangeEnd=2789>)
> ⏱ 2020-08-17 21:40:12 ^32435929-12-2736-2789
> 📌 [cargo build￼](<weread://bestbookmark?bookId=32435929&chapterUid=12&rangeStart=4645&rangeEnd=4697>)
> ⏱ 2020-08-17 21:41:08 ^32435929-12-4645-4697
> 📌 [./target/debug/hello_cargo # or .\target\debug\hello_cargo.exe on Windows](<weread://bestbookmark?bookId=32435929&chapterUid=12&rangeStart=5125&rangeEnd=5237>)
> ⏱ 2020-08-17 21:41:23 ^32435929-12-5125-5237
> 📌 [Cargo还提供了一个叫作cargo check的命令，你可以使用这个命令来快速检查当前的代码是否可以通过编译，而不需要花费额外的时间去真正生成可执行程序：
   $ cargo check](<weread://bestbookmark?bookId=32435929&chapterUid=12&rangeStart=6353&rangeEnd=6509>)
> ⏱ 2020-08-17 21:41:51 ^32435929-12-6353-6509
> 📌 [以Release模式进行构建
   当准备好发布自己的项目时，你可以使用命令cargo build --release在优化模式下构建并生成可执行程序。它生成的可执行文件会被放置在target/release目录下，而不是之前的target/debug目录下。这种模式会以更长的编译时间为代价来优化代码，从而使代码拥有更好的运行时性能。这也是存在两种不同的构建模式的原因。一种模式用于开发，它允许你快速地反复执行构建操作。而另一种模式则用于构建交付给用户的最终程序，这种构建场景不会经常发生，但却需要生成的代码拥有尽可能高效的运行时表现。值得指出的是，假如你想要对代码的运行效率进行基准测试，那么请确保你会通过cargo run --release命令进行构建，并使用target/release目录下的可执行程序完成基准测试。](<weread://bestbookmark?bookId=32435929&chapterUid=12&rangeStart=7399&rangeEnd=7913>)
> ⏱ 2020-08-17 21:42:48 ^32435929-12-7399-7913
### 处理一次猜测
> 📌 [在Rust中，变量都是默认不可变的](<weread://bestbookmark?bookId=32435929&chapterUid=16&rangeStart=2116&rangeEnd=2133>)
> ⏱ 2020-08-17 22:19:39 ^32435929-16-2116-2133
### 数据类型
> 📌 [标量类型是单个值类型的统称。Rust中内建了4种基础的标量类型：整数、浮点数、布尔值及字符。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=1691&rangeEnd=1744>)
> ⏱ 2020-08-27 12:19:43 ^32435929-23-1691-1744
> 📌 [有符号和无符号代表了一个整数类型是否拥有描述负数的能力。换句话说，对于有符号的整数类型来讲，数值需要一个符号来表示当前是否为正，而对于无符号的整数类型来讲，数值永远为正，不需要符号。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=2346&rangeEnd=2471>)
> ⏱ 2020-08-27 12:26:07 ^32435929-23-2346-2471
> 📌 [有符号数是通过二进制补码的形式来存储的。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=2551&rangeEnd=2571>)
> ⏱ 2020-08-27 12:26:11 ^32435929-23-2551-2571
> 📌 [Rust对于整数字面量的默认推导类型i32通常就是一个很好的选择：它在大部分情形下都是运算速度最快的那一个，即便是在64位系统上也是如此。较为特殊的两个整数类型usize和isize则主要用作某些集合的索引。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=3674&rangeEnd=3778>)
> ⏱ 2020-08-27 12:29:33 ^32435929-23-3674-3778
> 📌 [除了整数，Rust还提供了两种基础的浮点数类型，浮点数也就是带小数的数字。这两种类型是f32和f64，它们分别占用32位和64位空间。由于在现代CPU中f64与f32的运行效率相差无几，却拥有更高的精度，所以在Rust中，默认会将浮点数字面量的类型推导为f64。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=4469&rangeEnd=4627>)
> ⏱ 2020-08-27 12:30:00 ^32435929-23-4469-4627
> 📌 [Rust的布尔类型只拥有两个可能的值：true和false，它会占据单个字节的空间大小。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=5700&rangeEnd=5744>)
> ⏱ 2020-08-27 12:30:48 ^32435929-23-5700-5744
> 📌 [复合类型（compound type）可以将多个不同类型的值组合为一个类型。Rust提供了两种内置的基础复合类型：元组（tuple）和数组（array）。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=6825&rangeEnd=6963>)
> ⏱ 2020-08-27 12:32:52 ^32435929-23-6825-6963
> 📌 [元组是一种相当常见的复合类型，它可以将其他不同类型的多个值组合进一个复合类型中。元组还拥有一个固定的长度：你无法在声明结束后增加或减少其中的元素数量。](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=7031&rangeEnd=7106>)
> ⏱ 2020-08-27 12:39:52 ^32435929-23-7031-7106
> 📌 [我们同样可以在数组中存储多个值的集合。与元组不同，数组中的每一个元素都必须是相同的类型。Rust中的数组拥有固定的长度，一旦声明就再也不能随意更改大小，这与其他某些语言有所不同](<weread://bestbookmark?bookId=32435929&chapterUid=23&rangeStart=8352&rangeEnd=8467>)
> ⏱ 2020-08-27 12:42:11 ^32435929-23-8352-8467
### 函数
> 📌 [Rust代码使用蛇形命名法（snake case）来作为规范函数和变量名称的风格。蛇形命名法只使用小写的字母进行命名，并以下画线分隔单词。](<weread://bestbookmark?bookId=32435929&chapterUid=24&rangeStart=504&rangeEnd=600>)
> ⏱ 2020-08-27 12:56:34 ^32435929-24-504-600
### 什么是所有权
> 📌 [栈和堆都是代码在运行时可以使用的内存空间，不过它们通常以不同的结构组织而成。栈会以我们放入值时的顺序来存储它们，并以相反的顺序将值取出。这也就是所谓的“后进先出”策略。你可以把栈上的操作想象成堆放盘子：当你需要放置盘子时，你只能将它们放置在栈的顶部，而当你需要取出盘子时，你也只能从顶部取出。换句话说，你没有办法从中间或底部插入或移除盘子。用术语来讲，添加数据这一操作被称作入栈，移除数据则被称作出栈。](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=1180&rangeEnd=1381>)
> ⏱ 2023-01-15 15:59:22 ^32435929-29-1180-1381
> 📌 [• Rust中的每一个值都有一个对应的变量作为它的所有者。• 在同一时间内，值有且仅有一个所有者。• 当所有者离开自己的作用域时，它持有的值就会被释放掉。](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=2673&rangeEnd=2837>)
> ⏱ 2023-01-15 16:57:31 ^32435929-29-2673-2837
> 📌 [变量的作用域。简单来讲，作用域是一个对象在程序中有效的范围。假设有这样一个变量：](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=3112&rangeEnd=3179>)
> ⏱ 2023-11-03 14:29:17 ^32435929-29-3112-3179
> 📌 [对于字符串字面量而言，由于我们在编译时就知道其内容，所以这部分硬编码的文本被直接嵌入到了最终的可执行文件中。这就是访问字符串字面量异常高效的原因，而这些性质完全得益于字符串字面量的不可变性](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=5208&rangeEnd=5302>)
> ⏱ 2022-03-30 13:08:49 ^32435929-29-5208-5302
> 📌 [Rust提供了另一套解决方案：内存会自动地在拥有它的变量离开作用域后进行释放](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=6091&rangeEnd=6129>)
> ⏱ 2022-03-30 13:09:56 ^32435929-29-6091-6129
> 📌 [在C++中，这种在对象生命周期结束时释放资源的模式有时也被称作资源获取即初始化（Resource Acquisition Is Initialization， RAII）](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=6615&rangeEnd=6727>)
> ⏱ 2022-03-30 13:10:17 ^32435929-29-6615-6727
> 📌 [将一个值赋值给另一个变量时就会转移所有权。当一个持有堆数据的变量离开作用域时，它的数据就会被drop清理回收，除非这些数据的所有权移动到了另一个变量上。](<weread://bestbookmark?bookId=32435929&chapterUid=29&rangeStart=13731&rangeEnd=13807>)
> ⏱ 2023-02-18 21:52:37 ^32435929-29-13731-13807
### 不可恢复错误与panic!
> 📌 [代码里总是会出现一些令你束手无策的糟糕情形。为了应对这样的场景，Rust提供了一个特殊的panic! 宏。程序会在panic! 宏执行时打印出一段错误提示信息，展开并清理当前的调用栈，然后退出程序。](<weread://bestbookmark?bookId=32435929&chapterUid=56&rangeStart=399&rangeEnd=498>)
> ⏱ 2023-09-10 13:57:26 ^32435929-56-399-498
### 泛型数据类型
> 📌 [Result枚举拥有两个泛型：T和E。它也同样拥有两个变体：持有T类型值的Ok，以及一个持有E类型值的Err。](<weread://bestbookmark?bookId=32435929&chapterUid=62&rangeStart=6671&rangeEnd=6726>)
> ⏱ 2023-09-10 14:33:49 ^32435929-62-6671-6726
### trait：定义共享行为
> 📌 [类型的行为由该类型本身可供调用的方法组成。当我们可以在不同的类型上调用相同的方法时，我们就称这些类型共享了相同的行为。trait提供了一种将特定方法签名组合起来的途径，它定义了为达成某种目的所必需的行为集合。](<weread://bestbookmark?bookId=32435929&chapterUid=63&rangeStart=728&rangeEnd=832>)
> ⏱ 2023-11-27 11:18:44 ^32435929-63-728-832
### 闭包：能够捕获环境的匿名函数
> 📌 [Rust中的闭包是一种可以存入变量或作为参数传递给其他函数的匿名函数。你可以在一个地方创建闭包，然后在不同的上下文环境中调用该闭包来完成运算。](<weread://bestbookmark?bookId=32435929&chapterUid=81&rangeStart=400&rangeEnd=471>)
> ⏱ 2024-11-16 15:38:15 ^32435929-81-400-471
> 📌 [闭包的定义放置在=之后，它会被赋值给语句左侧的expensive_closure变量。为了定义闭包，我们需要以一对竖线（|）开始，并在竖线之间填写闭包的参数；之所以选择这样的写法是因为它与Smalltalk及Ruby中的闭包定义类似。这个闭包仅有一个名为num的参数，而当闭包需要多个参数时，我们需要使用逗号来分隔它们，例如|param1,param2|。](<weread://bestbookmark?bookId=32435929&chapterUid=81&rangeStart=5361&rangeEnd=5540>)
> ⏱ 2024-11-16 16:01:23 ^32435929-81-5361-5540
> 📌 [和fn定义的函数不同，闭包并不强制要求你标注参数和返回值的类型。Rust之所以要求我们在函数定义中进行类型标注，是因为类型信息是暴露给用户的显式接口的一部分。严格定义接口有助于所有人对参数和返回值的类型取得明确共识。但是，闭包并不会被用于这样的暴露接口：它们被存储在变量中，在使用时既不需要命名，也不会被暴露给代码库的用户。](<weread://bestbookmark?bookId=32435929&chapterUid=81&rangeStart=7375&rangeEnd=7537>)
> ⏱ 2024-11-16 16:06:21 ^32435929-81-7375-7537
### 使用迭代器处理元素序列
> 📌 [迭代器模式允许你依次为序列中的每一个元素执行某些任务。迭代器会在这个过程中负责遍历每一个元素并决定序列何时结束。](<weread://bestbookmark?bookId=32435929&chapterUid=82&rangeStart=397&rangeEnd=453>)
> ⏱ 2023-11-28 09:17:47 ^32435929-82-397-453
> 📌 [在Rust中，迭代器是惰性的（layzy）。这也就意味着创建迭代器后，除非你主动调用方法来消耗并使用迭代器，否则它们不会产生任何的实际效果。](<weread://bestbookmark?bookId=32435929&chapterUid=82&rangeStart=509&rangeEnd=579>)
> ⏱ 2023-11-28 09:18:14 ^32435929-82-509-579
> 📌 [调用next的方法也被称为消耗适配器（consuming adaptor）​，因为它们同样消耗了迭代器本身。以sum方法为例，这个方法会获取迭代器的所有权并反复调用next来遍历元素，进而导致迭代器被消耗。在迭代过程中，它会对所有元素进行求和并在迭代结束后将总和作为结果返回。](<weread://bestbookmark?bookId=32435929&chapterUid=82&rangeStart=3336&rangeEnd=3500>)
> ⏱ 2024-11-16 16:17:04 ^32435929-82-3336-3500
> 📌 [Iterator trait还定义了另外一些被称为迭代器适配器（iterator adaptor）的方法，这些方法可以使你将已有的迭代器转换成其他不同类型的迭代器。你可以链式地调用多个迭代器适配器完成一些复杂的操作，同时保持代码易于阅读。但因为所有的迭代器都是惰性的，所以你必须调用一个消耗适配器的方法才能从迭代器适配器中获得结果。](<weread://bestbookmark?bookId=32435929&chapterUid=82&rangeStart=4014&rangeEnd=4207>)
> ⏱ 2024-11-16 16:19:41 ^32435929-82-4014-4207
### 将包发布到crates.io上
> 📌 [我们可以使用三斜线（///）而不是双斜线来编写文档注释，并且可以在文档注释中使用Markdown语法来格式化内容。文档注释被放置在它所说明的条目之前。](<weread://bestbookmark?bookId=32435929&chapterUid=88&rangeStart=960&rangeEnd=1035>)
> ⏱ 2024-11-17 16:42:39 ^32435929-88-960-1035
> 📌 [文档注释形式 ：//!，它可以为包裹当前注释的外层条目（而不是紧随注释之后的条目）添加文档](<weread://bestbookmark?bookId=32435929&chapterUid=88&rangeStart=3370&rangeEnd=3415>)
> ⏱ 2024-11-17 19:22:30 ^32435929-88-3370-3415
> 📌 [使用pub use来重新导出部分条目](<weread://bestbookmark?bookId=32435929&chapterUid=88&rangeStart=5284&rangeEnd=5302>)
> ⏱ 2024-11-17 19:25:56 ^32435929-88-5284-5302
## 第15章 智能指针
> 📌 [指针（pointer）是一个通用概念，它指代那些包含内存地址的变量。这个地址被用于索引，或者说用于“指向”内存中的其他数据。](<weread://bestbookmark?bookId=32435929&chapterUid=93&rangeStart=589&rangeEnd=651>)
> ⏱ 2024-11-23 08:54:46 ^32435929-93-589-651
> 📌 [而智能指针（smart pointer）则是一些数据结构，它们的行为类似于指针但拥有额外的元数据和附加功能。](<weread://bestbookmark?bookId=32435929&chapterUid=93&rangeStart=777&rangeEnd=831>)
> ⏱ 2024-11-23 08:56:30 ^32435929-93-777-831
> 📌 [在拥有所有权和借用概念的Rust中，引用和智能指针之间还有另外一个差别：引用是只借用数据的指针；而与之相反地，大多数智能指针本身就拥有它们指向的数据。](<weread://bestbookmark?bookId=32435929&chapterUid=93&rangeStart=1047&rangeEnd=1149>)
> ⏱ 2024-11-23 08:58:03 ^32435929-93-1047-1149
### 使用Box<T>在堆上分配数据
> 📌 [装箱（box）是最为简单直接的一种智能指针，它的类型被写作Box<T>。装箱使我们可以将数据存储在堆上，并在栈中保留一个指向堆数据的指针。](<weread://bestbookmark?bookId=32435929&chapterUid=94&rangeStart=427&rangeEnd=509>)
> ⏱ 2024-11-23 09:00:29 ^32435929-94-427-509
> 📌 [除了将它们的数据存储在堆上而不是栈上，装箱没有其他任何的性能开销。当然，它们也无法提供太多的额外功能。装箱常常被用于下面的场景中：• 当你拥有一个无法在编译时确定大小的类型，但又想要在一个要求固定尺寸的上下文环境中使用这个类型的值时。• 当你需要传递大量数据的所有权，但又不希望产生大量数据的复制行为时。• 当你希望拥有一个实现了指定trait的类型值，但又不关心具体的类型时。](<weread://bestbookmark?bookId=32435929&chapterUid=94&rangeStart=559&rangeEnd=838>)
> ⏱ 2024-11-23 09:01:50 ^32435929-94-559-838
### 使用线程同时运行代码
> 📌 [在大部分现代操作系统中，执行程序的代码会运行在进程（process）中，操作系统会同时管理多个进程。类似地，程序内部也可以拥有多个同时运行的独立部分，用来运行这些独立部分的就叫作线程（thread）​。](<weread://bestbookmark?bookId=32435929&chapterUid=102&rangeStart=396&rangeEnd=497>)
> ⏱ 2024-11-23 09:09:19 ^32435929-102-396-497
> 📌 [由于多个线程可以同时运行，所以将程序中的计算操作拆分至多个线程可以提高性能。但这也增加了程序的复杂度，因为不同线程在执行过程中的具体顺序是无法确定的。这可能会导致一系列的问题，比如：](<weread://bestbookmark?bookId=32435929&chapterUid=102&rangeStart=526&rangeEnd=617>)
> ⏱ 2024-11-23 09:09:29 ^32435929-102-526-617
> 📌 [• 当多个线程以不一致的顺序访问数据或资源时产生的竞争状态（race condition）​。• 当两个线程同时尝试获取对方持有的资源时产生的死锁（deadlock）​，它会导致这两个线程无法继续运行。• 只会出现在特定情形下且难以稳定重现和修复的bug。](<weread://bestbookmark?bookId=32435929&chapterUid=102&rangeStart=647&rangeEnd=833>)
> ⏱ 2024-11-23 09:09:41 ^32435929-102-647-833
### 所有可以使用模式的场合
> 📌 [match表达式在形式上由match关键字、待匹配的值，以及至少一个匹配分支组合而成，而分支则由一个模式及匹配模式成功后应当执行的表达式组成：](<weread://bestbookmark?bookId=32435929&chapterUid=113&rangeStart=582&rangeEnd=653>)
> ⏱ 2024-11-25 19:25:18 ^32435929-113-582-653
### 可失败性：模式是否会匹配失败
> 📌 [模式可以被分为不可失败（irrefutable）和可失败（refutable）两种类型。](<weread://bestbookmark?bookId=32435929&chapterUid=114&rangeStart=400&rangeEnd=444>)
> ⏱ 2024-11-26 09:09:02 ^32435929-114-400-444
> 📌 [函数参数、let语句及for循环只接收不可失败模式，因为在这些场合下，我们的程序无法在值不匹配时执行任何有意义的行为。if let和while let表达式则只接收可失败模式，因为它们在被设计时就将匹配失败的情形考虑在内了：条件表达式的功能就是根据条件的成功与否执行不同的操作。](<weread://bestbookmark?bookId=32435929&chapterUid=114&rangeStart=663&rangeEnd=802>)
> ⏱ 2024-11-26 09:10:53 ^32435929-114-663-802
### 模式语法
> 📌 [我们可以使用...来匹配闭区间的值。](<weread://bestbookmark?bookId=32435929&chapterUid=115&rangeStart=2936&rangeEnd=2954>)
> ⏱ 2024-11-26 09:20:47 ^32435929-115-2936-2954
### 构建单线程Web服务器
> 📌 [Web服务器涉及的两个主要协议分别是超文本传输协议（HTTP）和传输控制协议（TCP）​。它们两者都是基于请求-响应（request-response）的协议，也就是说，这个协议由客户端发起请求，再由服务器监听并响应客户端。请求和响应的内容会由协议本身定义。](<weread://bestbookmark?bookId=32435929&chapterUid=125&rangeStart=528&rangeEnd=656>)
> ⏱ 2024-11-26 09:38:31 ^32435929-125-528-656
> 📌 [与new函数类似，代码中的bind函数会返回一个新的TcpListener实例。之所以选择bind作为函数的名称是因为在网络领域中，连接到端口这一行为也被称作“绑定到端口”​（binding to a port）​。](<weread://bestbookmark?bookId=32435929&chapterUid=125&rangeStart=2054&rangeEnd=2161>)
> ⏱ 2024-11-26 09:40:31 ^32435929-125-2054-2161

# 读书笔记

# 本书评论
