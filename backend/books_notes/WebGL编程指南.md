---
doc_type: weread-highlights-reviews
bookId: "3300053055"
title: WebGL编程指南
reviewCount: 0
noteCount: 12
author: 松田浩一  罗杰·李
cover: https://cdn.weread.qq.com/weread/cover/69/cpplatform_9qgc7bl7tdgcsnlnurwfje/t6_cpplatform_9qgc7bl7tdgcsnlnurwfje1679298463.jpg
readingStatus: "2"
progress: 54%
readingTime: 0小时57分钟
readingDate: 2023-05-04
isbn: 9787121229428
lastReadDate: 2023-05-06

---
# 元数据
> [!abstract] WebGL编程指南
> - ![ WebGL编程指南|200](https://cdn.weread.qq.com/weread/cover/69/cpplatform_9qgc7bl7tdgcsnlnurwfje/t6_cpplatform_9qgc7bl7tdgcsnlnurwfje1679298463.jpg)
> - 书名： WebGL编程指南
> - 作者： 松田浩一  罗杰·李
> - 简介： WebGL 是一项在网页上渲染三维图形的技术，也是HTML5 草案的一部分。本书的主要篇幅讲解了WebGL 原生API 和三维图形学的基础知识，包括渲染管线、着色器、矩阵变换、着色器编程语言（GLSL ES）等等，也讲解了使用WebGL 渲染三维场景的一般技巧，如光照、阴影、雾化等等。本书提供了丰富的示例程序供读者钻研，也提供了极具价值的附录供读者参考。
> - 出版时间： 2014-06-01 00:00:00
> - ISBN： 9787121229428
> - 分类： 计算机-计算机综合
> - 出版社： 电子工业出版社
> - PC地址：https://weread.qq.com/web/reader/520321c0813ab7b39g0153f0

# 高亮划线
## 第2章 WebGL入门
> 📌 [WebGL需要两种着色器，](<weread://bestbookmark?bookId=3300053055&chapterUid=12&rangeStart=19228&rangeEnd=19241>)
> ⏱ 2023-05-05 11:51:42 ^3300053055-12-19228-19241
> 📌 [●顶点着色器(Vertex shader)：顶点着色器是用来描述顶点特性（如位置、颜色等）的程序。顶点(vertex)是指二维或三维空间中的一个点，比如二维或三维图形的端点或交点。●片元着色器(Fragment shader)：进行逐片元处理过程如光照（见第8章“光照”）](<weread://bestbookmark?bookId=3300053055&chapterUid=12&rangeStart=19276&rangeEnd=19490>)
> ⏱ 2023-05-05 11:51:45 ^3300053055-12-19276-19490
> 📌 [通常，在WebGL中，当你面向计算机屏幕时，X轴是水平的（正方向为右），Y轴是垂直的（正方向为下），而Z轴垂直于屏幕（正方向为外）](<weread://bestbookmark?bookId=3300053055&chapterUid=12&rangeStart=30568&rangeEnd=30633>)
> ⏱ 2023-05-05 13:39:31 ^3300053055-12-30568-30633
> 📌 [默认情况下WebGL使用右手坐标系](<weread://bestbookmark?bookId=3300053055&chapterUid=12&rangeStart=30764&rangeEnd=30781>)
> ⏱ 2023-05-05 13:39:56 ^3300053055-12-30764-30781
## 第3章 绘制和变换三角形
> 📌 [构成三维模型的基本单位是三角形。](<weread://bestbookmark?bookId=3300053055&chapterUid=13&rangeStart=1228&rangeEnd=1244>)
> ⏱ 2023-05-05 13:44:21 ^3300053055-13-1228-1244
> 📌 [WebGL提供了一种很方便的机制，即缓冲区对象(buffer object)，它可以一次性地向着色器传入多个顶点的数据。缓冲区对象是WebGL系统中的一块内存区域，我们可以一次性地向缓冲区对象中填充大量的顶点数据，然后将这些数据保存在其中，供顶点着色器使用。](<weread://bestbookmark?bookId=3300053055&chapterUid=13&rangeStart=2759&rangeEnd=2914>)
> ⏱ 2023-05-05 13:45:42 ^3300053055-13-2759-2914
> 📌 [1.创建缓冲区对象（gl.createBuffer()）。2.绑定缓冲区对象（gl.bindBuffer()）。3.将数据写入缓冲区对象（gl.bufferData()）。4.将缓冲区对象分配给一个attribute变量（gl.vertexAttribPointer()）。5.开启attribute变量（gl.enableVertexAttribArray()）。](<weread://bestbookmark?bookId=3300053055&chapterUid=13&rangeStart=5965&rangeEnd=6304>)
> ⏱ 2023-05-05 13:48:50 ^3300053055-13-5965-6304
> 📌 [使用WebGL时，你需要调用gl.createBuffer()方法来创建缓冲区对象。](<weread://bestbookmark?bookId=3300053055&chapterUid=13&rangeStart=7256&rangeEnd=7298>)
> ⏱ 2023-05-05 13:49:37 ^3300053055-13-7256-7298
## 第5章 颜色与纹理
> 📌 [在三维图形学中，有一项很重要的技术可以解决这个问题，那就是纹理映射(texture mapping)。纹理映射其实非常简单，就是将一张图像（就像一张贴纸）映射（贴）到一个几何图形的表面上去。将一张真实世界的图片贴到一个由两个三角形组成的矩形上，这样矩形表面看上去就是这张图片。此时，这张图片又可以称为纹理图像(texture image)或纹理(texture)。](<weread://bestbookmark?bookId=3300053055&chapterUid=15&rangeStart=23644&rangeEnd=23904>)
> ⏱ 2023-05-06 09:58:13 ^3300053055-15-23644-23904
> 📌 [纹理映射的作用，就是根据纹理图像，为之前光栅化后的每个片元涂上合适的颜色。组成纹理图像的像素又被称为纹素(texels，texture elements)，每一个纹素的颜色都使用RGB或RGBA格式编码](<weread://bestbookmark?bookId=3300053055&chapterUid=15&rangeStart=23930&rangeEnd=24057>)
> ⏱ 2023-05-06 09:58:23 ^3300053055-15-23930-24057
> 📌 [在WebGL中，要进行纹理映射，需遵循以下四步：1. 准备好映射到几何图形上的纹理图像。2.为几何图形配置纹理映射方式。3.加载纹理图像，对其进行一些配置，以在WebGL中使用它。4.在片元着色器中将相应的纹素从纹理中抽取出来，并将纹素的颜色赋给片元。](<weread://bestbookmark?bookId=3300053055&chapterUid=15&rangeStart=24336&rangeEnd=24670>)
> ⏱ 2023-05-06 09:59:51 ^3300053055-15-24336-24670
> 📌 [纹理坐标是纹理图像上的坐标，通过纹理坐标可以在纹理图像上获取纹素颜色。WebGL系统中的纹理坐标系统是二维的](<weread://bestbookmark?bookId=3300053055&chapterUid=15&rangeStart=25750&rangeEnd=25804>)
> ⏱ 2023-05-06 10:00:56 ^3300053055-15-25750-25804

# 读书笔记

# 本书评论
