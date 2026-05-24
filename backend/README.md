cd backend; $content = Get-Content README.md -Raw; $oldSection = '## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Neo4j 5+
- Qdrant 1.12+

### Installation

```bash
# Clone and enter directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: .\venv\Scripts\Activate  # Windows

# Install dependencies
pip install -e .[dev]

# Copy environment file
cp .env.example .env
# Edit .env with your configuration

# Run tests
pytest

# Start server
uvicorn src.main:app --reload
```'; $newSection = @'
## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Neo4j 5+
- Qdrant 1.12+

### 运行服务 (Windows)

```powershell
# 1. 进入 backend 目录
cd backend

# 2. 激活虚拟环境（项目已包含 venv，无需重新创建）
.\venv\Scripts\Activate

# 3. 复制并编辑环境变量（首次运行）
copy .env.example .env
# 用编辑器打开 .env，填入数据库、Neo4j、Qdrant 地址和 API Key

# 4. 启动开发服务器
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问：
- **Swagger 文档**: http://localhost:8000/docs
- **API 服务**: http://localhost:8000

> 💡 如果只想测试文件导入功能，无需配置所有外部服务即可启动。

### 运行服务 (Linux / Mac)

```bash
# 1. 进入 backend 目录
cd backend

# 2. 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate

# 3. 安装依赖
pip install -e .[dev]

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 配置文件

# 5. 启动开发服务器
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问：
- **Swagger 文档**: http://localhost:8000/docs
- **API 服务**: http://localhost:8000

> 💡 如果只想测试文件导入功能，无需配置所有外部服务即可启动。
'@; $content = $content -replace [regex]::Escape($oldSection), $newSection; Set-Content README.md -Value $content -NoNewline -Encoding UTF8; Write-Output 'Done'

Done
