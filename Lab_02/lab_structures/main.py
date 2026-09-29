import random
from time import perf_counter

from book_processor.analytics import (
    calculate_average_pages,
    calculate_average_values,
    create_record,
    create_year_filter,
    filter_books,
    find_book_by_id,
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
    """Виведення книг у вигляді таблиці."""

    print(f"\n{title}")
    print("-" * 100)

    print(
        f"{'ID':<5}"
        f"{'Назва':<40}"
        f"{'Автор':<25}"
        f"{'Рік':<8}"
        f"{'Стор.':<8}"
    )

    print("-" * 100)

    for book in items:
        print(
            f"{book['id']:<5}"
            f"{book['title'][:37]:<40}"
            f"{book['author'][:22]:<25}"
            f"{book['year']:<8}"
            f"{book['pages']:<8}"
        )


def find_linear(
    books_data: list[dict],
    book_id: int,
) -> dict | None:
    """Лінійний пошук книги у списку."""

    for book in books_data:
        if book["id"] == book_id:
            return book

    return None


def run_benchmark() -> None:
    """Порівняння пошуку у list та dict."""

    print(
        "\n--- ЕКСПЕРИМЕНТАЛЬНА ЧАСТИНА ---"
    )

    sizes = [
        1_000,
        10_000,
        100_000,
    ]

    print(
        f"\n{'Records':>10}"
        f"{'List search':>20}"
        f"{'Dict build':>20}"
        f"{'Dict search':>20}"
    )

    print("-" * 75)

    for size in sizes:
        test_books = [
            {
                "id": i,
                "title": f"Book {i}",
                "author": f"Author {i % 100}",
                "year": random.randint(
                    1900,
                    2025,
                ),
                "pages": random.randint(
                    100,
                    1000,
                ),
            }
            for i in range(size)
        ]

        target_id = size - 1

        # Пошук у list
        start = perf_counter()

        find_linear(
            test_books,
            target_id,
        )

        list_time = (
            perf_counter() - start
        )

        # Побудова dict
        start = perf_counter()

        index = {
            book["id"]: book
            for book in test_books
        }

        dict_build_time = (
            perf_counter() - start
        )

        # Пошук у dict
        start = perf_counter()

        index.get(target_id)

        dict_search_time = (
            perf_counter() - start
        )

        print(
            f"{size:>10}"
            f"{list_time:>20.8f}"
            f"{dict_build_time:>20.8f}"
            f"{dict_search_time:>20.8f}"
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
    # List
    # ----------------------------------

    print_books(
        "Усі книги",
        books,
    )

    # ----------------------------------
    # Set comprehension
    # ----------------------------------

    authors = get_unique_authors(
        books
    )

    print(
        "\nУнікальні автори:"
    )

    for author in sorted(authors):
        print(f"- {author}")

    # ----------------------------------
    # Average
    # ----------------------------------

    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nСередня кількість сторінок: "
        f"{average_pages:.2f}"
    )

    # ----------------------------------
    # Largest book
    # ----------------------------------

    largest = find_largest_book(
        books
    )

    if largest is not None:
        print(
            "\nНайбільша книга:"
        )
        print(
            f"{largest['title']} — "
            f"{largest['pages']} стор."
        )

    # ----------------------------------
    # Search by title
    # ----------------------------------

    search_title = "1984"

    found_by_title = find_book_by_title(
        books,
        search_title,
    )

    print(
        f"\nПошук за назвою "
        f"'{search_title}':"
    )

    print(found_by_title)

    # ----------------------------------
    # Search by ID
    # ----------------------------------

    found_by_id = find_book_by_id(
        books,
        3,
    )

    print(
        "\nПошук за ID = 3:"
    )

    print(found_by_id)

    # ----------------------------------
    # Filter by year
    # ----------------------------------

    books_after_1950 = filter_by_year(
        books,
        1950,
    )

    print_books(
        "Книги з 1950 року",
        books_after_1950,
    )

    # ----------------------------------
    # Filter by author
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
    # Sorting
    # ----------------------------------

    sorted_books = sort_books_by_year(
        books
    )

    print_books(
        "Сортування за роком видання",
        sorted_books,
    )

    # ----------------------------------
    # Grouping
    # ----------------------------------

    grouped = group_books_by_author(
        books
    )

    print(
        "\nГрупування за авторами:"
    )

    for author, author_books in grouped.items():
        print(
            f"{author}: "
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
    # Dict comprehension / index
    # ----------------------------------

    index = create_book_index(
        books
    )

    print(
        "\nDict-index:"
    )

    print(
        "Книга з ID=3:",
        index.get(3),
    )

    # ----------------------------------
    # Closure
    # ----------------------------------

    is_recent = create_year_filter(
        2000
    )

    recent_books = filter_books(
        books,
        is_recent,
    )

    print_books(
        "Closure: книги з 2000 року",
        recent_books,
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
