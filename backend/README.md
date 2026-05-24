# Cognitive Reading Graph (认知阅读图谱)

AI-powered personal knowledge graph system based on WeChat Reading notes.

## Features

- 📚 **Markdown Import**: Import WeChat Reading notes (md files)
- 🧠 **AI Concept Extraction**: Automatic concept and domain analysis
- 🔗 **Knowledge Graph**: Visualize cognitive networks with Neo4j
- 🔍 **Semantic Search**: Natural language search with Qdrant
- 👤 **Reading Profile**: AI-generated reading persona analysis

## Tech Stack

- **Backend**: FastAPI + Python 3.11
- **Database**: PostgreSQL + pgvector
- **Graph**: Neo4j
- **Vector Search**: Qdrant
- **AI**: LangChain + OpenAI/Qwen/DeepSeek

## Quick Start

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
```

## Project Structure

```
backend/
├── src/
│   ├── models/         # Database models (SQLAlchemy)
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── api/            # FastAPI routes
│   └── utils/          # Utilities
├── tests/
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
└── docs/               # Documentation
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/v1/import | Upload md file |
| GET | /api/v1/books | List books |
| GET | /api/v1/books/{id} | Book details |
| POST | /api/v1/analyze | Trigger AI analysis |
| GET | /api/v1/graph | Knowledge graph data |
| GET | /api/v1/profile | Reading profile |
| GET | /api/v1/search | Semantic search |

## Development

```bash
# Run tests with coverage
pytest --cov=src --cov-report=html

# Type checking
mypy src/

# Linting
flake8 src/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## License

MIT
