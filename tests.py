from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert 'Дюна' in collector.books_genre

    @pytest.mark.parametrize(
        'name',
        ['', 'Очень длинное название книги, которое превышает 40 символов в длину']
    )
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Несуществующий жанр')
        assert collector.get_book_genre('Дюна') == ''

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

    def test_get_book_genre_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    @pytest.mark.parametrize(
        'genre, books, expected_books',
        [
            ('Фантастика', ['Дюна', 'Хоббит'], ['Дюна', 'Хоббит']),
            ('Ужасы', ['Мгла', 'Оно'], ['Мгла', 'Оно']),
        ]
    )
    def test_get_books_with_specific_genre_multiple_books(self, genre, books, expected_books):
        collector = BooksCollector()

        for book_name in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        assert collector.get_books_with_specific_genre(genre) == expected_books

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Дюна', 'Фантастика'),
            ('Винни-Пух', 'Мультфильмы'),
            ('Трое в лодке', 'Комедии')
        ]
    )
    def test_get_books_for_children_valid_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert book_name in collector.get_books_for_children()

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Мгла', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы')
        ]
    )
    def test_get_books_for_children_invalid_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert book_name not in collector.get_books_for_children()

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert 'Дюна' in collector.favorites

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.favorites

    def test_get_list_of_favorites_books_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Хоббит')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Хоббит']