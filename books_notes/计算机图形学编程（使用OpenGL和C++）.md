---
doc_type: weread-highlights-reviews
bookId: "31403518"
title: 计算机图形学编程（使用OpenGL和C++）
reviewCount: 0
noteCount: 24
author: V.斯科特·戈登 约翰·克莱维吉
cover: https://cdn.weread.qq.com/weread/cover/7/YueWen_31403518/t6_YueWen_31403518.jpg
readingStatus: "2"
progress: 62%
readingTime: 1小时16分钟
readingDate: 2021-05-22
isbn: 9787115521286
lastReadDate: 2021-12-05

---
# 元数据
> [!abstract] 计算机图形学编程（使用OpenGL和C++）
> - ![ 计算机图形学编程（使用OpenGL和C++）|200](https://cdn.weread.qq.com/weread/cover/7/YueWen_31403518/t6_YueWen_31403518.jpg)
> - 书名： 计算机图形学编程（使用OpenGL和C++）
> - 作者： V.斯科特·戈登 约翰·克莱维吉
> - 简介： 本书以C++和OpenGL 作为工具，教授计算机图形学编程。全书共14 章和3 个附录。首先从图形编程的基础和准备工作开始，依次介绍了OpenGL 图像管线、图形编程数学基础、管理3D 图形数据、纹理贴图、3D 模型、光照、阴影、天空和背景、增强表面细节、参数曲面、曲面细分、几何着色器，以及其他相关的图形编程技术。附录分别介绍了Windows、macOS 平台上的安装设置，以及Nsight 图形调试器的应用。本书每章最后配备了不同形式的习题，供读者巩固所学知识。本书适合作为高等院校计算机科学专业的计算机图形编程课程的教材或辅导书，也适合对计算机图形编程感兴趣的读者自学。
> - 出版时间： 2020-02-01 00:00:00
> - ISBN： 9787115521286
> - 分类： 计算机-编程设计
> - 出版社： 人民邮电出版社
> - PC地址：https://weread.qq.com/web/reader/0853289071df2dfe085a04a

# 高亮划线
### 2.1 OpenGL管线
> 📌 [将GLSL程序载入这些着色器阶段也是C++/OpenGL程序的责任之一，其过程如下。（1）首先使用C++获取GLSL着色器代码，既可以从文件中读取，也可以硬编码在字符串中。（2）接下来创建OpenGL着色器对象并将GLSL着色器代码加载进着色器对象。（3）最后，用OpenGL命令编译并连接着色器对象，并将它们安装进GPU。](<weread://bestbookmark?bookId=31403518&chapterUid=17&rangeStart=968&rangeEnd=1217>)
> ⏱ 2021-10-23 16:58:42 ^31403518-17-968-1217
### 3.1 3D坐标系统
> 📌 [3D空间通常用3个坐标轴X、Y和Z来表示。这3个轴可以以两种方式来布置：左手或右手（它们是以轴的朝向来命名的，通过左手或右手大拇指与食指、中指成直角来进行构造）。](<weread://bestbookmark?bookId=31403518&chapterUid=26&rangeStart=416&rangeEnd=615>)
> ⏱ 2021-12-05 13:48:14 ^31403518-26-416-615
> 📌 [例如，OpenGL中的坐标系大体是右手坐标系，而Direct3D中大体是左手坐标系。](<weread://bestbookmark?bookId=31403518&chapterUid=26&rangeStart=1038&rangeEnd=1080>)
> ⏱ 2021-12-05 13:48:49 ^31403518-26-1038-1080
### 3.2 点
> 📌 [3D空间中的点可以通过使用形如（2, 8, −3）的符号，列出X、Y、Z的值来表示。不过，如果用齐次坐标——一种在19世纪初首次描述的表示法来表示点会更有用。在每个点的齐次坐标有4个值。前3个值表示X、Y和Z，第四个值W总是非零值，通常为1。因此，我们会将之前的点表示为（2, 8, −3, 1）。正如我们稍后将要看到的，齐次坐标将会使我们的图形学计算更高效。](<weread://bestbookmark?bookId=31403518&chapterUid=27&rangeStart=411&rangeEnd=734>)
> ⏱ 2021-12-05 13:51:16 ^31403518-27-411-734
> 📌 [用来存储齐次3D坐标的GLSL数据类型是vec4（“vec”代表向量，同时也可以用来表示点）。GLM库包含适合在C++/OpenGL应用中创建和存储3元和4元（齐次）点的类，分别叫作vec3和vec4。](<weread://bestbookmark?bookId=31403518&chapterUid=27&rangeStart=763&rangeEnd=895>)
> ⏱ 2021-12-05 13:51:27 ^31403518-27-763-895
### 3.3 矩阵
> 📌 [矩阵是矩形的值阵列，它的元素通常使用下标访问。第一个下标表示行号，第二个下标表示列号，下标从0开始。](<weread://bestbookmark?bookId=31403518&chapterUid=28&rangeStart=436&rangeEnd=493>)
> ⏱ 2021-12-05 13:53:32 ^31403518-28-436-493
> 📌 [GLSL语言中的mat4数据类型用来存储4×4矩阵。同样，GLM中有mat4类用以实例化并存储4×4矩阵。单位矩阵中一条对角线的值为1，其余值全为0：](<weread://bestbookmark?bookId=31403518&chapterUid=28&rangeStart=796&rangeEnd=900>)
> ⏱ 2021-12-05 13:54:43 ^31403518-28-796-900
> 📌 [任何值乘以单位矩阵都不会改变。在GLM中，调用构造函数glm::mat4 m(1.0f)以在变量m中生成单位矩阵。](<weread://bestbookmark?bookId=31403518&chapterUid=28&rangeStart=1114&rangeEnd=1199>)
> ⏱ 2021-12-05 13:55:54 ^31403518-28-1114-1199
### 3.4 变换矩阵
> 📌 [平移矩阵用于将物体从一个位置移至另一位置。它包含一个单位矩阵，同时X、Y和Z的移动量在A03、A13、A23。图3.3展示了平移矩阵和它与齐次坐标点相乘的效果。其结果是一个以平移值“移动过”的点。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=1125&rangeEnd=1445>)
> ⏱ 2021-12-05 14:51:28 ^31403518-29-1125-1445
> 📌 [GLM中有一些函数是用于构建与点相乘的平移矩阵的。其中相关的操作有：●glm::translate(x, y, z)构建平移(x, y, z)的矩阵；●mat4 × vec4。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=2283&rangeEnd=2459>)
> ⏱ 2021-12-05 14:53:10 ^31403518-29-2283-2459
> 📌 [缩放矩阵变换由单位矩阵和位于A00, A11, A22的X、Y、Z缩放因子组成。图3.4中展示了缩放矩阵的形式和当它与齐次坐标点相乘的效果：所得的结果是经过缩放值修改后的新点。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=2686&rangeEnd=2961>)
> ⏱ 2021-12-05 14:54:38 ^31403518-29-2686-2961
> 📌 [GLM中有一些函数是用于构建与点相乘的缩放矩阵的。其中相关的操作有：●glm::scale(x, y, z) 构建缩放(x, y, z)的矩阵；●mat4 × vec4。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=3231&rangeEnd=3404>)
> ⏱ 2021-12-05 14:55:16 ^31403518-29-3231-3404
> 📌 [在16世纪中叶，数学家莱昂哈德·欧拉表明，围绕任何轴的旋转都可以表示为绕X、Y、Z轴旋转的组合[EU76]。围绕这3个轴的旋转角度被称为欧拉角。这个被称为欧拉定理的发现，对我们很有用，因为对于每个坐标轴的旋转可以用矩阵变换来表示。旋转变换有3种，分别是绕X、Y和Z轴旋转，见图3.5。同时GLM中也有一些用于构建旋转矩阵的函数。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=3924&rangeEnd=4351>)
> ⏱ 2021-12-05 14:56:41 ^31403518-29-3924-4351
> 📌 [●glm::rotate(mat4, θ, x, y, z)构建绕X, Y, Z轴旋转θ度的缩放矩阵。●mat4 × vec4。](<weread://bestbookmark?bookId=31403518&chapterUid=29&rangeStart=4622&rangeEnd=4772>)
> ⏱ 2021-12-05 14:57:56 ^31403518-29-4622-4772
### 3.5 向量
> 📌 [向量表示大小和方向。它们没有特定位置。“移动”向量并不改变它所代表的含义。](<weread://bestbookmark?bookId=31403518&chapterUid=30&rangeStart=412&rangeEnd=449>)
> ⏱ 2021-12-05 15:00:35 ^31403518-30-412-449
> 📌 [在GLM和GLSL中有许多3D图形学中经常用到的向量操作。如假设有向量A(u, v,w)和B(x, y, z)：加减法：A ± B=(u ± x, v ± y, w ± z)glm: vec3 ± vec3GLSL: vec3 ± vec3归一化（变为长度=1）：[插图]=A/|A|=A/sqrt(u2+v2+w2)，其中|A| ≡向量A的长度glm: normalize(vec3) 或normalize(vec4)GLSL: normalize(vec3) 或normalize(vec4)](<weread://bestbookmark?bookId=31403518&chapterUid=30&rangeStart=1649&rangeEnd=2862>)
> ⏱ 2021-12-05 15:03:42 ^31403518-30-1649-2862
> 📌 [点积：A·B=ux+vy+wzglm: dot(vec3,vec3) 或dot(vec4,vec4)GLSL: dot(vec3,vec3) 或dot(vec4,vec4)叉积：A × B=(vz-wy, wx-uz, uy-vx)glm: cross(vec3,vec3)GLSL: cross(vec3,vec3)](<weread://bestbookmark?bookId=31403518&chapterUid=30&rangeStart=2894&rangeEnd=3571>)
> ⏱ 2021-12-05 15:03:47 ^31403518-30-2894-3571
### 3.6 局部和世界空间
> 📌 [模型定义的空间叫作局部空间（local space）或模型空间（modelspace）。OpenGL文档使用的术语是物体空间（object space）。](<weread://bestbookmark?bookId=31403518&chapterUid=31&rangeStart=632&rangeEnd=803>)
> ⏱ 2021-12-05 15:09:37 ^31403518-31-632-803
> 📌 [通过设定物体在模拟世界中的朝向和大小，将物体放在模拟这个世界的空间中，这个空间叫作世界空间。将对象定位及定向在世界空间的矩阵称为模型矩阵或M。](<weread://bestbookmark?bookId=31403518&chapterUid=31&rangeStart=1257&rangeEnd=1419>)
> ⏱ 2021-12-05 15:13:33 ^31403518-31-1257-1419
### 3.7 视觉空间和合成相机
> 📌 [观察3D世界需要：（a）将相机放入世界的某个位置；（b）调整相机的角度，通常需要一套它自己的直角坐标轴U/V/N；（c）定义一个视体（view volume）；（d）将视体内的对象投影到投影平面（projectionplane）上。](<weread://bestbookmark?bookId=31403518&chapterUid=32&rangeStart=620&rangeEnd=821>)
> ⏱ 2021-12-05 15:15:11 ^31403518-32-620-821
### 3.8 投影矩阵
> 📌 [视场是可视空间的纵向角度。纵横比是远近剪裁平面的宽度比高度。通过这些元素所形成的形状叫作视锥（frustum）](<weread://bestbookmark?bookId=31403518&chapterUid=33&rangeStart=1784&rangeEnd=1901>)
> ⏱ 2021-12-05 15:19:03 ^31403518-33-1784-1901
> 📌 [透视矩阵用于将3D空间中的点变换至近剪裁平面上合适的位置，它的构建需要先计算q、A、B、C的值，之后用这些值来构建透视矩阵](<weread://bestbookmark?bookId=31403518&chapterUid=33&rangeStart=2190&rangeEnd=2279>)
> ⏱ 2021-12-05 15:20:35 ^31403518-33-2190-2279
> 📌 [生成透视变换矩阵很容易，只需要将所描述的公式插入一个4×4矩阵。GLM库也包含了一个用于构建透视矩阵的函数glm::perspective()。](<weread://bestbookmark?bookId=31403518&chapterUid=33&rangeStart=2667&rangeEnd=2739>)
> ⏱ 2021-12-05 15:21:06 ^31403518-33-2667-2739
> 📌 [正射投影是一种平行投影，其中所有的投影都与投影平面垂直。正射矩阵通过如下参数构建：（a）从相机到投影平面的距离Znear；（b）从相机到远剪裁平面的距离Zfar；（c）L、R、T、和B的值，其中L和R分别是投影平面左右边界的X坐标，T和B分别是投影平面上下边界的Y坐标](<weread://bestbookmark?bookId=31403518&chapterUid=33&rangeStart=3222&rangeEnd=3686>)
> ⏱ 2021-12-05 15:22:41 ^31403518-33-3222-3686

# 读书笔记

# 本书评论
