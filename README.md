"# NeuralNotes 知识星图

> 基于微信读书笔记的 AI 知识图谱，让阅读痕迹可视化

## 功能特性

- **📖 笔记导入** - 一键导入微信读书 Markdown 笔记
- **🧠 AI 分析** - 自动提取知识点，构建知识网络
- **🔍 语义搜索** - 用自然语言搜索你的笔记库
- **📊 阅读画像** - 可视化你的阅读兴趣和知识结构
- **⏱️ 阅读时间线** - 追踪阅读历程，发现阅读规律

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | FastAPI + Python 3.11+ |
| 数据库 | PostgreSQL + Neo4j + Qdrant |
| AI | OpenAI / MiniMax / 智谱 (可切换) |
| 前端 | React 18 + TypeScript + Vite |

## 项目结构

```
NeuralNotes/
├── backend/                 # FastAPI 后端
│   ├── src/
│   │   ├── api/            # API 路由
│   │   ├── models/         # 数据库模型
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # 业务逻辑
│   │   └── utils/         # 工具函数
│   ├── tests/             # 测试
│   └── uploads/           # 文件上传目录
│
├── frontend/               # React 前端
│   ├── src/
│   │   ├── api/           # API 调用
│   │   ├── components/    # 组件
│   │   ├── pages/         # 页面
│   │   ├── store/         # 状态管理
│   │   └── hooks/        # 自定义 Hooks
│   └── package.json
│
├── analysis/              # 数据分析脚本
└── docs/                  # 文档
```

## 快速开始

### 1. 环境要求

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+ (可选)
- Neo4j 5+ (可选)
- Qdrant 1.12+ (可选)

> 💡 **简化启动**: 如果只测试核心导入功能，可以不安装 PostgreSQL/Neo4j/Qdrant，配置好 AI Provider 后直接启动。

### 2. 后端安装

```powershell
# 进入 backend 目录
cd backend

# 激活虚拟环境
.\venv\Scripts\Activate

# 或在 Linux/Mac 上
source venv/bin/activate

# 复制并编辑环境配置
copy .env.example .env
# 用编辑器打开 .env，配置数据库和 AI API Key
```

编辑 `.env` 文件，填入必要的配置：

```env
# AI Provider (必填)
AI_PROVIDER=minimax  # 或 openai / zhipuai
MINIMAX_API_KEY=your-api-key
MINIMAX_MODEL=MiniMax-Text-01

# 数据库 (可选，未配置时使用 SQLite)
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname

# 图数据库 (可选)
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password

# 向量数据库 (可选)
QDRANT_URL=http://localhost:6333
```

### 3. 启动后端

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问 **http://localhost:8000/docs** 查看 API 文档。

### 4. 启动前端

```powershell
cd frontend
npm install
npm run dev
```

访问 **http://localhost:5173** 使用前端界面。

## API 文档

服务启动后访问 Swagger 文档：

- 后端 API: http://localhost:8000/docs
- 健康检查: http://localhost:8000/health

### 主要接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/v1/import` | 导入 Markdown 笔记 |
| GET | `/api/v1/books` | 获取书籍列表 |
| POST | `/api/v1/analyze` | AI 分析书籍 |
| GET | `/api/v1/graph` | 获取知识图谱 |
| GET | `/api/v1/search` | 语义搜索笔记 |
| GET | `/api/v1/profile` | 获取阅读画像 |
| GET | `/api/v1/timeline` | 获取阅读时间线 |

## 开发

### 运行测试

```bash
cd backend
pytest
```

### 代码检查

```bash
# flake8
flake8 src/

# mypy
mypy src/
```

## 环境变量说明

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `AI_PROVIDER` | AI 提供商 | `openai` |
| `OPENAI_API_KEY` | OpenAI API Key | - |
| `MINIMAX_API_KEY` | MiniMax API Key | - |
| `ZHIPUAI_API_KEY` | 智谱 API Key | - |
| `DATABASE_URL` | PostgreSQL 连接串 | SQLite |
| `NEO4J_URI` | Neo4j 连接地址 | `bolt://localhost:7687` |
| `QDRANT_URL` | Qdrant 连接地址 | `http://localhost:6333` |
| `DEBUG` | 调试模式 | `false` |

## 许可证

MIT License