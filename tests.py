import pytest

from main import BooksCollector

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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_no_add_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Букварь')
        assert collector.get_book_genre('Букварь') == ''

    @pytest.mark.parametrize('name', ['', 'Наименованиекнигисостоящееболеечемиз40сим'])
    def test_add_new_book_name_0_or_41_symbol_no_add(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_one_book_two_times(self):
        collector = BooksCollector()
        collector.add_new_book('Песни военных лет')
        collector.add_new_book('Песни военных лет')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_book_genre('Горе от ума') == 'Комедии'

    def test_set_book_genre_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Капитанская дочка')
        collector.set_book_genre('Капитанская дочка', 'Повесть')
        assert collector.get_book_genre('Капитанская дочка') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Внутри убийцы')
        collector.add_new_book('Тоннель')
        collector.add_new_book('Холодное сердце')
        collector.set_book_genre('Внутри убийцы', 'Детективы')
        collector.set_book_genre('Тоннель', 'Детективы')
        collector.set_book_genre('Холодное сердце', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Внутри убийцы', 'Тоннель']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Внутри убийцы')
        collector.add_new_book('Лес')
        collector.add_new_book('Холодное сердце')
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Внутри убийцы', 'Детективы')
        collector.set_book_genre('Лес', 'Ужасы')
        collector.set_book_genre('Холодное сердце', 'Мультфильмы')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.get_books_for_children() == ['Холодное сердце', 'Ревизор']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.add_book_in_favorites('Трое в лодке, не считая собаки')
        assert collector.favorites == ['Трое в лодке, не считая собаки']

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.add_book_in_favorites('Woe from Wit')
        assert collector.favorites == []

    def test_add_book_in_favorites_two_times(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.add_book_in_favorites('12 стульев')
        collector.add_book_in_favorites('12 стульев')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка на Луне')
        collector.add_new_book('Путешествие Алисы')
        collector.add_book_in_favorites('Незнайка на Луне')
        collector.add_book_in_favorites('Путешествие Алисы')
        collector.delete_book_from_favorites('Незнайка на Луне')
        assert collector.favorites == ['Путешествие Алисы']

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Красавица и чудовище')
        collector.add_new_book('Вий')
        collector.add_new_book('Хроники Нарнии')
        collector.add_book_in_favorites('Красавица и чудовище')
        collector.add_book_in_favorites('Хроники Нарнии')
        assert collector.favorites == ['Красавица и чудовище', 'Хроники Нарнии']
