"""Pytest fixtures and configuration for tests."""

from collections.abc import Generator
from typing import Any
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.models import Base


# Test database URL (SQLite for testing)
TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="function")
def test_engine():
    """Create a test database engine."""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(test_engine) -> Generator[Session, None, None]:
    """Create a test database session."""
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=test_engine,
    )
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="function")
def client(db_session) -> Generator[TestClient, None, None]:
    """Create a test client with database override."""
    # Import here to avoid heavy dependencies
    from src.database import get_db
    from src.main import app

    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def sample_markdown_content() -> str:
    """Sample WeChat Reading markdown content for testing."""
    return """# 思考，快与慢
作者: 丹尼尔·卡尼曼
分类: 心理学
ISBN: 978-7-111-35372-4

## 第一部分：两个系统

- 快速思考的第一系统依赖于直觉和情感，而慢速思考的第二系统则需要更多的努力和控制。
> 创建于 2024-01-15

- 我们倾向于过度相信小样本，对罕见事件的概率估计常常出现严重偏差。
> 创建于 2024-01-16

## 第二部分：启发法与偏见

- 锚定效应表明，人们在决策时会被最初获得的信息所影响。
> 创建于 2024-01-20

- 可得性启发法让我们倾向于根据容易想到的例子来判断事件的可能性。
> 创建于 2024-01-21
"""


@pytest.fixture
def sample_highlight_data() -> dict[str, Any]:
    """Sample highlight data for testing."""
    return {
        "content": "快速思考的第一系统依赖于直觉和情感",
        "chapter": "第一部分：两个系统",
        "create_time": "2024-01-15",
    }


@pytest.fixture
def mock_neo4j_client():
    """Mock Neo4j client for testing."""
    client = MagicMock()
    client.connect = MagicMock()
    client.disconnect = MagicMock()
    client.execute_query = MagicMock(return_value=[])
    return client


@pytest.fixture
def mock_qdrant_client():
    """Mock Qdrant client for testing."""
    client = MagicMock()
    client.connect = MagicMock()
    client.disconnect = MagicMock()
    client.search = MagicMock(return_value=[])
    client.upsert_point = MagicMock(return_value="test-id")
    return client
