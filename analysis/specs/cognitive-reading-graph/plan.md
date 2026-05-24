"# Implementation Plan: Cognitive Reading Graph (认知阅读图谱)

**Branch**: `feature/cognitive-reading-graph` | **Date**: 2025-07-19 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/cognitive-reading-graph/spec.md`

**Note**: This plan defines the implementation phases for building an AI-powered personal knowledge graph system based on WeChat Reading notes.

---

## Summary

Build an AI-native cognitive operating system that transforms scattered reading notes into a personal knowledge graph. The system will:
- Import WeChat Reading markdown exports
- Use LLM for automatic concept extraction and analysis
- Visualize cognitive networks via Neo4j
- Provide semantic search through Qdrant vector retrieval
- Generate AI-powered reading profiles and recommendations

**Technical Approach**: FastAPI backend with React frontend, Neo4j for graph storage, Qdrant for vector search, PostgreSQL for structured data, leveraging LangChain/LlamaIndex for AI orchestration.

---

## Technical Context

**Language/Version**: Python 3.11

**Primary Dependencies**:
- FastAPI (web framework)
- LangChain / LlamaIndex (AI orchestration)
- neo4j-driver (graph database)
- qdrant-client (vector search)
- psycopg2-binary (PostgreSQL)
- openai / zhipuai (AI providers)

**Storage**: 
- PostgreSQL + pgvector (structured data + embeddings)
- Neo4j (knowledge graph)
- Qdrant (vector index)

**Testing**: pytest with 80%+ coverage target

**Target Platform**: Linux server (cloud deployment)

**Project Type**: Full-stack web application (backend API + React frontend)

**Performance Goals**:
- API response < 3s
- Vector search < 1s
- AI analysis < 10s
- Support 1M+ graph nodes

**Constraints**:
- Single-user MVP (multi-user out of scope)
- Requires AI API keys (OpenAI/Qwen/DeepSeek)
- Network connectivity required for AI features

**Scale/Scope**:
- MVP: Single user with 100-1000 books
- 8 core modules to implement
- Phase 1: 5 MVP features (MD import, parse, AI extraction, Neo4j graph, AI profile)

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Python Project Constitution Gates:**

- [ ] **PEP 8 Compliance**: Code MUST follow Python style guide (indentation, naming, imports)
- [ ] **Type Annotations**: All functions MUST have complete type hints with mypy validation
- [ ] **TDD Enforcement**: Core features MUST have tests written before implementation
- [ ] **Virtual Environment**: Project MUST use isolated venv/conda with pinned dependencies
- [ ] **Documentation**: All public functions MUST have Google-style docstrings
- [ ] **Security**: No hardcoded credentials; use environment variables
- [ ] **Quality Gates**: Pre-commit hooks configured (flake8, mypy, pytest)

---

## Project Structure

### Documentation (this feature)

```text
specs/cognitive-reading-graph/
├── plan.md              # This file
├── research.md          # Phase 0 output (research findings)
├── data-model.md        # Phase 1 output (database schemas)
├── quickstart.md        # Phase 1 output (setup guide)
├── contracts/           # Phase 1 output (API contracts)
│   ├── import-api.md
│   ├── graph-api.md
│   └── profile-api.md
└── tasks.md             # Phase 2 output (task list)
```

### Source Code (repository root)

```text
# Backend (Python FastAPI)
backend/
├── src/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry
│   ├── config.py               # Configuration management
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── highlight.py
│   │   ├── concept.py
│   │   └── reader.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── highlight.py
│   │   └── graph.py
│   ├── services/               # Business logic
│   │   ├── __init__.py
│   │   ├── markdown_parser.py  # MD file parsing
│   │   ├── ai_analyzer.py      # LLM concept extraction
│   │   ├── graph_service.py    # Neo4j operations
│   │   ├── vector_service.py   # Qdrant operations
│   │   └── profile_service.py  # Reading profile generation
│   ├── api/                    # API routes
│   │   ├── __init__.py
│   │   ├── import.py           # /api/v1/import
│   │   ├── books.py            # /api/v1/books
│   │   ├── analyze.py          # /api/v1/analyze
│   │   ├── graph.py            # /api/v1/graph
│   │   ├── profile.py          # /api/v1/profile
│   │   ├── search.py           # /api/v1/search
│   │   └── timeline.py         # /api/v1/timeline
│   └── utils/                  # Utilities
│       ├── __init__.py
│       ├── exceptions.py
│       └── logging.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # pytest fixtures
│   ├── unit/
│   │   ├── test_markdown_parser.py
│   │   ├── test_ai_analyzer.py
│   │   └── test_services.py
│   └── integration/
│       └── test_api.py
├── requirements.txt
├── pyproject.toml
└── .env.example

# Frontend (React)
frontend/
├── src/
│   ├── App.tsx
│   ├── main.tsx
│   ├── api/                    # API client
│   │   └── client.ts
│   ├── components/
│   │   ├── GraphView/          # Cytoscape graph visualization
│   │   ├── BookList/           # Book management
│   │   ├── ProfileView/        # Reading profile
│   │   └── SearchPanel/        # Semantic search
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── Graph.tsx
│   │   └── Profile.tsx
│   └── types/
│       └── api.ts
├── package.json
└── vite.config.ts

# Docker Compose for local development
docker-compose.yml
```

**Structure Decision**: Full-stack application with clear backend/frontend separation. Backend follows service-layer architecture with separate modules for parsing, AI analysis, graph operations, and vector search. Frontend uses component-based structure with pages for different views.

---

## Implementation Phases

### Phase 0: Research & Architecture (1 week)

**Objectives**: Validate technical decisions and establish foundational architecture

| Task | Description | Deliverable |
|------|-------------|-------------|
| P0-1 | Research WeChat Reading MD format variations | Document parsing requirements |
| P0-2 | Compare LLM providers (OpenAI/Qwen/DeepSeek) | Provider selection with cost/quality analysis |
| P0-3 | Design Neo4j schema and Cypher queries | Graph data model documentation |
| P0-4 | Validate pgvector vs Qdrant for embeddings | Vector store selection document |
| P0-5 | Create API contract draft | OpenAPI/Swagger specification |

**Exit Criteria**: 
- Technical decisions documented and approved
- API contracts reviewed by stakeholders
- No blocking technical risks

---

### Phase 1: Infrastructure & Core (2 weeks)

**Objectives**: Build foundation for all features

| Task | Description | Deliverable |
|------|-------------|-------------|
| P1-1 | Setup project structure with Poetry/pyproject | Repository initialized |
| P1-2 | Configure pre-commit hooks (flake8, mypy, pytest) | Quality gates active |
| P1-3 | Implement data models with SQLAlchemy | Database models complete |
| P1-4 | Create config management with pydantic-settings | Environment-based config |
| P1-5 | Build markdown parser for WeChat format | Parser with test coverage |
| P1-6 | Setup Neo4j connection and basic CRUD | Graph service operational |
| P1-7 | Implement Qdrant vector index setup | Vector service operational |
| P1-8 | Create FastAPI application skeleton | API framework with routes |

**Exit Criteria**: 
- All infrastructure code passes lint and type checks
- Basic import/parse workflow functional
- Database connections verified

---

### Phase 2: MVP Features (3 weeks)

**Objectives**: Implement all Phase 1 MVP features

#### Module 1: Markdown Import System
| Task | Description |
|------|-------------|
| P2-1.1 | File upload endpoint with validation |
| P2-1.2 | Batch upload support |
| P2-1.3 | Format error handling and user feedback |

#### Module 2: Data Parsing
| Task | Description |
|------|-------------|
| P2-2.1 | Extract book metadata (title, author, category) |
| P2-2.2 | Parse highlight content and chapters |
| P2-2.3 | Store in PostgreSQL with proper relations |

#### Module 3: AI Concept Extraction
| Task | Description |
|------|-------------|
| P2-3.1 | LLM integration (provider abstraction) |
| P2-3.2 | Concept extraction prompt design |
| P2-3.3 | Batch processing with progress tracking |
| P2-3.4 | Error handling and retry logic |

#### Module 4: Knowledge Graph (Neo4j)
| Task | Description |
|------|-------------|
| P2-4.1 | Node creation (Book, Concept, Author, Highlight) |
| P2-4.2 | Relationship creation and maintenance |
| P2-4.3 | Graph query endpoints |
| P2-4.4 | Basic visualization data export |

#### Module 5: AI Reading Profile
| Task | Description |
|------|-------------|
| P2-5.1 | Reading preference analysis |
| P2-5.2 | Cognitive style detection |
| P2-5.3 | Blind spot identification |

**Exit Criteria**:
- All 5 MVP features functional and tested
- API endpoints documented
- User can complete full import → analysis → visualization flow

---

### Phase 3: Advanced Features (2 weeks)

**Objectives**: Implement P2 features for richer experience

| Task | Description | Module |
|------|-------------|--------|
| P3-1 | Semantic search with Qdrant | Vector Search |
| P3-2 | Thought aggregation | Vector Search |
| P3-3 | Book recommendation engine | AI Suggestions |
| P3-4 | Reading roadmap generation | AI Suggestions |

**Exit Criteria**:
- Semantic search working with <1s response
- Recommendations explainable

---

### Phase 4: Polish & Deploy (1 week)

**Objectives**: Production readiness

| Task | Description |
|------|-------------|
| P4-1 | Frontend graph visualization (Cytoscape.js) |
| P4-2 | Docker Compose setup |
| P4-3 | Error monitoring and logging |
| P4-4 | Performance optimization |
| P4-5 | Documentation (README, API docs) |

**Exit Criteria**:
- Application deployable with single command
- All tests passing
- Documentation complete

---

## Complexity Tracking

*No Constitution violations. All Python Project Constitution requirements will be followed throughout implementation.*

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| **Multi-project structure** | Backend + Frontend separation | Different tech stacks, independent deployment |
| **Service layer pattern** | Services separate from API routes | Testability, single responsibility |
| **Vector store choice** | Qdrant over pgvector | Better scalability, dedicated vector ops |
| **LLM abstraction** | Provider-agnostic interface | Flexibility across OpenAI/Qwen/DeepSeek |

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| MD format changes in WeChat | Medium | High | Version detection, extensible parser |
| AI API rate limits | High | Medium | Queue-based processing, retry logic |
| Neo4j performance at scale | Low | High | Index optimization, pagination |
| Vector search quality | Medium | Medium | Prompt tuning, relevance feedback |

---

## Timeline Summary

```text
Week 1-2:  Phase 0 (Research) + Phase 1 (Infrastructure)
Week 3-5:  Phase 2 (MVP Features)
Week 6-7:  Phase 3 (Advanced Features)
Week 8:    Phase 4 (Polish & Deploy)

Total: ~8 weeks
```

---

## Next Steps

1. **Constitution Check**: Verify all Python constitution requirements are understood
2. **Start Phase 0**: Begin technical research and API contract design
3. **Create research.md**: Document findings from Phase 0 research
4. **Create data-model.md**: Detail database schema designs
5. **Proceed to tasks generation**: Use `$speckit-tasks` after plan approval
</parameter>