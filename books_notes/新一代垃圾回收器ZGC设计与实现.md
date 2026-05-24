---
doc_type: weread-highlights-reviews
bookId: "26307940"
title: 新一代垃圾回收器ZGC设计与实现
reviewCount: 0
noteCount: 2
author: 彭成寒
cover: https://cdn.weread.qq.com/weread/cover/47/YueWen_26307940/t6_YueWen_26307940.jpg
readingStatus: "2"
progress: 10%
readingTime: 0小时19分钟
readingDate: 2022-09-18
isbn: 9787111633655
lastReadDate: 2023-04-25

---
# 元数据
> [!abstract] 新一代垃圾回收器ZGC设计与实现
> - ![ 新一代垃圾回收器ZGC设计与实现|200](https://cdn.weread.qq.com/weread/cover/47/YueWen_26307940/t6_YueWen_26307940.jpg)
> - 书名： 新一代垃圾回收器ZGC设计与实现
> - 作者： 彭成寒
> - 简介： Java 11版本包含一个全新的垃圾收集器ZGC，它由Oracle开发，承诺在数TB的堆上具有非常低的暂停时间。ZGC是2017年Oracle公司贡献给OpenJDK社区的，正式成为OpenJDK的开源项目。ZGC 所针对的是这些在未来普遍存在的大容量内存：TB 级别的堆容量，具有很低的停顿时间（小于 10 毫秒），对整体应用性能的影响也很小（对吞吐量的影响低于 15％）。ZGC 所采用的机制也可以在未来进行扩展，以支持一些令人兴奋的特性，如多层堆（用于热对象的 DRAM 和用于低频访问对象的 NVMe 闪存）或压缩堆。本书详细介绍ZGC涉及的基本概念和运行原理，以及调优方法。主要内容共9章，主要内容有：垃圾回收器概述、ZGC内存管理、ZGC线程、ZGC垃圾回收算法的设计、ZGC日志解读、ZGC参数和基准测试、ZGC的编译调试、ZGC特性总结和展望、ZGC的编译调试、Shenandoah简介等。
> - 出版时间： 2019-07-01 00:00:00
> - ISBN： 9787111633655
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/7e5327d071916d647e51559

# 高亮划线
### 1.1 垃圾回收算法
> 📌 [引用计数法：在堆内存中分配对象时，会为对象分配一段额外的空间，这个空间用于维护一个计数器，如果对象增加了一个新的引用，则将增加计数器的值；如果一个引用关系失效，则减少计数器的值。当一个对象的计数器的值变为0，则说明该对象已经被废弃，处于不活跃状态，可以被回收。引用计数法需要解决循环依赖的问题，大家熟知的Python语言中的垃圾回收就使用了引用计数法。](<weread://bestbookmark?bookId=26307940&chapterUid=5&rangeStart=651&rangeEnd=827>)
> ⏱ 2023-04-25 15:02:23 ^26307940-5-651-827
> 📌 [可达性分析法（也称为根引用分析法），基本思路就是通过根集合（root set）作为起始点，从这些节点出发，根据引用关系开始搜索，所经过的路径称为引用链，当一个对象没有被任何引用链访问到时，则证明此对象是不活跃的，可以被回收。在JVM中常见的根（root）有线程栈帧（thread frame，用于跟踪线程中活跃对象）、符号表（symbol dictionary）、字符串表（string table）、对象监视器（object synchronizer）、元数据对象（universe）等，这些根共同构成了根集合。](<weread://bestbookmark?bookId=26307940&chapterUid=5&rangeStart=889&rangeEnd=1146>)
> ⏱ 2023-04-25 15:02:43 ^26307940-5-889-1146

# 读书笔记

# 本书评论
