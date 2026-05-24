# Feature Specification: Cognitive Reading Graph (认知阅读图谱)

**Feature Branch**: `feature/cognitive-reading-graph`

**Created**: 2025-07-19

**Last Updated**: 2025-01-20

**Status**: In Progress

**Input**: 用户 PRD - 基于微信读书笔记的 AI 阅读分析与知识图谱系统

---

## 1. Product Vision

### 产品定位
**AI 原生认知操作系统** - 不是"读书笔记工具"，而是人类长期思想结构与认知演化的分析系统。

### 核心价值
将分散的阅读数据转化为：
- 概念网络
- 认知图谱
- AI 驱动的阅读洞察
- "第二大脑"

### 关键概念
- **核心对象**：用户的思想结构与认知演化
- **数据来源**：微信读书笔记（高亮、划线、阅读时间等）
- **目标**：Personal Cognitive OS

---

## 2. User Scenarios & Testing

### 用户角色定义

| 角色 | 特征 | 核心需求 |
|------|------|---------|
| 普通阅读者 | 日常阅读用户 | 管理笔记、快速搜索、AI总结 |
| 深度阅读者 | 长期阅读积累 | 认知分析、思想网络、作者关系 |
| 知识管理者 | 追求系统化 | 第二大脑、知识图谱、思维演化 |

---

### User Story 1 - Markdown 文件导入 (Priority: P1)

**用户旅程**：用户将微信读书导出的 md 文件导入系统，系统自动解析并提取所有数据。

**为什么这个优先级**：
- 这是整个系统的数据入口
- 没有数据导入就没有后续分析
- 是 MVP 的核心功能

**独立测试**：可以通过上传 md 文件并验证解析结果来完全测试

**验收场景**：

1. **Given** 用户有一个微信读书导出的 md 文件
   **When** 用户上传该文件
   **Then** 系统显示文件上传成功，并自动开始解析

2. **Given** md 文件包含高亮、章节、书名等信息
   **When** 解析完成
   **Then** 所有数据正确存储到数据库，包含书名、作者、高亮内容、章节、阅读时间

3. **Given** md 文件格式不符合预期
   **When** 用户上传
   **Then** 系统显示格式错误提示，并给出正确格式示例

4. **Given** 用户批量上传多个 md 文件
   **When** 上传完成
   **Then** 所有文件按书籍分组显示，每本书独立展示

---

### User Story 2 - AI 概念抽取 (Priority: P1)

**用户旅程**：用户导入书籍后，AI 自动分析每条高亮内容，提取核心概念、学科分类、情绪倾向。

**为什么这个优先级**：
- 概念抽取是构建知识图谱的核心能力
- 是区别于普通笔记工具的关键功能
- MVP 必须展示 AI 分析能力

**验收场景**：

1. **Given** 用户有一条领导力相关的高亮内容
   **When** AI 分析完成
   **Then** 返回概念列表、学科分类、情绪倾向

2. **Given** 用户有 100 条高亮内容等待分析
   **When** 用户触发批量分析
   **Then** 系统显示分析进度，所有内容分析完成后通知用户

3. **Given** 网络中断导致分析中断
   **When** 网络恢复
   **Then** 系统自动从中断处继续分析，不丢失已分析数据

---

### User Story 3 - 知识图谱可视化 (Priority: P1)

**用户旅程**：用户查看个人认知知识图谱，通过可视化界面探索概念之间的关系。

**为什么这个优先级**：
- 图谱可视化是产品的核心卖点
- 用户能直观看到自己的思想网络
- 是"第二大脑"概念的核心体现

**验收场景**：

1. **Given** 用户有 50+ 个概念节点
   **When** 用户打开图谱页面
   **Then** 图谱清晰展示节点和关系，支持缩放、拖拽、点击查看详情

2. **Given** 用户点击某个概念节点
   **When** 点击完成
   **Then** 右侧显示该概念的所有关联内容、高亮、书籍、阅读时间

3. **Given** 用户想筛选特定书籍的概念
   **When** 用户选择书籍过滤器
   **Then** 图谱只显示该书籍相关的概念和关系

---

### User Story 4 - AI 阅读画像 (Priority: P2)

**用户旅程**：用户查看 AI 自动生成的阅读人格与认知画像，包括阅读偏好、思维倾向、阅读盲区。

**验收场景**：

1. **Given** 用户有 10+ 本已导入的书籍
   **When** 用户请求生成阅读画像
   **Then** 系统分析后显示：阅读偏好列表、思维倾向分析、阅读盲区建议

2. **Given** 用户是新用户（少于 3 本书）
   **When** 用户请求生成画像
   **Then** 系统显示"数据不足"，并建议用户先导入更多书籍

---

### User Story 5 - 语义搜索与 RAG (Priority: P2)

**用户旅程**：用户使用自然语言搜索自己的所有阅读笔记，系统返回语义相关的结果。

**验收场景**：

1. **Given** 用户搜索"信任"
   **When** 搜索完成
   **Then** 返回所有包含"信任"相关概念的高亮内容，按相关性排序

2. **Given** 用户搜索"关于领导力的思考"
   **When** 语义搜索完成
   **Then** 返回包含领导力、影响力、指导等相关概念的内容

---

### User Story 6 - AI 阅读建议 (Priority: P3)

**验收场景**：

1. **Given** 用户的认知图谱显示近期关注领导力、愿景、信任
   **When** 用户请求阅读建议
   **Then** 系统推荐相关书籍，并说明理由

---

### User Story 7 - 认知成长轨迹 (Priority: P3)

**验收场景**：

1. **Given** 用户有 3 年以上的阅读数据
   **When** 用户查看成长轨迹
   **Then** 显示按年度组织的思想变化时间线

---

### Edge Cases

- **空数据**：用户首次使用，没有任何导入数据 → 显示引导教程
- **格式不支持**：用户上传非 md 格式文件 → 明确提示支持的格式
- **重复导入**：用户重复导入同一本书 → 询问是合并还是覆盖
- **API 限流**：AI 分析请求被限流 → 排队处理，显示预计等待时间
- **图数据库故障**：Neo4j 不可用 → 显示降级提示，数据仍可存储
- **向量检索失败**：Qdrant 不可用 → 降级为全文搜索
- **单本书过大**：一本书有 1000+ 高亮 → 分批处理，避免超时
- **用户隐私**：用户删除账号 → 所有个人数据完全清除

---

## 3. Requirements

### Functional Requirements

#### 3.1 Markdown 导入系统

- **FR-001**: 系统 MUST 支持导入微信读书导出的 md 文件
- **FR-002**: 系统 MUST 解析 md 文件并提取：书名、作者、分类、ISBN、阅读时间、阅读进度、阅读日期
- **FR-003**: 系统 MUST 解析 md 文件并提取高亮数据：章节、划线内容、阅读时间、原始链接
- **FR-004**: 系统 MUST 输出统一的 JSON 数据结构
- **FR-005**: 系统 MUST 支持批量上传多个 md 文件
- **FR-006**: 系统 MUST 验证 md 文件格式，不符合格式时给出明确错误提示

#### 3.2 阅读数据结构化

- **FR-007**: 系统 MUST 定义数据模型：Book, Highlight, Concept, Reader, Chapter
- **FR-008**: 系统 MUST 存储书籍的完整元数据
- **FR-009**: 系统 MUST 关联高亮内容与书籍、章节
- **FR-010**: 系统 MUST 维护概念库，支持概念的增删改查

#### 3.3 AI 概念抽取

- **FR-011**: 系统 MUST 使用 LLM 自动提取核心概念
- **FR-012**: 系统 MUST 对每个高亮内容进行学科分类
- **FR-013**: 系统 MUST 分析高亮内容的情绪倾向
- **FR-014**: 系统 MUST 提取用户关注点和作者观点
- **FR-015**: 系统 MUST 支持批量处理高亮内容
- **FR-016**: 系统 MUST 处理 API 限流和错误重试

#### 3.4 知识图谱系统

- **FR-017**: 系统 MUST 使用 Neo4j 构建个人认知知识图谱（可选）
- **FR-018**: 系统 MUST 定义节点类型：Book, Concept, Author, Highlight
- **FR-019**: 系统 MUST 定义关系类型
- **FR-020**: 系统 MUST 提供图谱可视化界面（可选）
- **FR-021**: 系统 MUST 支持点击节点查看详情
- **FR-022**: 系统 MUST 支持按书籍筛选图谱节点

#### 3.5 Embedding 向量检索

- **FR-023**: 系统 MUST 使用 Qdrant 实现向量检索（可选）
- **FR-024**: 系统 MUST 支持语义搜索
- **FR-025**: 系统 MUST 支持思想聚合
- **FR-026**: 系统 MUST 在向量检索失败时降级为全文搜索

#### 3.6 AI 阅读画像

- **FR-027**: 系统 MUST 生成阅读偏好分析
- **FR-028**: 系统 MUST 生成思维倾向分析
- **FR-029**: 系统 MUST 识别阅读盲区
- **FR-030**: 系统 MUST 在数据不足时提示用户

#### 3.7 AI 阅读建议系统

- **FR-031**: 系统 MUST 基于认知图谱推荐下一本书
- **FR-032**: 系统 MUST 推荐阅读路线和学习路径
- **FR-033**: 系统 MUST 推荐思维补全书籍
- **FR-034**: 系统 MUST 解释推荐理由

#### 3.8 认知成长轨迹

- **FR-035**: 系统 MUST 展示用户长期思想变化的时间线
- **FR-036**: 系统 MUST 按年度组织思想主题
- **FR-037**: 系统 MUST 标注"思想转型点"
- **FR-038**: 系统 MUST 支持点击时间节点查看详情

---

## 4. Technology Stack

| 模块 | 技术 | 说明 |
|------|------|------|
| 后端 | FastAPI + Python | Web 框架 |
| 数据库 | **MySQL** + SQLAlchemy | 关系型数据存储 |
| 图数据库 | Neo4j | 知识图谱存储（可选） |
| 向量库 | Qdrant | 语义搜索（可选） |
| **AI Provider** | **MiniMax** | **默认**，也支持 OpenAI、Zhipuai |
| 前端 | React | 可选，当前仅后端 |
| 图谱可视化 | Cytoscape.js | 可选 |

---

## 5. Assumptions

- **假设 1**：用户有微信读书账号并能导出 md 文件
- **假设 2**：用户使用 MiniMax API（**推荐**），也支持 OpenAI、Zhipuai
- **假设 3**：用户有一定技术背景（能部署和配置系统）
- **假设 4**：用户有 Neo4j 和 Qdrant 的使用经验或愿意学习（可选组件）
- **假设 5**：MVP 阶段为单用户，后续需要多用户支持
- **假设 6**：用户设备有稳定网络连接（依赖云端 API）
- **假设 7**：md 格式为微信读书标准导出格式

---

## 6. Technical Notes

### Database Configuration (MySQL)

**环境变量配置**：
```env
# MySQL 数据库
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/reading_graph

# MiniMax AI (推荐)
MINIMAX_API_KEY=your-api-key
MINIMAX_MODEL=MiniMax-Text-01
AI_PROVIDER=minimax

# 可选：OpenAI 备选
OPENAI_API_KEY=your-openai-key
```

**依赖安装**：
```bash
pip install sqlalchemy pymysql cryptography
```

### Data Model (MySQL)

#### books 表
```sql
CREATE TABLE books (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    isbn VARCHAR(20),
    reading_time VARCHAR(50),
    progress DECIMAL(5,2),
    reading_date DATE,
    created_at DATETIME,
    updated_at DATETIME,
    INDEX idx_title (title)
);
```

#### highlights 表
```sql
CREATE TABLE highlights (
    id VARCHAR(36) PRIMARY KEY,
    book_id VARCHAR(36) NOT NULL,
    content TEXT NOT NULL,
    chapter VARCHAR(255),
    create_time DATETIME,
    url TEXT,
    concepts JSON,
    emotion VARCHAR(50),
    domain VARCHAR(100),
    created_at DATETIME,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    INDEX idx_book_id (book_id)
);
```

#### concepts 表
```sql
CREATE TABLE concepts (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(100),
    frequency INT DEFAULT 0,
    last_mentioned VARCHAR(100),
    description VARCHAR(500),
    created_at DATETIME,
    INDEX idx_name (name)
);
```

### AI Provider Configuration

**支持的 AI 提供商**：

| Provider | API Key 环境变量 | 默认模型 | Base URL |
|----------|-----------------|---------|----------|
| **MiniMax** (推荐) | `MINIMAX_API_KEY` | MiniMax-Text-01 | https://api.minimax.chat/v1 |
| OpenAI | `OPENAI_API_KEY` | gpt-4 | https://api.openai.com/v1 |
| Zhipuai | `ZHIPUAI_API_KEY` | glm-4 | https://open.bigmodel.cn/api/paas/v4 |

**切换 Provider**：
```python
from src.services.llm_provider import LLMProvider

# 使用 MiniMax（默认）
llm = LLMProvider(provider="minimax")

# 使用 OpenAI
llm = LLMProvider(provider="openai")

# 使用 Zhipuai
llm = LLMProvider(provider="zhipuai")
```

### API Endpoints (MVP)

| 方法 | 端点 | 描述 |
|------|------|------|
| POST | /api/v1/import | 上传 md 文件 |
| POST | /api/v1/import/batch | 批量上传 md 文件 |
| GET | /api/v1/books | 获取书籍列表 |
| GET | /api/v1/books/{id} | 获取书籍详情 |
| POST | /api/v1/books | 创建书籍 |
| DELETE | /api/v1/books/{id} | 删除书籍 |
| POST | /api/v1/analyze | 触发 AI 分析 |
| GET | /api/v1/analyze/status/{job_id} | 获取分析状态 |
| GET | /api/v1/graph | 获取图谱数据 |
| GET | /api/v1/graph/stats | 获取图谱统计 |
| GET | /api/v1/profile | 获取阅读画像 |
| GET | /api/v1/profile/preferences | 获取阅读偏好 |
| GET | /api/v1/profile/blind-spots | 获取阅读盲区 |
| GET | /api/v1/search | 语义搜索 |
| GET | /api/v1/search/aggregate | 思想聚合 |
| GET | /api/v1/timeline | 获取成长轨迹 |
| GET | /api/v1/timeline/pivot-points | 获取认知转型点 |

---

## 7. MVP Scope (Phase 1)

### Must Have (MVP)

✅ 1. md 导入
✅ 2. 数据解析
✅ 3. AI 概念抽取
✅ 4. Neo4j 图谱
✅ 5. AI 阅读画像

### Out of Scope (Phase 1)

❌ 多用户系统
❌ 社交功能
❌ Agent
❌ 自动写作
❌ 多模态支持

---

## 8. Success Criteria

- **SC-001**: 用户能在 30 秒内完成单个 md 文件的上传和解析
- **SC-002**: AI 概念抽取准确率达到 85%+
- **SC-003**: 图谱可视化加载时间 < 3 秒（100 个节点）
- **SC-004**: 向量搜索响应时间 < 1 秒
- **SC-005**: AI 阅读画像生成时间 < 10 秒
- **SC-006**: 系统支持 100 万+ 图谱节点

---

## 9. Future Extensions

1. **AI 读书教练**：每日建议
2. **作者思想网络**：展示思想传承关系
3. **AI 自动生成读书报告**
4. **多用户认知社交**：发现思想最接近的人
5. **实时同步**：与微信读书 API 同步
6. **移动端**：iOS/Android 应用
7. **浏览器插件**：快速添加网页摘录到图谱