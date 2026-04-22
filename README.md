# qa_python
Тесты: 
1. test_add_new_book_valid_name_length - Параметризованная проверка на валидную длину
2. test_add_new_book_name_41_symbols_not_added - Проверка на длину больше 41 символа
3. test_add_new_book_double_add_prevented - Проверка на добавление одной и той же книги дважды
4. test_set_book_genre_successfully - Проверка на установку жанра книге
5. test_add_new_book_has_no_genre - Проверка книги, у которой нет установленного жанра
6. test_get_book_genre_by_name - Проверка на вывод жанра по книге
7. test_get_books_with_specific_genre - Проверка на получение списка книг по определенному жанру
8. test_get_books_for_children_exclude_horror - Проверка на возрастное ограничение по жанру
9. test_add_book_in_favorites_successfully - Проверка на добавление в "Избранное" книги
10. test_add_book_in_favorites_not_added_if_not_in_collector - Проверка на добавление книги в "Избранное", которой нет в "Словаре"
11. test_delete_book_from_favorites_successfully - Проверка на успешное удаление книги из "Избранного"