---
doc_type: weread-highlights-reviews
bookId: "3300122690"
title: NestJS全栈开发解析
reviewCount: 0
noteCount: 12
author: 温健民
cover: https://cdn.weread.qq.com/weread/cover/34/cpplatform_53u1wyykpdfeamkcddrxg7/t6_cpplatform_53u1wyykpdfeamkcddrxg71732680710.jpg
readingStatus: "2"
progress: 49%
readingTime: 0小时37分钟
readingDate: 2024-12-11
isbn: 9787302671008
lastReadDate: 2024-12-19

---
# 元数据
> [!abstract] NestJS全栈开发解析
> - ![ NestJS全栈开发解析|200](https://cdn.weread.qq.com/weread/cover/34/cpplatform_53u1wyykpdfeamkcddrxg7/t6_cpplatform_53u1wyykpdfeamkcddrxg71732680710.jpg)
> - 书名： NestJS全栈开发解析
> - 作者： 温健民
> - 简介： 《NestJS全栈开发解析:快速上手与实践》旨在帮助读者快速掌握NestJS（简称Nest）开发，并应用于实战项目。本书共10章，首先介绍基本概念，为读者打下坚实的知识基础。接着，通过简洁的代码示例进行知识点的串联讲解，帮助读者快速克服学习瓶颈。最终，通过实践能力和工程思维的培养，帮助读者将知识从线性结构转变为网状结构，形成以Nest为基础的全栈知识体系。《NestJS全栈开发解析:快速上手与实践》采用通俗易懂的点线面知识构建方式进行讲解，适合从事前端开发和Node.js开发的工程师学习，同时也适合有意向学习Nest全栈知识的开发者。
> - 出版时间： 2024-09-01 00:00:00
> - ISBN： 9787302671008
> - 分类： 计算机-计算机综合
> - 出版社： 清华大学出版社
> - PC地址：https://weread.qq.com/web/reader/a8c32ef0813ab966dg010e96

# 高亮划线
## 第1章 需要提前掌握的知识
> 📌 [Nest底层默认采用Express作为HTTP服务器框架。](<weread://bestbookmark?bookId=3300122690&chapterUid=6&rangeStart=561&rangeEnd=590>)
> ⏱ 2024-12-13 08:40:29 ^3300122690-6-561-590
> 📌 [在Node的内置HTTP模块中有两个核心对象：请求对象(Request)和响应对象(Response)。请求对象表示客户端向服务端发送的请求信息，而响应对象则表示服务端向客户端返回的响应数据。](<weread://bestbookmark?bookId=3300122690&chapterUid=6&rangeStart=1132&rangeEnd=1228>)
> ⏱ 2024-12-13 08:41:55 ^3300122690-6-1132-1228
## 第2章 Nest初识
> 📌 [Nest请求流程](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=23857&rangeEnd=23865>)
> ⏱ 2024-12-18 15:57:09 ^3300122690-7-23857-23865
> 📌 [中间的灰色区域属于AOP切面部分，包含Middleware（中间件）​、Guard（守卫）​、Interceptor（拦截器）​、Pipe（管道）和Filter（过滤器）​。它们都是AOP思想的具体实现。](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=23904&rangeEnd=24002>)
> ⏱ 2024-12-18 15:57:05 ^3300122690-7-23904-24002
> 📌 [Nest的中间件默认是基于Express](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=24297&rangeEnd=24317>)
> ⏱ 2024-12-18 15:58:20 ^3300122690-7-24297-24317
> 📌 [中间件可以在路由处理程序之前或之后插入执行任务，它们分为全局中间件和局部中间件两种类型。](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=24634&rangeEnd=24678>)
> ⏱ 2024-12-18 15:58:12 ^3300122690-7-24634-24678
> 📌 [守卫的职责很明确，通常用于权限、角色等授权操作](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=25626&rangeEnd=25649>)
> ⏱ 2024-12-18 16:00:50 ^3300122690-7-25626-25649
> 📌 [守卫在调用路由程序之前返回true或者false来判断是否通行，分为全局守卫和局部守卫。](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=25981&rangeEnd=26025>)
> ⏱ 2024-12-18 16:01:04 ^3300122690-7-25981-26025
> 📌 [拦截器不同于中间件和守卫，它在路由请求之前和之后都可以进行逻辑处理，能够充分操作request和response对象](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=26972&rangeEnd=27030>)
> ⏱ 2024-12-18 16:01:21 ^3300122690-7-26972-27030
> 📌 [拦截器通常用于记录请求日志、转换或格式化响应数据等。](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=27040&rangeEnd=27066>)
> ⏱ 2024-12-18 16:01:26 ^3300122690-7-27040-27066
> 📌 [管道用于处理通用逻辑，其中两个典型的用例是处理请求参数的验证(validation)和转换(transformation)。](<weread://bestbookmark?bookId=3300122690&chapterUid=7&rangeStart=28969&rangeEnd=29031>)
> ⏱ 2024-12-18 17:58:15 ^3300122690-7-28969-29031
## 第3章 Nest核心概念介绍
> 📌 [装饰器（Java中有个类似的概念叫注解）是用来装饰和扩展对象功能的。它能够在不改变原有对象结构的前提下，增加额外的功能，以满足更多的实际需求。](<weread://bestbookmark?bookId=3300122690&chapterUid=8&rangeStart=900&rangeEnd=971>)
> ⏱ 2024-12-19 08:45:00 ^3300122690-8-900-971

# 读书笔记

# 本书评论
