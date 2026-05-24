---
doc_type: weread-highlights-reviews
bookId: "3300055404"
title: Go语言学习笔记
reviewCount: 0
noteCount: 12
author: 雨痕
cover: https://cdn.weread.qq.com/weread/cover/7/cpplatform_ktikkvlm6pmo6x9pr1ju5w/t6_cpplatform_ktikkvlm6pmo6x9pr1ju5w1681438651.jpg
readingStatus: "2"
progress: 22%
readingTime: 0小时53分钟
readingDate: 2025-03-24
isbn: 9787121291609
lastReadDate: 2025-04-08

---
# 元数据
> [!abstract] Go语言学习笔记
> - ![ Go语言学习笔记|200](https://cdn.weread.qq.com/weread/cover/7/cpplatform_ktikkvlm6pmo6x9pr1ju5w/t6_cpplatform_ktikkvlm6pmo6x9pr1ju5w1681438651.jpg)
> - 书名： Go语言学习笔记
> - 作者： 雨痕
> - 简介： 作为时下流行的一种系统编程语言，Go 简单易学，性能很好，且支持各类主流平台。已有大量项目采用 Go 编写，这其中就包括 Docker 等明星作品，其开发和执行效率早已被证明。 本书经四年多逐步完善，内容覆盖了语言、运行时、性能优化、工具链等各层面知识。且内容经大量读者反馈和校对，没有明显的缺陷和错误。上卷细致解析了语言规范相关细节，便于读者深入理解语言相关功能的使用方法和注意事项。下卷则对运行时源码做出深度剖析，引导读者透彻了解语言功能背后的支持环境和运行体系，诸如内存分配、垃圾回收和并发调度等。 本书不适合编程初学入门，可供有实际编程经验或正在使用Go 工作的人群参考。
> - 出版时间： 2016-06-01 00:00:00
> - ISBN： 9787121291609
> - 分类： 计算机-计算机综合
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/b2332230813ab7c24g0149aa

# 高亮划线
## 上卷 语言详解 基于Go 1.6
> 📌 [抛开语法样式不谈，单就类型和规则而言，Go与C99、C11相似之处颇多，这也是我能接受它被冠以“NextC”名号的重要原因。](<weread://bestbookmark?bookId=3300055404&chapterUid=6&rangeStart=874&rangeEnd=936>)
> ⏱ 2025-04-02 10:25:27 ^3300055404-6-874-936
> 📌 [可以说，Goroutine是Go最显著的特征。它用类协程的方式来处理并发单元，却又在运行时层面做了更深度的优化处理。这使得语法上的并发编程变得极为容易，无须处理回调，无须关注执行绪切换，仅一个关键字，简单而自然。](<weread://bestbookmark?bookId=3300055404&chapterUid=6&rangeStart=1676&rangeEnd=1782>)
> ⏱ 2025-04-02 10:29:48 ^3300055404-6-1676-1782
### 第2章 类型
> 📌 [作为静态类型语言，Go变量总是有固定的数据类型，类型决定了变量内存的长度和存储格式。我们只能修改变量值，无法改变类型。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=546&rangeEnd=605>)
> ⏱ 2025-04-02 10:39:43 ^3300055404-7-546-605
> 📌 [只是要注意，简短模式(short variable declaration)有些限制：定义变量，同时显式初始化。不能提供数据类型。只能用在函数内部。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=1572&rangeEnd=1739>)
> ⏱ 2025-04-02 10:47:14 ^3300055404-7-1572-1739
> 📌 [命名建议以字母或下画线开始，由多个字母、数字和下画线组合而成。区分大小写。使用驼峰(camel case)拼写格式。局部变量优先使用短名。不要使用保留关键字。不建议使用与预定义常量、类型、内置函数相同的名字。专有名词通常会全部大写，例如escapeHTML。尽管Go支持用汉字等Unicode字符命名，但从编程习惯上来说，这并不是好选择。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=4724&rangeEnd=5142>)
> ⏱ 2025-04-02 10:49:54 ^3300055404-7-4724-5142
> 📌 [常量值必须是编译期可确定的字符、字符串、数字或布尔值。可指定常量类型，或由编译器通过初始化值推断，不支持C/C++数字类型后缀。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=5962&rangeEnd=6026>)
> ⏱ 2025-04-02 11:08:56 ^3300055404-7-5962-6026
> 📌 [所谓引用类型(reference type)特指slice、map、channel这三种预定义类型。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=12719&rangeEnd=12769>)
> ⏱ 2025-04-02 11:15:34 ^3300055404-7-12719-12769
> 📌 [内置函数new按指定类型长度分配零值内存，返回指针，并不关心类型内部构造和初始化方式。而引用类型则必须使用make函数创建，编译器会将make转换为目标类型专用的创建函数（或指令）​，以确保完成全部内存分配和相关属性初始化。](<weread://bestbookmark?bookId=3300055404&chapterUid=7&rangeStart=12896&rangeEnd=13007>)
> ⏱ 2025-04-02 11:16:31 ^3300055404-7-12896-13007
### 第4章 函数
> 📌 [不管是指针、引用类型，还是其他类型参数，都是值拷贝传递(pass-by-value)。区别无非是拷贝目标对象，还是拷贝指针而已。在函数调用前，会为形参和返回值分配内存空间，并将实参拷贝到形参内存。](<weread://bestbookmark?bookId=3300055404&chapterUid=9&rangeStart=4884&rangeEnd=4982>)
> ⏱ 2025-04-02 11:36:18 ^3300055404-9-4884-4982
> 📌 [闭包(closure)是在其词法上下文中引用了自由变量的函数，或者说是函数和其引用的环境的组合体。](<weread://bestbookmark?bookId=3300055404&chapterUid=9&rangeStart=12481&rangeEnd=12530>)
> ⏱ 2025-04-08 08:54:29 ^3300055404-9-12481-12530
> 📌 [语句defer向当前函数注册稍后执行的函数调用。这些调用被称作延迟调用，因为它们直到当前函数执行结束前才被执行，常用于资源释放、解除锁定，以及错误处理等操作。](<weread://bestbookmark?bookId=3300055404&chapterUid=9&rangeStart=15237&rangeEnd=15316>)
> ⏱ 2025-04-08 08:55:15 ^3300055404-9-15237-15316
### 第5章 数据
> 📌 [定义数组类型时，数组长度必须是非负整型常量表达式，长度是类型组成部分。也就是说，元素类型相同，但长度不同的数组不属于同一类型。](<weread://bestbookmark?bookId=3300055404&chapterUid=10&rangeStart=9475&rangeEnd=9538>)
> ⏱ 2025-04-08 09:03:41 ^3300055404-10-9475-9538

# 读书笔记

# 本书评论
