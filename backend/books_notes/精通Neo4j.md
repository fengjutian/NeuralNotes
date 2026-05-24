---
doc_type: weread-highlights-reviews
bookId: "3300056200"
title: 精通Neo4j
reviewCount: 0
noteCount: 18
author: 庞国明 叶伟民 宋建栋 马延超 杨志
cover: https://cdn.weread.qq.com/weread/cover/78/cpplatform_utbz5ufwf7cmk1nekyp8qn/t6_cpplatform_utbz5ufwf7cmk1nekyp8qn1681896099.jpg
readingStatus: "2"
progress: 77%
readingTime: 0小时39分钟
readingDate: 2025-07-12
isbn: 9787302618423
lastReadDate: 2025-07-13

---
# 元数据
> [!abstract] 精通Neo4j
> - ![ 精通Neo4j|200](https://cdn.weread.qq.com/weread/cover/78/cpplatform_utbz5ufwf7cmk1nekyp8qn/t6_cpplatform_utbz5ufwf7cmk1nekyp8qn1681896099.jpg)
> - 书名： 精通Neo4j
> - 作者： 庞国明 叶伟民 宋建栋 马延超 杨志
> - 简介： 图数据库是NoSQL类数据库的又一大典型代表，在国内图数据库属于新兴事物，其优异的复杂关系解决方案引起了国内众多大型互联网公司及IT开发者的关注，而Neo4j是目前图形化数据库中最为出色、最为成熟的产品。本书的第一版书名是《Neo4j**指南》，发行量超过13000册，本书在第一版的基础上补充完善了Neo4j的新特性、新功能。 本书基于Neo4j 4.4版本编写，共分10章，涵盖基本概念、基础入门、查询语言、程序开发技术、管理运维、集群技术、应用案例、高级应用、配置设置、内建过程、GDS、Fabric等内容。 本书内容涉及Neo4j的大部分知识，既可以作为Neo4j初学者的入门教材，也可以作为相关行业Neo4j技术专家的参考手册。
> - 出版时间： 2022-11-01 00:00:00
> - ISBN： 9787302618423
> - 分类： 计算机-计算机综合
> - 出版社： 清华大学出版社
> - PC地址：https://weread.qq.com/web/reader/adb32f90813ab7c74g010d12

# 高亮划线
### 2.1 Neo4j的安装部署
> 📌 [在页面顶部选项卡中，我们可以选择3种不同授权类型的版本，分别是“Enterprise Server”版（付费版，30天试用期，包含高级功能项）​、​“Community Server”版（免费版，不可商业使用，无高级功能项）​、​“Neo4j Desktop”版（桌面Neo4j管理平台，可以在此平台选择创建不同版本的Neo4j）​，如](<weread://bestbookmark?bookId=3300056200&chapterUid=22&rangeStart=1975&rangeEnd=2138>)
> ⏱ 2025-07-13 14:21:09 ^3300056200-22-1975-2138
> 📌 [在Neo4j运行目录下输入neo4j命令，系统会返回关于neo4j运行命令的相关指令，按照“neo4j <指令名>”的格式就可以运行相关操作了。](<weread://bestbookmark?bookId=3300056200&chapterUid=22&rangeStart=6924&rangeEnd=7002>)
> ⏱ 2025-07-13 14:22:40 ^3300056200-22-6924-7002
> 📌 [● console：打开Neo4j的控制台。● start：启动Neo4j。● stop：关闭Neo4j。● restart：重启Neo4j。● status：查看Neo4j运行状态。● install-service：安装Neo4j在Windows系统上的服务。● uninstall-service：卸载Neo4j在Windows系统上的服务。](<weread://bestbookmark?bookId=3300056200&chapterUid=22&rangeStart=7031&rangeEnd=7379>)
> ⏱ 2025-07-13 14:22:48 ^3300056200-22-7031-7379
### 2.3 Neo4j图数据中基本元素与概念
> 📌 [节点(Node)是图数据库中的一个基本元素，用以表示一个实体记录，就像关系数据库中的一条记录一样。在Neo4j中节点可以包含多个属性(Property)和多个标签(Label)](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=531&rangeEnd=619>)
> ⏱ 2025-07-13 14:25:37 ^3300056200-24-531-619
> 📌 [关系(Relationship)同样是图数据库中的基本元素。节点需要连接起来才能构成图。关系就是用来连接两个节点的，关系又称为图论的边(Edge)，其始端和末端都必须是节点，关系不能指向空也不能从空发起。关系和节点一样可以包含多个属性，但关系只能有一个类型(Type)](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=1344&rangeEnd=1478>)
> ⏱ 2025-07-13 14:26:30 ^3300056200-24-1344-1478
> 📌 [上面提到节点和关系都可以有多个属性。属性是由键值对组成的，就像Java的哈希表一样，属性名类似变量名，属性值类似变量值。属性值可以是基本的数据类型，或者由基本数据类型组成的数组。](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=3583&rangeEnd=3672>)
> ⏱ 2025-07-13 14:27:52 ^3300056200-24-3583-3672
> 📌 [需要注意的是属性值没有null的概念，如果一个属性不需要了，可以直接将整个键值对都移除。](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=3701&rangeEnd=3745>)
> ⏱ 2025-07-13 14:28:04 ^3300056200-24-3701-3745
> 📌 [当使用节点和关系创建了一个图后，在此图中任意两个节点间都是可能存在路径(Path)的](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=4178&rangeEnd=4220>)
> ⏱ 2025-07-13 14:30:38 ^3300056200-24-4178-4220
> 📌 [遍历(Traversal)一张图就是按照一定的规则，根据它们之间的关系，依次访问所有相关联的节点的操作。对于遍历操作不必自己实现，因为Neo4j提供了一套高效的遍历API，可以指定遍历规则，然后让Neo4j自动按照遍历规则遍历并返回遍历的结果。遍历规则可以是广度优先，也可以是深度优先。](<weread://bestbookmark?bookId=3300056200&chapterUid=24&rangeStart=5304&rangeEnd=5447>)
> ⏱ 2025-07-13 14:31:15 ^3300056200-24-5304-5447
### 2.4 官方入门实例介绍
> 📌 [这个实例将指引读者学习以下入门操作：(1)创建图数据：将电影、演员、导演等图数据导入到Neo4j数据库中。(2)检索节点：检索特定电影和演员。(3)查询关系：发现相关的演员和导演。(4)查询关系路径：查询他们之间的关系路径。](<weread://bestbookmark?bookId=3300056200&chapterUid=25&rangeStart=1486&rangeEnd=1714>)
> ⏱ 2025-07-13 14:34:53 ^3300056200-25-1486-1714
### 2.5 批量导入工具的使用
> 📌 [Neo4j ETL(Extract-Transform-Load)导入工具可以帮助开发人员轻松地将数据从关系数据库导入到图数据库中。它包括以下3个简单的步骤：步骤01通过JDBC设置指定源关系数据库。步骤02使用图形化的编辑工具建立数据模型映射。步骤03运行生成的脚本将所有数据导入到Neo4j。ETL工具有两个版本：Desktop版本和命令行版本。](<weread://bestbookmark?bookId=3300056200&chapterUid=26&rangeStart=912&rangeEnd=1365>)
> ⏱ 2025-07-13 15:20:00 ^3300056200-26-912-1365
### 3.1 Cypher概述
> 📌 [Cypher是一种声明式图数据库查询语言，它具有丰富的表现力，能高效地查询和更新图数据。](<weread://bestbookmark?bookId=3300056200&chapterUid=28&rangeStart=530&rangeEnd=574>)
> ⏱ 2025-07-13 15:24:08 ^3300056200-28-530-574
### 3.2 基本语法
> 📌 [Cypher支持的数据类型有：数值型、字符串、布尔型、节点、关系、路径、映射(Map)和列表(List)。](<weread://bestbookmark?bookId=3300056200&chapterUid=29&rangeStart=570&rangeEnd=623>)
> ⏱ 2025-07-13 15:25:02 ^3300056200-29-570-623
> 📌 [Cypher中的表达式如下：● 十进制（整型和双精度型）的字面值：13、-4000、3.14、6.022E23。● 十六进制整型字面值（以0x开头）​：0x13zf、0xFC3A9、-0x66eff。● 八进制整型字面值（以0开头）​：01372、02127、-05671。● 字符串字面值：'Hello'、"World"。● 布尔字面值：true、false、TRUE、FALSE。● 变量：n、x、rel、myFancyVariable、`A name with weird stuff in it[​]!`。● 属性：n.prop、x.prop、rel.thisProperty、myFancyVariable. `(weird property name)`。](<weread://bestbookmark?bookId=3300056200&chapterUid=29&rangeStart=1021&rangeEnd=1555>)
> ⏱ 2025-07-13 15:26:21 ^3300056200-29-1021-1555
> 📌 [● 动态属性：n["prop"]​、rel[n.city + n.zip]​、map[coll[0]​]​。● 参数：$param、$0。● 表达式列表：​['a', 'b']​、​[1, 2, 3]​、​['a', 2, n.property, $param]​、​[ ]​。● 函数调用：length(p)、nodes(p)。● 聚合函数：avg(x.prop)、count(*)。● 路径-模式：(a)-->()<--(b)。● 计算式：1 + 2 and 3 < 4。● 返回true或者false的断言表达式：a.prop = 'Hello'、length(p) >10、exists(a.name)。](<weread://bestbookmark?bookId=3300056200&chapterUid=29&rangeStart=1584&rangeEnd=2093>)
> ⏱ 2025-07-13 15:27:00 ^3300056200-29-1584-2093
> 📌 [● 正则表达式：a.name =～ 'Tob.*'。● 大小写敏感的字符串匹配表达式：a.surname STARTS WITH 'Sven'、a.surname ENDS WITH'son' or a.surname CONTAINS 'son'。](<weread://bestbookmark?bookId=3300056200&chapterUid=29&rangeStart=2122&rangeEnd=2276>)
> ⏱ 2025-07-13 15:27:19 ^3300056200-29-2122-2276
> 📌 [● CASE表达式。](<weread://bestbookmark?bookId=3300056200&chapterUid=29&rangeStart=2305&rangeEnd=2315>)
> ⏱ 2025-07-13 15:27:33 ^3300056200-29-2305-2315
### 3.3 语句
> 📌 [语句可分为三类，包括读语句、写语句和通用语句。● 读语句：包括MATCH、OPTIONAL MATCH、WHERE、START和Aggregation。● 写语句：包括LOAD CSV、CREATE、MERGE、SET、DELETE、REMOVE、FOREACH和CREATE UNIQUE。● 通用语句：包括RETURN、ORDER BY、LIMIT、SKIP、WITH、UNWIND、UNION和CALL。](<weread://bestbookmark?bookId=3300056200&chapterUid=30&rangeStart=444&rangeEnd=736>)
> ⏱ 2025-07-13 15:28:53 ^3300056200-30-444-736

# 读书笔记

# 本书评论
