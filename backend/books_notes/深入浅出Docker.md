---
doc_type: weread-highlights-reviews
bookId: "25916914"
title: 深入浅出Docker
reviewCount: 0
noteCount: 17
author: 奈吉尔·波尔顿
cover: https://cdn.weread.qq.com/weread/cover/21/YueWen_25916914/t6_YueWen_25916914.jpg
readingStatus: "4"
progress: 87%
readingTime: 4小时12分钟
readingDate: 2020-07-30
finishedDate: 2022-08-28
isbn: 9787115504890
lastReadDate: 2022-08-28

---
# 元数据
> [!abstract] 深入浅出Docker
> - ![ 深入浅出Docker|200](https://cdn.weread.qq.com/weread/cover/21/YueWen_25916914/t6_YueWen_25916914.jpg)
> - 书名： 深入浅出Docker
> - 作者： 奈吉尔·波尔顿
> - 简介： 本书是一本Docker入门图书，全书分为17章，从Docker概览和Docker技术两部分进行全面解析，深入浅出地介绍了Docker的相关知识，清晰详细的操作步骤结合大量的实际代码帮助读者学以致用，将Docker知识应用到真实的项目开发当中。本书适合对Docker感兴趣的入门新手、Docker技术开发人员以及运维人员阅读，本书也可作为Docker认证工程师考试的参考图书。
> - 出版时间： 2019-04-01 00:00:00
> - ISBN： 9787115504890
> - 分类： 计算机-计算机综合
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/a6332ce0718b75f2a63b772

# 高亮划线
## 第二部分 Docker技术
> 📌 [Docker 引擎是用来运行和管理容器的核心软件。](<weread://bestbookmark?bookId=25916914&chapterUid=12&rangeStart=972&rangeEnd=997>)
> ⏱ 2022-01-16 15:46:44 ^25916914-12-972-997
> 📌 [Docker引擎由如下主要的组件构成：Docker客户端（Docker Client）、Docker守护进程（Dockerdaemon）、containerd以及runc。它们共同负责容器的创建和运行。](<weread://bestbookmark?bookId=25916914&chapterUid=12&rangeStart=1415&rangeEnd=1517>)
> ⏱ 2022-01-16 15:45:34 ^25916914-12-1415-1517
> 📌 [Docker首次发布时，Docker引擎由两个核心组件构成：LXC和Docker daemon。Docker daemon是单一的二进制文件，包含诸如Docker客户端、Docker API、容器运行时、镜像构建等。LXC提供了对诸如命名空间（Namespace）和控制组（CGroup）等基础工具的操作能力，它们是基于Linux内核的容器虚拟化技术。](<weread://bestbookmark?bookId=25916914&chapterUid=12&rangeStart=1943&rangeEnd=2167>)
> ⏱ 2022-01-16 15:48:16 ^25916914-12-1943-2167
> 📌 [Docker公司开发了名为Libcontainer的自研工具，用于替代LXC。Libcontainer的目标是成为与平台无关的工具，可基于不同内核为Docker上层提供必要的容器交互功能。在Docker 0.9版本中，Libcontainer取代LXC成为默认的执行驱动。](<weread://bestbookmark?bookId=25916914&chapterUid=12&rangeStart=2746&rangeEnd=2906>)
> ⏱ 2022-01-16 15:50:09 ^25916914-12-2746-2906
### 第6章 Docker镜像
> 📌 [镜像可以理解为一种构建时（build-time）结构，而容器可以理解为一种运行时（run-time）结构](<weread://bestbookmark?bookId=25916914&chapterUid=13&rangeStart=1292&rangeEnd=1344>)
> ⏱ 2022-01-16 16:06:18 ^25916914-13-1292-1344
> 📌 [那些没有标签的镜像被称为悬虚镜像，在列表中展示为<none>:<none>。](<weread://bestbookmark?bookId=25916914&chapterUid=13&rangeStart=11595&rangeEnd=11645>)
> ⏱ 2022-01-16 16:22:07 ^25916914-13-11595-11645
> 📌 [Docker目前支持如下的过滤器。● dangling：可以指定true或者false，仅返回悬虚镜像（true），或者非悬虚镜像（false）。● before：需要镜像名称或者ID作为参数，返回在指定镜像之前被创建的全部镜像。● since：与before类似，不过返回的是指定镜像之后创建的全部镜像。● label：根据标注（label）的名称或者值，对镜像进行过滤。docker image ls命令输出中不显示标注内容。](<weread://bestbookmark?bookId=25916914&chapterUid=13&rangeStart=12061&rangeEnd=12400>)
> ⏱ 2022-01-16 16:28:27 ^25916914-13-12061-12400
> 📌 [另一种查看镜像分层的方式是通过docker image inspect命令。下面同样以ubuntu:latest镜像为例。](<weread://bestbookmark?bookId=25916914&chapterUid=13&rangeStart=16583&rangeEnd=16644>)
> ⏱ 2022-01-16 16:34:27 ^25916914-13-16583-16644
### 第7章 Docker容器
> 📌 [启动容器的简便方式是使用docker container run命令。该命令可以携带很多参数，在其基础的格式docker container run<image> <app>中，指定了启动所需的镜像以及要运行的应用。docker container run -it ubuntu /bin/bash则会启动某个Ubuntu Linux容器，并运行Bash Shell作为其应用](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=1212&rangeEnd=1413>)
> ⏱ 2022-01-16 16:59:33 ^25916914-14-1212-1413
> 📌 [-it参数可以将当前终端连接到容器的Shell终端之上。](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=1536&rangeEnd=1564>)
> ⏱ 2022-01-16 17:02:02 ^25916914-14-1536-1564
> 📌 [可以使用docker container stop命令手动停止容器运行，并且使用docker container start再次启动该容器。如果再也不需要该容器，则使用docker container rm命令来删除容器。](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=1985&rangeEnd=2096>)
> ⏱ 2022-01-16 17:03:05 ^25916914-14-1985-2096
> 📌 [加上-a参数再次运行前面的命令，就会显示出全部的容器，包括处于停止状态的。](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=13811&rangeEnd=13848>)
> ⏱ 2022-08-27 17:10:16 ^25916914-14-13811-13848
> 📌 [尽管上面的示例阐明了容器的持久化特性，还是需要指出卷（volume）才是在容器中存储持久化数据的首选方式。](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=14980&rangeEnd=15033>)
> ⏱ 2022-08-27 17:17:48 ^25916914-14-14980-15033
> 📌 [通过在docker container rm命令后面添加-f参数来一次性删除运行中的容器是可行的。但是，删除容器的最佳方式还是分两步，先停止容器然后删除。这样可以给容器中运行的应用/进程一个停止运行并清理残留数据的机会。](<weread://bestbookmark?bookId=25916914&chapterUid=14&rangeStart=15183&rangeEnd=15293>)
> ⏱ 2022-08-27 17:18:50 ^25916914-14-15183-15293
### 第11章 Docker网络
> 📌 [CNM定义了3个基本要素：沙盒（Sandbox）、终端（Endpoint）和网络（Network）。](<weread://bestbookmark?bookId=25916914&chapterUid=18&rangeStart=2688&rangeEnd=2738>)
> ⏱ 2022-08-28 12:28:56 ^25916914-18-2688-2738
> 📌 [沙盒是一个独立的网络栈。其中包括以太网接口、端口、路由表以及DNS配置。终端就是虚拟网络接口。就像普通网络接口一样，终端主要职责是负责创建连接。在CNM中，终端负责将沙盒连接到网络。网络是802.1d网桥（类似大家熟知的交换机）的软件实现。因此，网络就是需要交互的终端的集合，并且终端之间相互独立。](<weread://bestbookmark?bookId=25916914&chapterUid=18&rangeStart=2770&rangeEnd=3010>)
> ⏱ 2022-08-28 12:29:57 ^25916914-18-2770-3010
### 第13章 卷与持久化数据
> 📌 [在容器中持久化数据的方式推荐采用卷。总体来说，用户创建卷，然后创建容器，接着将卷挂载到容器上。卷会挂载到容器文件系统的某个目录之下，任何写到该目录下的内容都会写到卷中。即使容器被删除，卷与其上面的数据仍然存在。](<weread://bestbookmark?bookId=25916914&chapterUid=20&rangeStart=2620&rangeEnd=2749>)
> ⏱ 2022-08-28 13:27:45 ^25916914-20-2620-2749

# 读书笔记

# 本书评论
