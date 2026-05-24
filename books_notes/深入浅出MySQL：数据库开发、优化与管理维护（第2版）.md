---
doc_type: weread-highlights-reviews
bookId: "730561"
title: 深入浅出MySQL：数据库开发、优化与管理维护（第2版）
reviewCount: 0
noteCount: 14
author: 唐汉明 翟振兴 关宝军 王洪权 黄潇
cover: https://cdn.weread.qq.com/weread/cover/72/YueWen_730561/t6_YueWen_730561.jpg
readingStatus: "2"
progress: 12%
readingTime: 1小时52分钟
readingDate: 2020-06-29
isbn: 9787115335494
lastReadDate: 2022-01-23

---
# 元数据
> [!abstract] 深入浅出MySQL：数据库开发、优化与管理维护（第2版）
> - ![ 深入浅出MySQL：数据库开发、优化与管理维护（第2版）|200](https://cdn.weread.qq.com/weread/cover/72/YueWen_730561/t6_YueWen_730561.jpg)
> - 书名： 深入浅出MySQL：数据库开发、优化与管理维护（第2版）
> - 作者： 唐汉明 翟振兴 关宝军 王洪权 黄潇
> - 简介： 《深入浅出MySQL：数据库开发、优化与管理维护（第2版）》从数据库的基础、开发、优化、管理维护和架构5个方面对MySQL进行了详细的介绍，每一部分都独立成篇。基础篇主要适合于MySQL的初学者阅读，包括MySQL的安装与配置、SQL基础、MySQL支持的数据类型、MySQL中的运算符、常用函数、图形化工具的使用等内容。开发篇主要适合于MySQL的设计和开发人员阅读，内容包括表类型（存储引擎）的选择、选择合适的数据类型、字符集、索引的设计和使用、视图、存储过程和函数、触发器、事务控制和锁定语句、SQL中的安全问题、SQL Mode及相关问题、分区等。优化篇主要适合于开发人员和数据库管理员阅读，内容包括SQL优化、优化数据库对象、锁问题、优化MySQL Server、磁盘I/O问题、应用优化等。管理维护篇主要适合于数据库管理员阅读，内容包括MySQL高级安装和升级、MySQL中的常用工具、MySQL日志、备份与恢复、MySQL权限与安全、MySQL监控、MySQL常见问题和应用技巧等。架构篇主要适合高级数据库管理人员和数据库架构设计师阅读，包括MySQL复制、MySQL Cluster、高可用架构等内容。《深入浅出MySQL：数据库开发、优化与管理维护（第2版）》的作者都是MySQL方面的资深DBA。本书不但融入了他们丰富的工作经验和多年的使用心得，还提供了大量来自工作现场的实例，具有很强的实战性和可操作性。《深入浅出MySQL：数据库开发、优化与管理维护（第2版）》内容实用，覆盖广泛，讲解由浅入深，适合数据库管理人员、数据库开发人员、系统维护人员、数据库初学者及其他数据库从业人员阅读，也适合用作大中专院校相关专业师生的参考用书和相关培训机构的培训教材。
> - 出版时间： 2014-01-01 00:00:00
> - ISBN： 9787115335494
> - 分类： 计算机-数据库
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/f3e327e05b25c1f3e6d5ee2

# 高亮划线
### 第2章 SQL基础
> 📌 [数据库的排序操作，用关键字ORDERBY来实现，语法如下：SELECT * FROM tablename [WHERE CONDITION] [ORDERBY field1 [DESC|ASC]，field2 [DESC|ASC],…,fieldn[DESC|ASC]]](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=37762&rangeEnd=37929>)
> ⏱ 2022-01-23 00:12:30 ^730561-6-67235-67402
> 📌 [其中，DESC和ASC是排序顺序关键字，DESC表示按照字段进行降序排列，ASC则表示升序排列，如果不写此关键字默认是升序排列。ORDER BY后面可以跟多个不同的排序字段，并且每个排序字段可以有不同的排序顺序。](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=37958&rangeEnd=38064>)
> ⏱ 2022-01-23 00:12:47 ^730561-6-67431-67537
> 📌 [聚合操作的语法如下：SELECT [field1,field2,…,fieldn] fun_nameFROM tablename[WHERE where_contition][GROUP BY field1,field2,…,fieldn[WITH ROLLUP]][HAVING where_contition]对其参数进行以下说明。](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=42236&rangeEnd=42607>)
> ⏱ 2022-01-23 00:15:43 ^730561-6-71709-72080
> 📌 [fun_name 表示要做的聚合操作，也就是聚合函数，常用的有sum（求和）、count(*) （记录数）、max（最大值）、min（最小值）。GROUP BY关键字表示要进行分类聚合的字段，比如要按照部门分类统计员工数量，部门就应该写在 group by后面。WITH ROLLUP是可选语法，表明是否对分类聚合后的结果进行再汇总。HAVING关键字表示对分类后的结果再进行条件的过滤。](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=42638&rangeEnd=42931>)
> ⏱ 2022-01-23 00:16:15 ^730561-6-72111-72404
> 📌 [当需要同时显示多个表中的字段时，就可以用表连接来实现这样的功能。从大类上分，表连接分为内连接和外连接，它们之间的最主要区别是，内连接仅选出两张表中互相匹配的记录，而外连接会选出其他不匹配的记录。我们最常用的是内连接。](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=46168&rangeEnd=46328>)
> ⏱ 2022-01-23 00:18:28 ^730561-6-75641-75801
> 📌 [外连接又分为左连接和右连接，具体定义如下。左连接：包含所有的左边表中的记录甚至是右边表中没有和它匹配的记录。右连接：包含所有的右边表中的记录甚至是左边表中没有和它匹配的记录。](<weread://bestbookmark?bookId=730561&chapterUid=19&rangeStart=48050&rangeEnd=48251>)
> ⏱ 2022-01-23 13:31:42 ^730561-6-77523-77724
### 第3章 MySQL支持的数据类型
> 📌 [MySQL 支持所有标准 SQL 中的数值类型，其中包括严格数值类型（ INTEGER、SMALLINT、DECIMAL和NUMERIC），以及近似数值数据类型（FLOAT、REAL和DOUBLEPRECISION），并在此基础上做了扩展。扩展后增加了TINYINT、MEDIUMINT和BIGINT这3种长度不同的整型，并增加了BIT类型，用来存放位数据。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=726&rangeEnd=906>)
> ⏱ 2022-01-23 13:40:30 ^730561-6-97515-97695
> 📌 [如果要用来表示年月日，通常用DATE来表示。如果要用来表示年月日时分秒，通常用DATETIME表示。如果只用来表示时分秒，通常用TIME来表示。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=15393&rangeEnd=15527>)
> ⏱ 2022-01-23 13:47:43 ^730561-6-112185-112319
> 📌 [MySQL中提供了多种对字符数据的存储类型，不同的版本可能有所差异。以5.0版本为例， MySQL包括了CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET等多种字符串类型。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=29807&rangeEnd=29916>)
> ⏱ 2022-01-23 14:00:59 ^730561-6-126600-126709
> 📌 [CHAR和VARCHAR很类似，都用来保存MySQL中较短的字符串。二者的主要区别在于存储方式的不同：CHAR列的长度固定为创建表时声明的长度，长度可以为从0～255的任何值；而VARCHAR列中的值为可变长字符串，长度可以指定为0～255（MySQL 5.0.3版本以前）或者 65535（MySQL 5.0.3版本以后）之间的值。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=30332&rangeEnd=30499>)
> ⏱ 2022-01-23 14:03:01 ^730561-6-127126-127293
> 📌 [BINARY和VARBINARY类似于CHAR和VARCHAR，不同的是它们包含二进制字符串而不包含非二进制字符串。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=32100&rangeEnd=32158>)
> ⏱ 2022-01-23 14:05:57 ^730561-6-128894-128952
> 📌 [ENUM中文名称叫枚举类型，它的值范围需要在创建表时通过枚举方式显式指定，对1～255个成员的枚举需要1个字节存储；对于255～65535个成员，需要2个字节存储。最多允许有65535个成员。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=33318&rangeEnd=33414>)
> ⏱ 2022-01-23 14:07:35 ^730561-6-130112-130208
> 📌 [SET和ENUM类型非常类似，也是一个字符串对象，里面可以包含0～64个成员。根据成员的不同，存储上也有所不同。1～8成员的集合，占1个字节。9～16成员的集合，占2个字节。17～24成员的集合，占3个字节。25～32成员的集合，占4个字节。33～64成员的集合，占8个字节。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=34615&rangeEnd=34908>)
> ⏱ 2022-01-23 14:10:32 ^730561-6-131409-131702
> 📌 [SET 和 ENUM 除了存储之外，最主要的区别在于 SET 类型一次可以选取多个成员，而ENUM则只能选一个。](<weread://bestbookmark?bookId=730561&chapterUid=20&rangeStart=34937&rangeEnd=34993>)
> ⏱ 2022-01-23 14:11:01 ^730561-6-131731-131787

# 读书笔记

# 本书评论
