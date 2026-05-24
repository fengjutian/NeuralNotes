---
doc_type: weread-highlights-reviews
bookId: "43102030"
title: Spring Boot学习指南：构建云原生Java和Kotlin应用程序
reviewCount: 0
noteCount: 22
author: 【美】马克·赫克勒
cover: https://cdn.weread.qq.com/weread/cover/57/yuewen_43102030/t6_yuewen_431020301735115710.jpg
readingStatus: "2"
progress: 79%
readingTime: 2小时14分钟
readingDate: 2022-08-27
isbn: 9787111690245
lastReadDate: 2025-06-18

---
# 元数据
> [!abstract] Spring Boot学习指南：构建云原生Java和Kotlin应用程序
> - ![ Spring Boot学习指南：构建云原生Java和Kotlin应用程序|200](https://cdn.weread.qq.com/weread/cover/57/yuewen_43102030/t6_yuewen_431020301735115710.jpg)
> - 书名： Spring Boot学习指南：构建云原生Java和Kotlin应用程序
> - 作者： 【美】马克·赫克勒
> - 简介： 本书将指导你理解Spring Boot的架构和方法，包括调试、测试和部署等主题。第1章介绍Spring Boot的三个核心特性。第2章研究创建Spring Boot应用程序时可选择的工具。第3章演示如何使用Spring Boot来开发一个基本的应用程序。第4章演示如何对Spring Boot应用程序添加数据库访问。第5章演示如何使用Spring Boot的内置配置功能、自动配置报告和执行器来灵活且动态地创建、识别和修改应用程序环境设置。第6章深入地研究数据。第7章演示如何使用Spring MVC创建应用程序。第8章介绍响应式编程。第9章讨论并演示测试Spring Boot应用程序的核心方面。第10章介绍并解释安全性的核心方面，以及它们如何应用于应用程序。第11章研究如何部署Spring Boot应用程序。第12章深入探讨响应式编程。
> - 出版时间： 2021-09-14 00:00:00
> - ISBN： 9787111690245
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/738325a07291af4e738769e

# 高亮划线
## 第1章 Spring Boot概述
> 📌 [Spring Boot的一个优越之处在于它使得依赖项管理易于控制。](<weread://bestbookmark?bookId=43102030&chapterUid=92&rangeStart=705&rangeEnd=738>)
> ⏱ 2023-12-18 22:36:59 ^43102030-8-527-560
## 第2章 选择工具并开始
> 📌 [Gradle于2008年首次发布，使用域特定语言(Domain Specific Language, DSL)来生成build.gradle构建文件，该文件既小又灵活。下面是一个Spring Boot应用程序的Gradle构建文件示例。](<weread://bestbookmark?bookId=43102030&chapterUid=94&rangeStart=2442&rangeEnd=2588>)
> ⏱ 2025-03-10 16:02:01 ^43102030-94-2442-2588
> 📌 [Maven更严格的声明性（有些人可能会说是固执己见）方法使项目与项目之间、环境与环境之间保持了难以置信的一致性。如果你遵循Maven的方式，那么通常很少会出现问题，这样你就可以把精力放在代码上，而不必对构建太在意。](<weread://bestbookmark?bookId=43102030&chapterUid=94&rangeStart=3221&rangeEnd=3328>)
> ⏱ 2025-03-10 16:02:28 ^43102030-94-3221-3328
> 📌 [Gradle可以更快地进行构建（有时非常快）​，尤其是在大型项目中。也就是说，对于典型的基于微服务的项目，Maven和Gradle项目的构建时间不会有太大的差别。](<weread://bestbookmark?bookId=43102030&chapterUid=94&rangeStart=3494&rangeEnd=3574>)
> ⏱ 2025-03-10 16:02:45 ^43102030-94-3494-3574
### 2.2 Java还是Kotlin
> 📌 [令人惊奇的是，你其实不必做出选择。Kotlin编译成与Java相同的字节码输出。由于可以创建包含Java源文件和Kotlin的Spring项目，并且可以轻松地调用这两个编译器，因此即使在同一个项目中，你也可以使用对你更有意义的那一个](<weread://bestbookmark?bookId=43102030&chapterUid=95&rangeStart=2692&rangeEnd=2808>)
> ⏱ 2025-03-10 16:05:39 ^43102030-95-2692-2808
### 2.4 Spring Initializr
> 📌 [在机器上安装和管理一个或多个JDK的最简单的方法是使用SDKMAN!（https://sdkman.io）。](<weread://bestbookmark?bookId=43102030&chapterUid=97&rangeStart=1240&rangeEnd=1294>)
> ⏱ 2024-06-19 11:19:22 ^43102030-14-1377-1463
> 📌 [如果你不喜欢使用SDKMAN!也可以直接从https://adoptopenjdk.net下载并安装JDK。](<weread://bestbookmark?bookId=43102030&chapterUid=97&rangeStart=2158&rangeEnd=2212>)
> ⏱ 2024-06-19 11:21:15 ^43102030-14-2629-2722
## 第3章 创建你的第一个Spring Boot REST API
> 📌 [互联网是为了通信而建立的。](<weread://bestbookmark?bookId=43102030&chapterUid=102&rangeStart=1286&rangeEnd=1299>)
> ⏱ 2024-06-19 11:38:46 ^43102030-20-937-950
### 3.2 REST
> 📌 [REST是表述性状态转移（representational state transfer）的首字母缩写，这是一种比较隐晦的说法，即当一个应用程序与另一个应用程序通信时，应用程序A会带来它当前的状态。但它不期望应用程序B维护通信调用之间的状态——当前的和累积的、基于进程的信息。应用程序A为对应用程序B的每个请求提供其相关状态的表示。你可以很容易地看到为什么这会提高应用程序的生存能力和快速恢复能力，因为如果出现通信问题或应用程序B崩溃并重新启动了，它不会丢失其与应用程序A交互的当前状态。应用程序A可以简单地重新发出请求，并从两个应用程序停止的地方重新开始。](<weread://bestbookmark?bookId=43102030&chapterUid=103&rangeStart=495&rangeEnd=774>)
> ⏱ 2022-08-28 14:32:39 ^43102030-21-462-741
### 4.2 我们希望得到什么
> 📌 [为了从Spring Boot应用程序访问数据库，你需要：• 一个运行的数据库，无论是由应用程序启动或嵌入应用程序之中的，还是仅供应用程序访问的。• 允许编程访问的数据库驱动程序，通常由数据库提供商提供。• 用于访问目标数据库的Spring Data模块。](<weread://bestbookmark?bookId=43102030&chapterUid=108&rangeStart=925&rangeEnd=1145>)
> ⏱ 2025-03-10 16:10:57 ^43102030-108-925-1145
## 第5章 配置和检查Spring Boot应用程序
> 📌 [@Value注解可能是将配置设置导入代码的最直接的方法。](<weread://bestbookmark?bookId=43102030&chapterUid=112&rangeStart=3827&rangeEnd=3855>)
> ⏱ 2024-06-19 17:58:31 ^43102030-32-3270-3305
> 📌 [@Value带来灵活性的同时也带来了缺点，于是Spring团队创建了@ConfigurationProperties。使用@ConfigurationProperties，开发人员可以定义属性，将相关属性组成组，并以工具可验证和类型安全的方式引用或使用它们。](<weread://bestbookmark?bookId=43102030&chapterUid=112&rangeStart=8511&rangeEnd=8640>)
> ⏱ 2024-06-19 18:00:39 ^43102030-32-9696-9922
## 第6章 真正深入地研究数据
> 📌 [处理数据时往往涉及某种形式的域实体。无论是发票、汽车还是其他事物，它们的数据很少被作为不相关属性的集合来处理。通常，我们认为有用的数据是元素的聚合池，它们一起构成了一个有意义的整体。](<weread://bestbookmark?bookId=43102030&chapterUid=116&rangeStart=1086&rangeEnd=1177>)
> ⏱ 2025-03-10 16:12:40 ^43102030-116-1086-1177
## 第7章 使用Spring MVC创建应用程序
> 📌 [一般而言，Spring MVC指的是以下内容之一：• 在Spring应用程序中（以某种方式）实现Model（模型）-View（视图）-Controller（控制器）模式。• 专门使用Spring MVC组件概念（如Model接口、@Controller类和视图技术）来创建应用程序。• 使用Spring开发阻塞/非响应式应用程序。](<weread://bestbookmark?bookId=43102030&chapterUid=126&rangeStart=973&rangeEnd=1231>)
> ⏱ 2025-03-10 16:15:00 ^43102030-126-973-1231
## 第8章 使用Project Reactor和Spring WebFlux进行响应式编程
> 📌 [响应式宣言(Reactive Manifesto)(https://www.reactivemanifesto.org)指出响应式系统是：• 快速响应的• 可迅速恢复的• 有弹性的• 消息驱动的](<weread://bestbookmark?bookId=43102030&chapterUid=131&rangeStart=1495&rangeEnd=1716>)
> ⏱ 2025-06-18 09:03:52 ^43102030-131-1495-1716
### 8.6 用于全响应式进程间通信的RSocket
> 📌 [RSocket是多个行业领导者和前沿创新者合作的结果，它是一个快速的二进制协议，可以通过TCP、WebSocket和Aeron传输机制使用。RSocket支持四种异步交互模型：• 请求-响应• 请求-流• fire & forget• 请求通道（双向流）](<weread://bestbookmark?bookId=43102030&chapterUid=136&rangeStart=677&rangeEnd=932>)
> ⏱ 2025-06-18 09:07:25 ^43102030-136-677-932
### 9.3 测试片
> 📌 [Spring Boot的测试依赖项spring-boot-starter-test中内置了一些注解，这些注解可以自动配置这些功能片。所有这些测试片注解都以类似的方式工作，加载ApplicationContext并选择对指定片有意义的组件。这些注解的例子包括：](<weread://bestbookmark?bookId=43102030&chapterUid=140&rangeStart=476&rangeEnd=605>)
> ⏱ 2025-06-18 09:10:56 ^43102030-140-476-605
> 📌 [• @JsonTest• @WebMvcTest• @WebFluxText（之前介绍过）• @DataJpaTest• @JdbcTest• @DataJdbcTest• @JooqTest• @DataMongoTest• @DataNeo4jTest• @DataRedisTest• @DataLdapTest• @RestClientTest• @AutoConfigureRestDocs• @WebServiceClientTest](<weread://bestbookmark?bookId=43102030&chapterUid=140&rangeStart=636&rangeEnd=1262>)
> ⏱ 2025-06-18 09:11:13 ^43102030-140-636-1262
## 第10章 保护Spring Boot应用程序
> 📌 [认证是一种行为﹑过程或证明某事（如身份、艺术品或金融交易）真实、准确或可信的一种方法；是证明某物的行为或过程。](<weread://bestbookmark?bookId=43102030&chapterUid=142&rangeStart=1275&rangeEnd=1366>)
> ⏱ 2025-06-18 09:13:32 ^43102030-142-1275-1366
> 📌 [认证证明某人就是他声称的那个人。授权验证某人是否有权访问特定的资源或操作。](<weread://bestbookmark?bookId=43102030&chapterUid=142&rangeStart=1885&rangeEnd=2045>)
> ⏱ 2025-06-18 09:14:18 ^43102030-142-1885-2045
> 📌 [简单地说，认证就是证明某人（或某物）是否就是他们声称的那个人（或者是设备、应用程序或服务方面的某个东西）​。](<weread://bestbookmark?bookId=43102030&chapterUid=142&rangeStart=2138&rangeEnd=2192>)
> ⏱ 2025-06-18 09:15:01 ^43102030-142-2138-2192
> 📌 [一旦某人通过了认证，他就有可能获得访问可用资源或允许一个或多个人进行操作的权利。](<weread://bestbookmark?bookId=43102030&chapterUid=142&rangeStart=3061&rangeEnd=3101>)
> ⏱ 2025-06-18 11:33:58 ^43102030-142-3061-3101

# 读书笔记

# 本书评论
