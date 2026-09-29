import random
from time import perf_counter

from book_processor.analytics import (
    calculate_average_pages,
    calculate_average_values,
    create_record,
    create_year_filter,
    filter_books,
    find_book_by_title,
    find_largest_book,
    sort_books_by_year,
)

from book_processor.data import (
    books,
    library_metadata,
)

from book_processor.processors import (
    count_books_by_author,
    create_book_index,
    filter_by_author,
    filter_by_year,
    get_unique_authors,
    group_books_by_author,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:
    """Виведення книг у табличному форматі."""

    print(f"\n{title}")
    print("-" * 85)

    print(
        f"{'ID':<5}"
        f"{'Назва':<40}"
        f"{'Автор':<25}"
        f"{'Рік':<8}"
        f"{'Стор.':<8}"
    )

    print("-" * 85)

    for book in items:
        print(
            f"{book['id']:<5}"
            f"{book['title'][:37]:<40}"
            f"{book['author'][:22]:<25}"
            f"{book['year']:<8}"
            f"{book['pages']:<8}"
        )


def find_book_linear(
    books_data: list[dict],
    book_id: int,
) -> dict | None:
    """Лінійний пошук книги у списку."""

    for book in books_data:
        if book["id"] == book_id:
            return book

    return None


def run_benchmark() -> None:
    """
    Порівняння лінійного пошуку у list
    та пошуку у dict.
    """

    print("\n--- ЕКСПЕРИМЕНТАЛЬНА ЧАСТИНА ---")

    sizes = [
        1_000,
        10_000,
        100_000,
    ]

    for size in sizes:

        test_books = [
            {
                "id": i,
                "title": f"Book {i}",
                "author": f"Author {i % 100}",
                "year": random.randint(1900, 2025),
                "pages": random.randint(100, 1000),
            }
            for i in range(size)
        ]

        target_id = size - 1

        # -------------------------
        # Пошук у list
        # -------------------------

        start = perf_counter()

        find_book_linear(
            test_books,
            target_id,
        )

        list_time = perf_counter() - start

        # -------------------------
        # Побудова dict
        # -------------------------

        start = perf_counter()

        book_index = {
            book["id"]: book
            for book in test_books
        }

        dict_build_time = (
            perf_counter() - start
        )

        # -------------------------
        # Пошук у dict
        # -------------------------

        start = perf_counter()

        book_index.get(target_id)

        dict_search_time = (
            perf_counter() - start
        )

        print(
            f"\n{size:>8} записів:"
        )

        print(
            f"  list search:       "
            f"{list_time:.8f} с"
        )

        print(
            f"  dict build:        "
            f"{dict_build_time:.8f} с"
        )

        print(
            f"  dict search:       "
            f"{dict_search_time:.8f} с"
        )


def main() -> None:

    print(
        "=== АНАЛІЗ СИСТЕМИ ОБЛІКУ КНИГ ==="
    )

    # ----------------------------------
    # Tuple
    # ----------------------------------

    print(
        "\nІнформація про бібліотеку:"
    )

    print(
        f"Назва: {library_metadata[0]}"
    )

    print(
        f"Адреса: {library_metadata[1]}"
    )

    print(
        f"Кількість книг: {library_metadata[2]}"
    )

    # ----------------------------------
    # Усі книги
    # ----------------------------------

    print_books(
        "Усі книги",
        books,
    )

    # ----------------------------------
    # Унікальні автори
    # ----------------------------------

    authors = get_unique_authors(
        books
    )

    print(
        "\nУнікальні автори (Set):"
    )

    for author in sorted(authors):
        print(
            f" - {author}"
        )

    # ----------------------------------
    # Групування за авторами
    # ----------------------------------

    grouped = group_books_by_author(
        books
    )

    print(
        "\nГрупування книг за авторами:"
    )

    for author, author_books in grouped.items():
        print(
            f" - {author}: "
            f"{len(author_books)} книг"
        )

    # ----------------------------------
    # Counter
    # ----------------------------------

    counter = count_books_by_author(
        books
    )

    print(
        "\nCounter книг за авторами:"
    )

    print(counter)

    # ----------------------------------
    # Середня кількість сторінок
    # ----------------------------------

    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nСередня кількість сторінок: "
        f"{average_pages:.2f}"
    )

    # ----------------------------------
    # Найбільша книга
    # ----------------------------------

    largest = find_largest_book(
        books
    )

    if largest:
        print(
            "\nНайбільша книга:"
        )

        print(
            f"{largest['title']} — "
            f"{largest['pages']} стор."
        )

    # ----------------------------------
    # Пошук за назвою
    # ----------------------------------

    search_title = "1984"

    found = find_book_by_title(
        books,
        search_title,
    )

    print(
        f"\nПошук книги "
        f"'{search_title}':"
    )

    print(found)

    # ----------------------------------
    # Фільтрація за роком
    # ----------------------------------

    recent_books = filter_by_year(
        books,
        1950,
    )

    print_books(
        "Книги, видані після 1950 року",
        recent_books,
    )

    # ----------------------------------
    # Фільтрація за автором
    # ----------------------------------

    orwell_books = filter_by_author(
        books,
        "George Orwell",
    )

    print_books(
        "Книги George Orwell",
        orwell_books,
    )

    # ----------------------------------
    # Сортування
    # ----------------------------------

    sorted_books = sort_books_by_year(
        books
    )

    print_books(
        "Книги, відсортовані за роком",
        sorted_books,
    )

    # ----------------------------------
    # Dict index
    # ----------------------------------

    book_index = create_book_index(
        books
    )

    print(
        "\nDict-index:"
    )

    print(
        "Книга з ID=3:",
        book_index.get(3),
    )

    # ----------------------------------
    # Closure
    # ----------------------------------

    is_recent = create_year_filter(
        2000
    )

    recent_via_closure = filter_books(
        books,
        is_recent,
    )

    print_books(
        "Фільтрація через Closure "
        "(рік >= 2000)",
        recent_via_closure,
    )

    # ----------------------------------
    # *args
    # ----------------------------------

    average_demo = calculate_average_values(
        200,
        300,
        400,
        500,
    )

    print(
        "\nСереднє через *args:",
        average_demo,
    )

    # ----------------------------------
    # **kwargs
    # ----------------------------------

    new_book = create_record(
        id=9,
        title="New Book",
        author="Test Author",
        year=2026,
        pages=250,
    )

    print(
        "\nСтворена книга через **kwargs:"
    )

    print(new_book)

    # ----------------------------------
    # Benchmark
    # ----------------------------------

    run_benchmark()


if __name__ == "__main__":
    main()
