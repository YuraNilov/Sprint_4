import pytest
from data import book1


class TestDeleteBookFromFavorites:
    
    def test_delete_book_from_favorites_book_removed(self, collector):
        """Проверяем, что книга удаляется из избранного."""
        collector.add_new_book(book1)
        collector.add_book_in_favorites(book1)
        collector.delete_book_from_favorites(book1)
        assert book1 not in collector.favorites