import pytest
from data import book1, book2, genre_fantasy, genre_horror


class TestGetBooksForChildren:
    
    def test_get_books_for_children_excludes_books_with_age_rating(self, collector):
        """Проверяем, что книги с возрастным рейтингом не попадают в список для детей."""
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre_fantasy)
        collector.add_new_book(book2)
        collector.set_book_genre(book2, genre_horror)
        result = collector.get_books_for_children()
        assert book1 in result and book2 not in result