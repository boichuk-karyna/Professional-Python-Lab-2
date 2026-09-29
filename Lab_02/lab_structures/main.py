from src.data_processor.analytics import (
    aggregate_books,
    build_processing_pipeline,
    calculate_average_pages,
    calculate_summary,
    get_top_n,
)
from src.data_processor.benchmark import (
    run_benchmark,
)
from src.data_processor.data import books
from src.data_processor.decorators import (
    repeat,
)
from src.data_processor.export import (
    export_summary,
)
from src.data_processor.processors import (
    calculate_average_values,
    count_books_by_author,
    create_book_index,
    create_record,
    create_title_index,
    create_year_filter,
    filter_books,
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
    """Print books."""

    print(f"\n{title}")
    print("-" * 80)

    for book in items:
        print(
            f"{book['id']:2} | "
            f"{book['title']:<30} | "
            f"{book['author']:<20} | "
            f"{book['year']} | "
            f"{book['pages']} pages"
        )


@repeat(1)
def show_message() -> None:
    """Demonstrate parameterized decorator."""

    print("\nLab_02 - Variant 2")


def main() -> None:

    show_message()

    print_books(
        "All books",
        books,
    )

    authors = get_unique_authors(books)

    print(
        "\nUnique authors:",
        authors,
    )

    index = create_book_index(books)

    title_index = create_title_index(books)

    print(
        "\nBook index:",
        index,
    )

    found_by_id = find_book_by_id(
        books,
        4,
    )

    print(
        "\nSearch by ID:",
        found_by_id,
    )

    found_by_title = find_book_by_title(
        books,
        "Clean Code",
    )

    print(
        "\nSearch by title:",
        found_by_title,
    )

    found_in_index = find_book_in_index(
        index,
        5,
    )

    print(
        "\nDictionary search:",
        found_in_index,
    )

    filtered = filter_books(
        books,
        create_year_filter(2019),
    )

    print_books(
        "Books from 2019",
        filtered,
    )

    grouped = group_books_by_author(
        books,
    )

    print("\nBooks grouped by author:")

    for author, author_books in grouped.items():
        print(
            author,
            "->",
            len(author_books),
        )

    counter = count_books_by_author(
        books,
    )

    print(
        "\nCounter:",
        counter,
    )

    sorted_books = sort_by_year(
        books,
    )

    print_books(
        "Sorted by year",
        sorted_books,
    )

    sorted_pages = sort_by_pages(
        books,
    )

    print_books(
        "Sorted by pages",
        sorted_pages,
    )

    largest = find_largest_book(
        books,
    )

    print(
        "\nLargest book:",
        largest,
    )

    average = calculate_average_pages(
        books,
    )

    print(
        f"\nAverage pages: {average:.2f}"
    )

    stats = get_page_statistics(
        books,
    )

    print(
        "\nPage statistics tuple:",
        stats,
    )

    average_args = calculate_average_values(
        300,
        500,
        700,
        900,
    )

    print(
        "\nAverage using *args:",
        average_args,
    )

    record = create_record(
        id=100,
        title="Test Book",
        author="Test Author",
        year=2026,
        pages=200,
    )

    print(
        "\nRecord using **kwargs:",
        record,
    )

    top_books = get_top_n(
        books,
        3,
    )

    print_books(
        "Top 3 books by pages",
        top_books,
    )

    aggregation = aggregate_books(
        books,
    )

    print(
        "\nAggregation:",
        aggregation,
    )

    summary = calculate_summary(
        books,
    )

    print(
        "\nSummary:",
        summary,
    )

    pipeline = build_processing_pipeline(
        2019,
    )

    pipeline_result = pipeline(books)

    print_books(
        "Pipeline: year >= 2019, sorted by year",
        pipeline_result,
    )

    universal_filter = filter_books(
        books,
        lambda book: book["pages"] >= 500,
    )

    print_books(
        "Universal filter: pages >= 500",
        universal_filter,
    )

    exported = {
        **summary,
        "unique_authors": sorted(authors),
        "counter": dict(counter),
    }

    export_summary(
        exported,
        "summary.json",
    )

    print(
        "\nSummary exported to summary.json"
    )

    run_benchmark()


if __name__ == "__main__":
    main()
