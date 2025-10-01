import pytest
from data import book1, book2, book_1_char, book_40_chars


class TestAddNewBook:
    
    def test_add_new_book_add_two_books(self, collector):
        """Проверяем, что можно добавить две книги."""
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        assert len(collector.books_genre) == 2
    
    @pytest.mark.parametrize(
        'book_name',
        [book_1_char, book_40_chars]
    )
    def test_add_new_book_boundary_length(self, collector, book_name):
        """Проверяем добавление книг с валидной длиной названия (1-40 символов)."""
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre