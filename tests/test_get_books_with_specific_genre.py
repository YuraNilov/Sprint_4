import pytest
from data import book1, valid_genres


class TestGetBooksWithSpecificGenre:
    
    @pytest.mark.parametrize('genre', valid_genres)
    def test_get_books_with_specific_genre_returns_books_list(self, collector, genre):
        """Проверяем, что метод возвращает список книг с определённым жанром."""
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre)
        result = collector.get_books_with_specific_genre(genre)
        assert book1 in result