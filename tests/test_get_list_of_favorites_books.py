import pytest
from data import book1, book2


class TestGetListOfFavoritesBooks:
    
    def test_get_list_of_favorites_books_returns_favorites_list(self, collector):
        """Проверяем, что метод возвращает список избранных книг."""
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)
        result = collector.get_list_of_favorites_books()
        assert book1 in result and book2 in result