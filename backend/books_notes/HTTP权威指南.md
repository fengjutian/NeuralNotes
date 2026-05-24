---
doc_type: weread-highlights-reviews
bookId: "26211809"
title: HTTP权威指南
reviewCount: 0
noteCount: 44
author: David Gourley  Brian Totty等
cover: https://cdn.weread.qq.com/weread/cover/59/YueWen_26211809/t6_YueWen_26211809.jpg
readingStatus: "2"
progress: 46%
readingTime: 7小时7分钟
readingDate: 2020-06-23
isbn: 9787115281487
lastReadDate: 2022-02-06

---
# 元数据
> [!abstract] HTTP权威指南
> - ![ HTTP权威指南|200](https://cdn.weread.qq.com/weread/cover/59/YueWen_26211809/t6_YueWen_26211809.jpg)
> - 书名： HTTP权威指南
> - 作者： David Gourley  Brian Totty等
> - 简介： 本书是HTTP及其相关核心Web技术方面的权威著作，主要介绍了Web应用程序是如何工作的，核心的因特网协议如何与架构构建块交互，如何正确实现因特网客户端和服务器等。本书适合所有想了解HTTP和Web底层结构的人阅读。
> - 出版时间： 2012-08-28 00:00:00
> - ISBN： 9787115281487
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/1d9321c0718ff5e11d9afe8

# 高亮划线
### 第5章 Web服务器
> 📌 [Web服务器是资源服务器。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=14901&rangeEnd=14914>)
> ⏱ 2022-01-20 12:42:54 ^26211809-13-14901-14914
> 📌 [在Web服务器将内容传送给客户端之前，要将请求报文中的URI映射为Web服务器上适当的内容或内容生成器，以识别出内容的源头。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=14999&rangeEnd=15061>)
> ⏱ 2022-01-20 12:43:23 ^26211809-13-14999-15061
> 📌 [通常，Web服务器的文件系统中会有一个特殊的文件夹专门用于存放Web内容。这个文件夹被称为文档的根目录（document root，或docroot）。Web服务器从请求报文中获取URI，并将其附加在文档根目录的后面。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=15227&rangeEnd=15392>)
> ⏱ 2022-01-20 12:44:18 ^26211809-13-15227-15392
> 📌 [Web服务器有时会返回重定向响应而不是成功的报文。Web服务器可以将浏览器重定向到其他地方来执行请求。重定向响应由返回码3XX说明。Location响应首部包含了内容的新地址或优选地址的URI。重定向可用于下列情况。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=22708&rangeEnd=22816>)
> ⏱ 2022-01-20 12:50:02 ^26211809-13-22708-22816
> 📌 [资源可能已经被移动到了新的位置，或者被重新命名，有了一个新的URL。Web服务器可以告诉客户端资源已经被重命名了，这样客户端就可以在从新地址获取资源之前，更新书签之类的信息了。状态码301 MovedPermanently就用于此类重定向。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=22888&rangeEnd=23009>)
> ⏱ 2022-01-20 12:50:44 ^26211809-13-22888-23009
> 📌 [如果资源被临时移走或重命名了，服务器可能希望将客户端重定向到新的位置上去。但由于重命名是临时的，所以服务器希望客户端将来还可以回头去使用老的URL，不要对书签进行更新。状态码303 See Other以及状态码307 Temporary Redirect就用于此类重定向。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=23081&rangeEnd=23217>)
> ⏱ 2022-01-20 12:51:16 ^26211809-13-23081-23217
> 📌 [服务器通常用重定向来重写URL，往往用于嵌入上下文。当请求到达时，服务器会生成一个新的包含了嵌入式状态信息的URL，并将用户重定向到这个新的URL上去。[插图]客户端会跟随这个重定向信息，重新发起请求，但这次的请求会包含完整的、经过状态增强的URL。这是在事务间维护状态的一种有效方式。状态码303 See Other和307 Temporary Redirect用于此类重定向。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=23287&rangeEnd=23566>)
> ⏱ 2022-01-20 12:52:04 ^26211809-13-23287-23566
> 📌 [如果一个超载的服务器收到一条请求，服务器可以将客户端重定向到一个负载不太重的服务器上去。状态码303 See Other和307 TemporaryRedirect可用于此类重定向。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=23635&rangeEnd=23727>)
> ⏱ 2022-01-20 12:52:36 ^26211809-13-23635-23727
> 📌 [Web服务器上可能会有某些用户的本地信息；服务器可以将客户端重定向到包含了那个客户端信息的服务器上去。状态码303 See Other和307Temporary Redirect可用于此类重定向。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=23797&rangeEnd=23896>)
> ⏱ 2022-01-20 12:52:59 ^26211809-13-23797-23896
> 📌 [客户端请求的URI是一个不带尾部斜线的目录名时，大多数Web服务器都会将客户端重定向到一个加了斜线的URI上，这样相对链接就可以正常工作了。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=23967&rangeEnd=24037>)
> ⏱ 2022-01-20 12:53:32 ^26211809-13-23967-24037
> 📌 [最后，当事务结束时，Web服务器会在日志文件中添加一个条目，来描述已执行的事务。](<weread://bestbookmark?bookId=26211809&chapterUid=13&rangeStart=24539&rangeEnd=24579>)
> ⏱ 2022-01-20 12:54:40 ^26211809-13-24539-24579
### 第6章 代理
> 📌 [Web代理（proxy）服务器是网络的中间实体。代理位于客户端和服务器之间，扮演“中间人”的角色，在各端点之间来回传送HTTP报文](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=432&rangeEnd=497>)
> ⏱ 2022-01-20 12:55:40 ^26211809-14-432-497
> 📌 [单个客户端专用的代理被称为私有代理。众多客户端共享的代理被称为公共代理。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=1933&rangeEnd=2025>)
> ⏱ 2022-01-20 12:57:49 ^26211809-14-1933-2025
> 📌 [严格来说，代理连接的是两个或多个使用相同协议的应用程序，而网关连接的则是两个或多个使用不同协议的端点。网关扮演的是“协议转换器”的角色，即使客户端和服务器使用的是不同的协议，客户端也可以通过它完成与服务器之间的事务处理。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=2471&rangeEnd=2581>)
> ⏱ 2022-01-20 12:59:12 ^26211809-14-2471-2581
> 📌 [实际上，代理和网关之间的区别很模糊。由于浏览器和服务器实现的是不同版本的HTTP，代理也经常要做一些协议转换工作。而商业化的代理服务器也会实现网关的功能来支持SSL安全协议、SOCKS防火墙、FTP访问，以及基于Web的应用程序。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=3180&rangeEnd=3295>)
> ⏱ 2022-01-20 13:00:16 ^26211809-14-3180-3295
> 📌 [可以用代理服务器在大量Web服务器和Web资源之间实现统一的访问控制策略，创建审核跟踪机制。这在大型企业环境或其他分布式机构中是很有用的。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=4123&rangeEnd=4192>)
> ⏱ 2022-01-20 13:04:14 ^26211809-14-4123-4192
> 📌 [网络安全工程师通常会使用代理服务器来提高安全性。代理服务器会在网络中的单一安全节点上限制哪些应用层协议的数据可以流入或流出一个组织。还可以提供用来消除病毒的Web和E-mail代理使用的那种挂钩程序，以便对流量进行详细的检查](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=4941&rangeEnd=5053>)
> ⏱ 2022-01-20 13:05:50 ^26211809-14-4941-5053
> 📌 [代理缓存维护了常用文档的本地副本，并将它们按需提供，以减少缓慢且昂贵的因特网通信。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=5383&rangeEnd=5424>)
> ⏱ 2022-01-20 13:07:01 ^26211809-14-5383-5424
> 📌 [可以用这些反向代理来提高访问慢速Web服务器上公共内容时的性能。在这种配置中，通常将这些反向代理称为服务器加速器（serveraccelerator）（参见图6-7）。还可以将替代物与内容路由功能配合使用，以创建按需复制内容的分布式网络。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=6032&rangeEnd=6180>)
> ⏱ 2022-01-20 13:08:07 ^26211809-14-6032-6180
> 📌 [代理服务器在将内容发送给客户端之前，可以修改内容的主体格式。在这些数据表示法之间进行的透明转换被称为转码（transcoding）。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=7042&rangeEnd=7136>)
> ⏱ 2022-01-20 13:09:36 ^26211809-14-7042-7136
> 📌 [匿名者代理会主动从HTTP报文中删除身份特性（比如客户端IP地址、From首部、Referer首部、cookie、URI的会话ID），从而提供高度的私密性和匿名性。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=7885&rangeEnd=7967>)
> ⏱ 2022-01-20 13:11:00 ^26211809-14-7885-7967
> 📌 [通过HTTP OPTIONS方法，客户端（或代理）可以发现Web服务器或者其上某个特定资源所支持的功能（比如，它们所支持的方法）（参见图6-26）。通过使用OPTIONS，客户端可以在与服务器进行交互之前，确定服务器的能力，这样它就可以更方便地与具备不同特性的代理和服务器进行互操作了。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=35410&rangeEnd=35553>)
> ⏱ 2022-01-22 22:11:38 ^26211809-14-35410-35553
> 📌 [可以将Allow首部作为请求首部，建议在新的资源上支持某些方法。并不要求服务器支持这些方法，但应该在相应的响应中包含一个Allow首部，列出它实际支持的方法。](<weread://bestbookmark?bookId=26211809&chapterUid=14&rangeStart=36627&rangeEnd=36706>)
> ⏱ 2022-01-22 22:21:25 ^26211809-14-36627-36706
### 第7章 缓存
> 📌 [可以用已有的副本为某些到达缓存的请求提供服务。这被称为缓存命中（cache hit），参见图7-4a。其他一些到达缓存的请求可能会由于没有副本可用，而被转发给原始服务器。这被称为缓存未命中（cache miss）](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=4449&rangeEnd=4611>)
> ⏱ 2022-01-22 22:26:04 ^26211809-15-4449-4611
> 📌 [原始服务器的内容可能会发生变化，缓存要不时对其进行检测，看看它们保存的副本是否仍是服务器上最新的副本。这些“新鲜度检测”被称为HTTP再验证（revalidation）（参见图7-4c）。为了有效地进行再验证，HTTP定义了一些特殊的请求，不用从服务器上获取整个对象，就可以快速检测出内容是否是最新的。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=4971&rangeEnd=5150>)
> ⏱ 2022-01-22 22:27:42 ^26211809-15-4971-5150
> 📌 [缓存对缓存的副本进行再验证时，会向原始服务器发送一个小的再验证请求。如果内容没有变化，服务器会以一个小的304Not Modified进行响应。只要缓存知道副本仍然有效，就会再次将副本标识为暂时新鲜的，并将副本提供给客户端（参见图7-5a）这被称作再验证命中（revalidate hit）或缓慢命中（slow hit）。这种方式确实要与原始服务器进行核对，所以会比单纯的缓存命中要慢，但它没有从服务器中获取对象数据，所以要比缓存未命中快一些。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=5328&rangeEnd=5635>)
> ⏱ 2022-01-22 22:29:41 ^26211809-15-5328-5635
> 📌 [由缓存提供服务的请求所占的比例被称为缓存命中率（cachehit rate，或称为缓存命中比例）,[插图]有时也被称为文档命中率（document hit rate）。命中率在0到1之间，但通常是用百分数来描述的，0%表示每次请求都未命中（要通过网络来获取文档）,100%表示每次请求都命中了（在缓存中有一份副本）。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=6900&rangeEnd=7240>)
> ⏱ 2022-01-22 22:38:10 ^26211809-15-6900-7240
> 📌 [缓存的管理者希望缓存命中率接近100%。而实际得到的命中率则与缓存的大小、缓存用户兴趣点的相似性、缓存数据的变化或个性化频率，以及如何配置缓存有关。命中率很难预测，但对现在中等规模的Web缓存来说，40%的命中率是很合理的。缓存的好处是，即使是中等规模的缓存，其所包含的常见文档也足以显著地提高性能、减少流量了。缓存会努力确保将有用的内容保存在缓存中。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=7400&rangeEnd=7576>)
> ⏱ 2022-01-22 22:38:50 ^26211809-15-7400-7576
> 📌 [客户端有一种方法可以判断响应是否来自缓存，就是使用Date首部。将响应中Date首部的值与当前时间进行比较，如果响应中的日期值比较早，客户端通常就可以认为这是一条缓存的响应。客户端也可以通过Age首部来检测缓存的响应，通过这个首部可以分辨出这条响应的使用期](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=8369&rangeEnd=8497>)
> ⏱ 2022-01-22 22:46:50 ^26211809-15-8369-8497
> 📌 [缓存可以是单个用户专用的，也可以是数千名用户共享的。专用缓存被称为私有缓存（private cache）。私有缓存是个人的缓存，包含了单个用户最常用的页面（参见图7-7a）。共享的缓存被称为公有缓存（public cache）。公有缓存中包含了某个用户团体的常用页面](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=8615&rangeEnd=8804>)
> ⏱ 2022-01-22 22:47:29 ^26211809-15-8615-8804
> 📌 [私有缓存不需要很大的动力或存储空间，这样就可以将其做得很小，很便宜。Web浏览器中有内建的私有缓存——大多数浏览器都会将常用文档缓存在你个人电脑的磁盘和内存中，并且允许用户去配置缓存的大小和各种设置。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=9160&rangeEnd=9260>)
> ⏱ 2022-01-22 22:49:02 ^26211809-15-9160-9260
> 📌 [公有缓存是特殊的共享代理服务器，被称为缓存代理服务器（caching proxy server），或者更常见地被称为代理缓存（proxy cache）（第6章讨论过代理）。代理缓存会从本地缓存中提供文档，或者代表用户与服务器进行联系。公有缓存会接受来自多个用户的访问，所以通过它可以更好地减少冗余流量。[插图]](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=9579&rangeEnd=9787>)
> ⏱ 2022-01-22 22:54:50 ^26211809-15-9579-9787
> 📌 [现代的商业化代理缓存相当地复杂。这些缓存构建得非常高效，可以支持HTTP和其他一些技术的各种高级特性。但除了一些微妙的细节之外，Web缓存的基本工作原理大多很简单。对一条HTTP GET报文的基本缓存处理过程包括7个步骤](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=12888&rangeEnd=12998>)
> ⏱ 2022-01-22 23:07:59 ^26211809-15-12888-12998
> 📌 [通过特殊的HTTP Cache-Control首部和Expires首部，HTTP让原始服务器向每个文档附加了一个“过期日期”（参见图7-13）。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=17225&rangeEnd=17297>)
> ⏱ 2022-01-22 23:15:46 ^26211809-15-17225-17297
> 📌 [服务器用HTTP/1.0+的Expires首部或HTTP/1.1的Cache-Control: max-age响应首部来指定过期日期，同时还会带有响应主体。Expires首部和Cache-Control:max-age首部所做的事情本质上是一样的，但由于Cache-Control首部使用的是相对时间而不是绝对日期，所以我们更倾向于使用比较新的Cache-Control首部。绝对日期依赖于计算机时钟的正确设置。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=17870&rangeEnd=18076>)
> ⏱ 2022-01-22 23:17:33 ^26211809-15-17870-18076
> 📌 [服务器可以通过HTTP定义的几种方式来指定在文档过期之前可以将其缓存多长时间。按照优先级递减的顺序，服务器可以：· 附加一个Cache-Control: no-store首部到响应中去；· 附加一个Cache-Control: no-cache首部到响应中去；· 附加一个Cache-Control: must-revalidate首部到响应中去；· 附加一个Cache-Control: max-age首部到响应中去；· 附加一个Expires日期首部到响应中去；· 不附加过期信息，让缓存确定自己的过期日期。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=25550&rangeEnd=25986>)
> ⏱ 2022-01-22 23:28:48 ^26211809-15-25550-25986
> 📌 [Web浏览器都有Refresh（刷新）或Reload（重载）按钮，可以强制对浏览器或代理缓存中可能过期的内容进行刷新。Refresh按钮会发布一个附加了Cache-Control请求首部的GET请求，这个请求会强制进行再验证，或者无条件地从服务器获取文档。Refresh的确切行为取决于特定的浏览器、文档以及拦截缓存的配置。](<weread://bestbookmark?bookId=26211809&chapterUid=15&rangeStart=29885&rangeEnd=30047>)
> ⏱ 2022-01-22 23:38:27 ^26211809-15-29885-30047
### 第8章 集成点：网关、隧道及中继
> 📌 [开发者提出了网关（gateway）的概念，网关可以作为某种翻译器使用，它抽象出了一种能够到达资源的方法。网关是资源和应用程序之间的粘合剂。应用程序可以（通过HTTP或其他已定义的接口）请求网关来处理某条请求，网关可以提供一条响应。网关可以向数据库发送查询语句，或者生成动态的内容，就像一个门一样：进去一条请求，出来一个响应。](<weread://bestbookmark?bookId=26211809&chapterUid=16&rangeStart=1309&rangeEnd=1499>)
> ⏱ 2022-01-25 12:42:58 ^26211809-16-1309-1499
> 📌 [客户端和服务器端网关Web网关在一侧使用HTTP协议，在另一侧使用另一种协议。[插图]可以用一个斜杠来分隔客户端和服务器端协议，并以此对网关进行描述：<客户端协议>/<服务器端协议>因此，将HTTP客户端连接到NNTP新闻服务器的网关就是一个HTTP/NNTP网关。我们用术语服务器端网关和客户端网关来说明对话是在网关的哪一侧进行的。· 服务器端网关（server-side gateway）通过HTTP与客户端对话，通过其他协议与服务器通信（HTTP/＊）。· 客户端网关（client-side gateway）通过其他协议与客户端对话，通过HTTP与服务器通信（＊/HTTP）。](<weread://bestbookmark?bookId=26211809&chapterUid=16&rangeStart=2741&rangeEnd=3480>)
> ⏱ 2022-01-25 12:44:16 ^26211809-16-2741-3480
> 📌 [一个组织可以通过网关对所有的输入Web请求加密，以提供额外的隐私和安全性保护。客户端可以用普通的HTTP浏览Web内容，但网关会自动加密用户的对话](<weread://bestbookmark?bookId=26211809&chapterUid=16&rangeStart=5913&rangeEnd=5986>)
> ⏱ 2022-01-25 12:49:13 ^26211809-16-5913-5986
> 📌 [HTTP中继（relay）是没有完全遵循HTTP规范的简单HTTP代理。中继负责处理HTTP中建立连接的部分，然后对字节进行盲转发。](<weread://bestbookmark?bookId=26211809&chapterUid=16&rangeStart=17356&rangeEnd=17450>)
> ⏱ 2022-01-25 13:04:12 ^26211809-16-17356-17450
### 第11章 客户端识别与cookie机制
> 📌 [可以笼统地将cookie分为两类：会话cookie和持久cookie。会话cookie是一种临时cookie，它记录了用户访问站点时的设置和偏好。用户退出浏览器时，会话cookie就被删除了。持久cookie的生存时间更长一些；它们存储在硬盘上，浏览器退出，计算机重启时它们仍然存在。通常会用持久cookie维护某个用户会周期性访问的站点的配置文件或登录名。](<weread://bestbookmark?bookId=26211809&chapterUid=20&rangeStart=9538&rangeEnd=9717>)
> ⏱ 2022-02-06 18:37:32 ^26211809-20-9538-9717
> 📌 [会话cookie和持久cookie之间唯一的区别就是它们的过期时间。稍后我们会看到，如果设置了Discard参数，或者没有设置Expires或Max-Age参数来说明扩展的过期时间，这个cookie就是一个会话cookie。](<weread://bestbookmark?bookId=26211809&chapterUid=20&rangeStart=9746&rangeEnd=9858>)
> ⏱ 2022-02-06 18:53:58 ^26211809-20-9746-9858
### 第12章 基本认证机制
> 📌 [HTTP定义了两个官方的认证协议：基本认证和摘要认证。](<weread://bestbookmark?bookId=26211809&chapterUid=21&rangeStart=2583&rangeEnd=2610>)
> ⏱ 2022-02-06 19:07:29 ^26211809-21-2583-2610

# 读书笔记

# 本书评论
