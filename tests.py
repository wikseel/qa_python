import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize('name', [
        'A',       
        'A' * 40    
    ])

    def test_add_new_book_valid_name_length(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_name_41_symbols_not_added(self, collector):
        name_41 = 'A' * 41
        collector.add_new_book(name_41)
        assert name_41 not in collector.get_books_genre()

    def test_add_new_book_double_add_prevented(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_successfully(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_add_new_book_has_no_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_by_name(self, collector):
        collector.books_genre = {'Детектив Пул': 'Детективы'}
        assert collector.get_book_genre('Детектив Пул') == 'Детективы'

    def test_get_books_with_specific_genre_horror(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантакстика')
        horror_books = collector.get_books_with_specific_genre('Ужасы');
    
        assert 'Оно' in horror_books
        assert 'Дюна' not in horror_books
        assert len(horror_books) == 1

    def test_get_books_for_children_exclude_horror(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        children_books = collector.get_books_for_children()

        assert 'Шрек' in children_books
        assert 'Сияние' not in children_books
        assert len(children_books) == 1

    def test_add_book_in_favorites_successfully(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert 'Мастер и Маргарита' in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ['Ведьмак', 'Дюна']
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Ведьмак', 'Дюна']
        assert len(favorites) == 2

    def test_delete_book_from_favorites_successfully(self, collector):
        collector.favorites = ['Хоббит']
        collector.delete_book_from_favorites('Хоббит')
        assert 'Хоббит' not in collector.favorites
