from src.data_processor.analytics import (
    aggregate_books,
    calculate_average_pages,
    compose,
    get_top_n,
)
from src.data_processor.benchmark import run_benchmark
from src.data_processor.data import books
from src.data_processor.processors import (
    calculate_average_values,
    count_books_by_author,
    create_book_index,
    create_record,
    create_title_index,
    create_year_filter,
    filter_books,
    filter_by_year,
    find_book_by_id,
    find_book_by_title,
    find_book_in_index,
    find_largest_book,
    get_page_statistics,
    get_unique_authors,
    group_books_by_author,
    sort_by_pages,
    sort_by_year,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:
    print(f"\n{title}")
    print("-" * 80)

    for book in items:
        print(
            f"{book['id']:3} "
            f"{book['title'][:30]:30} "
            f"{book['author'][:20]:20} "
            f"{book['year']:4} "
            f"{book['pages']:5}"
        )


def main() -> None:
    print_books(
        "All books",
        books,
    )

    authors = get_unique_authors(books)
    print("\nUnique authors:")
    print(authors)

    average = calculate_average_pages(books)
    print(
        f"\nAverage pages: {average:.2f}"
    )

    largest = find_largest_book(books)

    if largest:
        print(
            "\nLargest book:",
            largest["title"],
            largest["pages"],
        )

    sorted_books = sort_by_year(books)

    print_books(
        "Sorted by year",
        sorted_books,
    )

    recent_books = filter_by_year(
        books,
        2019,
    )

    print_books(
        "Books from 2019+",
        recent_books,
    )

    grouped = group_books_by_author(books)

    print("\nBooks grouped by author:")

    for author, author_books in grouped.items():
        print(
            author,
            "->",
            len(author_books),
        )

    counter = count_books_by_author(books)

    print("\nCounter:")
    print(counter)

    index = create_book_index(books)

    print(
        "\nSearch by ID:",
        find_book_in_index(index, 4),
    )

    print(
        "\nLinear search:",
        find_book_by_id(books, 2),
    )

    print(
        "\nSearch by title:",
        find_book_by_title(
            books,
            "Clean Code",
        ),
    )

    title_index = create_title_index(books)

    print(
        "\nTitle index:",
        title_index.get("Python Basics"),
    )

    top_books = get_top_n(
        books,
        3,
    )

    print_books(
        "Top 3 books by pages",
        top_books,
    )

    aggregation = aggregate_books(books)

    print("\nAggregation:")
    print(aggregation)

    statistics = get_page_statistics(books)

    print(
        "\nPage statistics tuple:",
        statistics,
    )

    is_recent = create_year_filter(2019)

    recent = filter_books(
        books,
        is_recent,
    )

    print_books(
        "Closure filter: year >= 2019",
        recent,
    )

    excellent_pages = filter_books(
        books,
        lambda book: book["pages"] >= 500,
    )

    print_books(
        "Lambda filter: pages >= 500",
        excellent_pages,
    )

    pipeline = compose(
        lambda items: filter_by_year(
            items,
            2015,
        ),
        lambda items: sort_by_pages(
            items,
            reverse=True,
        ),
    )

    pipeline_result = pipeline(books)

    print_books(
        "Function composition pipeline",
        pipeline_result,
    )

    average_demo = calculate_average_values(
        100,
        200,
        300,
    )

    print(
        "\nAverage via *args:",
        average_demo,
    )

    record = create_record(
        id=100,
        title="Demo Book",
        author="Demo Author",
        year=2026,
        pages=200,
    )

    print(
        "\nRecord via **kwargs:",
        record,
    )

    run_benchmark()


if __name__ == "__main__":
    main()
