В проекте были реализованы следующие тесты:

1. test_add_new_book_one_book
   Проверяет успешное добавление одной книги в коллекцию.

2. test_add_new_book_invalid_name (параметризованный)
   Проверяет невозможность добавления книги с:
   - Пустым названием
   - Названием длиннее 40 символов

3. test_add_new_book_duplicate_name
   Проверяет защиту от добавления дубликатов книг.

4. test_set_book_genre_valid_genre
   Проверяет установку допустимого жанра ("Фантастика").

5. test_set_book_genre_invalid_genre
   Проверяет невозможность установки несуществующего жанра.

6. test_set_book_genre_nonexistent_book
   Проверяет обработку попытки установки жанра для отсутствующей книги.

7. test_get_book_genre_new_book
   Проверяет, что у новой книги изначально нет жанра.

8. test_get_books_with_specific_genre_multiple_books (параметризованный)
   Проверяет фильтрацию книг по:
   - Существующему жанру ("Фантастика")
   - Жанру с возрастным рейтингом ("Ужасы")

9. test_get_books_for_children_valid_books (параметризованный)
   Проверяет что возвращаются книги без возрастного рейтинга:
   - Фантастика
   - Мультфильмы
   - Комедии

10. test_get_books_for_children_invalid_books (параметризованный)
    Проверяет что не возвращаются:
    - Книги с возрастным рейтингом ("Ужасы", "Детективы")
    - Книги без жанра

11. test_add_book_in_favorites_one_book
    Проверяет добавление одной книги в избранное.

12. test_add_book_in_favorites_duplicate
    Проверяет невозможность дублирования книги в избранном.

13. test_delete_book_from_favorites_one_book
    Проверяет удаление книги из избранного.

14. test_get_list_of_favorites_books_multiple_books
    Проверяет корректность получения списка избранных книг (несколько книг).

15. test_get_books_genre_returns_all_added_books 
    Проверяет, что метод возвращает все добавленные книги с их текущими жанрами.