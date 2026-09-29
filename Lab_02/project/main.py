from data_processor.analytics import (
    OperationHistory,
    build_summary,
    calculate_average_pages,
    calculate_average_values,
    create_page_filter,
    create_record,
    create_year_filter,
    find_largest_book,
    sort_by_year,
)

from data_processor.data import (
    BENCHMARK_SIZES,
    books,
)

from data_processor.processors import (
    count_books_by_author,
    create_book_index,
    create_title_index,
    filter_by_year,
    filter_items,
    find_book_by_id,
    find_book_by_title,
    get_unique_authors,
    group_books_by_author,
    sort_books,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:
    """Print books in a readable table."""

    print(f"\n{title}")
    print("-" * 90)

    for book in items:
        print(
            f"{book['id']:3} | "
            f"{book['title'][:42]:42} | "
            f"{book['author'][:22]:22} | "
            f"{book['year']:4} | "
            f"{book['pages']:4}"
        )


def generate_large_dataset(
    size: int,
) -> list[dict]:
    """Generate a large dataset for benchmarking."""

    return [
        {
            "id": index,
            "title": f"Book {index}",
            "author": f"Author {index % 100}",
            "year": 1900 + index % 125,
            "pages": 100 + index % 900,
        }
        for index in range(1, size + 1)
    ]


def benchmark_search(
    size: int,
) -> tuple[float, float]:
    """
    Compare linear list search with dict lookup.
    """

    from time import perf_counter

    data = generate_large_dataset(size)

    target_id = size

    start = perf_counter()

    find_book_by_id(
        data,
        target_id,
    )

    list_time = perf_counter() - start

    start = perf_counter()

    index = create_book_index(data)

    index.get(target_id)

    dict_time = perf_counter() - start

    return list_time, dict_time


def run_benchmark() -> None:
    """Run list vs dict benchmark."""

    print("\nBENCHMARK: list search vs dict search")
    print("-" * 70)

    print(
        f"{'Records':>12} | "
        f"{'List search':>15} | "
        f"{'Dict search':>15}"
    )

    print("-" * 70)

    for size in BENCHMARK_SIZES:
        list_time, dict_time = benchmark_search(size)

        print(
            f"{size:12} | "
            f"{list_time:15.8f} | "
            f"{dict_time:15.8f}"
        )


def main() -> None:
    """Run the complete demonstration."""

    history = OperationHistory()

    print_books(
        "ALL BOOKS",
        books,
    )
    history.add("Printed all books")

    authors = get_unique_authors(books)

    print(
        "\nUNIQUE AUTHORS:"
    )

    for author in sorted(authors):
        print("-", author)

    history.add("Found unique authors")

    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nAVERAGE PAGES: "
        f"{average_pages:.2f}"
    )

    history.add("Calculated average pages")

    largest = find_largest_book(books)

    if largest:
        print(
            "\nLARGEST BOOK:"
        )
        print(
            f"{largest['title']} "
            f"({largest['pages']} pages)"
        )

    history.add("Found largest book")

    grouped = group_books_by_author(books)

    print(
        "\nBOOKS GROUPED BY AUTHOR:"
    )

    for author, author_books in grouped.items():
        print(
            f"{author}: "
            f"{len(author_books)} book(s)"
        )

    history.add("Grouped books by author")

    counter = count_books_by_author(books)

    print(
        "\nCOUNTER OF BOOKS BY AUTHOR:"
    )

    for author, count in counter.items():
        print(
            f"{author}: {count}"
        )

    history.add("Counted books by author")

    recent_books = filter_by_year(
        books,
        1950,
        2000,
    )

    print_books(
        "BOOKS PUBLISHED FROM 1950 TO 2000",
        recent_books,
    )

    history.add("Filtered books by year")

    sorted_books = sort_by_year(
        books
    )

    print_books(
        "BOOKS SORTED BY YEAR",
        sorted_books,
    )

    history.add("Sorted books by year")

    sorted_by_pages = sort_books(
        books,
        key=lambda book: book["pages"],
        reverse=True,
    )

    print_books(
        "BOOKS SORTED BY NUMBER OF PAGES",
        sorted_by_pages,
    )

    history.add("Sorted books by pages")

    book = find_book_by_id(
        books,
        3,
    )

    print(
        "\nSEARCH BY ID = 3:"
    )
    print(book)

    history.add("Searched book by ID")

    book = find_book_by_title(
        books,
        "1984",
    )

    print(
        "\nSEARCH BY TITLE = 1984:"
    )
    print(book)

    history.add("Searched book by title")

    index = create_book_index(
        books
    )

    print(
        "\nDICT INDEX SEARCH:"
    )
    print(
        index.get(10)
    )

    title_index = create_title_index(
        books
    )

    print(
        "\nTITLE INDEX SEARCH:"
    )
    print(
        title_index.get(
            "the hobbit"
        )
    )

    year_filter = create_year_filter(
        1950,
        2000,
    )

    books_from_closure = filter_items(
        books,
        year_filter,
    )

    print_books(
        "CLOSURE FILTER: 1950-2000",
        books_from_closure,
    )

    page_filter = create_page_filter(
        300
    )

    long_books = filter_items(
        books,
        page_filter,
    )

    print_books(
        "CLOSURE FILTER: 300+ PAGES",
        long_books,
    )

    average_demo = calculate_average_values(
        200,
        300,
        400,
        500,
    )

    print(
        "\nAVERAGE USING *args:",
        average_demo,
    )

    new_book = create_record(
        id=11,
        title="Dune",
        author="Frank Herbert",
        year=1965,
        pages=412,
    )

    print(
        "\nRECORD CREATED USING **kwargs:"
    )
    print(new_book)

    summary = build_summary(
        books,
        include_authors=True,
        include_years=True,
    )

    print(
        "\nSUMMARY:"
    )

    for key, value in summary.items():
        print(
            f"{key}: {value}"
        )

    print(
        "\nRECENT OPERATIONS:"
    )

    for operation in history.get_all():
        print("-", operation)

    run_benchmark()


if __name__ == "__main__":
    main()
