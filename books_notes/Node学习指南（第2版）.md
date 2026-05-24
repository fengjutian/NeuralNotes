---
doc_type: weread-highlights-reviews
bookId: "27112457"
title: Node学习指南（第2版）
reviewCount: 0
noteCount: 9
author: 谢利·鲍尔斯
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/457/27112457/t6_27112457.jpg
readingStatus: "2"
progress: 30%
readingTime: 2小时20分钟
readingDate: 2020-07-15
isbn: 9787115505415
lastReadDate: 2022-05-05

---
# 元数据
> [!abstract] Node学习指南（第2版）
> - ![ Node学习指南（第2版）|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/457/27112457/t6_27112457.jpg)
> - 书名： Node学习指南（第2版）
> - 作者： 谢利·鲍尔斯
> - 简介： Node.js是一套用来编写高性能网络服务器的JavaScript工具包。它可以让JavaScript在服务器端运行，因此，它可用来快速构建网络服务及应用的平台。本书是学习Node编程的入门指南。全书共12章，由浅入深。本书首先介绍Node的基础知识、Node的核心功能、Node的模块系统和REPL等，然后讲解Node的Web应用、流和管道、Node对文件系统的支持、网络和套接字、子进程、ES6等相关知识，最后介绍了全栈Node编程、Node的开发环境和产品环境以及Node的新应用。本书适合有一定基础的JavaScript程序员阅读，也适合对学习Node应用开发感兴趣的读者学习参考。
> - 出版时间： 2019-10-01 00:00:00
> - ISBN： 9787115505415
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/01232ea0719db409012f97f

# 高亮划线
### 2.1 global和process对象
> 📌 [在浏览器中，如果你在最顶层声明一个变量，它就会被声明成全局（global）的。但在Node中却不是这样。当你在模块或者应用中定义变量的时候，变量不是全局的；它被限制只能在定义它的模块或者应用中使用](<weread://bestbookmark?bookId=27112457&chapterUid=27&rangeStart=648&rangeEnd=746>)
> ⏱ 2022-05-05 13:06:26 ^27112457-27-648-746
> 📌 [避免使用共享的命名空间，是一个很显著的改进，然而也不是万能的。事实上，global对象为所有环境都提供了一个可以访问Node对象和函数的机制](<weread://bestbookmark?bookId=27112457&chapterUid=27&rangeStart=2318&rangeEnd=2401>)
> ⏱ 2022-05-05 13:07:53 ^27112457-27-2318-2401
> 📌 [process对象是Node环境中的基础组件，它提供了当前运行环境的信息。而且，通过process你可以操作标准输入/输出（I/O），可以终止一个Node程序，也可以在Node的事件循环（将在2.3.1节中讲到）结束的时候发信号。](<weread://bestbookmark?bookId=27112457&chapterUid=27&rangeStart=2639&rangeEnd=2783>)
> ⏱ 2022-05-05 13:08:25 ^27112457-27-2639-2783
> 📌 [命令行中的单引号和双引号注意双引号的使用：在Windows的命令行窗口中必须使用双引号。由于双引号可以在任何环境下使用，所以请在所有脚本中都使用双引号。](<weread://bestbookmark?bookId=27112457&chapterUid=27&rangeStart=3612&rangeEnd=3723>)
> ⏱ 2022-05-05 13:09:33 ^27112457-27-3612-3723
### 3.1 Node模块系统概览
> 📌 [当程序引用一个模块时，会发生这样几件事。首先，Node会检查模块是否有缓存。Node在首次加载一个模块之后，会将它缓存起来，而不是每次引用都重新加载。这种做法可以减少因系统对文件的查找而引起的延迟。](<weread://bestbookmark?bookId=27112457&chapterUid=32&rangeStart=1449&rangeEnd=1548>)
> ⏱ 2022-05-05 13:26:59 ^27112457-32-1449-1548
> 📌 [Node会在一个叫作node_modules的目录下面按照层级结构来搜索这个模块，搜索的优先级如下所示：（1）应用程序目录内的node_modules子目录；（2）当前应用程序的父目录中的node_modules目录；（3）继续向父目录中寻找node_modules目录，直到根目录；（4）最后，在全局安装的模块中进行寻找（下面会详细说明）。](<weread://bestbookmark?bookId=27112457&chapterUid=32&rangeStart=3713&rangeEnd=4016>)
> ⏱ 2022-05-05 13:32:13 ^27112457-32-3713-4016
> 📌 [如果你提供的是一个目录名，那么Node会搜索目录下的package.json文件。文件中包含一个main字段，它指明了要加载的模块文件](<weread://bestbookmark?bookId=27112457&chapterUid=32&rangeStart=4495&rangeEnd=4562>)
> ⏱ 2022-05-05 13:34:12 ^27112457-32-4495-4562
> 📌 [如果Node在目录中没有找到package.json文件，就会寻找index.js或者index.node文件来加载。以上文件都没有的话，Node就会报错。](<weread://bestbookmark?bookId=27112457&chapterUid=32&rangeStart=4688&rangeEnd=4766>)
> ⏱ 2022-05-05 13:34:30 ^27112457-32-4688-4766
> 📌 [学习JavaScript的时候，首先要避免的就是使用eval()。原因是，eval()会使用和你的应用程序相同的上下文来执行JavaScript。意味着对于一段你一无所知或者不甚了解的代码，你要给予它们和你自己认真写好的代码一样的信任，并且执行它们。](<weread://bestbookmark?bookId=27112457&chapterUid=32&rangeStart=6622&rangeEnd=6747>)
> ⏱ 2022-05-05 13:39:48 ^27112457-32-6622-6747

# 读书笔记

# 本书评论
