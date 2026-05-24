# Tasks: Cognitive Reading Graph (认知阅读图谱)

**Input**: Design documents from `specs/cognitive-reading-graph/`

**Prerequisites**: plan.md, spec.md

**Organization**: Tasks grouped by user story (US1-US7) for independent implementation

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story (e.g., US1, US2, US3)
- Path: `backend/src/`, `backend/tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 [P] Create project structure per plan.md (`backend/src/`, `backend/tests/`)
- [ ] T002 Create `backend/pyproject.toml` with dependencies (fastapi, langchain, neo4j, qdrant, pytest)
- [ ] T003 [P] Create and activate virtual environment with `python -m venv venv`
- [ ] T004 [P] Configure `backend/setup.cfg` for flake8 (max-line-length=79, exclude=venv)
- [ ] T005 [P] Configure `backend/mypy.ini` for strict type checking
- [ ] T006 Configure `backend/pytest.ini` with coverage (min 80%), testpaths=tests
- [ ] T007 Create `backend/.pre-commit-config.yaml` (flake8, mypy, pytest hooks)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story

**⚠️ CRITICAL**: No user story work until Phase 2 is complete

### Models & Schemas

- [ ] T008 [P] Create `backend/src/models/__init__.py` and base classes
- [ ] T009 [P] Create `backend/src/models/book.py` (Book entity with type annotations)
- [ ] T010 [P] Create `backend/src/models/highlight.py` (Highlight entity)
- [ ] T011 [P] Create `backend/src/models/concept.py` (Concept entity)
- [ ] T012 [P] Create `backend/src/models/reader.py` (Reader entity)
- [ ] T013 [P] Create `backend/src/models/chapter.py` (Chapter entity)

### Schemas (Pydantic)

- [ ] T014 [P] Create `backend/src/schemas/__init__.py`
- [ ] T015 [P] Create `backend/src/schemas/book.py` (BookCreate, BookResponse)
- [ ] T016 [P] Create `backend/src/schemas/highlight.py` (HighlightCreate, HighlightResponse)
- [ ] T017 [P] Create `backend/src/schemas/graph.py` (GraphNode, GraphEdge)

### Infrastructure

- [ ] T018 [P] Create `backend/src/config.py` with pydantic-settings (.env handling)
- [ ] T019 [P] Create `backend/src/utils/logging.py` with structured logging setup
- [ ] T020 [P] Create `backend/src/utils/exceptions.py` (custom exception hierarchy)
- [ ] T021 [P] Create `backend/src/utils/__init__.py` utility functions
- [ ] T022 Create `backend/src/database.py` (SQLAlchemy session management)
- [ ] T023 Create `backend/src/neo4j_client.py` (Neo4j connection management)
- [ ] T024 Create `backend/src/qdrant_client.py` (Qdrant connection management)

### API Foundation

- [ ] T025 Create `backend/src/main.py` (FastAPI application skeleton)
- [ ] T026 Create `backend/src/api/__init__.py` and router aggregation

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Markdown File Import (Priority: P1) 🎯 MVP

**Goal**: Users upload WeChat Reading md files, system parses and stores data

**Independent Test**: Upload md file → verify book and highlights stored in database

### Tests for User Story 1 (MANDATORY - TDD) ⚠️

> **Write tests FIRST, ensure they FAIL before implementation**

- [ ] T027 [P] [US1] Unit tests in `backend/tests/unit/test_markdown_parser.py`
- [ ] T028 [P] [US1] Type checking validation with `mypy backend/src/services/markdown_parser.py`

### Implementation for User Story 1

- [ ] T029 [P] [US1] Create `backend/src/services/markdown_parser.py` with parse functions
- [ ] T030 [P] [US1] Create `backend/src/services/file_service.py` for file handling
- [ ] T031 [US1] Create `backend/src/api/import.py` with POST `/api/v1/import` endpoint
- [ ] T032 [US1] Create `backend/src/api/books.py` with GET `/api/v1/books` endpoints
- [ ] T033 [US1] Add validation for md format, return clear error messages
- [ ] T034 [US1] Add logging for import operations in `backend/src/services/markdown_parser.py`

**Checkpoint**: US1 functional - can upload md file and retrieve book data

---

## Phase 4: User Story 2 - AI Concept Extraction (Priority: P1) 🎯 MVP

**Goal**: AI automatically extracts concepts, domains, emotions from highlights

**Independent Test**: Provide highlight → verify LLM returns concepts, domain, emotion

### Tests for User Story 2 (MANDATORY - TDD) ⚠️

> **Write tests FIRST, ensure they FAIL before implementation**

- [ ] T035 [P] [US2] Unit tests in `backend/tests/unit/test_ai_analyzer.py` (mock LLM)
- [ ] T036 [P] [US2] Type checking validation with `mypy backend/src/services/ai_analyzer.py`

### Implementation for User Story 2

- [ ] T037 [P] [US2] Create `backend/src/services/llm_provider.py` (provider abstraction)
- [ ] T038 [P] [US2] Create `backend/src/services/concept_extractor.py` (extraction logic)
- [ ] T039 [US2] Create `backend/src/services/ai_analyzer.py` (batch processing)
- [ ] T040 [US2] Create `backend/src/api/analyze.py` with POST `/api/v1/analyze` endpoint
- [ ] T041 [US2] Implement retry logic for API rate limits
- [ ] T042 [US2] Add progress tracking for batch operations

**Checkpoint**: US2 functional - can analyze highlights and extract concepts

---

## Phase 5: User Story 3 - Knowledge Graph Visualization (Priority: P1) 🎯 MVP

**Goal**: Visualize personal cognitive knowledge graph with Neo4j

**Independent Test**: View graph → verify nodes and relationships display correctly

### Tests for User Story 3 (MANDATORY - TDD) ⚠️

> **Write tests FIRST, ensure they FAIL before implementation**

- [ ] T043 [P] [US3] Unit tests in `backend/tests/unit/test_graph_service.py`
- [ ] T044 [P] [US3] Integration tests in `backend/tests/integration/test_graph_api.py`
- [ ] T045 [P] [US3] Type checking validation with `mypy backend/src/services/graph_service.py`

### Implementation for User Story 3

- [ ] T046 [P] [US3] Create `backend/src/services/graph_service.py` (Neo4j operations)
- [ ] T047 [P] [US3] Implement node creation (Book, Concept, Author, Highlight)
- [ ] T048 [P] [US3] Implement relationship creation
- [ ] T049 [US3] Create `backend/src/api/graph.py` with GET `/api/v1/graph` endpoint
- [ ] T050 [US3] Add book filtering for graph nodes
- [ ] T051 [US3] Implement node detail view endpoint

**Checkpoint**: US3 functional - can view and interact with knowledge graph

---

## Phase 6: User Story 4 - AI Reading Profile (Priority: P2)

**Goal**: Generate reading persona with preferences, tendencies, blind spots

**Independent Test**: 10+ books → verify profile shows preferences and suggestions

### Tests for User Story 4 (OPTIONAL) ⚠️

- [ ] T052 [P] [US4] Unit tests in `backend/tests/unit/test_profile_service.py`

### Implementation for User Story 4

- [ ] T053 [P] [US4] Create `backend/src/services/profile_service.py` (profile generation)
- [ ] T054 [P] [US4] Implement reading preference analysis
- [ ] T055 [P] [US4] Implement cognitive style detection
- [ ] T056 [US4] Create `backend/src/api/profile.py` with GET `/api/v1/profile` endpoint
- [ ] T057 [US4] Add insufficient data handling (< 3 books)

**Checkpoint**: US4 functional - can view reading profile

---

## Phase 7: User Story 5 - Semantic Search & RAG (Priority: P2)

**Goal**: Natural language search across all highlights with vector similarity

**Independent Test**: Search "trust" → verify returns semantically related highlights

### Tests for User Story 5 (OPTIONAL) ⚠️

- [ ] T058 [P] [US5] Unit tests in `backend/tests/unit/test_vector_service.py`

### Implementation for User Story 5

- [ ] T059 [P] [US5] Create `backend/src/services/embedding_service.py` (text vectorization)
- [ ] T060 [P] [US5] Create `backend/src/services/vector_service.py` (Qdrant operations)
- [ ] T061 [P] [US5] Implement semantic search with fallback to full-text
- [ ] T062 [US5] Create `backend/src/api/search.py` with GET `/api/v1/search` endpoint
- [ ] T063 [US5] Implement thought aggregation endpoint

**Checkpoint**: US5 functional - can search highlights semantically

---

## Phase 8: User Story 6 - AI Reading Suggestions (Priority: P3)

**Goal**: Recommend next books based on cognitive graph

**Independent Test**: View graph → verify book recommendations with explanations

### Implementation for User Story 6

- [ ] T064 [P] [US6] Create `backend/src/services/recommendation_service.py`
- [ ] T065 [P] [US6] Implement recommendation algorithm
- [ ] T066 [US6] Create `backend/src/api/recommendations.py` with GET `/api/v1/recommendations`
- [ ] T067 [US6] Implement reading roadmap generation

**Checkpoint**: US6 functional - can receive book recommendations

---

## Phase 9: User Story 7 - Cognitive Growth Timeline (Priority: P3)

**Goal**: Visualize long-term cognitive evolution over time

**Independent Test**: 3+ years data → verify timeline shows topic shifts

### Implementation for User Story 7

- [ ] T068 [P] [US7] Create `backend/src/services/timeline_service.py`
- [ ] T069 [P] [US7] Implement topic shift detection
- [ ] T070 [US7] Create `backend/src/api/timeline.py` with GET `/api/v1/timeline`
- [ ] T071 [US7] Add "cognitive pivot point" detection

**Checkpoint**: US7 functional - can view cognitive growth timeline

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements affecting multiple user stories

- [ ] T072 [P] Update `backend/README.md` with setup instructions
- [ ] T073 [P] Create `backend/docs/api.md` with endpoint documentation
- [ ] T074 Code cleanup and refactoring across services
- [ ] T075 Performance optimization (caching, pagination)
- [ ] T076 Additional unit tests for edge cases
- [ ] T077 Security hardening (input sanitization, rate limiting)
- [ ] T078 Run `backend/quickstart.md` validation
- [ ] T079 Create `backend/docker-compose.yml` for local development

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Phase 1: Setup | None | All |
| Phase 2: Foundational | Phase 1 | All User Stories |
| Phase 3-9: User Stories | Phase 2 | None (can parallel) |
| Phase 10: Polish | All US complete | None |

### User Story Dependencies

| Story | Priority | Can Start After | Dependencies |
|-------|----------|-----------------|--------------|
| US1: MD Import | P1 | Foundational | None |
| US2: AI Extraction | P1 | Foundational | None |
| US3: Graph Visualization | P1 | Foundational | None |
| US4: AI Profile | P2 | Foundational | US2 |
| US5: Semantic Search | P2 | Foundational | US2 |
| US6: Suggestions | P3 | Foundational | US4 |
| US7: Timeline | P3 | Foundational | US1, US2 |

### Parallel Opportunities

```
Phase 1 (Setup):           T001, T003, T004, T005 → parallel
Phase 2 (Foundational):    T008-T017 → parallel models/schemas
                          T018-T024 → parallel infrastructure
Phase 3-9 (User Stories):  All can parallel after Foundational
                          (different services, different files)
```

---

## Implementation Strategy

### MVP First (US1 + US2 + US3 + US4) 🎯

1. Phase 1: Setup
2. Phase 2: Foundational
3. **Phase 3: US1 (MD Import)** → Test → MVP core!
4. **Phase 4: US2 (AI Extraction)** → Test → Add AI power
5. **Phase 5: US3 (Graph)** → Test → Add visualization
6. **Phase 6: US4 (Profile)** → Test → MVP complete!
7. Deploy MVP

### Full Implementation

1. Phase 1-2 (Setup + Foundational)
2. Phases 3-7 (All user stories in parallel)
3. Phase 10 (Polish)
4. Full release

---

## Progress Tracking

| Phase | Tasks | Completed | Status |
|-------|-------|-----------|--------|
| Phase 1 | 7 | 0 | ⬜ Not Started |
| Phase 2 | 16 | 0 | ⬜ Not Started |
| Phase 3 (US1) | 8 | 0 | ⬜ Not Started |
| Phase 4 (US2) | 6 | 0 | ⬜ Not Started |
| Phase 5 (US3) | 6 | 0 | ⬜ Not Started |
| Phase 6 (US4) | 5 | 0 | ⬜ Not Started |
| Phase 7 (US5) | 6 | 0 | ⬜ Not Started |
| Phase 8 (US6) | 4 | 0 | ⬜ Not Started |
| Phase 9 (US7) | 4 | 0 | ⬜ Not Started |
| Phase 10 | 8 | 0 | ⬜ Not Started |
| **Total** | **70** | **0** | **0%** |

---

## Notes

- **[P]** = Parallelizable (different files)
- All user stories should be independently testable
- **TDD**: Write tests for US1-US3 BEFORE implementation
- Commit after each logical group
- Stop at checkpoints to validate independently
