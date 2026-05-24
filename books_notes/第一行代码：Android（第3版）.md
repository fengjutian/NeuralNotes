---
doc_type: weread-highlights-reviews
bookId: "37683759"
title: 第一行代码：Android（第3版）
reviewCount: 0
noteCount: 18
author: 郭霖
cover: https://cdn.weread.qq.com/weread/cover/74/YueWen_37683759/t6_YueWen_37683759.jpg
readingStatus: "2"
progress: 39%
readingTime: 3小时14分钟
readingDate: 2021-05-23
isbn: 9787115524836
lastReadDate: 2021-12-07

---
# 元数据
> [!abstract] 第一行代码：Android（第3版）
> - ![ 第一行代码：Android（第3版）|200](https://cdn.weread.qq.com/weread/cover/74/YueWen_37683759/t6_YueWen_37683759.jpg)
> - 书名： 第一行代码：Android（第3版）
> - 作者： 郭霖
> - 简介： 《第一行代码 Android 第3版》被Android开发者誉为“Android学习第一书”。全书系统全面、循序渐进地介绍了Android软件开发的必备知识、经验和技巧。《第一行代码 Android 第3版》基于Android 10.0对第2版进行了全面更新，不仅将所有知识点都在Android 10.0系统上进行了重新适配，同时加入Kotlin语言的全面讲解，使用Kotlin对全书代码进行重写，而且还介绍了最新系统特性以及Jetpack架构组件的使用，使本书更加实用。《第一行代码 Android 第3版》内容通俗易懂，由浅入深，既是Android初学者的入门必备，也是Android开发者的进阶首选。
> - 出版时间： 2020-04-01 00:00:00
> - ISBN： 9787115524836
> - 分类： 计算机-计算机综合
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/73532150723f022f73516a6

# 高亮划线
## 第 1 章 开始启程，你的第一行Android代码
> 📌 [Android大致可以分为4层架构：Linux内核层、系统运行库层、应用框架层和应用层。](<weread://bestbookmark?bookId=37683759&chapterUid=5&rangeStart=2009&rangeEnd=2053>)
> ⏱ 2021-05-23 19:29:07 ^37683759-5-2009-2053
## 第 2 章 探究新语言，快速入门Kotlin编程
> 📌 [Kotlin中定义一个变量，只允许在变量前声明两种关键字：val和var。val（value的简写）用来声明一个不可变的变量，这种变量在初始赋值之后就再也不能重新赋值，对应Java中的final变量。var（variable的简写）用来声明一个可变的变量，这种变量在初始赋值之后仍然可以再被重新赋值，对应Java中的非final变量。](<weread://bestbookmark?bookId=37683759&chapterUid=6&rangeStart=6963&rangeEnd=7156>)
> ⏱ 2021-05-23 22:12:15 ^37683759-6-6963-7156
> 📌 [程序的执行语句主要分为3种：顺序语句、条件语句和循环语句。](<weread://bestbookmark?bookId=37683759&chapterUid=6&rangeStart=14539&rangeEnd=14568>)
> ⏱ 2021-05-23 22:26:23 ^37683759-6-14539-14568
## 第 3 章 先从看得到的入手，探究Activity
> 📌 [项目中的任何Activity都应该重写onCreate()方法](<weread://bestbookmark?bookId=37683759&chapterUid=7&rangeStart=2796&rangeEnd=2827>)
> ⏱ 2021-12-04 22:59:41 ^37683759-7-2796-2827
> 📌 [android:id是给当前的元素定义一个唯一的标识符，之后可以在代码中对这个元素进行操作。](<weread://bestbookmark?bookId=37683759&chapterUid=7&rangeStart=5029&rangeEnd=5075>)
> ⏱ 2021-12-04 23:05:12 ^37683759-7-5029-5075
> 📌 [android:layout_width指定了当前元素的宽度，这里使用match_parent表示让当前元素和父元素一样宽。android:layout_height指定了当前元素的高度，这里使用wrap_content表示当前元素的高度只要能刚好包含里面的内容就行。](<weread://bestbookmark?bookId=37683759&chapterUid=7&rangeStart=5252&rangeEnd=5386>)
> ⏱ 2021-12-05 16:37:06 ^37683759-7-5252-5386
> 📌 [Intent大致可以分为两种：显式Intent和隐式Intent。](<weread://bestbookmark?bookId=37683759&chapterUid=7&rangeStart=19570&rangeEnd=19603>)
> ⏱ 2021-12-05 17:10:57 ^37683759-7-19570-19603
## 第 4 章 软件也要拼脸蛋，UI开发的点点滴滴
> 📌 [android:layout_width和android:layout_height指定了控件的宽度和高度。Android中所有的控件都具有这两个属性，可选值有3种：match_parent、wrap_content和固定值。match_parent表示让当前控件的大小和父布局的大小一样，也就是由父布局来决定当前控件的大小。wrap_content表示让当前控件的大小能够刚好包含住里面的内容，也就是由控件内容决定当前控件的大小。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=2577&rangeEnd=2793>)
> ⏱ 2021-12-05 19:32:34 ^37683759-8-2577-2793
> 📌 [android:gravity来指定文字的对齐方式，可选值有top、bottom、start、end、center等，可以用“|”来同时指定多个值，](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=3831&rangeEnd=3905>)
> ⏱ 2021-12-05 19:33:17 ^37683759-8-3831-3905
> 📌 [Android系统默认会将按钮上的英文字母全部转换成大写，可能是认为按钮上的内容都比较重要吧。如果这不是你想要的效果，可以在XML中添加android:textAllCaps="false"这个属性，这样系统就会保留你指定的原始文字内容了。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=6262&rangeEnd=6382>)
> ⏱ 2021-12-05 19:42:55 ^37683759-8-6262-6382
> 📌 [Android控件的可见属性。所有的Android控件都具有这个属性，可以通过android:visibility进行指定，可选值有3种：visible、invisible和gone。visible表示控件是可见的，这个值是默认值，不指定android:visibility时，控件都是可见的。invisible表示控件不可见，但是它仍然占据着原来的位置和大小，可以理解成控件变成透明状态了。gone则表示控件不仅不可见，而且不再占用任何屏幕空间。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=15119&rangeEnd=15343>)
> ⏱ 2021-12-05 20:21:57 ^37683759-8-15119-15343
> 📌 [LinearLayout又称作线性布局，是一种非常常用的布局。正如它的名字所描述的一样，这个布局会将它所包含的控件在线性方向上依次排列。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=19745&rangeEnd=19813>)
> ⏱ 2021-12-05 20:24:44 ^37683759-8-19745-19813
> 📌 [既然是线性排列，肯定就不只有一个方向，那为什么上一节中的控件都是在垂直方向排列的呢？这是由于我们通过android:orientation属性指定了排列方向是vertical，如果指定的是horizontal，控件就会在水平方向上排列了。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=19906&rangeEnd=20025>)
> ⏱ 2021-12-05 20:25:52 ^37683759-8-19906-20025
> 📌 [RelativeLayout又称作相对布局，也是一种非常常用的布局。和LinearLayout的排列规则不同，RelativeLayout显得更加随意，它可以通过相对定位的方式让控件出现在布局的任何位置](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=26652&rangeEnd=26753>)
> ⏱ 2021-12-05 20:33:52 ^37683759-8-26652-26753
> 📌 [FrameLayout又称作帧布局，它相比于前面两种布局就简单太多了，因此它的应用场景少了很多。这种布局没有丰富的定位方式，所有的控件都会默认摆放在布局的左上角。](<weread://bestbookmark?bookId=37683759&chapterUid=8&rangeStart=31551&rangeEnd=31632>)
> ⏱ 2021-12-05 20:35:08 ^37683759-8-31551-31632
## 第 6 章 全局大喇叭，详解广播机制
> 📌 [标准广播（normal broadcasts）是一种完全异步执行的广播，在广播发出之后，所有的BroadcastReceiver几乎会在同一时刻收到这条广播消息，因此它们之间没有任何先后顺序可言。这种广播的效率会比较高，但同时也意味着它是无法被截断的。](<weread://bestbookmark?bookId=37683759&chapterUid=10&rangeStart=1149&rangeEnd=1275>)
> ⏱ 2021-12-07 12:48:32 ^37683759-10-1149-1275
> 📌 [有序广播（ordered broadcasts）则是一种同步执行的广播，在广播发出之后，同一时刻只会有一个BroadcastReceiver能够收到这条广播消息，当这个BroadcastReceiver中的逻辑执行完毕后，广播才会继续传递。](<weread://bestbookmark?bookId=37683759&chapterUid=10&rangeStart=1548&rangeEnd=1668>)
> ⏱ 2021-12-07 12:49:35 ^37683759-10-1548-1668
> 📌 [注册BroadcastReceiver的方式一般有两种：在代码中注册和在AndroidManifest.xml中注册。其中前者也被称为动态注册，后者也被称为静态注册。](<weread://bestbookmark?bookId=37683759&chapterUid=10&rangeStart=2498&rangeEnd=2581>)
> ⏱ 2021-12-07 12:50:04 ^37683759-10-2498-2581

# 读书笔记

# 本书评论
