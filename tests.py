import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name,count', [
        (['Гордость и предубеждение и зомби', 'Гордость и предубеждение и зомби'], 1),
        (['Гордость и предубеждение и зомби', 'Гордость'], 2),
        (['Гордость и предубеждение и зомби'], 1)])
    def test_add_new_book(self, book, book_name, count):
        for name_ in book_name:
            book.add_new_book(name_)
        assert len(book.get_books_genre()) == count

    def test_get_book_genre_without_genre(self, book):
        book.add_new_book('1984')
        assert book.get_book_genre('1984') == ''

    def test_set_book_genre(self, book):
        book.add_new_book('1984')
        book.set_book_genre('1984', 'Детективы')
        assert book.get_book_genre('1984') == 'Детективы'

    def test_get_books_genre_fantasy(self, book):
        assert 'Фантастика' in book.genre

    def test_add_book_in_favorites(self, book):
        book.add_new_book('Гадкая муха')
        book.add_book_in_favorites('Гадкая муха')
        assert 'Гадкая муха' in book.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, book):
        book.add_new_book('Оно')
        book.add_book_in_favorites('Оно')
        book.delete_book_from_favorites('Оно')
        assert len(book.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize('book_name,genre', [
        ('Гордость и предубеждение и зомби', 'Фантастика'),
        ('Поросенок', 'Мультфильмы'),
        ('Веселые парни', 'Комедии')])
    def test_get_books_for_children(self, book, book_name, genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert book_name in book.get_books_for_children()

    def test_get_books_with_specific_genre(self, book):
        book.add_new_book('1984')
        book.add_new_book('Оно')
        book.set_book_genre('Оно', 'Детективы')
        book.set_book_genre('1984', 'Фантастика')
        assert len(book.get_books_with_specific_genre('Фантастика')) == 1

    @pytest.mark.parametrize('book_name,genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Поросенок', 'Детективы')])
    def test_get_books_for_children_adult_genre(self, book, book_name, genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert book_name not in book.get_books_for_children()