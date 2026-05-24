---
doc_type: weread-highlights-reviews
bookId: "25462424"
title: 深入理解Kafka：核心设计与实践原理
reviewCount: 0
noteCount: 3
author: 朱忠华
cover: https://cdn.weread.qq.com/weread/cover/5/YueWen_25462424/t6_YueWen_25462424.jpg
readingStatus: "2"
progress: 3%
readingTime: 0小时12分钟
readingDate: 2022-02-03
isbn: 9787121359026
lastReadDate: 2022-02-14

---
# 元数据
> [!abstract] 深入理解Kafka：核心设计与实践原理
> - ![ 深入理解Kafka：核心设计与实践原理|200](https://cdn.weread.qq.com/weread/cover/5/YueWen_25462424/t6_YueWen_25462424.jpg)
> - 书名： 深入理解Kafka：核心设计与实践原理
> - 作者： 朱忠华
> - 简介： 本书从Kafka的基础概念切入，循序渐进地转入对其内部原理的剖析。本书主要阐述了Kafka中生产者客户端、消费者客户端、主题与分区、日志存储、原理解析、监控管理、应用扩展及流式计算等内容。虽然Kafka的内核使用Scala语言编写，但本书基本以Java语言作为主要的示例语言，方便大多数读者的理解。虽然本书没有明确的界定，但总体上可以划分为三个部分：基础篇、原理篇和扩展篇，前4章为基础篇，包括基础概念、生产者、消费者，以及主题与分区，学习完这4章的内容完全可以应对绝大多数的开发场景。第5章至第8章为原理篇，包括对日志存储、协议设计、控制器、组协调器、事务、一致性、可靠性等内容的探究，学习完这4章的内容可以让读者对Kafka有一个深刻的认知。最后4章从应用扩展层面来做讲解，可以归类为扩展篇，主要内容包括监控、应用工具、应用扩展（延时队列、重试队列、死信队列、消息轨迹等）、与Spark的集成等，让读者可以对Kafka的生态有一个更加全面的认知。本
> - 出版时间： 2019-01-01 00:00:00
> - ISBN： 9787121359026
> - 分类： 计算机-编程设计
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/e9a32a0071848698e9a39b8

# 高亮划线
## 第1章 初识Kafka
> 📌 [Kafka起初是由LinkedIn公司采用Scala语言开发的一个多分区、多副本且基于ZooKeeper协调的分布式消息系统，现已被捐献给Apache基金会。](<weread://bestbookmark?bookId=25462424&chapterUid=4&rangeStart=449&rangeEnd=528>)
> ⏱ 2022-02-14 13:09:16 ^25462424-4-449-528
### 1.1 基本概念
> 📌 [一个典型的 Kafka 体系架构包括若干 Producer、若干Broker、若干 Consumer，以及一个ZooKeeper集群](<weread://bestbookmark?bookId=25462424&chapterUid=5&rangeStart=447&rangeEnd=514>)
> ⏱ 2022-02-14 13:11:12 ^25462424-5-447-514
> 📌 [整个Kafka体系结构中引入了以下3个术语。（1）Producer：生产者，也就是发送消息的一方。生产者负责创建消息，然后将其投递到Kafka中。（2）Consumer：消费者，也就是接收消息的一方。消费者连接到Kafka上并接收消息，进而进行相应的业务逻辑处理。（3）Broker：服务代理节点。对于Kafka而言，Broker可以简单地看作一个独立的Kafka服务节点或Kafka服务实例。大多数情况下也可以将Broker看作一台Kafka服务器，前提是这台服务器上只部署了一个Kafka实例。一个或多个Broker组成了一个Kafka集群。一般而言，我们更习惯使用首字母小写的broker来表示服务代理节点。](<weread://bestbookmark?bookId=25462424&chapterUid=5&rangeStart=907&rangeEnd=1301>)
> ⏱ 2022-02-14 13:12:53 ^25462424-5-907-1301

# 读书笔记

# 本书评论
