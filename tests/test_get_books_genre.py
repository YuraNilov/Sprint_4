import pytest
from data import book1, book2


class TestGetBooksGenre:
    
    def test_get_books_genre_returns_books_dict(self, collector):
        """Проверяем, что метод возвращает словарь с добавленными книгами."""
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        result = collector.get_books_genre()
        assert book1 in result and book2 in result