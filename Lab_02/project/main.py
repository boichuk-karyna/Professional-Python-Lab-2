"""Main program for Variant 2 — Library Book Analysis."""

from data_processor.analytics import (
    aggregate_books,
    calculate_average_pages,
    calculate_average_values,
    create_record,
    create_year_filter,
    find_largest_book,
)
from data_processor.benchmark import run_benchmark
from data_processor.data import books
from data_processor.processors import (
    count_books_by_author,
    create_book_index,
    filter_by_year,
    get_unique_authors,
    group_books_by_author,
    find_book_by_id,
    find_book_by_title,
    sort_books,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:
    """Print books in a formatted table."""

    print(f"\n{title}")
    print("-" * 100)

    print(
        f"{'ID':<5}"
        f"{'Назва':<45}"
        f"{'Автор':<25}"
        f"{'Рік':<8}"
        f"{'Сторінки':<10}"
    )

    print("-" * 100)

    for book in items:
        print(
            f"{book['id']:<5}"
            f"{book['title'][:42]:<45}"
            f"{book['author'][:22]:<25}"
            f"{book['year']:<8}"
            f"{book['pages']:<10}"
        )


def main() -> None:
    print(
        "=== АНАЛІЗ СИСТЕМИ ОБЛІКУ КНИГ "
        "(ВАРІАНТ 2) ==="
    )

    # 1. Виведення всіх книг.
    print_books(
        "Усі книги",
        books,
    )

    # 2. Унікальні автори — set comprehension.
    authors = get_unique_authors(books)

    print(
        "\nУнікальні автори (Set):"
    )

    for author in sorted(authors):
        print(f"  - {author}")

    # 3. Середня кількість сторінок.
    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nСередня кількість сторінок: "
        f"{average_pages:.2f}"
    )

    # 4. Найбільша книга.
    largest = find_largest_book(books)

    if largest:
        print(
            "\nНайбільша книга:"
        )
        print(
            f"  {largest['title']} — "
            f"{largest['pages']} сторінок"
        )

    # 5. Пошук книги за ID.
    search_id = 5

    found_by_id = find_book_by_id(
        books,
        search_id,
    )

    print(
        f"\nПошук книги за ID {search_id}:"
    )
    print(found_by_id)

    # 6. Пошук книги за назвою.
    search_title = "1984"

    found_by_title = find_book_by_title(
        books,
        search_title,
    )

    print(
        f"\nПошук книги за назвою "
        f"'{search_title}':"
    )
    print(found_by_title)

    # 7. Фільтрація за роком.
    filtered_books = filter_by_year(
        books,
        1900,
        2000,
    )

    print_books(
        "Книги, видані з 1900 по 2000 рік",
        filtered_books,
    )

    # 8. Сортування за роком.
    sorted_books = sort_books(
        books,
        key=lambda book: book["year"],
    )

    print_books(
        "Книги, відсортовані за роком",
        sorted_books,
    )

    # 9. Групування за авторами.
    grouped = group_books_by_author(
        books
    )

    print(
        "\nГрупування книг за авторами:"
    )

    for author, author_books in grouped.items():
        print(
            f"  - {author}: "
            f"{len(author_books)} книга(и)"
        )

    # 10. Counter.
    author_counter = count_books_by_author(
        books
    )

    print(
        "\nCounter книг за авторами:"
    )

    for author, count in author_counter.items():
        print(
            f"  - {author}: {count}"
        )

    # 11. Dict index.
    index = create_book_index(books)

    print(
        "\nDict-index за ID:"
    )
    print(
        f"Ключ 5 -> {index.get(5)}"
    )

    # 12. Closure.
    is_recent_book = create_year_filter(
        1950
    )

    recent_books = [
        book
        for book in books
        if is_recent_book(book)
    ]

    print_books(
        "Книги після 1950 року "
        "(Closure)",
        recent_books,
    )

    # 13. *args.
    demo_average = calculate_average_values(
        200,
        300,
        400,
        500,
    )

    print(
        "\nСереднє через *args:"
    )
    print(
        f"  {demo_average:.2f}"
    )

    # 14. **kwargs.
    new_book = create_record(
        id=11,
        title="Python Programming",
        author="John Smith",
        year=2024,
        pages=500,
    )

    print(
        "\nСтворений запис через **kwargs:"
    )
    print(new_book)

    # 15. Агрегація.
    summary = aggregate_books(
        books
    )

    print(
        "\nСтатистика бібліотеки:"
    )

    print(
        f"  Кількість книг: "
        f"{summary['count']}"
    )

    print(
        f"  Загальна кількість сторінок: "
        f"{summary['total_pages']}"
    )

    print(
        f"  Середня кількість сторінок: "
        f"{summary['average_pages']:.2f}"
    )

    print(
        f"  Найстарший рік: "
        f"{summary['min_year']}"
    )

    print(
        f"  Найновіший рік: "
        f"{summary['max_year']}"
    )

    # 16. Benchmark.
    run_benchmark()


if __name__ == "__main__":
    main()
