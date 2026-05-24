---
doc_type: weread-highlights-reviews
bookId: "37730890"
title: JavaScript深度学习
reviewCount: 0
noteCount: 12
author: 蔡善清 斯坦利·比列斯奇 埃里克·D. 尼尔森 弗朗索瓦·肖莱
cover: https://cdn.weread.qq.com/weread/cover/59/YueWen_37730890/t6_YueWen_37730890.jpg
readingStatus: "2"
progress: 46%
readingTime: 1小时21分钟
readingDate: 2021-05-23
isbn: 9787115561145
lastReadDate: 2021-10-22

---
# 元数据
> [!abstract] JavaScript深度学习
> - ![ JavaScript深度学习|200](https://cdn.weread.qq.com/weread/cover/59/YueWen_37730890/t6_YueWen_37730890.jpg)
> - 书名： JavaScript深度学习
> - 作者： 蔡善清 斯坦利·比列斯奇 埃里克·D. 尼尔森 弗朗索瓦·肖莱
> - 简介： 本书教你使用TensorFlow.js构建强大的JavaScript深度学习应用程序。本书作者均是谷歌大脑团队的资深工程师，也是TensorFlow.js的核心开发人员。你将了解JavaScript与深度学习结合的独特优势，掌握客户端预测与分析、图像识别、监督学习、迁移学习、强化学习等核心概念，并动手在浏览器中实现计算机视觉和音频处理以及自然语言处理，构建并训练神经网络，利用客户端数据优化机器学习模型，开发基于浏览器的交互式游戏，同时为深度学习探索新的应用空间。你还可以获得深度学习模型构建过程中不同问题所涉及的策略和相关限制的实用知识，同时了解训练和部署这些模型的具体步骤以及重要的注意事项。
> - 出版时间： 2021-04-01 00:00:00
> - ISBN： 9787115561145
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/05232050723fba4a0522a7c

# 高亮划线
### 第 2 章 TensorFlow.js入门：从简单的线性回归开始
> 📌 [一个输入和一个输出对应的组合通常叫作样例（example）。输出通常又叫作目标（target），输入中的各种元素叫作特征（feature）。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=5689&rangeEnd=5810>)
> ⏱ 2021-08-19 20:30:35 ^37730890-15-5689-5810
> 📌 [向量和矩阵，其实它们本质上分别是一维张量和二维张量。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=7566&rangeEnd=7592>)
> ⏱ 2021-08-19 20:28:16 ^37730890-15-7566-7592
> 📌 [维度数和每个维度的尺寸叫作张量的形状（shape）](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=7611&rangeEnd=7653>)
> ⏱ 2021-08-19 20:28:08 ^37730890-15-7611-7653
> 📌 [在张量的语境下，维度通常又叫作轴（axis）。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=7714&rangeEnd=7754>)
> ⏱ 2021-08-19 20:28:33 ^37730890-15-7714-7754
> 📌 [在深度学习的语境下，将输入特征映射到输出目标上的函数叫作模型（model）。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=7928&rangeEnd=7983>)
> ⏱ 2021-08-19 20:29:11 ^37730890-15-7928-7983
> 📌 [在深度学习中，模型还可以叫作网络（network](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=8054&rangeEnd=8095>)
> ⏱ 2021-08-19 20:29:23 ^37730890-15-8054-8095
> 📌 [在机器学习中，回归（regression）指模型会输出实数值，并且会尝试匹配训练集中的目标](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=8173&rangeEnd=8235>)
> ⏱ 2021-08-23 11:41:23 ^37730890-15-8173-8235
> 📌 [神经网络的核心组成部分是层（layer），它是一个数据处理模块，可以看作张量之间的一个可调函数。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=8821&rangeEnd=8886>)
> ⏱ 2021-08-19 20:31:58 ^37730890-15-8821-8886
> 📌 [密集层就是执行每组输入与输出之间的可调的乘积累加（multiply-add）运算。因为只有一个输入和一个输出，所以这个模型就是高中所学的简单线性方程：y = m * x + b。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=9077&rangeEnd=9183>)
> ⏱ 2021-08-19 20:32:28 ^37730890-15-9077-9183
> 📌 [在密集层中，m叫作核（kernel），b叫作偏差（bias）。](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=9191&rangeEnd=9256>)
> ⏱ 2021-08-19 20:32:38 ^37730890-15-9191-9256
> 📌 [针对训练集的每一次完整迭代叫作一个轮次](<weread://bestbookmark?bookId=37730890&chapterUid=15&rangeStart=11881&rangeEnd=11908>)
> ⏱ 2021-08-19 20:41:27 ^37730890-15-11881-11908
### 第 4 章 用convnet识别图像和音频
> 📌 [深度学习会用三维张量来表示图像数据。张量的前两个维度分别是我们熟悉的高度和宽度，第3个维度是颜色通道（color channel）。](<weread://bestbookmark?bookId=37730890&chapterUid=17&rangeStart=1609&rangeEnd=1692>)
> ⏱ 2021-10-22 20:46:16 ^37730890-17-1609-1692

# 读书笔记

# 本书评论
