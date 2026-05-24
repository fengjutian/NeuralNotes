---
doc_type: weread-highlights-reviews
bookId: "33692196"
title: C++ Primer（中文版）（第5版）
reviewCount: 0
noteCount: 21
author: 【美】Stanley B·Lippman Josée Lajoie Barbara E·Moo
cover: https://cdn.weread.qq.com/weread/cover/59/YueWen_33692196/t6_YueWen_33692196.jpg
readingStatus: "2"
progress: 36%
readingTime: 3小时17分钟
readingDate: 2020-11-26
isbn: 9787121155352
lastReadDate: 2021-12-11

---
# 元数据
> [!abstract] C++ Primer（中文版）（第5版）
> - ![ C++ Primer（中文版）（第5版）|200](https://cdn.weread.qq.com/weread/cover/59/YueWen_33692196/t6_YueWen_33692196.jpg)
> - 书名： C++ Primer（中文版）（第5版）
> - 作者： 【美】Stanley B·Lippman Josée Lajoie Barbara E·Moo
> - 简介： 这本久负盛名的C++经典教程，时隔八年之久，终于迎来史无前例的重大升级。除令全球无数程序员从中受益，甚至为之迷醉的——C++大师Stanley B. Lippman的丰富实践经验，C++标准委员会原负责人Josée Lajoie对C++标准的深入理解，以及C++先驱Barbara E. Moo在C++教学方面的真知灼见外，更是基于全新的C++11标准进行了全面而彻底的内容更新。非常难能可贵的是，书中所有示例均全部采用C++11标准改写，这在经典升级版中极其罕见——充分体现了C++语言的重大进展及其全面实践。书中丰富的教学辅助内容、醒目的知识点提示，以及精心组织的编程示范，让这本书在C++领域的权威地位更加不可动摇。无论是初学者入门，或是中高级程序员提升使用，本书均为不容置疑的首选。
> - 出版时间： 2013-09-01 00:00:00
> - ISBN： 9787121155352
> - 分类： 计算机-编程设计
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/ff732fe072021a24ff7bb24

# 高亮划线
#### 5.1 简单语句
> 📌 [复合语句（compound statement）是指用花括号括起来的（可能为空的）语句和声明的序列，复合语句也被称作块（block）。一个块就是一个作用域（参见2.2.4节，第43页），在块中引入的名字只能在块内部以及嵌套在块中的子块里访问。](<weread://bestbookmark?bookId=33692196&chapterUid=52&rangeStart=3239&rangeEnd=3402>)
> ⏱ 2021-07-18 21:11:23 ^33692196-52-3239-3402
#### 5.3 条件语句
> 📌 [switch语句（switch statement）提供了一条便利的途径使得我们能够在若干固定选项中做出选择。](<weread://bestbookmark?bookId=33692196&chapterUid=54&rangeStart=7123&rangeEnd=7185>)
> ⏱ 2021-07-21 13:52:44 ^33692196-54-7123-7185
#### 6.1 函数基础
> 📌 [语句块称为函数体（function body）。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=544&rangeEnd=568>)
> ⏱ 2021-07-22 22:36:42 ^33692196-61-544-568
> 📌 [函数的调用完成两项工作：一是用实参初始化函数对应的形参，二是将控制权转移给被调用函数。此时，主调函数（calling function）的执行被暂时中断，被调函数（called function）开始执行。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=1894&rangeEnd=2032>)
> ⏱ 2021-07-22 22:39:29 ^33692196-61-1894-2032
> 📌 [遇到一条return语句时函数结束执行过程。和函数调用一样，return语句也完成两项工作：一是返回return语句中的值（如果有的话），二是将控制权从被调函数转移回主调函数。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=2166&rangeEnd=2254>)
> ⏱ 2021-07-22 23:08:26 ^33692196-61-2166-2254
> 📌 [函数体是一个语句块。块构成一个新的作用域，我们可以在其中定义变量。形参和函数体内部定义的变量统称为局部变量（local variable）。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=5959&rangeEnd=6064>)
> ⏱ 2021-07-25 20:00:41 ^33692196-61-5959-6064
> 📌 [我们把只存在于块执行期间的对象称为自动对象（automatic object）。当块的执行结束后，块中创建的自动对象的值就变成未定义的了。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=6415&rangeEnd=6519>)
> ⏱ 2021-07-25 20:01:13 ^33692196-61-6415-6519
> 📌 [形参是一种自动对象。函数开始时为形参申请存储空间，因为形参定义在函数体作用域之内，所以一旦函数终止，形参也就被销毁。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=6548&rangeEnd=6606>)
> ⏱ 2021-07-25 20:01:21 ^33692196-61-6548-6606
> 📌 [局部静态对象（local static object）在程序的执行路径第一次经过对象定义语句时初始化，并且直到程序终止才被销毁，在此期间即使对象所在的函数结束执行也不会对它有影响。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=6967&rangeEnd=7064>)
> ⏱ 2021-07-25 20:02:10 ^33692196-61-6967-7064
> 📌 [函数声明也称作函数原型（function prototype）。](<weread://bestbookmark?bookId=33692196&chapterUid=61&rangeStart=8633&rangeEnd=8700>)
> ⏱ 2021-07-25 20:03:00 ^33692196-61-8633-8700
#### 6.2 参数传递
> 📌 [当形参是引用类型时，我们说它对应的实参被引用传递（passed by reference）或者函数被传引用调用（called by reference）。和其他引用一样，引用形参也是它绑定的对象的别名；也就是说，引用形参是它对应的实参的别名。当实参的值被拷贝给形参时，形参和实参是两个相互独立的对象。我们说这样的实参被值传递（passed by value）或者函数被传值调用（called by value）。](<weread://bestbookmark?bookId=33692196&chapterUid=62&rangeStart=849&rangeEnd=1224>)
> ⏱ 2021-07-25 20:05:00 ^33692196-62-849-1224
#### 6.3 返回类型和return语句
> 📌 [没有返回值的return语句只能用在返回类型是void的函数中。](<weread://bestbookmark?bookId=33692196&chapterUid=63&rangeStart=769&rangeEnd=801>)
> ⏱ 2021-07-25 20:09:09 ^33692196-63-769-801
#### 6.7 函数指针
> 📌 [函数的类型由它的返回类型和形参类型共同决定，与函数名无关。](<weread://bestbookmark?bookId=33692196&chapterUid=67&rangeStart=445&rangeEnd=474>)
> ⏱ 2021-08-12 19:20:09 ^33692196-67-445-474
### 第7章 类
> 📌 [类的基本思想是数据抽象（data abstraction）和封装（encapsulation）。数据抽象是一种依赖于接口（interface）和实现（implementation）分离的编程（以及设计）技术。类的接口包括用户所能执行的操作；类的实现则包括类的数据成员、负责接口实现的函数体以及定义类所需的各种私有函数。](<weread://bestbookmark?bookId=33692196&chapterUid=70&rangeStart=2590&rangeEnd=2889>)
> ⏱ 2021-12-04 23:50:50 ^33692196-70-2590-2889
#### 7.1 定义抽象数据类型
> 📌 [每个类都分别定义了它的对象被初始化的方式，类通过一个或几个特殊的成员函数来控制其对象的初始化过程，这些函数叫做构造函数（constructor）。构造函数的任务是初始化类对象的数据成员，无论何时只要类的对象被创建，就会执行构造函数。](<weread://bestbookmark?bookId=33692196&chapterUid=71&rangeStart=15252&rangeEnd=15403>)
> ⏱ 2021-12-11 21:49:56 ^33692196-71-15252-15403
> 📌 [构造函数的名字和类名相同。和其他函数不一样的是，构造函数没有返回类型；除此之外类似于其他的函数，构造函数也有一个（可能为空的）参数列表和一个（可能为空的）函数体。类可以包含多个构造函数，和其他重载函数差不多（参见6.4节，第206页），不同的构造函数之间必须在参数数量或参数类型上有所区别。](<weread://bestbookmark?bookId=33692196&chapterUid=71&rangeStart=15562&rangeEnd=15707>)
> ⏱ 2021-12-11 21:52:38 ^33692196-71-15562-15707
> 📌 [类通过一个特殊的构造函数来控制默认初始化过程，这个函数叫做默认构造函数（default constructor）。默认构造函数无须任何实参。](<weread://bestbookmark?bookId=33692196&chapterUid=71&rangeStart=16393&rangeEnd=16498>)
> ⏱ 2021-12-11 21:53:11 ^33692196-71-16393-16498
#### 7.2 访问控制与封装
> 📌 [在C++语言中，我们使用访问说明符（access specifiers）加强类的封装性：· 定义在public说明符之后的成员在整个程序内可被访问，public成员定义类的接口。· 定义在private说明符之后的成员可以被类的成员函数访问，但是不能被使用该类的代码访问，private部分封装了（即隐藏了）类的实现细节。](<weread://bestbookmark?bookId=33692196&chapterUid=72&rangeStart=497&rangeEnd=821>)
> ⏱ 2021-12-11 21:56:17 ^33692196-72-497-821
> 📌 [类可以允许其他类或者函数访问它的非公有成员，方法是令其他类或者函数成为它的友元（friend）。如果类想把一个函数作为它的友元，只需要增加一条以friend关键字开始的函数声明语句即可](<weread://bestbookmark?bookId=33692196&chapterUid=72&rangeStart=2909&rangeEnd=3036>)
> ⏱ 2021-12-11 21:58:41 ^33692196-72-2909-3036
> 📌 [友元声明只能出现在类定义的内部，但是在类内出现的具体位置不限。友元不是类的成员也不受它所在区域访问控制级别的约束。](<weread://bestbookmark?bookId=33692196&chapterUid=72&rangeStart=3496&rangeEnd=3553>)
> ⏱ 2021-12-11 22:02:53 ^33692196-72-3496-3553
> 📌 [封装有两个重要的优点：· 确保用户代码不会无意间破坏封装对象的状态。· 被封装的类的具体实现细节可以随时改变，而无须调整用户级别的代码。](<weread://bestbookmark?bookId=33692196&chapterUid=72&rangeStart=3973&rangeEnd=4119>)
> ⏱ 2021-12-11 22:05:16 ^33692196-72-3973-4119

# 读书笔记

# 本书评论
