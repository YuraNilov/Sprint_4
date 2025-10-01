import pytest
from data import book1


class TestAddBookInFavorites:
    
    def test_add_book_in_favorites_book_added_to_favorites(self, collector):
        """Проверяем, что книга добавляется в избранное."""
        collector.add_new_book(book1)
        collector.add_book_in_favorites(book1)
        assert book1 in collector.favorites