---
doc_type: weread-highlights-reviews
bookId: "39888211"
title: WebRTC音视频实时互动技术：原理、实战与源码分析
reviewCount: 0
noteCount: 15
author: 李超编著
cover: https://cdn.weread.qq.com/weread/cover/92/YueWen_39888211/t6_YueWen_39888211.jpg
readingStatus: "2"
progress: 96%
readingTime: 2小时30分钟
readingDate: 2021-09-10
isbn: 9787111685012
lastReadDate: 2024-09-13

---
# 元数据
> [!abstract] WebRTC音视频实时互动技术：原理、实战与源码分析
> - ![ WebRTC音视频实时互动技术：原理、实战与源码分析|200](https://cdn.weread.qq.com/weread/cover/92/YueWen_39888211/t6_YueWen_39888211.jpg)
> - 书名： WebRTC音视频实时互动技术：原理、实战与源码分析
> - 作者： 李超编著
> - 简介： 本书分为三部分，共13章。其中第1～3章为第一部分，主要介绍WebRTC的由来，为什么要选择WebRTC，以及实时音视频通信的本质是什么。其中第3章最为关键，只有了解了音视频实时通信的本质，你才能知道音视频实时通信要解决什么问题，然后才能知道如何解决这些问题，从而理解WebRTC为什么要这样做。第二部分包括第4～10章，这部分的内容比较多，我会循序渐进地向你讲解WebRTC的理论和实战。其中第4章介绍了一个最简单的WebRTC信令服务器该如何构建，第5章介绍了如何通过浏览器实现一对一通信，通过这两章你就可以搭建出一个WebRTC一对一实时通信系统了。第6章介绍了WebRTC底层是如何传输音视频数据的，重点是如何进行NAT穿越；第7章详述了WebRTC媒体协商使用的SDP各字段的含义。需要说明的是，SDP中的每个字段你都需要牢记在心，这样才能为后续阅读WebRTC代码扫清障碍。第8章介绍如何通过移动端（Android、iOS）Native的方式实现一对一通信，读完本章内容后，将能实现Web端与移动端的互联互通；第9章介绍了WebRTC底层的传输协议RTP/RTCP，这部分内容是每个从事实时通信工作的读者必须掌握的；第10章介绍了WebRTC的两种拥塞控制算法，详细介绍了WebRTC为什么最终选择Transport-CC作为默认拥塞控制算法。第三部分包括第11～13章。其中第11章介绍了编译WebRTC源码库的方法，对于大多数刚入门的读者来说，学习WebRTC的第一道门槛便是如何编译WebRTC，通过对该章的学习，相信你一定可以顺利地将WebRTC库编译出来；第12章对WebRTC的peerconnect_client例子做了深入剖析，这个例子可以说是我们学习WebRTC源码的必经之路，这一章你一定要多花些时间将其全部掌握；第13章是对WebRTC源码的整体架构和运转流程的详细分析，也是本书最难的部分，将这章了解清楚后，你就知道WebRTC是如何运转的了。
> - 出版时间： 2021-06-01 00:00:00
> - ISBN： 9787111685012
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/377320f07260a55337761c1

# 高亮划线
## 第4章 构建WebRTC一对一信令服务器
> 📌 [信令服务器的作用主要有两个：一是实现业务层的管理，如用户创建房间，加入房间，退出房间等；二是让通信的双方彼此交换信息，其中最常见的是交换通信双方的IP地址和端口](<weread://bestbookmark?bookId=39888211&chapterUid=31&rangeStart=474&rangeEnd=554>)
> ⏱ 2024-09-13 08:39:01 ^39888211-31-474-554
### 4.1 WebRTC一对一架构
> 📌 [WebRTC由四部分组成，分别为两个WebRTC终端、一个信令服务器、一台中继服务器（STUN[插图]/TURN[插图]）和两个NAT[插图]，这是最经典的一对一通信架构。](<weread://bestbookmark?bookId=39888211&chapterUid=32&rangeStart=522&rangeEnd=917>)
> ⏱ 2024-05-28 13:52:19 ^39888211-32-522-917
### 4.2 细化架构
> 📌 [音视频采集模块](<weread://bestbookmark?bookId=39888211&chapterUid=33&rangeStart=764&rangeEnd=771>)
> ⏱ 2024-05-28 13:57:32 ^39888211-33-764-771
> 📌 [信令模块与信令服务器建立连接](<weread://bestbookmark?bookId=39888211&chapterUid=33&rangeStart=857&rangeEnd=871>)
> ⏱ 2024-05-28 13:57:49 ^39888211-33-857-871
> 📌 [向STUN/TRUN服务器发送请求](<weread://bestbookmark?bookId=39888211&chapterUid=33&rangeStart=1366&rangeEnd=1383>)
> ⏱ 2024-05-28 14:02:06 ^39888211-33-1366-1383
#### 4.3.2 信令时序
> 📌 [信令服务器SigServer建立连接](<weread://bestbookmark?bookId=39888211&chapterUid=36&rangeStart=682&rangeEnd=700>)
> ⏱ 2024-05-28 14:22:02 ^39888211-36-682-700
> 📌 [媒体协商（媒体协商会在第5章介绍），即通过message消息交换WebRTC需要的ofer/answer等内容；](<weread://bestbookmark?bookId=39888211&chapterUid=36&rangeStart=846&rangeEnd=902>)
> ⏱ 2024-05-28 14:23:03 ^39888211-36-846-902
#### 4.3.3 信令传输协议的选择
> 📌 [一般选择TCP或基于TCP的HTTP/HTTPS、WS/WSS等协议作为信令服务器的传输协议。](<weread://bestbookmark?bookId=39888211&chapterUid=37&rangeStart=383&rangeEnd=430>)
> ⏱ 2024-05-28 14:25:18 ^39888211-37-383-430
> 📌 [；二是在TCP上传输的数据是流式的，因此不必担心传输的数据过大导致拆包传输的问题。](<weread://bestbookmark?bookId=39888211&chapterUid=37&rangeStart=479&rangeEnd=520>)
> ⏱ 2024-09-13 13:00:20 ^39888211-37-479-520
### 5.1 浏览器对WebRTC的支持
> 📌 [苹果公司要求第三方只能使用它的WebView来实现浏览器，而WebView却不支持WebRTC，因此导致其他使用WebView的浏览器也无法使用WebRTC。不过从iOS 14.3开始，WebView终于支持WebRTC了](<weread://bestbookmark?bookId=39888211&chapterUid=46&rangeStart=1144&rangeEnd=1255>)
> ⏱ 2024-05-28 14:43:24 ^39888211-46-1144-1255
### 5.4 MediaStream与MediaStreamTrack
> 📌 [MediaStream有两个重要作用，一是可以作为录制或者渲染的源，这样我们就可以将Stream中的内容录制成文件或者将Stream中的数据通过浏览器中的<video>标签播放出来；二是在同一个MediaStream中的MediaStreamTrack数据会进行同步（比如同一个MediaStream中的音频轨和视频轨会进行时间同步），而不同MediaStream中的MediaStreamTrack之间不进行时间同步。](<weread://bestbookmark?bookId=39888211&chapterUid=49&rangeStart=618&rangeEnd=834>)
> ⏱ 2024-05-28 14:50:59 ^39888211-49-618-834
#### 5.7.4 ICE
> 📌 [当媒体协商完成后，WebRTC就开始建立网络连接了，其过程称为ICE](<weread://bestbookmark?bookId=39888211&chapterUid=56&rangeStart=375&rangeEnd=409>)
> ⏱ 2024-05-28 15:15:58 ^39888211-56-375-409
## 第10章 web RTC拥塞控制
> 📌 [减少数据量、适当增加时延和更准确的带宽评估被统称为拥塞控制。](<weread://bestbookmark?bookId=39888211&chapterUid=125&rangeStart=605&rangeEnd=635>)
> ⏱ 2024-05-30 11:53:59 ^39888211-125-605-635
### 10.1 WebRTC的拥塞控制算法
> 📌 [Transport-CC是WebRTC默认使用的拥塞控制算法，](<weread://bestbookmark?bookId=39888211&chapterUid=126&rangeStart=1201&rangeEnd=1232>)
> ⏱ 2024-05-30 11:54:26 ^39888211-126-1201-1232
#### 10.1.1 Goog­REMB
> 📌 [如前所述，WebRTC中的GCC有两种基于延时的拥塞控制算法：一种是接收端的延时拥塞控制算法，称为Goog-REMB；另一种是发送端的延时拥塞控制算法，称为Transport CC。](<weread://bestbookmark?bookId=39888211&chapterUid=127&rangeStart=382&rangeEnd=473>)
> ⏱ 2024-05-30 11:55:40 ^39888211-127-382-473

# 读书笔记

# 本书评论
