# Cognitive Reading Graph (璁ょ煡闃呰鍥捐氨)

AI-powered personal knowledge graph system based on WeChat Reading notes.

## Features

- 馃摎 **Markdown Import**: Import WeChat Reading notes (md files)
- 馃 **AI Concept Extraction**: Automatic concept and domain analysis
- 馃敆 **Knowledge Graph**: Visualize cognitive networks with Neo4j
- 馃攳 **Semantic Search**: Natural language search with Qdrant
- 馃懁 **Reading Profile**: AI-generated reading persona analysis

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
鈹溾攢鈹€ src/
鈹?  鈹溾攢鈹€ models/         # Database models (SQLAlchemy)
鈹?  鈹溾攢鈹€ schemas/        # Pydantic schemas
鈹?  鈹溾攢鈹€ services/       # Business logic
鈹?  鈹溾攢鈹€ api/            # FastAPI routes
鈹?  鈹斺攢鈹€ utils/          # Utilities
鈹溾攢鈹€ tests/
鈹?  鈹溾攢鈹€ unit/           # Unit tests
鈹?  鈹斺攢鈹€ integration/    # Integration tests
鈹斺攢鈹€ docs/               # Documentation
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
