---
doc_type: weread-highlights-reviews
bookId: "858204"
title: 深入浅出React和Redux
reviewCount: 0
noteCount: 29
author: 程墨
cover: https://wfqqreader-1252317822.image.myqcloud.com/cover/204/858204/t6_858204.jpg
readingStatus: "2"
progress: 58%
readingTime: 3小时11分钟
readingDate: 2019-10-20
isbn: 9787111565635
lastReadDate: 2021-04-06

---
# 元数据
> [!abstract] 深入浅出React和Redux
> - ![ 深入浅出React和Redux|200](https://wfqqreader-1252317822.image.myqcloud.com/cover/204/858204/t6_858204.jpg)
> - 书名： 深入浅出React和Redux
> - 作者： 程墨
> - 简介： 如果你熟悉传统的jQuery应用开发，那么通过阅读本书会让你发现不一样的应用构建模式；如果你之前学习过Angular.js或者Vue.js，那么对理解React和Redux的工作机理很有帮助，同时有机会体验同样一种思想的不同实现之道。
> - 出版时间： 2017-04-01 00:00:00
> - ISBN： 9787111565635
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/a0b327005d185ca0b5a7803

# 高亮划线
### 2.2 React组件的数据
> 📌 [prop是组件的对外接口，state是组件的内部状态，对外用prop，内部用state。](<weread://bestbookmark?bookId=858204&chapterUid=19&rangeStart=711&rangeEnd=755>)
> ⏱ 2021-04-06 22:02:15 ^858204-19-711-755
#### 2.2.1 React的prop
> 📌 [在React中，prop（property的简写）是从外部传递给组件的数据，一个React组件通过定义自己能够接受的prop就定义了自己的对外公共接口。](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=436&rangeEnd=512>)
> ⏱ 2021-03-11 18:36:43 ^858204-20-436-512
> 📌 [当prop的类型不是字符串类型时，在JSX中必须用花括号{}把prop值包住](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=1176&rangeEnd=1214>)
> ⏱ 2021-03-11 18:41:12 ^858204-20-1176-1214
> 📌 [当外部世界要传递一些数据给React组件，一个最直接的方式就是通过prop；同样，React组件要反馈数据给外部世界，也可以用prop，因为prop的类型不限于纯数据，也可以是函数](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=1292&rangeEnd=1382>)
> ⏱ 2021-03-11 18:42:56 ^858204-20-1292-1382
> 📌 [函数类型的prop等于让父组件交给了子组件一个回调函数，子组件在恰当的实际调用函数类型的prop，可以带上必要的参数，这样就可以反过来把信息传递给外部世界。](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=1383&rangeEnd=1461>)
> ⏱ 2021-03-11 18:43:00 ^858204-20-1383-1461
> 📌 [如何接收传入的prop的，首先是构造函数](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=2426&rangeEnd=2446>)
> ⏱ 2021-03-11 18:46:08 ^858204-20-2426-2446
> 📌 [如果一个组件需要定义自己的构造函数，一定要记得在构造函数的第一行通过super调用父类也就是React.Component的构造函数。如果在构造函数中没有调用super(props)，那么组件实例被构造之后，类实例的所有成员函数就无法通过this.props访问到父组件传递过来的props值。](<weread://bestbookmark?bookId=858204&chapterUid=20&rangeStart=2797&rangeEnd=2944>)
> ⏱ 2021-03-11 18:33:50 ^858204-20-2797-2944
#### 2.2.2 React的state
> 📌 [state代表组件的内部状态。由于React组件不能修改传入的prop，所以需要记录自身数据变化，就要使用state。](<weread://bestbookmark?bookId=858204&chapterUid=21&rangeStart=462&rangeEnd=521>)
> ⏱ 2021-03-11 19:35:04 ^858204-21-462-521
> 📌 [state代表组件的内部状态。](<weread://bestbookmark?bookId=858204&chapterUid=21&rangeStart=462&rangeEnd=477>)
> ⏱ 2021-03-11 18:36:18 ^858204-21-462-477
> 📌 [组件的state必须是一个JavaScript对象，不能是string或者number这样的简单数据类型，即使我们需要存储的只是一个数字类型的数据，也只能把它存作state某个字段对应的值](<weread://bestbookmark?bookId=858204&chapterUid=21&rangeStart=1053&rangeEnd=1147>)
> ⏱ 2021-03-11 19:37:52 ^858204-21-1053-1147
#### 2.2.3 prop和state的对比
> 📌 [prop和state的区别：□ prop用于定义外部接口，state用于记录内部状态；□ prop的赋值在外部世界使用组件时，state的赋值在组件内部；□ 组件不应该改变prop的值，而state存在的目的就是让组件来改变的。](<weread://bestbookmark?bookId=858204&chapterUid=22&rangeStart=443&rangeEnd=647>)
> ⏱ 2021-03-11 20:01:22 ^858204-22-443-647
### 2.3 组件的生命周期
> 📌 [React严格定义了组件的生命周期，生命周期可能会经历如下三个过程：□ 装载过程（Mount），也就是把组件第一次在DOM树中渲染的过程；□ 更新过程（Update），当组件被重新渲染的过程；□ 卸载过程（Unmount），组件从DOM中删除的过程。三种不同的过程，React库会依次调用组件的一些成员函数，这些函数称为生命周期函数。](<weread://bestbookmark?bookId=858204&chapterUid=23&rangeStart=546&rangeEnd=832>)
> ⏱ 2021-03-11 20:06:49 ^858204-23-546-832
#### 2.3.1 装载过程
> 📌 [装载过程，当组件第一次被渲染的时候，依次调用的函数是如下这些：□ constructor□ getInitialState□ getDefaultProps□ componentWillMount□ render□ componentDidMount](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=435&rangeEnd=740>)
> ⏱ 2021-03-11 20:07:20 ^858204-24-435-740
> 📌 [一个React组件需要构造函数，往往是为了下面的目的：□ 初始化state，因为组件生命周期中任何函数都可能要访问state，那么整个生命周期中第一个被调用的构造函数自然是初始化state最理想的地方；□ 绑定成员函数的this环境。](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=1014&rangeEnd=1191>)
> ⏱ 2021-03-11 20:07:45 ^858204-24-1014-1191
> 📌 [实际上getInitialState和getDefaultProps两个方法在ES6的方法定义的React组件中根本不会用到。](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=2411&rangeEnd=2474>)
> ⏱ 2021-03-11 20:43:30 ^858204-24-2411-2474
> 📌 [用ES6的话，在构造函数中通过给this.state赋值完成状态的初始化，通过给类属性（注意是类属性，而不是类的实例对象属性）defaultProps赋值指定props初始值，达到的效果是完全一样的，代码如下：](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=2816&rangeEnd=2921>)
> ⏱ 2021-03-11 20:46:43 ^858204-24-2816-2921
> 📌 [一个React组件可以忽略其他所有函数都不实现，但是一定要实现render函数，因为所有React组件的父类React.Component类对除render之外的生命周期函数都有默认实现。](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=3442&rangeEnd=3536>)
> ⏱ 2021-03-11 20:47:49 ^858204-24-3442-3536
> 📌 [componentWillMount会在调用render函数之前被调用，component-DidMount会在调用render函数之后被调用，这两个函数就像是render函数的前哨和后卫，一前一后，把render函数夹住，正好分别做render前后必要的工作。](<weread://bestbookmark?bookId=858204&chapterUid=24&rangeStart=4045&rangeEnd=4176>)
> ⏱ 2021-03-11 20:58:21 ^858204-24-4045-4176
#### 2.3.2 更新过程
> 📌 [只要是父组件的render函数被调用，在render函数里面被渲染的子组件就会经历更新过程，不管父组件传给子组件的props有没有改变，都会触发子组件的componentWill-ReceiveProps函数。](<weread://bestbookmark?bookId=858204&chapterUid=25&rangeStart=1103&rangeEnd=1208>)
> ⏱ 2021-03-13 11:08:13 ^858204-25-1103-1208
#### 2.3.3 卸载过程
> 📌 [React组件的卸载过程只涉及一个函数componentWillUnmount，当React组件要从DOM树上删除掉之前，对应的componentWillUnmount函数会被调用，所以这个函数适合做一些清理性的工作。](<weread://bestbookmark?bookId=858204&chapterUid=26&rangeStart=430&rangeEnd=539>)
> ⏱ 2021-03-13 11:22:35 ^858204-26-430-539
#### 3.1.1 MVC框架的缺陷
> 📌 [一个Flux应用包含四个部分，我们先粗略了解一下：□ Dispatcher，处理动作分发，维持Store之间的依赖关系；□ Store，负责存储数据和处理数据相关逻辑；□ Action，驱动Dispatcher的JavaScript对象；□ View，视图部分，负责显示用户界面。](<weread://bestbookmark?bookId=858204&chapterUid=33&rangeStart=3254&rangeEnd=3514>)
> ⏱ 2021-03-13 12:24:45 ^858204-33-3254-3514
#### 3.1.2 Flux应用
> 📌 [Dispatcher存在的作用，就是用来派发action，](<weread://bestbookmark?bookId=858204&chapterUid=34&rangeStart=1564&rangeEnd=1593>)
> ⏱ 2021-03-13 12:30:26 ^858204-34-1564-1593
> 📌 [作为管理，action对象必须有一个名为type的字段，代表这个action对象的类型，为了记录日志和debug方便，这个type应该是字符串类型。](<weread://bestbookmark?bookId=858204&chapterUid=34&rangeStart=1885&rangeEnd=1959>)
> ⏱ 2021-03-13 12:33:25 ^858204-34-1885-1959
> 📌 [定义action通常需要两个文件，一个定义action的类型，一个定义action的构造函数（也称为action creator）。分成两个文件的主要原因是在Store中会根据action类型做不同操作，也就有单独导入action类型的需要。](<weread://bestbookmark?bookId=858204&chapterUid=34&rangeStart=1988&rangeEnd=2109>)
> ⏱ 2021-03-13 12:33:09 ^858204-34-1988-2109
> 📌 [一个Store也是一个对象，这个对象存储应用状态，同时还要接受Dispatcher派发的动作，根据动作来决定是否要更新应用状态。](<weread://bestbookmark?bookId=858204&chapterUid=34&rangeStart=3351&rangeEnd=3415>)
> ⏱ 2021-03-13 12:38:10 ^858204-34-3351-3415
### 3.2 Redux
> 📌 [Redux是Flux的一种实现](<weread://bestbookmark?bookId=858204&chapterUid=37&rangeStart=527&rangeEnd=542>)
> ⏱ 2021-03-13 16:36:40 ^858204-37-527-542
#### 3.2.1 Redux的基本原则
> 📌 [Flux的基本原则是“单向数据流”, Redux在此基础上强调三个基本原则：□ 唯一数据源（Single Source of Truth）；□ 保持状态只读（State is read-only）；□ 数据改变只能通过纯函数完成（Changes are made with purefunctions）。](<weread://bestbookmark?bookId=858204&chapterUid=38&rangeStart=554&rangeEnd=797>)
> ⏱ 2021-03-13 16:38:24 ^858204-38-554-797
> 📌 [唯一数据源指的是应用的状态数据应该只存储在唯一的一个Store上。](<weread://bestbookmark?bookId=858204&chapterUid=38&rangeStart=910&rangeEnd=943>)
> ⏱ 2021-03-13 16:39:05 ^858204-38-910-943
#### 7.1.2 React组件访问服务器的生命周期
> 📌 [访问服务器API是一个异步操作。因为JavaScript是单线程的语言，不可能让唯一的线程一直等待网络请求的结果，所以所有对服务器的数据请求必定是异步请求。](<weread://bestbookmark?bookId=858204&chapterUid=90&rangeStart=874&rangeEnd=952>)
> ⏱ 2021-04-06 22:12:20 ^858204-90-874-952

# 读书笔记

# 本书评论
