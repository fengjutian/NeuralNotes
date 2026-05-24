---
doc_type: weread-highlights-reviews
bookId: "34105326"
title: Head First Go语言程序设计
reviewCount: 0
noteCount: 12
author: 杰伊·麦克格瑞恩
cover: https://cdn.weread.qq.com/weread/cover/98/YueWen_34105326/t6_YueWen_34105326.jpg
readingStatus: "4"
progress: 78%
readingTime: 3小时42分钟
readingDate: 2021-08-06
finishedDate: 2022-02-01
isbn: 9787111664932
lastReadDate: 2022-01-01

---
# 元数据
> [!abstract] Head First Go语言程序设计
> - ![ Head First Go语言程序设计|200](https://cdn.weread.qq.com/weread/cover/98/YueWen_34105326/t6_YueWen_34105326.jpg)
> - 书名： Head First Go语言程序设计
> - 作者： 杰伊·麦克格瑞恩
> - 简介： Go是为高性能网络和多处理而设计的， 但与python和javascript一样，该语言易于阅读和使用。通过这本实用的实践指南，读者将学习如何使用演示实际语言的清晰示例来编写Go代码。最重要的是，读者将会了解到用人单位希望入门级Go开发人员所知晓的惯例和技术。主要内容包括语法基础、条件和循环、函数、包、数组、映射、结构、封装和嵌入、接口、故障恢复、共享、自动化测试、Web应用程序等。
> - 出版时间： 2020-09-01 00:00:00
> - ISBN： 9787111664932
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/cc0329f0720867eecc0f00a

# 高亮划线
### 切片
> 📌 [与数组相同的是，切片由多个相同类型的元素构成。不同的是，切片允许我们在结尾追加更多的元素。](<weread://bestbookmark?bookId=34105326&chapterUid=163&rangeStart=398&rangeEnd=443>)
> ⏱ 2021-12-28 13:24:38 ^34105326-163-398-443
> 📌 [不像数组变量，声明切片变量并不会自动创建一个切片。为此，你可以调用内建的make函数。](<weread://bestbookmark?bookId=34105326&chapterUid=163&rangeStart=905&rangeEnd=948>)
> ⏱ 2021-12-28 13:26:30 ^34105326-163-905-948
### 切片运算符
> 📌 [每一个切片都构建于一个底层的数组之上。实际上是底层的数组存储了切片的数据；切片仅仅是数组中的一部分（或者所有）元素的视图。](<weread://bestbookmark?bookId=34105326&chapterUid=166&rangeStart=374&rangeEnd=435>)
> ⏱ 2021-12-28 13:30:00 ^34105326-166-374-435
> 📌 [有两个索引：其中一个标识切片开始的位置，另一个标识切片在此位置之前结束](<weread://bestbookmark?bookId=34105326&chapterUid=166&rangeStart=768&rangeEnd=803>)
> ⏱ 2021-12-28 13:30:28 ^34105326-166-768-803
### 底层数组
> 📌 [切片并不会自己保存任何数据，它仅仅是底层数组的元素的视图](<weread://bestbookmark?bookId=34105326&chapterUid=168&rangeStart=383&rangeEnd=411>)
> ⏱ 2021-12-28 23:32:02 ^34105326-168-383-411
### 使用“append”函数在切片上添加数据（续）
> 📌 [切片的底层数组并不能增长大小。如果数组没有足够的空间来保存新的元素，所有的元素会被拷贝至一个新的更大的数组，并且切片会被更新为引用这个新的数组。](<weread://bestbookmark?bookId=34105326&chapterUid=171&rangeStart=486&rangeEnd=558>)
> ⏱ 2021-12-28 23:38:24 ^34105326-171-486-558
### 映射字面量
> 📌 [映射字面量以映射类型（以“映射[键类型]值类型”的形式）开始。后面跟着花括号，内含你想要映射初始就包含的键/值对。对于每一个键/值对，包含一个键、一个冒号和值。多个键/值对之间以逗号分隔。](<weread://bestbookmark?bookId=34105326&chapterUid=199&rangeStart=411&rangeEnd=505>)
> ⏱ 2021-12-31 13:12:49 ^34105326-199-411-505
### 使用“delete”函数删除键/值对
> 📌 [Go提供了内建的delete函数。只需要传递给delete两个参数：你希望删除数据的映射和你希望删除的键。然后键和它关联的值都会被删除。](<weread://bestbookmark?bookId=34105326&chapterUid=204&rangeStart=414&rangeEnd=482>)
> ⏱ 2021-12-31 13:17:31 ^34105326-204-414-482
### 定义类型和struct
> 📌 [为了定义一个类型，需要使用type关键字，后面跟着新类型的名字，然后是你希望基于的基础类型](<weread://bestbookmark?bookId=34105326&chapterUid=218&rangeStart=809&rangeEnd=854>)
> ⏱ 2021-12-31 13:26:56 ^34105326-218-809-854
### 使用函数修改struct
> 📌 [Go是一个按值传递的语言，意味着函数调用时接收的是一个参数的拷贝。如果函数修改了参数值，它修改的只是拷贝，而不是原始值。](<weread://bestbookmark?bookId=34105326&chapterUid=223&rangeStart=873&rangeEnd=933>)
> ⏱ 2022-01-01 23:19:04 ^34105326-223-873-933
### 定义类型的名称首字母必须大写才能导出该类型
> 📌 [Go类型名称与变量和函数名称遵循相同的规则：如果变量、函数或者类型以大写字母开头，它就会被认为是导出的，并且可以从外部包来访问。](<weread://bestbookmark?bookId=34105326&chapterUid=229&rangeStart=752&rangeEnd=816>)
> ⏱ 2022-01-01 23:24:51 ^34105326-229-752-816
### 具有底层基础类型的定义类型
> 📌 [Go经常使用struct作为基础类型来定义类型，但是它们也能基于int、string、bool或者其他任何类型。](<weread://bestbookmark?bookId=34105326&chapterUid=244&rangeStart=380&rangeEnd=436>)
> ⏱ 2022-01-01 23:54:20 ^34105326-244-380-436

# 读书笔记

# 本书评论
