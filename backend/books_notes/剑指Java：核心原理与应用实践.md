---
doc_type: weread-highlights-reviews
bookId: "3300064178"
title: 剑指Java：核心原理与应用实践
reviewCount: 0
noteCount: 13
author: 尚硅谷教育
cover: https://cdn.weread.qq.com/weread/cover/95/cpplatform_skboprgsauzthfwythdrpa/t6_cpplatform_skboprgsauzthfwythdrpa1689310807.jpg
readingStatus: "2"
progress: 66%
readingTime: 3小时5分钟
readingDate: 2023-09-02
isbn: 9787121436642
lastReadDate: 2023-10-11

---
# 元数据
> [!abstract] 剑指Java：核心原理与应用实践
> - ![ 剑指Java：核心原理与应用实践|200](https://cdn.weread.qq.com/weread/cover/95/cpplatform_skboprgsauzthfwythdrpa/t6_cpplatform_skboprgsauzthfwythdrpa1689310807.jpg)
> - 书名： 剑指Java：核心原理与应用实践
> - 作者： 尚硅谷教育
> - 简介： 本书分为四大部分：第1～6章，初步认识Java的基础语法及主流编程工具的使用；第7～11章，详解Java面向对象编程语言的语法、核心编程思想、基础API等；第12～17章，介绍使用Java进行高级应用开发所需的API和基础原理；第18、19章，介绍了Java8～Java17版本的新特性。本书核心内容基于目前企业应用最主流的Java8进行讲解，读者可以直接进阶到最近的长期支持版本Java17。本书遵循深入浅出的原则编写，既有生动活泼的生活化案例讲解，又有干货满满的源码级分析，可以让读者轻松领会Java技术精髓，快速掌握Java开发技能。本书为每一个知识点的讲解都配备了案例，代码量庞大，如果读者跟随本书案例练习会大大提升自身的代码编写能力。本书配套名师视频教程，读者在学习过程中可结合视频学习，让你的Java进阶之路事半功倍，为后续的技术提升打下坚实的基础。 本书适合初学Java编程语言的自学者、编程爱好者学习，还适合各类院校计算机相关专业的师生作为教材或教辅资料使用，是Java编程语言入门的必备图书。
> - 出版时间： 2023-06-01 00:00:00
> - ISBN： 9787121436642
> - 分类： 计算机-计算机综合
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/5a132bd0813ab7f91g01828f

# 高亮划线
### 10.1 异常体系结构
> 📌 [Java将程序执行过程中发生的不正常情况称为异常。](<weread://bestbookmark?bookId=3300064178&chapterUid=83&rangeStart=620&rangeEnd=645>)
> ⏱ 2023-09-26 10:44:41 ^3300064178-83-620-645
> 📌 [编程的错误分为语法错误、逻辑错误、异常三种，其中语法错误和逻辑错误不属于异常。](<weread://bestbookmark?bookId=3300064178&chapterUid=83&rangeStart=770&rangeEnd=809>)
> ⏱ 2023-09-26 10:44:38 ^3300064178-83-770-809
> 📌 [Java将程序执行时可能发生的错误(Error)或异常(Exception)，都封装成了类，作为java.lang.Throwable的子类，即Throwable是所有错误或异常的超类。Throwable类中定义了子类通用的方法，当错误或异常发生时，则会创建对应异常类型的对象并且抛出。为什么子类又分为错误和异常呢？显然，二者的特点是不同的。](<weread://bestbookmark?bookId=3300064178&chapterUid=83&rangeStart=1221&rangeEnd=1392>)
> ⏱ 2023-09-26 10:46:37 ^3300064178-83-1221-1392
> 📌 [Java编译器将不会给出任何“你的程序代码可能发生某种运行时异常，你必须处理它”这样的校验和提醒，因此运行时异常又称为非受检异常。](<weread://bestbookmark?bookId=3300064178&chapterUid=83&rangeStart=2263&rangeEnd=2328>)
> ⏱ 2023-09-26 10:49:22 ^3300064178-83-2263-2328
> 📌 [编译器就会提醒“你的程序很可能发生××异常，你必须编写相应的处理代码”，而如果你此时不听建议，仍然不处理，那么编译就会不通过。这些异常称为受检异常。](<weread://bestbookmark?bookId=3300064178&chapterUid=83&rangeStart=2797&rangeEnd=2871>)
> ⏱ 2023-09-26 10:49:38 ^3300064178-83-2797-2871
### 10.3 异常类型的扩展
> 📌 [Java规定异常或错误的类型必须继承现有的Throwable或其子类。因为只有当对象是Throwable（或其子类之一）的实例时，才能通过Java虚拟机或throw语句抛出。](<weread://bestbookmark?bookId=3300064178&chapterUid=85&rangeStart=709&rangeEnd=796>)
> ⏱ 2023-09-28 11:13:15 ^3300064178-85-709-796
### 11.1 Object类
> 📌 [java.lang.Object类是类层次结构的根类，每个类（除了Object类本身）都使用Object类作为超类。一个类如果没有显式声明继承另一个类，则相当于默认继承了Object类。](<weread://bestbookmark?bookId=3300064178&chapterUid=88&rangeStart=421&rangeEnd=514>)
> ⏱ 2023-09-28 11:25:05 ^3300064178-88-421-514
> 📌 [如果要比较两个对象的内容是否相等，则需要调用equals方法](<weread://bestbookmark?bookId=3300064178&chapterUid=88&rangeStart=4370&rangeEnd=4400>)
> ⏱ 2023-09-28 11:55:59 ^3300064178-88-4370-4400
> 📌 [对于引用类型变量，“==”判断的不是属性信息，而是二者引用的是否是同一个对象，也就是地址是否相等。](<weread://bestbookmark?bookId=3300064178&chapterUid=88&rangeStart=5402&rangeEnd=5451>)
> ⏱ 2023-09-28 11:57:54 ^3300064178-88-5402-5451
### 11.2 包装类
> 📌 [包装类主要分为三种不同类型：数值类型（Byte、Short、Integer、Long、Float和Double）、Character类型、Boolean类型。](<weread://bestbookmark?bookId=3300064178&chapterUid=89&rangeStart=777&rangeEnd=856>)
> ⏱ 2023-09-28 14:20:53 ^3300064178-89-777-856
> 📌 [为什么Java语言当初不直接使用包装类来代替基本数据类型，使其成为纯面向对象的语言呢？Java语言最初保留基本数据类型的主要考量是性能。](<weread://bestbookmark?bookId=3300064178&chapterUid=89&rangeStart=894&rangeEnd=962>)
> ⏱ 2023-09-28 14:16:56 ^3300064178-89-894-962
### 12.3 List集合
> 📌 [List集合中的元素是有序的、可重复的](<weread://bestbookmark?bookId=3300064178&chapterUid=99&rangeStart=480&rangeEnd=499>)
> ⏱ 2023-10-11 13:48:39 ^3300064178-99-480-499
> 📌 [动态数组扩容并不是在原有连续的内存空间后进行简单的叠加，而是重新申请一块更大的新内存，并把现有容器中的元素逐个复制过去，然后销毁旧的内存。](<weread://bestbookmark?bookId=3300064178&chapterUid=99&rangeStart=4762&rangeEnd=4831>)
> ⏱ 2023-10-11 14:02:14 ^3300064178-99-4762-4831

# 读书笔记

# 本书评论
