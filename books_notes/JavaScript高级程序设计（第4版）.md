---
doc_type: weread-highlights-reviews
bookId: "34336683"
title: JavaScript高级程序设计（第4版）
reviewCount: 0
noteCount: 30
author: 马特·弗里斯比
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/683/34336683/t6_34336683.jpg
readingStatus: "4"
progress: 88%
readingTime: 21小时15分钟
readingDate: 2021-02-26
finishedDate: 2023-07-17
isbn: 9787115545381
lastReadDate: 2022-04-24

---
# 元数据
> [!abstract] JavaScript高级程序设计（第4版）
> - ![ JavaScript高级程序设计（第4版）|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/683/34336683/t6_34336683.jpg)
> - 书名： JavaScript高级程序设计（第4版）
> - 作者： 马特·弗里斯比
> - 简介： 本书是JavaScript经典图书的新版。第4版涵盖ECMAScript2019，全面、深入地介绍了JavaScript开发者必须掌握的前端开发技术，涉及JavaScript的基础特性和高级特性。书中详尽讨论了JavaScript的各个方面，从JavaScript的起源开始，逐步讲解到新出现的技术，其中重点介绍ECMAScript和DOM标准。在此基础上，接下来的各章揭示了JavaScript的基本概念，包括类、期约、迭代器、代理，等等。另外，书中深入探讨了客户端检测、事件、动画、表单、错误处理及JSON。本书同时也介绍了近几年来涌现的重要新规范，包括FetchAPI、模块、工作者线程、服务线程以及大量新API。
> - 出版时间： 2020-09-11 00:00:00
> - ISBN： 9787115545381
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/751326d0720befab7514782

# 高亮划线
### 3.4 数据类型
> 📌 [toString()返回数值的十进制字符串表示。而通过传入参数，可以得到数值的二进制、八进制、十六进制，或者其他任何有效基数的字符串表示，比如：](<weread://bestbookmark?bookId=34336683&chapterUid=26&rangeStart=18094&rangeEnd=18166>)
> ⏱ 2022-04-19 13:02:43 ^34336683-26-18094-18166
> 📌 [符号的用途是确保对象属性使用唯一标识符，不会发生属性冲突的危险。](<weread://bestbookmark?bookId=34336683&chapterUid=26&rangeStart=26355&rangeEnd=26387>)
> ⏱ 2022-04-19 13:07:54 ^34336683-26-26355-26387
> 📌 [Symbol.for()对每个字符串键都执行幂等操作。第一次使用某个字符串调用时，它会检查全局运行时注册表，发现不存在对应的符号，于是就会生成一个新符号实例并添加到注册表中。后续使用相同字符串的调用同样会检查注册表，发现存在与该字符串对应的符号，然后就会返回该符号实例。](<weread://bestbookmark?bookId=34336683&chapterUid=26&rangeStart=28710&rangeEnd=28845>)
> ⏱ 2022-04-21 12:48:49 ^34336683-26-28710-28845
> 📌 [可以使用Symbol.keyFor()来查询全局注册表，这个方法接收符号，返回该全局符号对应的字符串键。如果查询的不是全局符号，则返回undefined。](<weread://bestbookmark?bookId=34336683&chapterUid=26&rangeStart=29547&rangeEnd=29624>)
> ⏱ 2022-04-21 12:51:05 ^34336683-26-29547-29624
> 📌 [因为符号属性是对内存中符号的一个引用，所以直接创建并用作属性的符号不会丢失。但是，如果没有显式地保存对这些属性的引用，那么必须遍历对象的所有符号属性才能找到相应的属性键：](<weread://bestbookmark?bookId=34336683&chapterUid=26&rangeStart=31606&rangeEnd=31691>)
> ⏱ 2022-04-21 13:25:29 ^34336683-26-31606-31691
### 3.5 操作符
> 📌 [ECMAScript中的所有数值都以IEEE 754 64位格式存储，但位操作并不直接应用到64位表示，而是先把值转换为32位整数，再进行位操作，之后再把结果转换为64位。对开发者而言，就好像只有32位整数一样，因为64位整数存储格式是不可见的。](<weread://bestbookmark?bookId=34336683&chapterUid=27&rangeStart=5451&rangeEnd=5574>)
> ⏱ 2022-04-24 13:04:34 ^34336683-27-5451-5574
### 4.1 原始值与引用值
> 📌 [ECMAScript变量可以包含两种不同类型的数据：原始值和引用值。原始值（primitive value）就是最简单的数据，引用值（reference value）则是由多个值构成的对象。](<weread://bestbookmark?bookId=34336683&chapterUid=32&rangeStart=430&rangeEnd=577>)
> ⏱ 2022-04-24 13:09:04 ^34336683-32-430-577
> 📌 [保存原始值的变量是按值（by value）访问的，因为我们操作的就是存储在变量中的实际值。](<weread://bestbookmark?bookId=34336683&chapterUid=32&rangeStart=702&rangeEnd=773>)
> ⏱ 2022-04-24 13:11:22 ^34336683-32-702-773
> 📌 [保存引用值的变量是按引用（by reference）访问的。](<weread://bestbookmark?bookId=34336683&chapterUid=32&rangeStart=937&rangeEnd=993>)
> ⏱ 2022-04-24 13:11:33 ^34336683-32-937-993
> 📌 [ECMAScript中所有函数的参数都是按值传递的。](<weread://bestbookmark?bookId=34336683&chapterUid=32&rangeStart=3437&rangeEnd=3463>)
> ⏱ 2022-04-24 13:16:01 ^34336683-32-3437-3463
## 第5章 基本引用类型
> 📌 [引用类型有时候也被称为对象定义，因为它们描述了自己的对象应有的属性和方法。](<weread://bestbookmark?bookId=34336683&chapterUid=36&rangeStart=818&rangeEnd=881>)
> ⏱ 2021-02-26 13:08:16 ^34336683-36-818-881
> 📌 [对象被认为是某个特定引用类型的实例。新对象通过使用new操作符后跟一个构造函数（constructor）来创建](<weread://bestbookmark?bookId=34336683&chapterUid=36&rangeStart=1015&rangeEnd=1122>)
> ⏱ 2021-02-26 13:09:25 ^34336683-36-1015-1122
### 5.1 Date
> 📌 [Date类型将日期保存为自协调世界时（UTC, Universal Time Coordinated）时间1970年1月1日午夜（零时）至今所经过的毫秒数。使用这种存储格式，Date类型可以精确表示1970年1月1日之前及之后285616年的日期。](<weread://bestbookmark?bookId=34336683&chapterUid=37&rangeStart=472&rangeEnd=596>)
> ⏱ 2021-02-26 13:11:25 ^34336683-37-472-596
### 5.2 RegExp
> 📌 [ECMAScript通过RegExp类型支持正则表达式。正则表达式使用类似Perl的简洁语法来创建：[插图]](<weread://bestbookmark?bookId=34336683&chapterUid=38&rangeStart=426&rangeEnd=485>)
> ⏱ 2021-02-26 13:19:47 ^34336683-38-426-485
> 📌 [正则表达式也可以使用RegExp构造函数来创建，它接收两个参数：模式字符串和（可选的）标记字符串。](<weread://bestbookmark?bookId=34336683&chapterUid=38&rangeStart=2022&rangeEnd=2071>)
> ⏱ 2021-02-26 13:38:41 ^34336683-38-2022-2071
> 📌 [RegExp实例的主要方法是exec()，主要用于配合捕获组使用。这个方法只接收一个参数，即要应用模式的字符串。](<weread://bestbookmark?bookId=34336683&chapterUid=38&rangeStart=4695&rangeEnd=4751>)
> ⏱ 2021-02-26 13:50:40 ^34336683-38-4695-4751
> 📌 [正则表达式的另一个方法是test()，接收一个字符串参数。如果输入的文本与模式匹配，则参数返回true，否则返回false](<weread://bestbookmark?bookId=34336683&chapterUid=38&rangeStart=7887&rangeEnd=7944>)
> ⏱ 2021-02-26 13:56:40 ^34336683-38-7887-7944
### 5.3 原始值包装类型
> 📌 [引用类型与原始值包装类型的主要区别在于对象的生命周期。在通过new实例化引用类型后，得到的实例会在离开作用域时被销毁，而自动创建的原始值包装对象则只存在于访问它的那行代码执行期间。这意味着不能在运行时给原始值添加属性和方法](<weread://bestbookmark?bookId=34336683&chapterUid=39&rangeStart=1307&rangeEnd=1418>)
> ⏱ 2021-02-26 14:14:19 ^34336683-39-1307-1418
### 6.2 Array
> 📌 [ECMAScript也为数组提供了unshift()方法。顾名思义，unshift()就是执行跟shift()相反的操作：在数组开头添加任意多个值，然后返回新的数组长度。](<weread://bestbookmark?bookId=34336683&chapterUid=44&rangeStart=18316&rangeEnd=18401>)
> ⏱ 2021-02-27 16:36:59 ^34336683-44-18316-18401
> 📌 [方法slice()用于创建一个包含原有数组中一个或多个元素的新数组。slice()方法可以接收一个或两个参数：返回元素的开始索引和结束索引。如果只有一个参数，则slice()会返回该索引到数组末尾的所有元素。如果有两个参数，则slice()返回从开始索引到结束索引对应的所有元素，其中不包含结束索引对应的元素。记住，这个操作不影响原始数组。](<weread://bestbookmark?bookId=34336683&chapterUid=44&rangeStart=23405&rangeEnd=23575>)
> ⏱ 2021-02-27 16:56:47 ^34336683-44-23405-23575
### 8.2 创建对象
> 📌 [原型模式也不是没有问题。首先，它弱化了向构造函数传递初始化参数的能力，会导致所有实例默认都取得相同的属性值。虽然这会带来不便，但还不是原型的最大问题。原型的最主要问题源自它的共享特性。](<weread://bestbookmark?bookId=34336683&chapterUid=59&rangeStart=30573&rangeEnd=30665>)
> ⏱ 2021-02-28 14:58:21 ^34336683-59-30573-30665
### 16.2 样式
> 📌 [连字符表示法（用连字符分隔两个单词，如background-image）](<weread://bestbookmark?bookId=34336683&chapterUid=116&rangeStart=841&rangeEnd=877>)
> ⏱ 2021-04-06 22:50:22 ^34336683-116-841-877
> 📌 [大多数属性名会这样直接转换过来。但有一个CSS属性名不能直接转换，它就是float。因为float是JavaScript的保留字，所以不能用作属性名。DOM2 Style规定它在style对象中对应的属性应该是cssFloat。](<weread://bestbookmark?bookId=34336683&chapterUid=116&rangeStart=1175&rangeEnd=1289>)
> ⏱ 2021-04-06 22:51:14 ^34336683-116-1175-1289
### 20.2 跨上下文消息
> 📌 [跨文档消息，有时候也简称为XDM（cross-documentmessaging），是一种在不同执行上下文（如不同工作线程或不同源的页面）间传递信息的能力。](<weread://bestbookmark?bookId=34336683&chapterUid=143&rangeStart=453&rangeEnd=539>)
> ⏱ 2021-03-16 22:08:32 ^34336683-143-453-539
> 📌 [postMessage()方法接收3个参数：消息、表示目标接收源的字符串和可选的可传输对象的数组（只与工作线程相关）](<weread://bestbookmark?bookId=34336683&chapterUid=143&rangeStart=1001&rangeEnd=1059>)
> ⏱ 2021-03-16 22:06:34 ^34336683-143-1001-1059
## 第27章 工作者线程
> 📌 [工作者线程的价值所在：允许把主线程的工作转嫁给独立的实体，而不会改变现有的单线程模型。](<weread://bestbookmark?bookId=34336683&chapterUid=191&rangeStart=1218&rangeEnd=1261>)
> ⏱ 2021-03-16 22:13:09 ^34336683-191-1218-1261
### 27.1 工作者线程简介
> 📌 [JavaScript环境实际上是运行在托管操作系统中的虚拟环境。在浏览器中每打开一个页面，就会分配一个它自己的环境。这样，每个页面都有自己的内存、事件循环、DOM，等等。每个页面就相当于一个沙盒，不会干扰其他页面。对于浏览器来说，同时管理多个环境是非常简单的，因为所有这些环境都是并行执行的。使用工作者线程，浏览器可以在原始页面环境之外再分配一个完全独立的二级子环境。这个子环境不能与依赖单线程交互的API（如DOM）互操作，但可以与父环境并行执行代码。](<weread://bestbookmark?bookId=34336683&chapterUid=192&rangeStart=428&rangeEnd=736>)
> ⏱ 2021-03-16 22:17:22 ^34336683-192-428-736
> 📌 [工作者线程和线程确实有很多共同之处。❑ 工作者线程是以实际线程实现的。例如，Blink浏览器引擎实现工作者线程的WorkerThread就对应着底层的线程。❑ 工作者线程并行执行。虽然页面和工作者线程都是单线程JavaScript环境，每个环境中的指令则可以并行执行。❑ 工作者线程可以共享某些内存。工作者线程能够使用SharedArrayBuffer在多个环境间共享内容。虽然线程会使用锁实现并发控制，但JavaScript使用Atomics接口实现并发控制。](<weread://bestbookmark?bookId=34336683&chapterUid=192&rangeStart=887&rangeEnd=1286>)
> ⏱ 2021-03-16 22:17:48 ^34336683-192-887-1286
> 📌 [工作者线程与线程有很多类似之处，但也有重要的区别。❑ 工作者线程不共享全部内存。在传统线程模型中，多线程有能力读写共享内存空间。除了Shared-ArrayBuffer外，从工作者线程进出的数据需要复制或转移。❑ 工作者线程不一定在同一个进程里。通常，一个进程可以在内部产生多个线程。根据浏览器引擎的实现，工作者线程可能与页面属于同一进程，也可能不属于。例如，Chrome的Blink引擎对共享工作者线程和服务工作者线程使用独立的进程。❑ 创建工作者线程的开销更大。工作者线程有自己独立的事件循环、全局对象、事件处理程序和其他JavaScript环境必需的特性。创建这些结构的代价不容忽视](<weread://bestbookmark?bookId=34336683&chapterUid=192&rangeStart=1315&rangeEnd=1777>)
> ⏱ 2021-03-16 22:17:57 ^34336683-192-1315-1777
> 📌 [Web工作者线程规范中定义了三种主要的工作者线程：专用工作者线程、共享工作者线程和服务工作者线程。](<weread://bestbookmark?bookId=34336683&chapterUid=192&rangeStart=2089&rangeEnd=2183>)
> ⏱ 2021-03-16 22:19:59 ^34336683-192-2089-2183

# 读书笔记

# 本书评论
