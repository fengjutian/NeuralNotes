---
doc_type: weread-highlights-reviews
bookId: "33692222"
title: 深入理解ES6
reviewCount: 0
noteCount: 17
author: 尼古拉斯·泽卡斯
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/222/33692222/t6_33692222.jpg
readingStatus: "4"
progress: 83%
readingTime: 8小时25分钟
readingDate: 2021-03-02
finishedDate: 2025-03-16
isbn: 9787121317989
lastReadDate: 2022-05-13

---
# 元数据
> [!abstract] 深入理解ES6
> - ![ 深入理解ES6|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/222/33692222/t6_33692222.jpg)
> - 书名： 深入理解ES6
> - 作者： 尼古拉斯·泽卡斯
> - 简介： 在整个JavaScript语言的发展历史中，ECMAScript 6代表了最大的核心变化。最新的ECMAScript 6不仅增加了新的对象类型，还添加了新的语法和令人兴奋的新功能。通过多年的研究和讨论，ECMAScript 6在2014年达到了功能完善的状态。但是要让所有的JavaScript环境都能支持ECMAScript 6还需要一段时间，因此还是有必要了解即将出现的以及已经可用的功能。
> - 出版时间： 2017-03-01 00:00:00
> - ISBN： 9787121317989
> - 分类： 计算机-编程设计
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/2333247072021a3e233f996

# 高亮划线
### 类的声明
> 📌 [函数声明可以被提升，而类声明与let声明类似，不能被提升；真正执行声明语句之前，它们会一直存在于临时死区中。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2090&rangeEnd=2145>)
> ⏱ 2022-04-29 21:56:10 ^33692222-76-2090-2145
> 📌 [类声明中的所有代码将自动运行在严格模式下，而且无法强行让代码脱离严格模式执行。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2176&rangeEnd=2215>)
> ⏱ 2022-04-29 21:58:31 ^33692222-76-2176-2215
> 📌 [在自定义类型中，需要通过Object.defineProperty()方法手工指定某个方法为不可枚举；而在类中，所有方法都是不可枚举的。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2246&rangeEnd=2314>)
> ⏱ 2022-04-29 21:59:00 ^33692222-76-2246-2314
> 📌 [每个类都有一个名为[[Construct]]的内部方法，通过关键字new调用那些不含[[Construct]]的方法会导致程序抛出错误。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2345&rangeEnd=2413>)
> ⏱ 2022-04-29 21:59:22 ^33692222-76-2345-2413
> 📌 [使用除关键字new以外的方式调用类的构造函数会导致程序抛出错误。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2444&rangeEnd=2476>)
> ⏱ 2022-04-29 21:59:33 ^33692222-76-2444-2476
> 📌 [在类中修改类名会导致程序报错。](<weread://bestbookmark?bookId=33692222&chapterUid=76&rangeStart=2507&rangeEnd=2522>)
> ⏱ 2022-04-29 21:59:47 ^33692222-76-2507-2522
### 类表达式
> 📌 [类和函数都有两种存在形式：声明形式和表达式形式。声明形式的函数和类都由相应的关键字（分别为function和class）进行定义，随后紧跟一个标识符；表达式形式的函数和类与之类似，只是不需要在关键字后添加标识符。类表达式的设计初衷是为了声明相应变量或传入函数作为参数](<weread://bestbookmark?bookId=33692222&chapterUid=77&rangeStart=414&rangeEnd=547>)
> ⏱ 2022-04-29 22:21:14 ^33692222-77-414-547
### 作为一等公民的类
> 📌 [在程序中，一等公民是指一个可以传入函数，可以从函数返回，并且可以赋值给变量的值。JavaScript函数是一等公民（也被称作头等函数），这也正是JavaScript中的一个独特之处。ECMAScript 6延续了这个传统，将类也设计为一等公民，允许通过多种方式使用类的特性。](<weread://bestbookmark?bookId=33692222&chapterUid=78&rangeStart=418&rangeEnd=584>)
> ⏱ 2022-04-29 22:39:07 ^33692222-78-418-584
> 📌 [调用类构造函数可以创建单例](<weread://bestbookmark?bookId=33692222&chapterUid=78&rangeStart=968&rangeEnd=981>)
> ⏱ 2022-04-29 22:47:06 ^33692222-78-968-981
### 可计算成员名称
> 📌 [类和对象字面量还有更多相似之处，类方法和访问器属性也支持使用可计算名称。](<weread://bestbookmark?bookId=33692222&chapterUid=80&rangeStart=417&rangeEnd=453>)
> ⏱ 2022-04-29 23:31:29 ^33692222-80-417-453
### 继承与派生类
> 📌 [当使用super()时切记以下几个关键点：· 只可在派生类的构造函数中使用super()，如果尝试在非派生类（不是用extends声明的类）或函数中使用则会导致程序抛出错误。· 在构造函数中访问this之前一定要调用super()，它负责初始化this，如果在调用super()之前尝试访问this会导致程序出错。· 如果不想调用super()，则唯一的方法是让类的构造函数返回一个对象。](<weread://bestbookmark?bookId=33692222&chapterUid=83&rangeStart=2414&rangeEnd=2725>)
> ⏱ 2022-04-30 17:23:06 ^33692222-83-2414-2725
> 📌 [派生类中的方法总会覆盖基类中的同名方法。](<weread://bestbookmark?bookId=33692222&chapterUid=83&rangeStart=2805&rangeEnd=2825>)
> ⏱ 2022-04-30 17:35:18 ^33692222-83-2805-2825
### 定型数组
> 📌 [定型数组是一种用于处理数值类型（正如其名，不是所有类型）数据的专用数组，](<weread://bestbookmark?bookId=33692222&chapterUid=89&rangeStart=409&rangeEnd=445>)
> ⏱ 2022-05-12 13:37:39 ^33692222-89-409-445
> 📌 [在JavaScript中，数字是以64位浮点格式存储的，并按需转换为32位整数，所以算术运算非常慢，无法满足WebGL的需求。因此在ECMAScript 6中引入定型数组来解决这个问题，并提供更高性能的算术运算。所谓定型数组，就是将任何数字转换为一个包含数字比特的数组，随后就可以通过我们熟悉的JavaScript数组方法来进一步处理。](<weread://bestbookmark?bookId=33692222&chapterUid=89&rangeStart=578&rangeEnd=746>)
> ⏱ 2022-05-12 13:38:09 ^33692222-89-578-746
### 用get陷阱验证对象结构（Object Shape）
> 📌 [get陷阱来检测，它接受3个参数：· trapTarget　被读取属性的源对象（代理的目标）。· key　要读取的属性键（字符串或Symbol）。· receiver　操作发生的对象（通常是代理）。](<weread://bestbookmark?bookId=33692222&chapterUid=107&rangeStart=1157&rangeEnd=1448>)
> ⏱ 2022-05-13 13:29:13 ^33692222-107-1157-1448
### 使用has陷阱隐藏已有属性
> 📌 [在代理中使用has陷阱可以拦截这些in操作并返回一个不同的值。每当使用in操作符时都会调用has陷阱，并传入两个参数：· trapTarget　读取属性的对象（代理的目标）。· key　要检查的属性键（字符串或Symbol）。](<weread://bestbookmark?bookId=33692222&chapterUid=108&rangeStart=812&rangeEnd=1082>)
> ⏱ 2022-05-13 13:35:39 ^33692222-108-812-1082
### 用deleteProperty陷阱防止删除属性
> 📌 [每当通过delete操作符删除对象属性时，deleteProperty陷阱都会被调用，它接受两个参数：· trapTarget　要删除属性的对象（代理的目标）。· key　要删除的属性键（字符串或Symbol）。](<weread://bestbookmark?bookId=33692222&chapterUid=109&rangeStart=985&rangeEnd=1219>)
> ⏱ 2022-05-13 13:42:21 ^33692222-109-985-1219

# 读书笔记

# 本书评论
