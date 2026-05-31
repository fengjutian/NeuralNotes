# NeuralNotes 知识星图 - 产品文档

> **AI-powered personal knowledge graph based on WeChat Reading notes**
>
> 让阅读痕迹可视化，用 AI 构建属于你自己的知识网络。

---

## 目录

1. [产品概述](#1-产品概述)
2. [核心功能](#2-核心功能)
3. [系统架构](#3-系统架构)
4. [技术栈](#4-技术栈)
5. [项目结构](#5-项目结构)
6. [数据模型](#6-数据模型)
7. [API 接口文档](#7-api-接口文档)
8. [前端页面说明](#8-前端页面说明)
9. [AI 分析引擎](#9-ai-分析引擎)
10. [部署指南](#10-部署指南)
11. [开发指南](#11-开发指南)
12. [配置说明](#12-配置说明)

---

## 1. 产品概述

### 1.1 产品简介

NeuralNotes（知识星图）是一款基于微信读书笔记的 AI 知识图谱工具。它允许用户一键导入微信读书导出的 Markdown 笔记，通过 AI 自动提取知识点、概念和主题，构建可视化知识网络，并提供语义搜索、阅读画像和阅读时间线等功能。

### 1.2 产品定位

- **目标用户**：有大量微信读书笔记、希望深度管理和发现知识关联的阅读者
- **核心价值**：将零散的阅读笔记转化为结构化的知识网络，发现跨书籍的知识关联
- **差异化**：结合 AI 语义理解与图数据库，从笔记中自动提取概念并建立关系

### 1.3 关键特性

| 特性 | 描述 |
|------|------|
| 📖 **笔记导入** | 拖拽式上传微信读书 Markdown 笔记，自动解析元数据和高亮内容 |
| 🧠 **AI 分析** | 支持 OpenAI / MiniMax / 智谱三种 LLM，批量提取概念和知识领域 |
| 🔍 **语义搜索** | 基于 Qdrant 向量数据库的自然语言搜索，跨书籍检索笔记 |
| 📊 **知识图谱** | 基于 Neo4j 图数据库的交互式可视化，展示书籍-概念-作者关系网络 |
| 📈 **阅读画像** | 可视化阅读兴趣分布、阅读趋势和知识结构 |
| ⏱️ **阅读时间线** | 按时间轴追踪阅读历程，发现阅读规律 |

---

## 2. 核心功能

### 2.1 笔记导入

支持两种微信读书导出的 Markdown 格式：

- **Format A（简化格式）**：`# 书名`、`## 章节`、`- 高亮内容`、`> 创建于 2024-01-01`
- **Format B（完整格式）**：YAML 前置元数据 + Obsidian 风格的 callout 高亮标注

解析内容包括：
- 书名、作者、分类、ISBN
- 阅读时长、阅读日期、阅读进度
- 章节结构
- 每条高亮的正文、创建时间、原文链接

### 2.2 AI 分析引擎

AI 分析引擎对每条笔记高亮进行语义分析，提取：

- **概念（Concepts）**：从笔记内容中自动识别关键概念/术语
- **领域（Domain）**：判断知识点所属学科领域（如计算机科学、心理学、经济学等）
- **情感（Emotion）**：分析笔记的情感倾向

分析过程支持：
- **批量处理**：分批提交高亮到 LLM，避免请求过载
- **异步任务**：通过 Job 机制管理分析任务，前端可轮询进度
- **重试机制**：指数退避重试，最多 3 次
- **可切换模型**：支持 OpenAI、MiniMax、智谱三种 LLM Provider

### 2.3 知识图谱

基于 Neo4j 图数据库构建四种节点类型和五种关系类型：

**节点类型**：
| 节点 | 属性 |
|------|------|
| Book | id, title, author, category, isbn |
| Concept | id, name, domain, frequency |
| Author | name, bio |
| Highlight | id, content, chapter |

**关系类型**：
| 关系 | 方向 | 含义 |
|------|------|------|
| HAS_CONCEPT | Book → Concept | 书籍包含某概念 |
| WRITTEN_BY | Book → Author | 书籍由作者撰写 |
| RELATED_TO | Highlight → Concept | 高亮与概念相关 |
| FROM_BOOK | Highlight → Book | 高亮来自某书籍 |
| LIKES | Reader → Book | 读者喜欢某书籍 |

### 2.4 语义搜索

基于 Qdrant 向量数据库实现：

- 将笔记高亮通过 Embedding 模型向量化存储
- 支持自然语言查询，返回语义相似度最高的笔记
- 可筛选书籍范围、概念类别

### 2.5 阅读画像

统计和分析用户的阅读行为：

- 阅读兴趣分布（按分类统计）
- 阅读趋势（按时间统计阅读量）
- 知识结构（按领域分布概念）
- 阅读习惯（阅读时段、平均进度等）

### 2.6 阅读时间线

按时间轴展示阅读历程：

- 按日期排列书籍阅读记录
- 显示每本书的阅读时间/日期
- 支持按月份/年份筛选

---

## 3. 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                     Frontend (React 18)                  │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐     │
│  │ Books │ │Import │ │Search │ │Profile│ │ Graph │     │
│  └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘     │
│      └─────────┴─────────┴─────────┴─────────┘          │
│                         │ HTTP/REST                      │
│                    Axios + React Query                   │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────┐
│                   Backend (FastAPI)                      │
│  ┌──────────────────────────────────────────────────┐   │
│  │                  API Router (/api/v1)             │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐   │   │
│  │  │ Books  │ │ Import │ │Analyze │ │ Graph  │   │   │
│  │  └────────┘ └────────┘ └────────┘ └────────┘   │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐   │   │
│  │  │Profile │ │ Search │ │Timeline│ │  Sync  │   │   │
│  │  └────────┘ └────────┘ └────────┘ └────────┘   │   │
│  └──────────────────────────────────────────────────┘   │
│                         │                                │
│  ┌──────────────────────────────────────────────────┐   │
│  │                  Service Layer                    │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────┐     │   │
│  │  │  Book    │ │  Graph   │ │  AI Analyzer │     │   │
│  │  │ Service  │ │ Service  │ │              │     │   │
│  │  └──────────┘ └──────────┘ └──────────────┘     │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────┐     │   │
│  │  │  Vector  │ │  Profile │ │  Highlight   │     │   │
│  │  │ Service  │ │ Service  │ │   Service    │     │   │
│  │  └──────────┘ └──────────┘ └──────────────┘     │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────┐     │   │
│  │  │ Markdown │ │  Concept │ │  Embedding   │     │   │
│  │  │  Parser  │ │Extractor │ │   Service    │     │   │
│  │  └──────────┘ └──────────┘ └──────────────┘     │   │
│  └──────────────────────────────────────────────────┘   │
└───────────┬──────────────────┬──────────────────┬───────┘
            │                  │                  │
    ┌───────┴───────┐  ┌───────┴───────┐  ┌───────┴───────┐
    │  PostgreSQL   │  │    Neo4j      │  │    Qdrant     │
    │  (主数据库)   │  │  (图数据库)   │  │  (向量数据库)  │
    └───────────────┘  └───────────────┘  └───────────────┘
            │                  │                  │
    ┌───────┴──────────────────┴──────────────────┴───────┐
    │              External AI Services                   │
    │  ┌──────────┐  ┌──────────┐  ┌──────────────┐     │
    │  │  OpenAI  │  │ MiniMax  │  │   智谱AI     │     │
    │  └──────────┘  └──────────┘  └──────────────┘     │
    └────────────────────────────────────────────────────┘
```

### 3.1 架构说明

- **前端**：React 18 SPA 应用，使用 Ant Design 组件库，React Query 管理服务端状态，Zustand 管理客户端状态
- **后端**：FastAPI 框架，分层架构（API 路由 → 服务层 → 数据访问层），支持异步处理
- **数据存储**：
  - PostgreSQL：存储书籍、高亮、读者等结构化数据（SQLAlchemy ORM）
  - Neo4j：存储知识图谱节点和关系（Cypher 查询）
  - Qdrant：存储笔记向量用于语义搜索
- **外部服务**：LLM API（OpenAI/MiniMax/智谱）用于 AI 分析

---

## 4. 技术栈

### 4.1 后端

| 类别 | 技术 | 版本 |
|------|------|------|
| 框架 | FastAPI | - |
| 语言 | Python | 3.11+ |
| ORM | SQLAlchemy | - |
| 数据校验 | Pydantic | v2 |
| 数据库驱动 | asyncpg, psycopg2 | - |
| Neo4j 驱动 | neo4j (官方) | - |
| Qdrant 客户端 | qdrant-client | - |
| YAML 解析 | PyYAML | - |
| 日志 | Python logging | - |
| 测试 | pytest | - |
| 代码检查 | flake8, mypy, ruff | - |
| 类型检查 | mypy | - |

### 4.2 前端

| 类别 | 技术 | 版本 |
|------|------|------|
| 框架 | React | 18.3+ |
| 语言 | TypeScript | 5.6+ |
| 构建工具 | Vite | 6.0 |
| UI 框架 | Ant Design | 5.22 |
| 路由 | React Router DOM | 6.28 |
| HTTP 客户端 | Axios | 1.7 |
| 服务端状态 | TanStack React Query | 5.60 |
| 客户端状态 | Zustand | 5.0 |
| 日期处理 | dayjs | 1.11 |

### 4.3 基础设施

| 类别 | 技术 | 版本 |
|------|------|------|
| 关系数据库 | PostgreSQL | 15+ |
| 图数据库 | Neo4j | 5+ |
| 向量数据库 | Qdrant | 1.12+ |
| AI 服务 | OpenAI / MiniMax / 智谱 | - |

---

## 5. 项目结构

```
NeuralNotes/
├── README.md                        # 项目说明
├── docs/                            # 文档
│   └── PRODUCT_DOCUMENTATION.md     # 产品文档（本文件）
│
├── backend/                         # FastAPI 后端
│   ├── run_server.py                # 服务启动脚本
│   ├── setup.cfg                    # 项目配置 (flake8, mypy)
│   ├── mypy.ini                     # Mypy 配置
│   ├── .pre-commit-config.yaml      # Pre-commit 钩子
│   ├── env_example.txt              # 环境变量示例
│   ├── PROGRESS.md                  # 开发进度
│   ├── STATUS.md                    # 项目状态
│   ├── docs/                        # 后端文档
│   │   └── QUICKSTART.md            # 快速开始指南
│   ├── scripts/                     # 脚本工具
│   │   ├── import_books_notes.py    # 批量导入脚本
│   │   └── uploads/                 # 上传文件临时目录
│   ├── books_notes/                 # 示例笔记文件（170+ 本）
│   ├── uploads/                     # 文件上传目录
│   ├── tests/                       # 测试目录
│   │   ├── conftest.py              # Pytest 配置
│   │   ├── unit/                    # 单元测试
│   │   │   ├── test_ai_analyzer.py
│   │   │   └── test_markdown_parser.py
│   │   └── integration/             # 集成测试
│   │       ├── test_books_api.py
│   │       └── test_import_api.py
│   └── src/                         # 主源码
│       ├── main.py                  # FastAPI 入口
│       ├── config.py                # 配置管理
│       ├── database.py              # SQLAlchemy 数据库设置
│       ├── neo4j_client.py          # Neo4j 客户端
│       ├── qdrant_wrapper.py        # Qdrant 客户端封装
│       ├── api/                     # API 路由层
│       │   ├── __init__.py          # 路由聚合
│       │   ├── books.py             # 书籍 CRUD
│       │   ├── import_routes.py     # 笔记导入
│       │   ├── analyze.py           # AI 分析
│       │   ├── graph.py             # 知识图谱
│       │   ├── search.py            # 语义搜索
│       │   ├── profile.py           # 阅读画像
│       │   ├── timeline.py          # 阅读时间线
│       │   ├── sync.py              # 数据同步
│       │   └── mysql_graph.py       # MySQL 图操作
│       ├── models/                  # SQLAlchemy 模型
│       │   ├── book.py              # Book 模型
│       │   ├── chapter.py           # Chapter 模型
│       │   ├── concept.py           # Concept 模型
│       │   ├── highlight.py         # Highlight 模型
│       │   └── reader.py            # Reader 模型
│       ├── schemas/                 # Pydantic 数据校验
│       │   ├── book.py              # Book schemas
│       │   ├── graph.py             # Graph schemas
│       │   └── highlight.py         # Highlight schemas
│       ├── services/                # 业务逻辑层
│       │   ├── markdown_parser.py   # Markdown 解析器
│       │   ├── book_service.py      # 书籍服务
│       │   ├── ai_analyzer.py       # AI 分析引擎
│       │   ├── concept_extractor.py  # 概念提取器
│       │   ├── llm_provider.py      # LLM 提供商
│       │   ├── embedding_service.py # 向量嵌入服务
│       │   ├── vector_service.py    # 向量搜索服务
│       │   ├── graph_service.py     # 图谱服务
│       │   ├── highlight_service.py # 高亮服务
│       │   ├── profile_service.py   # 画像服务
│       │   └── file_service.py      # 文件服务
│       └── utils/                   # 工具函数
│           ├── exceptions.py        # 自定义异常
│           └── logging.py           # 日志配置
│
├── frontend/                        # React 前端
│   ├── package.json                 # 依赖配置
│   ├── tsconfig.json                # TypeScript 配置
│   ├── tsconfig.node.json           # Node TypeScript 配置
│   ├── vite.config.ts               # Vite 配置
│   ├── index.html                   # HTML 入口
│   └── src/
│       ├── main.tsx                 # 应用入口
│       ├── App.tsx                  # 根组件 + 路由
│       ├── index.css                # 全局样式
│       ├── api/
│       │   └── index.ts             # API 客户端封装
│       ├── components/
│       │   └── AppLayout.tsx        # 应用布局组件
│       ├── pages/
│       │   ├── BooksPage.tsx        # 书架页
│       │   ├── BookDetailPage.tsx   # 书籍详情页
│       │   ├── ImportPage.tsx       # 导入页
│       │   ├── SearchPage.tsx       # 搜索页
│       │   ├── ProfilePage.tsx      # 阅读画像页
│       │   └── GraphPage.tsx        # 知识图谱页
│       ├── hooks/                   # 自定义 Hooks
│       └── store/                   # Zustand 状态管理
│
├── analysis/                        # 数据分析脚本
└── .venv/                           # Python 虚拟环境
```

---

## 6. 数据模型

### 6.1 Book（书籍）

```python
Book {
    id: UUID                  # 主键
    title: str                # 书名
    author: str               # 作者
    category: str?            # 分类
    isbn: str?                # ISBN
    reading_time: str?        # 阅读时长
    reading_date: str?        # 阅读日期
    progress: float?          # 阅读进度 (0-100%)
    created_at: datetime      # 创建时间
    updated_at: datetime      # 更新时间
}
```

### 6.2 Highlight（高亮/笔记）

```python
Highlight {
    id: UUID                  # 主键
    book_id: UUID             # 所属书籍 ID
    content: str              # 高亮内容
    chapter: str?             # 所属章节
    create_time: datetime?    # 笔记创建时间
    url: str?                 # 原文链接
    embedding: vector?        # 向量嵌入 (Qdrant)
    created_at: datetime      # 记录创建时间
}
```

### 6.3 Concept（概念）

```python
Concept {
    id: UUID                  # 主键
    name: str                 # 概念名称
    domain: str?              # 所属领域
    frequency: int            # 出现频次
    created_at: datetime      # 创建时间
}
```

### 6.4 Chapter（章节）

```python
Chapter {
    id: UUID                  # 主键
    book_id: UUID             # 所属书籍 ID
    name: str                 # 章节名
    order: int?               # 排序
    created_at: datetime      # 创建时间
}
```

### 6.5 Reader（读者）

```python
Reader {
    id: UUID                  # 主键
    name: str                 # 读者名
    bio: str?                 # 简介
    created_at: datetime      # 创建时间
}
```

### 6.6 ER 关系图

```
┌──────────┐    1:N    ┌───────────┐
│   Book   │──────────>│  Chapter  │
│          │           └───────────┘
│          │    1:N    ┌───────────┐
│          │──────────>│ Highlight │──> Qdrant Vector
│          │           └───────────┘
│          │    M:N    ┌───────────┐
│          │<────────>│  Concept  │
└──────────┘           └───────────┘
      │
      │ N:1
      ▼
┌──────────┐
│  Author  │
└──────────┘

┌──────────┐    M:N    ┌───────────┐
│  Reader  │<────────>│   Book    │
└──────────┘  (LIKES)  └───────────┘
```

---

## 7. API 接口文档

Base URL: `http://localhost:8000/api/v1`

### 7.1 健康检查

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/health` | 服务健康检查 |
| GET | `/` | 根路径，返回 API 信息 |

### 7.2 导入

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/import` | 上传 Markdown 笔记文件 |

**请求**：`multipart/form-data`
- `file`: .md 文件

**响应示例**：
```json
{
  "book_id": "uuid",
  "title": "书名",
  "author": "作者",
  "highlight_count": 42,
  "message": "导入成功"
}
```

### 7.3 书籍

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/books` | 获取书籍列表（支持分页 & 分类筛选） |
| GET | `/api/v1/books/{id}` | 获取书籍详情（含高亮列表） |
| PUT | `/api/v1/books/{id}` | 更新书籍信息 |
| DELETE | `/api/v1/books/{id}` | 删除书籍 |

**查询参数**：
- `skip`: 偏移量 (默认 0)
- `limit`: 数量 (默认 20)
- `category`: 分类筛选

### 7.4 AI 分析

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/analyze` | 触发 AI 分析任务 |
| GET | `/api/v1/analyze/{job_id}` | 查询分析任务状态与结果 |

**请求体**：
```json
{
  "book_id": "uuid",
  "highlight_ids": ["uuid1", "uuid2", ...]
}
```

**响应**（创建任务）：
```json
{
  "job_id": "uuid",
  "status": "pending",
  "total": 42
}
```

**响应**（查询状态）：
```json
{
  "job_id": "uuid",
  "status": "processing",
  "total": 42,
  "completed": 20,
  "errors": 0,
  "progress_percent": 47.6
}
```

### 7.5 知识图谱

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/graph` | 获取全局知识图谱 |
| GET | `/api/v1/graph/book/{book_id}` | 获取某书籍的子图谱 |
| GET | `/api/v1/graph/concept/{name}` | 获取概念详情 |

**查询参数**：
- `limit`: 节点数量限制 (默认 100)

**响应**：
```json
{
  "nodes": [
    {
      "id": "uuid",
      "type": "book",
      "label": "书名",
      "properties": {...}
    }
  ],
  "edges": [
    {
      "source": "uuid",
      "target": "uuid",
      "type": "has_concept",
      "properties": {"weight": 1.0}
    }
  ]
}
```

### 7.6 语义搜索

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/search` | 语义搜索笔记 |

**查询参数**：
- `q`: 搜索查询文本
- `book_id`: (可选) 限定书籍范围
- `limit`: 返回数量 (默认 10)

### 7.7 阅读画像

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/profile` | 获取阅读画像数据 |

**响应**：
```json
{
  "total_books": 42,
  "total_highlights": 1024,
  "categories": [
    {"name": "计算机科学", "count": 15},
    {"name": "经济学", "count": 8}
  ],
  "top_concepts": [
    {"name": "机器学习", "frequency": 23},
    {"name": "设计模式", "frequency": 18}
  ]
}
```

### 7.8 阅读时间线

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/timeline` | 获取阅读时间线 |

**查询参数**：
- `year`: (可选) 年份筛选
- `month`: (可选) 月份筛选

### 7.9 数据同步

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/sync` | 同步数据到 Neo4j / Qdrant |

### 7.10 MySQL 图操作

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/v1/mysql-graph` | 获取 MySQL 存储的图数据 |

---

## 8. 前端页面说明

### 8.1 页面路由

| 路径 | 页面 | 说明 |
|------|------|------|
| `/` | 重定向 | 自动跳转到 `/books` |
| `/books` | 书架页 | 展示所有已导入书籍 |
| `/books/:id` | 书籍详情 | 展示书籍元数据和高亮列表 |
| `/import` | 导入页 | 拖拽上传 Markdown 笔记文件 |
| `/search` | 搜索页 | 语义搜索笔记内容 |
| `/profile` | 阅读画像 | 阅读统计和知识结构可视化 |
| `/graph` | 知识图谱 | 交互式知识网络可视化 |

### 8.2 布局组件 (AppLayout)

- **侧边栏导航**：固定左侧，可折叠，包含 5 个导航项
  - 书架 (BookOutlined)
  - 导入 (UploadOutlined)
  - 搜索 (SearchOutlined)
  - 画像 (UserOutlined)
  - 图谱 (ApartmentOutlined)
- **顶部标题**：展开时显示 "Neural Notes"，折叠时显示 "NN"
- **内容区域**：根据侧边栏状态自适应宽度

### 8.3 导入流程

1. 用户访问导入页面，看到拖拽上传区域
2. 拖拽或点击选择 .md 文件
3. 前端调用 `POST /api/v1/import` 上传
4. 上传成功后显示结果卡片：
   - 书名、作者、笔记数量
   - "查看书籍"按钮跳转到详情页
   - "继续导入"按钮清空结果

### 8.4 状态管理

- **服务端状态**：使用 TanStack React Query 管理（自动缓存、重新获取、错误重试）
- **客户端状态**：使用 Zustand 管理（如 UI 状态、用户偏好等）

---

## 9. AI 分析引擎

### 9.1 工作流程

```
用户触发分析
     │
     ▼
创建 AnalysisJob (status: pending)
     │
     ▼
启动异步处理 (status: processing)
     │
     ▼
将高亮列表分批 (batch_size=10)
     │
     ▼
逐批调用 LLM 提取概念 ──── 失败时重试 (max_retries=3)
     │
     ▼
更新 Job 进度 (completed, errors)
     │
     ▼
所有批次完成 (status: completed/failed)
```

### 9.2 概念提取器 (ConceptExtractor)

- 接收单个高亮的文本内容
- 通过 LLM Prompt 提取关键概念
- 返回 `ExtractedConcepts` 结构：
  - `concepts`: 概念列表
  - `domain`: 所属领域
  - `emotion`: 情感倾向 (positive/neutral/negative)

### 9.3 LLM Provider 配置

支持切换三种 LLM 提供商：

| Provider | 环境变量 | 说明 |
|----------|----------|------|
| OpenAI | `OPENAI_API_KEY` | GPT 系列模型 |
| MiniMax | `MINIMAX_API_KEY`, `MINIMAX_MODEL` | MiniMax-Text-01 等 |
| 智谱AI | `ZHIPUAI_API_KEY` | GLM 系列模型 |

通过 `AI_PROVIDER` 环境变量切换。

### 9.4 容错机制

- **指数退避重试**：失败后等待 2^retry 秒后重试，最多 3 次
- **优雅降级**：单条高亮分析失败不影响整体任务
- **任务可取消**：支持手动取消正在进行的分析任务
- **过期清理**：支持自动清理 24 小时前的已完成任务

---

## 10. 部署指南

### 10.1 环境要求

| 组件 | 版本要求 | 是否必须 |
|------|----------|----------|
| Python | 3.11+ | ✅ 必须 |
| Node.js | 18+ | ✅ 必须 |
| PostgreSQL | 15+ | ⚠️ 可选（无配置时使用 SQLite） |
| Neo4j | 5+ | ⚠️ 可选（无配置时跳过图谱功能） |
| Qdrant | 1.12+ | ⚠️ 可选（无配置时跳过向量搜索） |
| AI API Key | - | ⚠️ 可选（需 AI 分析功能时必填） |

### 10.2 后端部署

```bash
# 1. 进入后端目录
cd backend

# 2. 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .\.venv\Scripts\Activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp env_example.txt .env
# 编辑 .env 文件，填入必要配置

# 5. 启动服务
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### 10.3 前端部署

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖
npm install

# 3. 开发模式
npm run dev

# 4. 生产构建
npm run build

# 5. 预览生产构建
npm run preview
```

### 10.4 Docker 部署（数据库服务）

```bash
# PostgreSQL
docker run -d --name nn-postgres \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=neuralnotes \
  -p 5432:5432 postgres:15

# Neo4j
docker run -d --name nn-neo4j \
  -e NEO4J_AUTH=neo4j/password \
  -p 7474:7474 -p 7687:7687 neo4j:5

# Qdrant
docker run -d --name nn-qdrant \
  -p 6333:6333 qdrant/qdrant
```

### 10.5 生产环境建议

- 使用 Gunicorn + Uvicorn workers 部署后端
- 使用 Nginx 反向代理前后端
- 数据库配置持久化存储卷
- 配置 HTTPS 证书
- 限制 CORS 允许的域名

---

## 11. 开发指南

### 11.1 本地开发

```bash
# 后端开发
cd backend
pip install -e ".[dev]"
uvicorn src.main:app --reload

# 前端开发
cd frontend
npm run dev
```

### 11.2 代码质量

```bash
cd backend

# 代码风格检查
flake8 src/

# 类型检查
mypy src/

# 代码格式化
ruff format src/

# 运行所有检查
pre-commit run --all-files
```

### 11.3 运行测试

```bash
cd backend
pytest                    # 运行所有测试
pytest -v                 # 详细输出
pytest tests/unit/        # 仅单元测试
pytest tests/integration/ # 仅集成测试
```

### 11.4 API 文档

启动后端服务后访问：
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## 12. 配置说明

### 12.1 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `APP_NAME` | 应用名称 | Cognitive Reading Graph |
| `APP_VERSION` | 应用版本 | 0.1.0 |
| `DEBUG` | 调试模式 | false |
| `DATABASE_URL` | PostgreSQL 连接串 | SQLite 文件数据库 |
| `NEO4J_URI` | Neo4j Bolt 地址 | bolt://localhost:7687 |
| `NEO4J_USER` | Neo4j 用户名 | neo4j |
| `NEO4J_PASSWORD` | Neo4j 密码 | - |
| `QDRANT_URL` | Qdrant 服务地址 | http://localhost:6333 |
| `AI_PROVIDER` | AI 提供商 (openai/minimax/zhipuai) | openai |
| `OPENAI_API_KEY` | OpenAI API Key | - |
| `MINIMAX_API_KEY` | MiniMax API Key | - |
| `MINIMAX_MODEL` | MiniMax 模型名 | MiniMax-Text-01 |
| `ZHIPUAI_API_KEY` | 智谱 AI API Key | - |

### 12.2 简化启动

如果只测试核心导入功能，只需：
1. 配置 AI Provider 的 API Key
2. 不安装 PostgreSQL / Neo4j / Qdrant
3. 系统会自动使用 SQLite，并跳过图数据库和向量数据库功能

---

## 附录

### A. 支持的微信读书导出格式

**Format A 示例**：
```markdown
# JavaScript高级程序设计（第4版）
作者: 马特·弗里斯比

## 第1章 什么是JavaScript
- JavaScript的组成：ECMAScript、DOM、BOM
- ECMAScript是JavaScript的核心
> 创建于 2023-06-15
```

**Format B 示例**：
```markdown
---
doc_type: weread-highlights-reviews
bookId: "3300044333"
title: Spring实战（第6版）
author: 克雷格·沃斯
isbn: 9787115598691
readingTime: 3小时28分钟
progress: 99%
readingDate: 2023-04-18
---

# 高亮划线
#### 8.1 OAuth 2简介
> 📌 OAuth 2是一个开放的授权标准
> ⏱ 2023-11-06 11:02:52
```

### B. 知识图谱节点类型枚举

```python
class NodeType(str, Enum):
    BOOK = "book"
    CONCEPT = "concept"
    AUTHOR = "author"
    HIGHLIGHT = "highlight"
    READER = "reader"
```

### C. 知识图谱关系类型枚举

```python
class EdgeType(str, Enum):
    HAS_CONCEPT = "has_concept"   # Book → Concept
    LIKES = "likes"               # Reader → Book
    WRITTEN_BY = "written_by"     # Book → Author
    RELATED_TO = "related_to"     # Highlight → Concept
    FROM_BOOK = "from_book"       # Highlight → Book
```

### D. AI 分析任务状态

```python
class JobStatus(str, Enum):
    PENDING = "pending"         # 等待处理
    PROCESSING = "processing"   # 处理中
    COMPLETED = "completed"     # 已完成
    FAILED = "failed"           # 失败
    CANCELLED = "cancelled"     # 已取消
```

---

> 📝 文档版本: 1.0  
> 📅 最后更新: 2025  
> ✍️ 项目: NeuralNotes 知识星图