"""Tests for ProfileService -- rule-based reading profile analysis."""

from src.services.profile_service import ProfileService, ReadingProfile


class TestProfileService:
    """Test suite for ProfileService."""

    def test_creates_singleton(self):
        from src.services.profile_service import profile_service
        assert isinstance(profile_service, ProfileService)

    def test_min_books_threshold(self):
        svc = ProfileService()
        assert svc.MIN_BOOKS_FOR_PROFILE == 3

    def test_generate_profile_insufficient_data(self):
        svc = ProfileService()
        try:
            svc.generate_profile([
                {"title": "A", "author": "X", "category": "psychology"},
                {"title": "B", "author": "Y", "category": "history"},
            ], [])
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "3" in str(e)

    def test_analyze_preferences_categories(self):
        svc = ProfileService()
        books = [
            {"title": "A", "author": "X", "category": "psychology"},
            {"title": "B", "author": "Y", "category": "psychology"},
            {"title": "C", "author": "Z", "category": "history"},
        ]
        prefs = svc.analyze_preferences(books, [])
        cats = prefs["categories"]
        assert cats[0]["name"] == "psychology"
        assert cats[0]["count"] == 2
        assert cats[1]["name"] == "history"
        assert cats[1]["count"] == 1

    def test_analyze_preferences_authors(self):
        svc = ProfileService()
        books = [
            {"title": "A", "author": "X"},
            {"title": "B", "author": "X"},
            {"title": "C", "author": "Y"},
        ]
        prefs = svc.analyze_preferences(books, [])
        authors = prefs["top_authors"]
        assert authors[0]["name"] == "X"
        assert authors[0]["count"] == 2

    def test_analyze_cognitive_style(self):
        svc = ProfileService()
        concepts = [{"name": "logical reasoning"}, {"name": "data analysis"}]
        style = svc.analyze_cognitive_style(concepts)
        assert "primary_style" in style
        assert "distribution" in style
        assert "intensity" in style

    def test_analyze_cognitive_style_empty(self):
        svc = ProfileService()
        style = svc.analyze_cognitive_style([])
        for v in style["distribution"].values():
            assert v == 0.0

    def test_detect_blind_spots_empty(self):
        svc = ProfileService()
        spots = svc.detect_blind_spots([], [])
        assert len(spots) == 5
        assert spots[0]["severity"] in ("medium", "low")

    def test_detect_blind_spots_with_data(self):
        svc = ProfileService()
        books = [{"title": "A", "category": "psychology"}]
        concepts = [{"name": "cognition", "domain": "psychology"}]
        spots = svc.detect_blind_spots(books, concepts)
        domains = {s["domain"] for s in spots}
        assert "psychology" not in domains

    def test_should_regenerate(self):
        svc = ProfileService()
        assert svc.should_regenerate(5, 2) is True
        assert svc.should_regenerate(3, 1) is False
        assert svc.should_regenerate(10, 0, threshold=5) is True

    def test_reading_profile_to_dict(self):
        rp = ReadingProfile(
            preferences={"cats": []},
            cognitive_style={"primary": "X"},
            blind_spots=[{"domain": "Y"}],
            summary="Z",
        )
        d = rp.to_dict()
        assert d["preferences"] == {"cats": []}
        assert d["cognitive_style"]["primary"] == "X"
        assert d["blind_spots"][0]["domain"] == "Y"
        assert d["summary"] == "Z"
