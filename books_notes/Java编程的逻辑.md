---
doc_type: weread-highlights-reviews
bookId: "923038"
title: Java编程的逻辑
reviewCount: 0
noteCount: 58
author: 马俊昌
cover: https://cdn.weread.qq.com/weread/cover/7/YueWen_923038/t6_YueWen_923038.jpg
readingStatus: "4"
progress: 96%
readingTime: 15小时41分钟
readingDate: 2021-08-15
finishedDate: 2025-03-15
isbn: 9787111587729
lastReadDate: 2023-11-20

---
# 元数据
> [!abstract] Java编程的逻辑
> - ![ Java编程的逻辑|200](https://cdn.weread.qq.com/weread/cover/7/YueWen_923038/t6_YueWen_923038.jpg)
> - 书名： Java编程的逻辑
> - 作者： 马俊昌
> - 简介： 写一本关于编程的书，是我大概15年前就有的一个想法，当时，我体会到了编程中数据结构的美妙和神奇，有一种收获的喜悦和分享的冲动。这种收获是我反复阅读教程十几遍，花大量时间上机练习调试得到的，这是一个比较痛苦的过程。我想，如果把我学到的知识更为清晰易懂地表达出来，其他人不就可以掌握编程容易一些，并体会到那种喜悦了吗？不过，当时感觉自己学识太浅，要学习的东西太多，想一想也就算了。
> - 出版时间： 2018-01-01 00:00:00
> - ISBN： 9787111587729
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/b51320f05e159eb51b29226

# 高亮划线
### 第3章 类的基础
> 📌 [Java定义了8种基本数据类型：4种整型byte、short、int、long，两种浮点类型float、double，一种真假类型boolean，一种字符类型char。其他类型的数据都用类这个概念表达。](<weread://bestbookmark?bookId=923038&chapterUid=20&rangeStart=630&rangeEnd=757>)
> ⏱ 2021-08-15 22:17:26 ^923038-20-630-757
#### 3.1 类的基本概念
> 📌 [类也确实只是函数的容器，但类更多表示的是自定义数据类型。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=448&rangeEnd=502>)
> ⏱ 2021-12-08 13:02:10 ^923038-21-448-502
> 📌 [一个数据类型由其包含的属性以及该类型可以进行的操作组成，属性又可以分为是类型本身具有的属性，还是一个具体实例具有的属性](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=2182&rangeEnd=2241>)
> ⏱ 2022-05-06 13:13:43 ^923038-21-2182-2241
> 📌 [类变量和实例变量都叫成员变量，也就是类的成员，类变量也叫静态变量或静态成员变量。类方法和实例方法都叫成员方法，也都是类的成员，类方法也叫静态方法。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=2734&rangeEnd=2937>)
> ⏱ 2021-08-22 23:00:08 ^923038-21-2734-2937
> 📌 [类变量的时候，static修饰符是必需的，但public和final都不是必需的](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=3777&rangeEnd=3817>)
> ⏱ 2021-08-22 23:00:43 ^923038-21-3777-3817
> 📌 [❑ 类方法只能访问类变量，不能访问实例变量，可以调用其他的类方法，不能调用实例方法。
   ❑ 实例方法既能访问实例变量，也能访问类变量，既可以调用实例方法，也可以调用类方法。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=5264&rangeEnd=5378>)
> ⏱ 2021-08-22 23:02:50 ^923038-21-5264-5378
> 📌 [方法要执行需要被调用，而实例方法被调用，首先需要一个实例。实例也称为对象，我们可能会交替使用。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=5583&rangeEnd=5630>)
> ⏱ 2021-12-08 13:07:16 ^923038-21-5583-5630
> 📌 [STATIC_TWO=2；语句外面包了一个static {}，这叫静态初始化代码块。静态初始化代码块在类加载的时候执行，这是在任何对象创建之前，且只执行一次。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=8092&rangeEnd=8171>)
> ⏱ 2021-12-08 13:13:59 ^923038-21-8092-8171
> 📌 [这是this的第二个用法，用于在构造方法中调用其他构造方法。](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=10538&rangeEnd=10568>)
> ⏱ 2022-04-26 23:50:22 ^923038-21-10538-10568
> 📌 [每个类都至少要有一个构造方法，在通过new创建对象的过程中会被调用。但构造方法如果没什么操作要做，可以省略。Java编译器会自动生成一个默认构造方法，也没有具体操作。但一旦定义了构造方法，Java就不会再自动生成默认的](<weread://bestbookmark?bookId=923038&chapterUid=21&rangeStart=11224&rangeEnd=11333>)
> ⏱ 2022-05-06 13:49:00 ^923038-21-11224-11333
#### 3.3 代码的组织机制
> 📌 [默认情况下，类位于默认包下](<weread://bestbookmark?bookId=923038&chapterUid=23&rangeStart=1393&rangeEnd=1406>)
> ⏱ 2022-05-06 13:57:14 ^923038-23-1393-1406
> 📌 [如果什么修饰符都不写，它的可见性范围就是同一个包内，同一个包内的其他类可以访问，而其他包内的类则不可以访问。](<weread://bestbookmark?bookId=923038&chapterUid=23&rangeStart=4433&rangeEnd=4487>)
> ⏱ 2022-05-07 13:04:06 ^923038-23-4433-4487
> 📌 [需要说明的是，同一个包指的是同一个直接包，子包下的类并不能访问。比如，类shuo.laoma.Hello和shuo.laoma.inner.Test，其所在的包shuo.laoma和shuo.laoma.inner是两个完全独立的包，并没有逻辑上的联系，Hello类和Test类不能互相访问对方的包可见性方法和属性。](<weread://bestbookmark?bookId=923038&chapterUid=23&rangeStart=4516&rangeEnd=4674>)
> ⏱ 2022-05-07 13:04:55 ^923038-23-4516-4674
> 📌 [总结来说，可见性范围从小到大是：private < 默认(包) < protected < public。](<weread://bestbookmark?bookId=923038&chapterUid=23&rangeStart=4908&rangeEnd=5022>)
> ⏱ 2022-05-07 13:05:19 ^923038-23-4908-5022
#### 4.1 基本概念
> 📌 [为什么要有多态和动态绑定呢？创建对象的代码（ShapeManager以外的代码）和操作对象的代码（ShapeManager本身的代码），经常不在一起，操作对象的代码往往只知道对象是某种父类型，也往往只需要知道它是某种父类型就可以了。](<weread://bestbookmark?bookId=923038&chapterUid=25&rangeStart=11330&rangeEnd=11446>)
> ⏱ 2022-05-07 13:20:07 ^923038-25-11330-11446
> 📌 [可以说，多态和动态绑定是计算机程序的一种重要思维方式，使得操作对象的程序不需要关注对象的实际类型，从而可以统一处理不同对象，但又能实现每个对象的特有行为。](<weread://bestbookmark?bookId=923038&chapterUid=25&rangeStart=11494&rangeEnd=11571>)
> ⏱ 2022-05-07 13:20:19 ^923038-25-11494-11571
#### 4.2 继承的细节
> 📌 [重载是指方法名称相同但参数签名不同（参数个数、类型或顺序不同），重写是指子类重写与父类相同参数签名的方法](<weread://bestbookmark?bookId=923038&chapterUid=26&rangeStart=4725&rangeEnd=4777>)
> ⏱ 2022-04-29 13:24:31 ^923038-26-4725-4777
> 📌 [当有多个重名函数的时候，在决定要调用哪个函数的过程中，首先是按照参数类型进行匹配的，换句话说，寻找在所有重载版本中最匹配的，然后才看变量的动态类型，进行动态绑定。](<weread://bestbookmark?bookId=923038&chapterUid=26&rangeStart=6451&rangeEnd=6532>)
> ⏱ 2022-05-07 13:35:44 ^923038-26-6451-6532
> 📌 [重写时，子类方法不能降低父类方法的可见性。不能降低是指，父类如果是public，则子类也必须是public，父类如果是protected，子类可以是protected，也可以是public，即子类可以升级父类方法的可见性但不能降低。](<weread://bestbookmark?bookId=923038&chapterUid=26&rangeStart=9389&rangeEnd=9512>)
> ⏱ 2022-04-29 13:26:39 ^923038-26-9389-9512
> 📌 [有的时候我们不希望父类方法被子类重写，有的时候甚至不希望类被继承，可以通过final关键字实现。final关键字可以修饰变量，而这是final的另一种用法。一个Java类，默认情况下都是可以被继承的，但加了final关键字之后就不能被继承了](<weread://bestbookmark?bookId=923038&chapterUid=26&rangeStart=10273&rangeEnd=10393>)
> ⏱ 2022-05-07 13:45:13 ^923038-26-10273-10393
#### 4.4 为什么说继承是把双刃剑
> 📌 [继承为什么会有破坏力呢？主要是因为继承可能破坏封装，而封装可以说是程序设计的第一原则；](<weread://bestbookmark?bookId=923038&chapterUid=28&rangeStart=652&rangeEnd=695>)
> ⏱ 2022-04-29 13:30:48 ^923038-28-652-695
#### 5.1 接口的本质
> 📌 [接口声明了一组能力，但它自己并没有实现这个能力，它只是一个约定。接口涉及交互两方对象，一方需要实现这个接口，另一方使用这个接口，但双方对象并不直接互相依赖，它们只是通过接口间接交互](<weread://bestbookmark?bookId=923038&chapterUid=30&rangeStart=1411&rangeEnd=1520>)
> ⏱ 2022-05-08 13:24:52 ^923038-30-1411-1520
> 📌 [针对接口而非具体类型进行编程，是计算机程序的一种重要思维方式。](<weread://bestbookmark?bookId=923038&chapterUid=30&rangeStart=7595&rangeEnd=7633>)
> ⏱ 2022-05-07 12:18:20 ^923038-30-7595-7633
> 📌 [接口更重要的是降低了耦合，提高了灵活性。](<weread://bestbookmark?bookId=923038&chapterUid=30&rangeStart=7788&rangeEnd=7815>)
> ⏱ 2022-05-08 13:42:35 ^923038-30-7788-7815
> 📌 [接口也可以继承，一个接口可以继承其他接口，继承的基本概念与类一样，但与类不同的是，接口可以有多个父接口](<weread://bestbookmark?bookId=923038&chapterUid=30&rangeStart=8666&rangeEnd=8717>)
> ⏱ 2022-05-07 12:19:46 ^923038-30-8666-8717
#### 5.2 抽象类
> 📌 [抽象类就是抽象的类。抽象是相对于具体而言的，一般而言，具体类有直接对应的对象，而抽象类没有，它表达的是抽象概念，一般是具体类的比较上层的父类。](<weread://bestbookmark?bookId=923038&chapterUid=31&rangeStart=442&rangeEnd=520>)
> ⏱ 2022-05-08 14:29:19 ^923038-31-442-520
> 📌 [抽象类不能创建对象(比如，不能使用new Shape())，而具体类可以。](<weread://bestbookmark?bookId=923038&chapterUid=31&rangeStart=1248&rangeEnd=1337>)
> ⏱ 2022-05-08 16:27:54 ^923038-31-1248-1337
> 📌 [每个人都可能会犯错，减少错误不能只依赖人的优秀素质，还需要一些机制，使得一个普通人都容易把事情做对，而难以把事情做错。抽象类就是Java提供的这样一种机制。](<weread://bestbookmark?bookId=923038&chapterUid=31&rangeStart=2318&rangeEnd=2396>)
> ⏱ 2022-05-08 16:34:26 ^923038-31-2318-2396
> 📌 [抽象类和接口是配合而非替代关系，它们经常一起使用，接口声明能力，抽象类提供默认实现，实现全部或部分方法，一个接口经常有一个对应的抽象类。](<weread://bestbookmark?bookId=923038&chapterUid=31&rangeStart=2689&rangeEnd=2757>)
> ⏱ 2022-05-08 16:37:03 ^923038-31-2689-2757
#### 5.3 内部类的本质
> 📌 [类都对应于一个独立的Java源文件，但一个类还可以放在另一个类的内部，称之为内部类，相对而言，包含它的类称之为外部类。](<weread://bestbookmark?bookId=923038&chapterUid=32&rangeStart=428&rangeEnd=513>)
> ⏱ 2022-05-08 16:43:20 ^923038-32-428-513
> 📌 [内部类与包含它的外部类有比较密切的关系，而与其他类关系不大，定义在类内部，可以实现对外部完全隐藏，可以有更好的封装性，代码实现上也往往更为简洁。](<weread://bestbookmark?bookId=923038&chapterUid=32&rangeStart=566&rangeEnd=638>)
> ⏱ 2022-05-08 16:43:58 ^923038-32-566-638
> 📌 [内部类可以方便地访问外部类的私有变量，可以声明为private从而实现对外完全隐藏，相关代码写在一起，写法也更为简洁，这些都是内部类的好处。](<weread://bestbookmark?bookId=923038&chapterUid=32&rangeStart=866&rangeEnd=962>)
> ⏱ 2022-05-08 16:44:46 ^923038-32-866-962
#### 7.1 包装类
> 📌 [将基本类型转换为包装类的过程，一般称为“装箱”，而将包装类型转换为基本类型的过程，则称为“拆箱”。装箱/拆箱写起来比较烦琐，Java 5以后引入了自动装箱和拆箱技术，可以直接将基本类型赋值给引用类型，反之亦可，比如：](<weread://bestbookmark?bookId=923038&chapterUid=40&rangeStart=1499&rangeEnd=1607>)
> ⏱ 2022-05-08 19:11:09 ^923038-40-1499-1607
#### 8.1 基本概念和原理
> 📌 [Java有Java编译器和Java虚拟机，编译器将Java源代码转换为．class文件，虚拟机加载并运行．class文件。对于泛型类，Java编译器会将泛型代码转换为普通的非泛型代码，就像上面的普通Pair类代码及其使用代码一样，将类型参数T擦除，替换为Object，插入必要的强制类型转换。](<weread://bestbookmark?bookId=923038&chapterUid=48&rangeStart=3885&rangeEnd=4031>)
> ⏱ 2022-08-25 23:16:34 ^923038-48-3885-4031
> 📌 [泛型主要有两个好处：❑ 更好的安全性。❑ 更好的可读性。](<weread://bestbookmark?bookId=923038&chapterUid=48&rangeStart=4450&rangeEnd=4538>)
> ⏱ 2022-05-08 20:07:15 ^923038-48-4450-4538
> 📌 [开发环境（如Eclipse）会提示类型错误，即使没有好的开发环境，编译时Java编译器也会提示。这称之为类型安全，也就是说，通过使用泛型，开发环境和编译器能确保不会用错类型，为程序多设置一道安全防护网。](<weread://bestbookmark?bookId=923038&chapterUid=48&rangeStart=5155&rangeEnd=5282>)
> ⏱ 2022-08-25 23:37:50 ^923038-48-5155-5282
> 📌 [泛型类最常见的用途是作为容器类。所谓容器类，简单地说，就是容纳并管理多项数据的类。](<weread://bestbookmark?bookId=923038&chapterUid=48&rangeStart=5413&rangeEnd=5454>)
> ⏱ 2022-05-08 20:08:52 ^923038-48-5413-5454
#### 9.1 剖析ArrayList
> 📌 [对于ArrayList，它的特点是内部采用动态数组实现，这决定了以下几点。1）可以随机访问，按照索引位置进行访问效率很高，用算法描述中的术语，效率是O(1)，简单说就是可以一步到位。2）除非数组已排序，否则按照内容查找元素效率比较低，具体是O(N), N为数组内容长度，也就是说，性能与数组长度成正比。3）添加元素的效率还可以，重新分配和复制数组的开销被平摊了，具体来说，添加N个元素的效率为O(N)。4）插入和删除元素的效率比较低，因为需要移动元素，具体为O(N)。](<weread://bestbookmark?bookId=923038&chapterUid=52&rangeStart=19424&rangeEnd=20026>)
> ⏱ 2022-05-10 13:14:33 ^923038-52-19424-20026
#### 9.2 剖析LinkedList
> 📌 [用法上，LinkedList是一个List，但也实现了Deque接口，可以作为队列、栈和双端队列使用。实现原理上，LinkedList内部是一个双向链表，并维护了长度、头节点和尾节点，这决定了它有如下特点。1）按需分配空间，不需要预先分配很多空间。2）不可以随机访问，按照索引位置访问效率比较低，必须从头或尾顺着链接找，效率为O(N/2)。3）不管列表是否已排序，只要是按照内容查找元素，效率都比较低，必须逐个比较，效率为O(N)。4）在两端添加、删除元素的效率很高，为O(1)。5）在中间插入、删除元素，要先定位，效率比较低，为O(N)，但修改本身的效率很高，效率为O(1)。](<weread://bestbookmark?bookId=923038&chapterUid=53&rangeStart=14793&rangeEnd=15451>)
> ⏱ 2022-05-10 13:18:47 ^923038-53-14793-15451
#### 9.3 剖析ArrayDeque
> 📌 [ArrayDeque实现了双端队列，内部使用循环数组实现，这决定了它有如下特点。1）在两端添加、删除元素的效率很高，动态扩展需要的内存分配以及数组复制开销可以被平摊，具体来说，添加N个元素的效率为O(N)。2）根据元素内容查找和删除的效率比较低，为O(N)。3）与ArrayList和LinkedList不同，没有索引位置的概念，不能根据索引位置进行操作。](<weread://bestbookmark?bookId=923038&chapterUid=54&rangeStart=10565&rangeEnd=10970>)
> ⏱ 2022-05-10 13:23:24 ^923038-54-10565-10970
#### 10.1 剖析HashMap
> 📌 [Map有键和值的概念。一个键映射到一个值，Map按照键存储和访问值，键不能重复，即一个键只会存储一份，给同一个键重复设值会覆盖原来的值。](<weread://bestbookmark?bookId=923038&chapterUid=56&rangeStart=665&rangeEnd=785>)
> ⏱ 2022-05-11 12:07:18 ^923038-56-665-785
> 📌 [内部使用数组链表和哈希的方式进行实现，这决定了它有如下特点：1）根据键保存和获取值的效率都很高，为O(1)，每个单向链表往往只有一个或少数几个节点，根据hash值就可以直接快速定位；2）HashMap中的键值对没有顺序，因为hash值是随机的。](<weread://bestbookmark?bookId=923038&chapterUid=56&rangeStart=19243&rangeEnd=19451>)
> ⏱ 2022-05-11 12:11:38 ^923038-56-19243-19451
#### 10.2 剖析HashSet
> 📌 [HashMap，有如下特点：1）没有重复元素；2）可以高效地添加、删除元素、判断元素是否存在，效率都为O(1)；3）没有顺序。](<weread://bestbookmark?bookId=923038&chapterUid=57&rangeStart=6164&rangeEnd=6342>)
> ⏱ 2022-05-11 12:47:19 ^923038-57-6164-6342
#### 10.3 排序二叉树
> 📌 [排序二叉树也是二叉树，但它没有重复元素，而且是有序的二叉树。什么顺序呢？对每个节点而言：❑ 如果左子树不为空，则左子树上的所有节点都小于该节点；❑ 如果右子树不为空，则右子树上的所有节点都大于该节点。](<weread://bestbookmark?bookId=923038&chapterUid=58&rangeStart=1282&rangeEnd=1442>)
> ⏱ 2022-05-11 12:56:30 ^923038-58-1282-1442
#### 13.1 文件概述
> 📌 [流有输入流和输出流之分。输入流就是可以从中获取数据，输入流的实际提供者可以是键盘、文件、网络等；输出流就是可以向其中写入数据，输出流的实际目的地可以是显示终端、文件、网络等。](<weread://bestbookmark?bookId=923038&chapterUid=74&rangeStart=7143&rangeEnd=7282>)
> ⏱ 2022-05-19 12:00:30 ^923038-74-7143-7282
#### 15.1 线程的基本概念
> 📌 [线程表示一条单独的执行流，它有自己的程序执行计数器，有自己的栈。](<weread://bestbookmark?bookId=923038&chapterUid=86&rangeStart=590&rangeEnd=622>)
> ⏱ 2022-05-21 19:02:41 ^923038-86-590-622
> 📌 [怎么确认代码是在哪个线程中执行的呢？Thread有一个静态方法currentThread，返回当前执行的线程对象：](<weread://bestbookmark?bookId=923038&chapterUid=86&rangeStart=1866&rangeEnd=1923>)
> ⏱ 2022-05-26 12:54:31 ^923038-86-1866-1923
#### 15.2 理解synchronized
> 📌 [共享内存有两个重要问题，一个是竞态条件，另一个是内存可见性，解决这两个问题的一个方案是使用synchronized关键字](<weread://bestbookmark?bookId=923038&chapterUid=87&rangeStart=438&rangeEnd=498>)
> ⏱ 2022-11-20 22:27:35 ^923038-87-438-498
> 📌 [synchronized实例方法实际保护的是同一个对象的方法调用，确保同时只能有一个线程执行。再具体来说，synchronized实例方法保护的是当前实例对象，即this, this对象有一个锁和一个等待队列，锁只能被一个线程持有，其他试图获得同样锁的线程需要等待。执行synchronized实例方法的过程大致如下：](<weread://bestbookmark?bookId=923038&chapterUid=87&rangeStart=3189&rangeEnd=3374>)
> ⏱ 2022-11-20 22:49:43 ^923038-87-3189-3374
> 📌 [1）尝试获得锁，如果能够获得锁，继续下一步，否则加入等待队列，阻塞并等待唤醒。2）执行实例方法体代码。3）释放锁，如果等待队列上有等待的线程，从中取一个并唤醒，如果有多个等待的线程，唤醒哪一个是不一定的，不保证公平性。](<weread://bestbookmark?bookId=923038&chapterUid=87&rangeStart=3403&rangeEnd=3570>)
> ⏱ 2022-11-20 22:55:23 ^923038-87-3403-3570
> 📌 [synchronized保护的是对象而非代码，只要访问的是同一个对象的synchronized方法，即使是不同的代码，也会被同步顺序访问。](<weread://bestbookmark?bookId=923038&chapterUid=87&rangeStart=3772&rangeEnd=3886>)
> ⏱ 2022-11-20 22:55:36 ^923038-87-3772-3886
> 📌 [一般在保护变量时，需要在所有访问该变量的方法上加上synchronized。](<weread://bestbookmark?bookId=923038&chapterUid=87&rangeStart=4285&rangeEnd=4349>)
> ⏱ 2022-11-20 22:56:08 ^923038-87-4285-4349
#### 20.1 线程安全的机制
> 📌 [线程表示一条单独的执行流，每个线程有自己的执行计数器，有自己的栈，但可以共享内存，共享内存是实现线程协作的基础，但共享内存有两个问题，竞态条件和内存可见性](<weread://bestbookmark?bookId=923038&chapterUid=110&rangeStart=424&rangeEnd=501>)
> ⏱ 2022-11-23 11:27:11 ^923038-110-424-501
#### 21.1 Class类
> 📌 [Java中，类信息对应的类就是java.lang.Class。](<weread://bestbookmark?bookId=923038&chapterUid=116&rangeStart=482&rangeEnd=513>)
> ⏱ 2022-11-23 11:37:15 ^923038-116-482-513
#### 26.1 Lambda表达式
> 📌 [通过接口传递行为代码，就要传递一个实现了该接口的实例对象，在之前的章节中，最简洁的方式是使用匿名内部类，比如：](<weread://bestbookmark?bookId=923038&chapterUid=144&rangeStart=1655&rangeEnd=1710>)
> ⏱ 2023-11-17 11:43:00 ^923038-144-1655-1710
> 📌 [从以上内容可以看出，Lambda表达式与匿名内部类很像，主要就是简化了语法，那它是不是语法糖，内部实现其实就是内部类呢？答案是否定的，Java会为每个匿名内部类生成一个类，但Lambda表达式不会。Lambda表达式通常比较短，为每个表达式生成一个类会生成大量的类，性能会受到影响。](<weread://bestbookmark?bookId=923038&chapterUid=144&rangeStart=5693&rangeEnd=5886>)
> ⏱ 2023-11-17 13:39:34 ^923038-144-5693-5886
> 📌 [Lambda表达式不是匿名内部类，那它的类型到底是什么呢？是函数式接口。](<weread://bestbookmark?bookId=923038&chapterUid=144&rangeStart=6232&rangeEnd=6294>)
> ⏱ 2023-11-17 13:39:57 ^923038-144-6232-6294
#### 26.2 函数式数据处理：基本用法
> 📌 [代码更为直观易读了，但你可能会担心它的性能有问题。filter()和map()都需要对流中的每个元素操作一次，一起使用会不会就需要遍历两次呢？答案是否定的，只需要一次。实际上，调用filter()和map()都不会执行任何实际的操作，它们只是在构建操作的流水线，调用collect才会触发实际的遍历执行，在一次遍历中完成过滤、转换以及收集结果的任务。](<weread://bestbookmark?bookId=923038&chapterUid=145&rangeStart=3858&rangeEnd=4156>)
> ⏱ 2023-11-20 09:15:16 ^923038-145-3858-4156

# 读书笔记

# 本书评论
