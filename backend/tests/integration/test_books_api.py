"""Integration tests for Books API endpoints."""

from uuid import uuid4

from fastapi.testclient import TestClient

from src.models.book import Book
from src.models.highlight import Highlight


class TestBooksAPI:
    """Test cases for books endpoints."""

    def test_create_book(self, client: TestClient, db_session):
        """Test creating a new book."""
        response = client.post(
            "/api/v1/books/",
            json={
                "title": "Test Book",
                "author": "Test Author",
                "category": "Fiction",
            },
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Book"
        assert data["author"] == "Test Author"
        assert "id" in data

    def test_list_books(self, client: TestClient, db_session):
        """Test listing books with pagination."""
        # Create test books
        for i in range(3):
            book = Book(
                title=f"Book {i}",
                author=f"Author {i}",
            )
            db_session.add(book)
        db_session.commit()

        response = client.get("/api/v1/books/")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
        assert "total" in data
        assert len(data["items"]) == 3

    def test_get_book(self, client: TestClient, db_session):
        """Test getting a specific book."""
        # Create test book
        book = Book(title="Get Test", author="Test Author")
        db_session.add(book)
        db_session.commit()
        db_session.refresh(book)

        response = client.get(f"/api/v1/books/{book.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Get Test"

    def test_get_nonexistent_book(self, client: TestClient):
        """Test getting a book that doesn't exist."""
        fake_id = str(uuid4())
        response = client.get(f"/api/v1/books/{fake_id}")
        assert response.status_code == 404

    def test_delete_book(self, client: TestClient, db_session):
        """Test deleting a book."""
        # Create test book
        book = Book(title="Delete Test", author="Test Author")
        db_session.add(book)
        db_session.commit()
        db_session.refresh(book)

        response = client.delete(f"/api/v1/books/{book.id}")
        assert response.status_code == 204

        # Verify deleted
        get_response = client.get(f"/api/v1/books/{book.id}")
        assert get_response.status_code == 404

    def test_filter_by_category(self, client: TestClient, db_session):
        """Test filtering books by category."""
        # Create test books
        categories = ["Fiction", "Non-fiction", "Fiction"]
        for cat in categories:
            book = Book(title=f"Book {cat}", author="Author", category=cat)
            db_session.add(book)
        db_session.commit()

        response = client.get("/api/v1/books/?category=Fiction")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        for item in data["items"]:
            assert item["category"] == "Fiction"

    def test_pagination(self, client: TestClient, db_session):
        """Test pagination of book list."""
        # Create 15 test books
        for i in range(15):
            book = Book(title=f"Paginated Book {i}", author="Author")
            db_session.add(book)
        db_session.commit()

        # Get first page
        response = client.get("/api/v1/books/?page=1&page_size=5")
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 5
        assert data["page"] == 1
        assert data["page_size"] == 5

        # Get second page
        response = client.get("/api/v1/books/?page=2&page_size=5")
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 5
        assert data["page"] == 2