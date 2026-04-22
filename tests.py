import pytest
from main import BooksCollector

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

    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize('name', [
        'A',       
        'A' * 40    
    ])

    def test_add_new_book_valid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_name_41_symbols_not_added(self):
        collector = BooksCollector()
        name_41 = 'A' * 41
        collector.add_new_book(name_41)
        assert name_41 not in collector.get_books_genre()

    def test_add_new_book_double_add_prevented(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_add_new_book_has_no_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        collector.add_new_book('Детектив Пул')
        collector.set_book_genre('Детектив Пул', 'Детективы')
        assert collector.get_book_genre('Детектив Пул') == 'Детективы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_for_children_exclude_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert 'Сияние' not in collector.get_books_for_children()

    def test_add_book_in_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_added_if_not_in_collector(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert len(collector.get_list_of_favorites_books()) == 0


    def test_delete_book_from_favorites_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Хоббит')
        assert 'Хоббит' not in collector.get_list_of_favorites_books()
