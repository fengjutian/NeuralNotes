---
doc_type: weread-highlights-reviews
bookId: "840978"
title: Java核心技术·卷Ⅰ：基础知识（原书第10版）
reviewCount: 0
noteCount: 42
author: 凯S.霍斯特曼
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/978/840978/t6_840978.jpg
readingStatus: "4"
progress: 90%
readingTime: 10小时22分钟
readingDate: 2020-12-13
finishedDate: 2024-11-19
isbn: 9787111547426
lastReadDate: 2022-02-20

---
# 元数据
> [!abstract] Java核心技术·卷Ⅰ：基础知识（原书第10版）
> - ![ Java核心技术·卷Ⅰ：基础知识（原书第10版）|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/978/840978/t6_840978.jpg)
> - 书名： Java核心技术·卷Ⅰ：基础知识（原书第10版）
> - 作者： 凯S.霍斯特曼
> - 简介： 本书是《Java核心技术》第10版的卷Ⅰ。自《Java核心技术》出版以来，每个新版本都尽可能快地跟上Java开发工具箱发展的步伐，而且每一版都重新改写了部分内容，以便适应Java的最新特性。在这一版中，已经反映了Java标准版（Java SE 8）的特性。与前几版一样，本版仍然将读者群定位在那些打算将Java应用到实际工程项目中的程序设计人员。本书假设读者是一名具有程序设计语言（除Java之外）坚实背景知识的程序设计人员，并且不希望书中充斥着玩具式的示例（诸如，烤面包机、动物园的动物或神经质的跳动文本）。这些内容绝对不会在本书中出现。本书的目标是让读者充分理解书中介绍的Java语言及Java类库的相关特性，而不会产生任何误解。在本书中，我们选用大量的示例代码演示所讨论的每一个语言特性和类库特性。我们有意使用简单的示例程序以突出重点，然而，其中的大部分既不是赝品也没有偷工减料。它们将成为读者自己编写代码的良好开端。
> - 出版时间： 2016-09-01 00:00:00
> - ISBN： 9787111547426
> - 分类： 计算机-计算机综合
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/80a32bc05cd51280a170717

# 高亮划线
### 3.1 一个简单的Java应用程序
> 📌 [变量名必须是一个以字母开头并由字母或数字构成的序列。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=17425&rangeEnd=17451>)
> ⏱ 2022-02-12 21:31:24 ^840978-11-17425-17451
> 📌 [变量名中所有的字符都是有意义的，并且大小写敏感。变量名的长度基本上没有限制。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=17638&rangeEnd=17676>)
> ⏱ 2022-02-12 21:31:41 ^840978-11-17638-17676
> 📌 [声明一个变量之后，必须用赋值语句对变量进行显式初始化，千万不要使用未初始化的变量。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=19465&rangeEnd=19506>)
> ⏱ 2022-02-12 21:32:27 ^840978-11-19465-19506
> 📌 [在Java中，利用关键字final指示常量。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=21344&rangeEnd=21366>)
> ⏱ 2022-02-12 21:33:35 ^840978-11-21344-21366
> 📌 [在Java中，经常希望某个常量可以在一个类中的多个方法中使用，通常将这些常量称为类常量。可以使用关键字static final设置一个类常量。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=21666&rangeEnd=21737>)
> ⏱ 2022-02-12 21:37:50 ^840978-11-21666-21737
> 📌 [double类型使用64位存储一个数值，而有些处理器使用80位浮点寄存器。这些寄存器增加了中间过程的计算精度。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=22909&rangeEnd=22964>)
> ⏱ 2022-02-12 21:41:27 ^840978-11-22909-22964
> 📌 [对于使用strictfp关键字标记的方法必须使用严格的浮点计算来生成可再生的结果。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=23476&rangeEnd=23517>)
> ⏱ 2022-02-12 21:42:57 ^840978-11-23476-23517
> 📌 [于是，在main方法中的所有指令都将使用严格的浮点计算。如果将一个类标记为strictfp，这个类中的所有方法都要使用严格的浮点计算。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=23750&rangeEnd=23817>)
> ⏱ 2022-02-12 21:43:24 ^840978-11-23750-23817
> 📌 [要想通过控制台进行输入，首先需要构造一个Scanner对象，并与“标准输入流”System.in关联。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=59673&rangeEnd=59724>)
> ⏱ 2022-02-12 22:17:28 ^840978-11-59673-59724
> 📌 [注释：因为输入是可见的，所以Scanner类不适用于从控制台读取密码。Java SE 6特别引入了Console类实现这个目的。要想读取一个密码，可以采用下列代码：](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=61839&rangeEnd=61949>)
> ⏱ 2022-02-12 22:26:54 ^840978-11-61839-61949
> 📌 [格式说明符尾部的转换符将指示被格式化的数值类型：f表示浮点数，s表示字符串，d表示十进制整数](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=65500&rangeEnd=65546>)
> ⏱ 2022-02-12 22:37:51 ^840978-11-65500-65546
> 📌 [块（即复合语句）是指由一对大括号括起来的若干条简单的Java语句。块确定了变量的作用域。一个块可以嵌套在另一个块中。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=75087&rangeEnd=75145>)
> ⏱ 2022-02-12 23:10:16 ^840978-11-75087-75145
> 📌 [如果基本的整数和浮点数精度不能够满足需求，那么可以使用java.math包中的两个很有用的类：BigInteger和BigDecimal。这两个类可以处理包含任意长度数字序列的数值。BigInteger类实现了任意精度的整数运算，BigDecimal实现了任意精度的浮点数运算。](<weread://bestbookmark?bookId=840978&chapterUid=11&rangeStart=91274&rangeEnd=91413>)
> ⏱ 2022-02-12 23:12:50 ^840978-11-91274-91413
### 4.1 面向对象程序设计概述
> 📌 [首先从设计类开始，然后再往每个类中添加方法。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=4320&rangeEnd=4342>)
> ⏱ 2021-05-20 09:38:15 ^840978-13-4320-4342
> 📌 [在Java程序设计语言中，使用构造器（constructor）构造新实例。构造器是一种特殊的方法，用来构造并初始化对象。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=7463&rangeEnd=7551>)
> ⏱ 2021-05-20 10:05:22 ^840978-13-7463-7551
> 📌 [构造器的名字应该与类名相同。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=8252&rangeEnd=8266>)
> ⏱ 2021-05-20 10:05:07 ^840978-13-8252-8266
> 📌 [在构造Employee类的对象时，构造器会运行，以便将实例域初始化为所希望的状态。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=27617&rangeEnd=27658>)
> ⏱ 2021-05-20 10:42:18 ^840978-13-27617-27658
> 📌 [构造器与其他的方法有一个重要的不同。构造器总是伴随着new操作符的执行被调用，而不能对一个已经存在的对象调用构造器来达到重新设置实例域的目的。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=28154&rangeEnd=28225>)
> ⏱ 2021-05-20 10:43:14 ^840978-13-28154-28225
> 📌 [在Java中，为了实现一个私有的方法，只需将关键字public改为private即可。对于私有方法，如果改用其他方法实现相应的操作，则不必保留原有的方法。如果数据的表达方式发生了变化，这个方法可能会变得难以实现，或者不再需要。然而，只要方法是私有的，类的设计者就可以确信：它不会被外部的其他类操作调用，可以将其删去。如果方法是公有的，就不能将其删去，因为其他的代码很可能依赖它。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=36649&rangeEnd=36867>)
> ⏱ 2021-05-20 10:54:56 ^840978-13-36649-36867
> 📌 [可以将实例域定义为final。构建对象时必须初始化这样的域。也就是说，必须确保在每一个构造器执行之后，这个域的值被设置，并且在后面的操作中，不能够再对它进行修改。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=36954&rangeEnd=37035>)
> ⏱ 2021-05-20 10:57:58 ^840978-13-36954-37035
> 📌 [术语“static”有一段不寻常的历史。起初，C引入关键字static是为了表示退出一个块后依然存在的局部变量。在这种情况下，术语“static”是有意义的：变量一直存在，当再次进入该块时仍然存在。随后，static在C中有了第二种含义，表示不能被其他文件访问的全局变量和函数。为了避免引入一个新的关键字，关键字static被重用了。最后，C++第三次重用了这个关键字，与前面赋予的含义完全不一样，这里将其解释为：属于类且不属于类对象的变量和函数。这个含义与Java相同。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=43310&rangeEnd=43546>)
> ⏱ 2021-05-20 11:08:41 ^840978-13-43310-43546
> 📌 [Java程序设计语言总是采用按值调用。也就是说，方法得到的是所有参数值的一个拷贝，特别是，方法不能修改传递给它的任何参数变量的内容。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=47342&rangeEnd=47408>)
> ⏱ 2021-05-20 11:15:51 ^840978-13-47342-47408
> 📌 [有些类有多个构造器。](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=53588&rangeEnd=53598>)
> ⏱ 2021-05-20 11:23:23 ^840978-13-53588-53598
> 📌 [这种特征叫做重载（overloading）。如果多个方法（比如，StringBuilder构造器方法）有相同的名字、不同的参数，便产生了重载。编译器必须挑选出具体执行哪个方法，它通过用各个方法给出的参数类型与特定方法调用所使用的值类型进行匹配来挑选出相应的方法。如果编译器找不到匹配的参数，就会产生编译时错误，因为根本不存在匹配，或者没有一个比其他的更好。（这个过程被称为重载解析（overloading resolution）。）](<weread://bestbookmark?bookId=840978&chapterUid=13&rangeStart=54070&rangeEnd=54286>)
> ⏱ 2021-05-20 11:24:12 ^840978-13-54070-54286
### 7.1 处理错误
> 📌 [Error类层次结构描述了Java运行时系统的内部错误和资源耗尽错误。应用程序不应该抛出这种类型的对象。](<weread://bestbookmark?bookId=840978&chapterUid=19&rangeStart=3521&rangeEnd=3573>)
> ⏱ 2022-02-13 14:05:18 ^840978-19-3521-3573
> 📌 [在设计Java程序时，需要关注Exception层次结构。这个层次结构又分解为两个分支：一个分支派生于RuntimeException；另一个分支包含其他异常。划分两个分支的规则是：由程序错误导致的异常属于RuntimeException；而程序本身没有问题，但由于像I/O错误这类问题导致的异常属于其他异常。](<weread://bestbookmark?bookId=840978&chapterUid=19&rangeStart=3654&rangeEnd=3809>)
> ⏱ 2022-02-13 14:06:10 ^840978-19-3654-3809
> 📌 [派生于RuntimeException的异常包含下面几种情况：● 错误的类型转换。● 数组访问越界。● 访问null指针。不是派生于RuntimeException的异常包括：● 试图在文件尾部后面读取数据。● 试图打开一个不存在的文件。● 试图根据给定的字符串查找Class对象，而这个字符串表示的类并不存在。](<weread://bestbookmark?bookId=840978&chapterUid=19&rangeStart=3838&rangeEnd=4203>)
> ⏱ 2022-02-13 14:07:18 ^840978-19-3838-4203
> 📌 [Java语言规范将派生于Error类或RuntimeException类的所有异常称为非受查（unchecked）异常，所有其他的异常称为受查（checked）异常。](<weread://bestbookmark?bookId=840978&chapterUid=19&rangeStart=4522&rangeEnd=4605>)
> ⏱ 2022-02-13 14:19:43 ^840978-19-4522-4605
> 📌 [静态的Thread.getAllStackTrace方法，它可以产生所有线程的堆栈轨迹。下面给出使用这个方法的具体方式：](<weread://bestbookmark?bookId=840978&chapterUid=19&rangeStart=26858&rangeEnd=26918>)
> ⏱ 2022-02-20 14:34:00 ^840978-19-26858-26918
### 8.1 为什么要使用泛型程序设计
> 📌 [泛型程序设计（Generic programming）意味着编写的代码可以被很多不同类型的对象所重用。](<weread://bestbookmark?bookId=840978&chapterUid=21&rangeStart=890&rangeEnd=948>)
> ⏱ 2022-02-20 14:52:47 ^840978-21-890-948
> 📌 [一个泛型类（generic class）就是具有一个或多个类型变量的类。](<weread://bestbookmark?bookId=840978&chapterUid=21&rangeStart=4895&rangeEnd=4959>)
> ⏱ 2022-02-20 14:59:15 ^840978-21-4895-4959
### 9.1 Java集合框架
> 📌 [在Java类库中，集合类的基本接口是Collection接口。这个接口有两个基本方法：](<weread://bestbookmark?bookId=840978&chapterUid=23&rangeStart=4073&rangeEnd=4116>)
> ⏱ 2022-02-20 17:59:53 ^840978-23-4073-4116
> 📌 [通过反复调用next方法，可以逐个访问集合中的每个元素。但是，如果到达了集合的末尾，next方法将抛出一个NoSuchElementException。](<weread://bestbookmark?bookId=840978&chapterUid=23&rangeStart=4906&rangeEnd=4982>)
> ⏱ 2022-02-20 18:03:41 ^840978-23-4906-4982
> 📌 [在Java程序设计语言中，所有链表实际上都是双向链接的（doubly linked）——即每个结点还存放着指向前驱结点的引用](<weread://bestbookmark?bookId=840978&chapterUid=23&rangeStart=17279&rangeEnd=17369>)
> ⏱ 2022-02-20 18:15:42 ^840978-23-17279-17369
> 📌 [从链表中间删除一个元素是一个很轻松的操作，即需要更新被删除元素附近的链接](<weread://bestbookmark?bookId=840978&chapterUid=23&rangeStart=17646&rangeEnd=17682>)
> ⏱ 2022-02-20 18:16:25 ^840978-23-17646-17682
> 📌 [树集是一个有序集合（sorted collection）。可以以任意顺序将元素插入到集合中。在对集合进行遍历时，每个值将自动地按照排序后的顺序呈现](<weread://bestbookmark?bookId=840978&chapterUid=23&rangeStart=34410&rangeEnd=34483>)
> ⏱ 2022-02-20 18:34:05 ^840978-23-34410-34483
### 10.1 Swing概述
> 📌 [抽象窗口工具箱（Abstract Window Toolkit, AWT）](<weread://bestbookmark?bookId=840978&chapterUid=25&rangeStart=936&rangeEnd=973>)
> ⏱ 2021-07-01 23:11:20 ^840978-25-936-973
> 📌 [在Java中，顶层窗口（就是没有包含在其他窗口中的窗口）被称为框架（frame）。在AWT库中有一个称为Frame的类，用于描述顶层窗口。这个类的Swing版本名为JFrame，它扩展于Frame类。JFrame是极少数几个不绘制在画布上的Swing组件之一。因此，它的修饰部件（按钮、标题栏、图标等）由用户的窗口系统绘制，而不是由Swing绘制。](<weread://bestbookmark?bookId=840978&chapterUid=25&rangeStart=6454&rangeEnd=6628>)
> ⏱ 2021-07-01 23:20:29 ^840978-25-6454-6628
### 13.1 JAR文件
> 📌 [Java归档（JAR）文件就是为此目的而设计的。一个JAR文件既可以包含类文件，也可以包含诸如图像和声音这些其他类型的文件。此外，JAR文件是压缩的，它使用了大家熟悉的ZIP压缩格式。](<weread://bestbookmark?bookId=840978&chapterUid=31&rangeStart=1068&rangeEnd=1160>)
> ⏱ 2021-12-11 22:24:31 ^840978-31-1068-1160
> 📌 [除了类文件、图像和其他资源外，每个JAR文件还包含一个用于描述归档特征的清单文件（manifest）。清单文件被命名为MANIFEST.MF，它位于JAR文件的一个特殊META-INF子目录中。](<weread://bestbookmark?bookId=840978&chapterUid=31&rangeStart=2920&rangeEnd=3046>)
> ⏱ 2021-12-11 22:27:13 ^840978-31-2920-3046
### 14.1 什么是线程
> 📌 [一个程序同时执行多个任务。通常，每一个任务称为一个线程（thread），它是线程控制的简称。可以同时运行一个以上线程的程序称为多线程程序（multithreaded）。](<weread://bestbookmark?bookId=840978&chapterUid=33&rangeStart=653&rangeEnd=793>)
> ⏱ 2021-07-04 18:26:05 ^840978-33-653-793
> 📌 [多进程与多线程有哪些区别呢？本质的区别在于每个进程拥有自己的一整套变量，而线程则共享数据。](<weread://bestbookmark?bookId=840978&chapterUid=33&rangeStart=825&rangeEnd=926>)
> ⏱ 2021-12-11 22:32:27 ^840978-33-825-926

# 读书笔记

# 本书评论
