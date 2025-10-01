import pytest
from data import book1, genre_fantasy


class TestGetBookGenre:
    
    def test_get_book_genre_returns_genre(self, collector):
        """Проверяем, что метод возвращает жанр книги."""
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre_fantasy)
        assert collector.get_book_genre(book1) == genre_fantasy