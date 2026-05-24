---
doc_type: weread-highlights-reviews
bookId: "25755855"
title: Three.js开发指南：基于WebGL和HTML5在网页上渲染3D图形和动画（原书第3版）
reviewCount: 0
noteCount: 24
author: 乔斯·德克森
cover: https://cdn.weread.qq.com/weread/cover/56/YueWen_25755855/t6_YueWen_25755855.jpg
readingStatus: "4"
progress: 99%
readingTime: 4小时4分钟
readingDate: 2020-11-25
finishedDate: 2022-03-06
isbn: 9787111628842
lastReadDate: 2022-02-28

---
# 元数据
> [!abstract] Three.js开发指南：基于WebGL和HTML5在网页上渲染3D图形和动画（原书第3版）
> - ![ Three.js开发指南：基于WebGL和HTML5在网页上渲染3D图形和动画（原书第3版）|200](https://cdn.weread.qq.com/weread/cover/56/YueWen_25755855/t6_YueWen_25755855.jpg)
> - 书名： Three.js开发指南：基于WebGL和HTML5在网页上渲染3D图形和动画（原书第3版）
> - 作者： 乔斯·德克森
> - 简介： 本书将介绍如何直接在浏览器中创建漂亮的3D场景和动画，并且充分发挥WebGL和现代浏览器的潜能。首先介绍基本概念和基础组件，然后通过逐渐扩展示例代码逐步深入讲解更多高级技术。在本书中读者将学到如何从外部加载3D模型和具有真实效果的材质纹理、学习使用Three.js提供的摄像机组件来实现在3D场景中飞行和走动、如何将HTML5视频和画布作为材质贴在3D模型表面。此外还将学习变形动画和骨骼动画，甚至还会涉及在场景中使用物理模拟的方法，例如重力、碰撞检测等等。
> - 出版时间： 2019-06-01 00:00:00
> - ISBN： 9787111628842
> - 分类： 计算机-编程设计
> - 出版社： 机械工业出版社
> - PC地址：https://weread.qq.com/web/reader/6b232c00718900cf6b26bb6

# 高亮划线
### 2.1 创建场景
> 📌 [THREE.Scene对象有时被称为场景图，可以用来保存所有图形场景的必要信息。](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=958&rangeEnd=998>)
> ⏱ 2022-02-21 13:03:47 ^25755855-16-958-998
> 📌 [场景相关的方法：[插图]THREE.Scene.Add：用于向场景中添加对象[插图]THREE.Scene.Remove：用于移除场景中的对象[插图]THREE.Scene.children：用于获取场景中所有的子对象列表[插图]THREE.Scene.getObjectByName：利用name属性，用于获取场景中特定的对象](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=5561&rangeEnd=6365>)
> ⏱ 2022-02-21 13:04:55 ^25755855-16-5561-6365
> 📌 [使用fog属性就可以为整个场景添加雾化效果。雾化效果是：场景中的物体离摄像机越远就会变得越模糊。](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=7277&rangeEnd=7325>)
> ⏱ 2022-02-21 13:07:16 ^25755855-16-7277-7325
> 📌 [在Three.js中为场景添加雾化效果是很简单的，在定义完场景后只要添加如下代码即可：](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=7410&rangeEnd=7453>)
> ⏱ 2022-02-21 13:07:49 ^25755855-16-7410-7453
> 📌 [我们在这里定义一个白色雾化效果（0xffffff）。后面的两个参数是用来调节雾的显示，0.015是near（近处）属性的值，100是far（远处）属性的值。通过这两个属性可以决定雾化开始和结束的地方，以及加深的程度。](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=7905&rangeEnd=8013>)
> ⏱ 2022-02-21 13:09:35 ^25755855-16-7905-8013
> 📌 [在这个方法中不再指定near和far属性，只需要设置雾的颜色（0xffffff）和浓度（0.01）即可。需要注意的是，该方法中雾的浓度不再是线性增长的，而是随着距离呈指数增长。](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=8282&rangeEnd=8370>)
> ⏱ 2022-02-21 13:11:19 ^25755855-16-8282-8370
> 📌 [它是在渲染时你想使用的所有物体、光源的容器。](<weread://bestbookmark?bookId=25755855&chapterUid=16&rangeStart=9382&rangeEnd=9404>)
> ⏱ 2022-02-21 13:12:11 ^25755855-16-9382-9404
### 2.2 几何体和网格
> 📌 [在Three.js中几何体基本上是三维空间中的点集（也被称作顶点）和将这些点连接起来的面。以立方体为例：](<weread://bestbookmark?bookId=25755855&chapterUid=17&rangeStart=1332&rangeEnd=1384>)
> ⏱ 2022-02-21 13:18:18 ^25755855-17-1332-1384
> 📌 [一个立方体有8个角。每个角都可以用x、y和z坐标点来定义，所以每个立方体在三维空间中都有8个点。在Three.js中，这些点称为顶点。[插图]一个立方体有6个面，每个角有一个顶点。在Three.js中，每个面都是包含3个顶点的三角形。所以，立方体的每个面都是由两个三角形面组成的。](<weread://bestbookmark?bookId=25755855&chapterUid=17&rangeStart=1548&rangeEnd=1848>)
> ⏱ 2022-02-21 13:29:55 ^25755855-17-1548-1848
### 2.3 选择合适的摄像机
> 📌 [Three.js库提供了两种不同的摄像机：正交投影摄像机和透视投影摄像机。](<weread://bestbookmark?bookId=25755855&chapterUid=18&rangeStart=416&rangeEnd=453>)
> ⏱ 2021-12-12 14:50:55 ^25755855-18-416-453
### 3.2 基础光源
> 📌 [在创建THREE.AmbientLight时，颜色将会应用到全局。该光源并没有特别的来源方向，并且THREE.AmbientLight不会生成阴影。通常，不能将THREE.AmbientLight作为场景中唯一的光源，因为它会将场景中的所有物体渲染为相同的颜色，而不管是什么形状。](<weread://bestbookmark?bookId=25755855&chapterUid=22&rangeStart=547&rangeEnd=687>)
> ⏱ 2022-02-24 13:01:33 ^25755855-22-547-687
> 📌 [[插图]THREE.PointLight从特定的一点向所有方向发射光线。[插图]THREE.SpotLight从特定的一点以锥形发射光线。[插图]THREE.DirectionalLight不是从单个点发射光线，而是从二维平面发射光线，光线彼此平行。](<weread://bestbookmark?bookId=25755855&chapterUid=22&rangeStart=6208&rangeEnd=6649>)
> ⏱ 2021-12-12 14:56:32 ^25755855-22-6074-6649
### 4.1 理解材质的共有属性
> 📌 [[插图]基础属性：这些属性是最常用的。通过这些属性，可以控制物体的不透明度、是否可见以及如何被引用（通过ID或是自定义名称）。[插图]融合属性：每个物体都有一系列的融合属性。这些属性决定了物体如何与背景融合。[插图]高级属性：有一些高级属性可以控制底层WebGL上下文对象渲染物体的方式。大多数情况下是不需要使用这些属性的。](<weread://bestbookmark?bookId=25755855&chapterUid=26&rangeStart=666&rangeEnd=1144>)
> ⏱ 2022-02-27 12:27:15 ^25755855-26-532-1144
> 📌 [材质有几个与融合相关的一般属性。融合决定了我们渲染的颜色如何与它们后面的颜色交互。](<weread://bestbookmark?bookId=25755855&chapterUid=26&rangeStart=1954&rangeEnd=1995>)
> ⏱ 2022-02-27 12:30:31 ^25755855-26-1954-1995
### 4.2 从简单的网格材质开始
> 📌 [MeshBasicMaterial是一种非常简单的材质，这种材质不考虑场景中光照的影响。](<weread://bestbookmark?bookId=25755855&chapterUid=27&rangeStart=1645&rangeEnd=1689>)
> ⏱ 2022-02-27 12:39:46 ^25755855-27-1645-1689
> 📌 [使用这种材质的物体，其外观不是由光照或某个材质属性决定的，而是由物体到摄像机的距离决定的。可以将这种材质与其他材质结合使用，从而很容易地创建出逐渐消失的效果。](<weread://bestbookmark?bookId=25755855&chapterUid=27&rangeStart=3876&rangeEnd=3955>)
> ⏱ 2022-02-27 12:42:25 ^25755855-27-3876-3955
> 📌 [如果回头看看THREE.MeshDepthMaterial的属性，你会发现没有选项可以用来设置方块的颜色。一切都是由材质的默认属性决定的。但是，Three.js库可以通过联合材质创建出新效果（这也是材质融合起作用的地方）。下面的代码展示了如何联合材质：](<weread://bestbookmark?bookId=25755855&chapterUid=27&rangeStart=5690&rangeEnd=5816>)
> ⏱ 2022-02-27 12:44:18 ^25755855-27-5690-5816
### 4.3 高级材质
> 📌 [这种材质可以用来创建暗淡的并不光亮的表面。该材质非常易用，而且会对场景中的光源产生反应。](<weread://bestbookmark?bookId=25755855&chapterUid=28&rangeStart=725&rangeEnd=769>)
> ⏱ 2022-02-27 12:56:51 ^25755855-28-725-769
> 📌 [通过THREE.MeshPhongMaterial可以创建一种光亮的材质。](<weread://bestbookmark?bookId=25755855&chapterUid=28&rangeStart=2206&rangeEnd=2243>)
> ⏱ 2022-02-27 13:06:40 ^25755855-28-2206-2243
> 📌 [THREE.MeshStandardMaterial这种材质使用更加正确的物理计算来决定物体表面如何与场景中的光源互动。这种材质不但能够更好地表现塑料质感和金属质感的表面，而且像开发者提供了表4.10中所列的两个新属性。](<weread://bestbookmark?bookId=25755855&chapterUid=28&rangeStart=4154&rangeEnd=4264>)
> ⏱ 2022-02-27 13:08:26 ^25755855-28-4154-4264
> 📌 [该材质与THREE.MeshStandardMaterial非常相似，但提供了对反光度的更多控制，因此它除了具有标准材质的全部属性之外，还增加了表4.11列出新属性。](<weread://bestbookmark?bookId=25755855&chapterUid=28&rangeStart=4973&rangeEnd=5056>)
> ⏱ 2022-02-27 13:09:32 ^25755855-28-4973-5056
### 4.4 线性几何体的材质
> 📌 [Three.js库提供了两种可用于线段的不同材质，如下所示：[插图]THREE.LineBasicMaterial：用于线段的基础材质，可以设置colors、linewidth、linecap和linejoin属性。[插图]THREE.LineDashedMaterial：它的属性与THREE.LineBasicMaterial的属性一样，但是可以通过指定虚线和空白间隙的长度来创建出虚线效果。](<weread://bestbookmark?bookId=25755855&chapterUid=29&rangeStart=483&rangeEnd=1001>)
> ⏱ 2022-02-27 13:13:55 ^25755855-29-483-1001
### 5.1 Three.js提供的基础几何体
> 📌 [通过这个几何体，你可以创建一个非常简单的二维圆（或部分圆）。](<weread://bestbookmark?bookId=25755855&chapterUid=32&rangeStart=2630&rangeEnd=2660>)
> ⏱ 2022-02-28 13:07:08 ^25755855-32-2630-2660
> 📌 [这个对象不仅非常类似于THREE.CircleGeometry，而且可以在中心定义一个孔](<weread://bestbookmark?bookId=25755855&chapterUid=32&rangeStart=5262&rangeEnd=5306>)
> ⏱ 2022-02-28 13:09:49 ^25755855-32-5262-5306

# 读书笔记

# 本书评论
