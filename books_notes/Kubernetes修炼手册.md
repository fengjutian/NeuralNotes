---
doc_type: weread-highlights-reviews
bookId: "38153670"
title: Kubernetes修炼手册
reviewCount: 0
noteCount: 10
author: 奈吉尔·波尔顿
cover: https://cdn.weread.qq.com/weread/cover/5/YueWen_38153670/t6_YueWen_38153670.jpg
readingStatus: "2"
progress: 32%
readingTime: 0小时48分钟
readingDate: 2022-10-26
isbn: 9787115561091
lastReadDate: 2022-11-23

---
# 元数据
> [!abstract] Kubernetes修炼手册
> - ![ Kubernetes修炼手册|200](https://cdn.weread.qq.com/weread/cover/5/YueWen_38153670/t6_YueWen_38153670.jpg)
> - 书名： Kubernetes修炼手册
> - 作者： 奈吉尔·波尔顿
> - 简介： 本书是一本Kubernetes入门图书，共分为12章，涵盖了Kubernetes的基础知识，并附带了大量的配置案例。此外，还介绍了Kubernetes架构、构建Kubernetes集群、在Kubernetes上部署和管理应用程序、Kubernetes安全，以及云本地、微服务、容器化等术语的含义。本书在内容上不断进行充实和完善，可以帮助读者快速入门Kubernetes。本书适合系统管理员、开发人员，以及对Kubernetes感兴趣的初学者阅读。
> - 出版时间： 2021-05-01 00:00:00
> - ISBN： 9787115561091
> - 分类： 计算机-计算机综合
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/faa3296072462dc6faa52bf

# 高亮划线
### 1.2 Kubernetes的诞生
> 📌 [Docker是一种更加偏向底层的技术，它负责诸如启停容器的操作；而Kubernetes是一种更加偏向上层的技术，它注重集群范畴的管理，比如决定在哪个节点上运行容器、决定什么适合进行扩缩容或升级。](<weread://bestbookmark?bookId=38153670&chapterUid=10&rangeStart=1786&rangeEnd=1883>)
> ⏱ 2022-10-27 12:02:44 ^38153670-10-1786-1883
> 📌 [Kubernetes（读作koo-ber-net-eez）一词来源于希腊语“舵手”——轮船的掌舵之人。](<weread://bestbookmark?bookId=38153670&chapterUid=10&rangeStart=4122&rangeEnd=4173>)
> ⏱ 2022-10-27 12:05:18 ^38153670-10-4122-4173
> 📌 [Kubernetes的部分创始人想将其称作九之七（Seven of Nine）。如果读者了解星际迷航，就会知道九之七是一个被联邦星舰企业号解救的女性博格（Borg），下令解救她的是凯瑟琳·珍妮薇舰长。然而，版权法不允许用这个名字。不过图标中的“七个把手”也有向“九之七”致敬的意味。](<weread://bestbookmark?bookId=38153670&chapterUid=10&rangeStart=4220&rangeEnd=4361>)
> ⏱ 2022-10-27 12:06:22 ^38153670-10-4220-4361
### 2.6 Pod
> 📌 [在VMware的世界中，调度的原子单位是虚拟机（VM）；在Docker的世界中，调度的原子单位是容器；而在Kubernetes的世界中，调度的原子单位是Pod](<weread://bestbookmark?bookId=38153670&chapterUid=19&rangeStart=373&rangeEnd=480>)
> ⏱ 2022-10-28 13:29:03 ^38153670-19-373-480
> 📌 [在英语中，会将a group of whales（一群鲸鱼）称作a Pod of whales，Pod就是来源于此。因为Docker的Logo是鲸鱼，所以在Kubernetes中会将包含了一组容器的事物称作Pod](<weread://bestbookmark?bookId=38153670&chapterUid=19&rangeStart=888&rangeEnd=1050>)
> ⏱ 2022-10-28 13:29:51 ^38153670-19-888-1050
### 4.1 Pod原理
> 📌 [在Kubernetes的世界中，最小单元是Pod。因此，在Kubernetes中部署应用即在Pod中进行应用的部署。](<weread://bestbookmark?bookId=38153670&chapterUid=35&rangeStart=563&rangeEnd=621>)
> ⏱ 2022-11-23 13:39:35 ^38153670-35-563-621
> 📌 [Pod只是运行应用的载具。](<weread://bestbookmark?bookId=38153670&chapterUid=35&rangeStart=3075&rangeEnd=3088>)
> ⏱ 2022-11-23 13:41:14 ^38153670-35-3075-3088
> 📌 [Pod就是被一个或多个容器共享的执行环境。所谓共享的执行环境，是指Pod中的一系列被其内部每个容器所共享的资源。这些资源包括IP地址、端口、主机名、套接字、内存、卷，等等。](<weread://bestbookmark?bookId=38153670&chapterUid=35&rangeStart=3714&rangeEnd=3800>)
> ⏱ 2022-11-23 13:41:53 ^38153670-35-3714-3800
> 📌 [在使用Docker作为容器运行时，Pod实际上是一个名为pause container的特殊容器。没错，Pod就是一种特殊容器的花哨称谓。](<weread://bestbookmark?bookId=38153670&chapterUid=35&rangeStart=3826&rangeEnd=3895>)
> ⏱ 2022-11-23 13:42:20 ^38153670-35-3826-3895
> 📌 [部署一个Pod是一种原子操作。也就是说，这一操作要么整体成功，要么全部失败——没有Pod被“部分”部署成功的状态。同样也意味着，Pod中的所有容器将被调度到同一个节点上。一旦所有的Pod资源就绪，Pod就变为可用状态](<weread://bestbookmark?bookId=38153670&chapterUid=35&rangeStart=6606&rangeEnd=6740>)
> ⏱ 2022-11-23 13:43:29 ^38153670-35-6606-6740

# 读书笔记

# 本书评论
