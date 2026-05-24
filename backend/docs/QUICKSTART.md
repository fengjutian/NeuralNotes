# Quick Start Guide - Cognitive Reading Graph

## Development Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# .\venv\Scripts\Activate  # Windows

# 3. Install dependencies
pip install -e .[dev]

# 4. Set up environment
cp .env.example .env  # Note: Use .env.example as reference
# Edit .env with your configuration

# 5. Run tests
pytest

# 6. Start development server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Required Services

### PostgreSQL
```bash
# Start with Docker
docker run -d \
  --name reading-graph-db \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=reading_graph \
  -p 5432:5432 \
  postgres:15
```

### Neo4j
```bash
# Start with Docker
docker run -d \
  --name reading-graph-neo4j \
  -e NEO4J_AUTH=neo4j/password \
  -p 7474:7474 -p 7687:7687 \
  neo4j:5
```

### Qdrant
```bash
# Start with Docker
docker run -d \
  --name reading-graph-qdrant \
  -p 6333:6333 \
  qdrant/qdrant
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| POST | /api/v1/import | Upload md file |
| GET | /api/v1/books | List books |
| GET | /api/v1/books/{id} | Book details |
| POST | /api/v1/analyze | Trigger AI analysis |
| GET | /api/v1/graph | Knowledge graph |
| GET | /api/v1/profile | Reading profile |
| GET | /api/v1/search | Semantic search |
| GET | /api/v1/timeline | Growth timeline |

## Project Structure

```
backend/
├── src/
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Configuration
│   ├── database.py          # SQLAlchemy setup
│   ├── neo4j_client.py      # Neo4j client
│   ├── qdrant_client.py     # Qdrant client
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   ├── api/                 # API routes
│   └── utils/               # Utilities
└── tests/
    ├── unit/                # Unit tests
    └── integration/         # Integration tests
```

## Quality Tools

```bash
# Linting
flake8 src/

# Type checking
mypy src/

# Formatting
ruff format src/

# Run all checks
pre-commit run --all-files
```

## Environment Variables

See `.env.example` for all configuration options.

Key variables:
- `DATABASE_URL` - PostgreSQL connection string
- `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD` - Neo4j connection
- `QDRANT_URL` - Qdrant connection
- `OPENAI_API_KEY` - OpenAI API key (or use Qwen/DeepSeek)
