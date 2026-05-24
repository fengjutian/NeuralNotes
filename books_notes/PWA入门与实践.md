---
doc_type: weread-highlights-reviews
bookId: "30842580"
title: PWA入门与实践
reviewCount: 0
noteCount: 10
author: 王乐平
cover: https://cdn.weread.qq.com/weread/cover/20/YueWen_30842580/t6_YueWen_30842580.jpg
readingStatus: "2"
progress: 31%
readingTime: 0小时44分钟
readingDate: 2022-01-08
isbn: 9787111652588
lastReadDate: 2022-01-09

---
# 元数据
> [!abstract] PWA入门与实践
> - ![ PWA入门与实践|200](https://cdn.weread.qq.com/weread/cover/20/YueWen_30842580/t6_YueWen_30842580.jpg)
> - 书名： PWA入门与实践
> - 作者： 王乐平
> - 简介： 本书对PWA的核心技术进行了比较透彻的讲解，对PWA中可能遇到的问题也进行了充分说明，通过阅读本书，读者可以对PWA有深入的理解。全书共7章：第1章介绍PWA的发展历程及生态环境；第2章介绍PWA的一些前置技术及预备知识；第3章学习PWA的核心部分——Service Worker；第4章进入PWA的核心API部分；第5章给出了PWA使用过程中的配套工具；第6章为PWA的实践部分；第7章讲解Web的系统集成能力。本书适用于有一定Web开发基础，或想学习PWA、需要一本全面的PWA手册的开发者。
> - 出版时间： 2020-04-01 00:00:00
> - ISBN： 9787111652588
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/30d3298071d69ed430da245

# 高亮划线
#### 2.4.2 简介
> 📌 [Web Worker有两种不同线程类型，分别是：❑ Dedicated Worker （专用线程）。只能被首次生成它的脚本使用。❑ Shared Worker （共享线程）。可以同时被多个脚本使用。](<weread://bestbookmark?bookId=30842580&chapterUid=60&rangeStart=908&rangeEnd=1067>)
> ⏱ 2022-01-09 21:46:40 ^30842580-60-908-1067
### 3.1 Service Worker的结构
> 📌 [Service Worker包含以下特性：❑ Service Worker是一个独立的Worker线程，有自己的上下文，独立于当前网页进程。❑ Service Worker一旦安装成功，将永远存在，除非手动卸载。❑ Service Worker节省性能，使用Service Worker的时候会自动唤醒，不使用的时候会自动进入线程休眠。❑ Service Worker必须运行在https下或者localhost（127.0.0.1）下。❑ 注册的Service Worker文件必须是在当前域名下的。](<weread://bestbookmark?bookId=30842580&chapterUid=66&rangeStart=967&rangeEnd=1368>)
> ⏱ 2022-01-09 22:10:58 ^30842580-66-967-1368
> 📌 [Service Worker相关的接口有：Worker注册实例的引用，可用于注册同步消息，推送消息、通知等。❑ ServiceWorker：对Service Worker线程的引用，可用于获取线程信息和向线程发送消息。❑ ServiceWorkerRegistration：对Service❑ ServiceWorkerContaine:window环境下用于注册、注销Service Worker线程的容器。❑ ServiceWorkerGlobalScope:Service Worker线程中的Context。](<weread://bestbookmark?bookId=30842580&chapterUid=66&rangeStart=1800&rangeEnd=2178>)
> ⏱ 2022-01-09 22:25:27 ^30842580-66-1800-2178
#### 3.2.1 脚本的生命周期
> 📌 [❑ 解析：当ServiceWorkerContainer.register执行成功后，并不意味着注册的Service Worker文件已经安装或者激活了，而仅仅是注册的Service Worker文件解析完成了，符合文件同源及https协议等。❑ 安装中：注册完成后，Service Worker线程会转入installing状态，此时ServiceWorkerGlobalScope.oninstall事件会被触发，可以在这个事件中做一些静态资源的缓存等操作。](<weread://bestbookmark?bookId=30842580&chapterUid=72&rangeStart=1094&rangeEnd=1355>)
> ⏱ 2022-01-09 22:33:47 ^30842580-72-1094-1355
> 📌 [❑ 已安装：ServiceWorkerGlobalScope.oninstall中处理完成后，状态即为installed。此时新的Service Worker线程处于等待状态，可以手动调用self.skipWating或者重新打开页面来进行激活。当网站第一次安装Service Worker时会自动触发激活。❑ 激活中：激活中状态下会触发ServiceWorkerGlobalScope.onactivate事件，可以在这个事件里处理一些旧版本的资源删除操作。在此状态下手动调用self. clients.claim() ，相关页面会立刻被新的ServiceWorker线程控制，并触发ServiceWorkerContainer.oncontrollerchange事件。](<weread://bestbookmark?bookId=30842580&chapterUid=72&rangeStart=1385&rangeEnd=1753>)
> ⏱ 2022-01-09 22:34:03 ^30842580-72-1385-1753
> 📌 [❑ 已激活：ServiceWorkerGlobalScope.onactivate事件中的处理逻辑完成后，则状态为已激活。❑ 废弃：安装失败、激活失败会导致当前注册的ServiceWorker线程废弃。新的Service Worker线程激活成功都会导致旧的Service Worker线程废弃。](<weread://bestbookmark?bookId=30842580&chapterUid=72&rangeStart=1783&rangeEnd=1962>)
> ⏱ 2022-01-09 22:34:20 ^30842580-72-1783-1962
#### 3.2.2 线程的生命周期
> 📌 [Service Worker线程的生命周期状态：❑ STARTING：正在启动。❑ RUNNING：正在运行。❑ STOPPING：正在停止。❑ STOPPED：已停止。](<weread://bestbookmark?bookId=30842580&chapterUid=73&rangeStart=480&rangeEnd=685>)
> ⏱ 2022-01-09 22:36:19 ^30842580-73-480-685
#### 3.2.3 线程退出
> 📌 [Service Worker线程并不会一直运行，在以下条件下会停止：](<weread://bestbookmark?bookId=30842580&chapterUid=74&rangeStart=442&rangeEnd=476>)
> ⏱ 2022-01-09 22:37:57 ^30842580-74-442-476
> 📌 [❑ Service Worker文件中存在异常会导致Service Worker线程退出。例如JS文件语法错误、Service Worker文件安装/激活失败、Service Worker线程执行时存在未捕获的异常。❑ Service Worker线程监听事件函数是否处理完成，变为空闲状态时，Service Worker线程会自动退出。❑ Service Worker JS执行时间过长，Service Worker线程会自动退出，比如Service Worker JS执行时间超过30秒，或fetch请求超过5分钟还未完成。❑ 浏览器也会周期性地检查所有Service Worker线程是否可以退出，通常在启动Service Worker线程30秒后会检查，关掉空闲超过30秒的线程。](<weread://bestbookmark?bookId=30842580&chapterUid=74&rangeStart=506&rangeEnd=940>)
> ⏱ 2022-01-09 22:38:09 ^30842580-74-506-940
#### 3.2.4 更新Service Worker文件的条件
> 📌 [❑ 当线上的Service Worker文件与浏览器运行的ServiceWorker文件有一个字节不同时，会触发更新。❑ 当注册的Service Worker文件发生变化时，即使只是查询参数不一致，也会认为这是一个新的文件，会触发更新。❑ 手动调用ServiceWorkerRegistration.update() 时，浏览器会主动拉取新的Service Worker文件并进行对比，如果发现两个文件不一致，则触发更新。❑ 在Service Worker文件中，importScripts包含进来的JS文件内容变化时，默认情况下遵循HTTP缓存规则，当然可以通过设置updateViaCache来配置为不走缓存。❑ 当Service Worker文件安装24小时后，浏览器会主动无缓存地去拉取相关文件进行比较，不一样时会触发更新。](<weread://bestbookmark?bookId=30842580&chapterUid=75&rangeStart=575&rangeEnd=1062>)
> ⏱ 2022-01-09 22:39:15 ^30842580-75-575-1062

# 读书笔记

# 本书评论
