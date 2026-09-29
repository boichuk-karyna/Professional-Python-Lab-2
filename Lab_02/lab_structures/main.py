from src.data_processor.analytics import (
    aggregate_books,
    calculate_average_pages,
    calculate_average_values,
    calculate_page_statistics,
    compose,
    create_page_filter,
    create_record,
)

from src.data_processor.data import books

from src.data_processor.processors import (
    count_books_by_author,
    create_book_index,
    filter_by_pages,
    filter_by_year,
    find_book_by_id,
    find_book_by_title,
    find_largest_book,
    get_unique_authors,
    group_books_by_author,
    sort_by_pages,
    sort_by_year,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:

    print()
    print(title)
    print("-" * 80)

    for book in items:
        print(
            f"{book['id']:2} | "
            f"{book['title'][:35]:35} | "
            f"{book['author'][:20]:20} | "
            f"{book['year']:4} | "
            f"{book['pages']:4}"
        )


def main() -> None:

    print_books(
        "ALL BOOKS",
        books,
    )

    authors = get_unique_authors(
        books
    )

    print(
        "\nUnique authors:",
        authors,
    )

    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nAverage pages: "
        f"{average_pages:.2f}"
    )

    largest = find_largest_book(
        books
    )

    print(
        "\nLargest book:",
        largest,
    )

    recent_books = filter_by_year(
        books,
        minimum_year=2015,
    )

    print_books(
        "BOOKS FROM 2015",
        recent_books,
    )

    large_books = filter_by_pages(
        books,
        minimum_pages=500,
    )

    print_books(
        "BOOKS WITH 500+ PAGES",
        large_books,
    )

    sorted_books = sort_by_year(
        books
    )

    print_books(
        "SORTED BY YEAR",
        sorted_books,
    )

    grouped = group_books_by_author(
        books
    )

    print("\nGROUPED BY AUTHOR")

    for author, author_books in grouped.items():
        print(
            f"{author}: "
            f"{len(author_books)} book(s)"
        )

    counter = count_books_by_author(
        books
    )

    print(
        "\nCounter:",
        counter,
    )

    book_index = create_book_index(
        books
    )

    print(
        "\nSearch by ID:",
        book_index.get(5),
    )

    print(
        "\nSearch by ID using function:",
        find_book_by_id(
            books,
            5,
        ),
    )

    print(
        "\nSearch by title:",
        find_book_by_title(
            books,
            "Clean Code",
        ),
    )

    page_statistics = calculate_page_statistics(
        books
    )

    print(
        "\nPage statistics:",
        page_statistics,
    )

    demo_average = calculate_average_values(
        100,
        200,
        300,
    )

    print(
        "\nAverage using *args:",
        demo_average,
    )

    new_book = create_record(
        id=100,
        title="Demo Book",
        author="Demo Author",
        year=2026,
        pages=300,
    )

    print(
        "\nRecord using **kwargs:",
        new_book,
    )

    is_large = create_page_filter(
        500
    )

    large_by_closure = [
        book
        for book in books
        if is_large(book)
    ]

    print_books(
        "FILTER USING CLOSURE",
        large_by_closure,
    )

    pipeline = compose(
        lambda data: filter_by_year(
            data,
            2010,
        ),
        sort_by_pages,
    )

    pipeline_result = pipeline(
        books
    )

    print_books(
        "COMPOSE PIPELINE",
        pipeline_result,
    )

    aggregation = aggregate_books(
        books
    )

    print(
        "\nAGGREGATION"
    )

    print(
        "Count:",
        aggregation["count"],
    )

    print(
        "Sum pages:",
        aggregation["sum_pages"],
    )

    print(
        "Average pages:",
        aggregation["average_pages"],
    )

    print(
        "Author statistics:",
        aggregation["author_stats"],
    )


if __name__ == "__main__":
    main()
