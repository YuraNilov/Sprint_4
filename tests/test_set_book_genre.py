import pytest
from data import book1, genre_fantasy, valid_genres


class TestSetBookGenre:
    
    def test_set_book_genre_genre_is_set(self, collector):
        """Проверяем, что жанр устанавливается для добавленной книги."""
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre_fantasy)
        assert collector.books_genre[book1] == genre_fantasy
    
    @pytest.mark.parametrize('genre', valid_genres)
    def test_set_book_genre_all_valid_genres(self, collector, genre):
        """Проверяем установку всех доступных жанров."""
        collector.add_new_book(book1)
        collector.set_book_genre(book1, genre)
        assert collector.books_genre[book1] == genre