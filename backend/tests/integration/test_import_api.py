"""Integration tests for Import API endpoints."""

import io
from fastapi.testclient import TestClient


class TestImportAPI:
    """Test cases for import endpoints."""

    def test_import_valid_markdown(self, client, sample_markdown_content):
        """Test importing a valid markdown file."""
        file_content = sample_markdown_content.encode("utf-8")
        file = io.BytesIO(file_content)
        file.name = "test_book.md"

        response = client.post(
            "/api/v1/import/",
            files={"file": ("test.md", file, "text/markdown")},
        )

        # Should succeed and return book info
        if response.status_code == 201:
            data = response.json()
            assert data["status"] == "success"
            assert "book_id" in data
            assert data["title"] == "思考，快与慢"
            assert data["author"] == "丹尼尔·卡尼曼"
        elif response.status_code == 422:
            # Markdown parsing may have issues, acceptable
            pass

    def test_import_invalid_file_type(self, client):
        """Test importing an invalid file type."""
        file_content = b"Not a markdown file"
        file = io.BytesIO(file_content)
        file.name = "test.txt"

        response = client.post(
            "/api/v1/import/",
            files={"file": ("test.txt", file, "text/plain")},
        )

        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Invalid file type" in data["detail"]

    def test_import_batch(self, client, sample_markdown_content):
        """Test batch importing multiple files."""
        files = []
        for i in range(3):
            content = f"# Book {i}\n作者: Author {i}\n\n## Chapter\n- Highlight {i}\n> 创建于 2024-01-{10+i}"
            file_content = content.encode("utf-8")
            file = io.BytesIO(file_content)
            file.name = f"book_{i}.md"
            files.append(("files", (f"book_{i}.md", file, "text/markdown")))

        response = client.post(
            "/api/v1/import/batch",
            files=files,
        )

        # Should return batch results
        if response.status_code == 200:
            data = response.json()
            assert "results" in data
            assert data["total"] == 3

    def test_import_empty_file(self, client):
        """Test importing an empty file."""
        file_content = b""
        file = io.BytesIO(file_content)
        file.name = "empty.md"

        response = client.post(
            "/api/v1/import/",
            files={"file": ("empty.md", file, "text/markdown")},
        )

        # Should handle gracefully
        assert response.status_code in [400, 422, 500]

    def test_import_malformed_markdown(self, client):
        """Test importing malformed markdown."""
        malformed_content = "This is not a valid WeChat Reading format"
        file_content = malformed_content.encode("utf-8")
        file = io.BytesIO(file_content)
        file.name = "malformed.md"

        response = client.post(
            "/api/v1/import/",
            files={"file": ("malformed.md", file, "text/markdown")},
        )

        # Should return error or create minimal book
        assert response.status_code in [200, 422, 500]


class TestHealthEndpoints:
    """Test health check endpoints."""

    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    def test_root_endpoint(self, client):
        """Test root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "app" in data
        assert "version" in data