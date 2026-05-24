---
doc_type: weread-highlights-reviews
bookId: "25462418"
title: Java并发编程之美
reviewCount: 0
noteCount: 7
author: 翟陆续 薛宾田
cover: https://cdn.weread.qq.com/weread/cover/78/YueWen_25462418/t6_YueWen_25462418.jpg
readingStatus: "2"
progress: 15%
readingTime: 1小时57分钟
readingDate: 2022-01-23
isbn: 9787121349478
lastReadDate: 2022-02-12

---
# 元数据
> [!abstract] Java并发编程之美
> - ![ Java并发编程之美|200](https://cdn.weread.qq.com/weread/cover/78/YueWen_25462418/t6_YueWen_25462418.jpg)
> - 书名： Java并发编程之美
> - 作者： 翟陆续 薛宾田
> - 简介： Java并发编程无处不在，涉及的知识点多，要掌握并用好它并非易事。作者加多拥有在大型互联网公司阿里巴巴的丰富工作经验，遇到并解决了业务场景中很多实际的并发问题。本书是他对自己实践经验的总结与升华。为帮助读者解决学习中的各类痛点，作者将全书明确地分为基础篇、高级篇和实践篇，脉络清晰；全书以代码说话，辅以图表，让初学者能一步一步地深入堂奥，掌握并发编程的精髓。
> - 出版时间： 2018-10-01 00:00:00
> - ISBN： 9787121349478
> - 分类： 计算机-编程设计
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/81c32b507184869281c2a23

# 高亮划线
### 第1章 并发编程线程基础
> 📌 [线程是进程中的一个实体，线程本身是不会独立存在的。进程是代码在数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，线程则是进程的一个执行路径，一个进程中至少有一个线程，进程中的多个线程共享进程的资源。](<weread://bestbookmark?bookId=25462418&chapterUid=7&rangeStart=510&rangeEnd=615>)
> ⏱ 2022-01-23 17:41:30 ^25462418-7-510-615
> 📌 [操作系统在分配资源时是把资源分配给进程的，但是CPU资源比较特殊，它是被分配到线程的，因为真正要占用CPU运行的是线程，所以也说线程是CPU分配的基本单位。](<weread://bestbookmark?bookId=25462418&chapterUid=7&rangeStart=644&rangeEnd=722>)
> ⏱ 2022-01-23 17:47:46 ^25462418-7-644-722
> 📌 [在Java中，当我们启动main函数时其实就启动了一个JVM的进程，而main函数所在的线程就是这个进程中的一个线程，也称主线程。](<weread://bestbookmark?bookId=25462418&chapterUid=7&rangeStart=751&rangeEnd=816>)
> ⏱ 2022-01-23 17:48:17 ^25462418-7-751-816
> 📌 [一个进程中有多个线程，多个线程共享进程的堆和方法区资源，但是每个线程有自己的程序计数器和栈区域。](<weread://bestbookmark?bookId=25462418&chapterUid=7&rangeStart=1134&rangeEnd=1182>)
> ⏱ 2022-01-23 17:49:22 ^25462418-7-1134-1182
> 📌 [程序计数器是一块内存区域，用来记录线程当前要执行的指令地址。](<weread://bestbookmark?bookId=25462418&chapterUid=7&rangeStart=1211&rangeEnd=1241>)
> ⏱ 2022-01-23 17:50:39 ^25462418-7-1211-1241
#### 1.2 线程创建与运行
> 📌 [Java中有三种线程创建方式，分别为实现Runnable接口的run方法，继承Thread类并重写run的方法，使用FutureTask方式。](<weread://bestbookmark?bookId=25462418&chapterUid=8&rangeStart=440&rangeEnd=511>)
> ⏱ 2022-01-23 17:52:18 ^25462418-8-440-511
> 📌 [其实调用start方法后线程并没有马上执行而是处于就绪状态，这个就绪状态是指该线程已经获取了除CPU资源外的其他资源，等待获取CPU资源后才会真正处于运行状态。一旦run方法执行完毕，该线程就处于终止状态。](<weread://bestbookmark?bookId=25462418&chapterUid=8&rangeStart=1172&rangeEnd=1275>)
> ⏱ 2022-02-12 23:33:26 ^25462418-8-1172-1275

# 读书笔记

# 本书评论
