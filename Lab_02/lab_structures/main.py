from src.data_processor.analytics import (
    calculate_average_pages,
    calculate_average_values,
    calculate_author_statistics,
    create_page_filter,
    create_record,
    find_largest_book,
    get_page_statistics,
    process_pipeline,
    sort_by_year,
)

from src.data_processor.benchmark import run_benchmark

from src.data_processor.data import books

from src.data_processor.decorators import repeat

from src.data_processor.export import export_summary

from src.data_processor.processors import (
    count_books_by_author,
    create_book_index,
    create_operation_history,
    filter_by_year,
    filter_items,
    get_books_by_author,
    get_unique_authors,
    group_books_by_author,
    group_books_by_author_and_year,
    record_operation,
    search_book,
    sort_items,
)


def print_books(
    title: str,
    items: list[dict],
) -> None:

    print(f"\n{title}")
    print("-" * 100)

    for book in items:

        print(
            f"{book['id']:3} "
            f"{book['title'][:40]:42} "
            f"{book['author'][:25]:27} "
            f"{book['year']:4} "
            f"{book['pages']:4}"
        )


@repeat(1)
def print_program_title() -> None:
    print("=" * 100)
    print("BOOK DATA PROCESSOR")
    print("Variant 2 - Library Book Analysis")
    print("=" * 100)


def main() -> None:

    print_program_title()

    history = create_operation_history()

    print_books(
        "All books",
        books,
    )

    record_operation(
        history,
        "Displayed all books",
    )

    print("\nLIST:")
    print(type(books))
    print(f"Number of books: {len(books)}")

    first_book_info = (
        books[0]["title"],
        books[0]["year"],
        books[0]["pages"],
    )

    print("\nTUPLE:")
    print(first_book_info)

    authors = get_unique_authors(books)

    print("\nUnique authors:")
    for author in sorted(authors):
        print(author)

    record_operation(
        history,
        "Calculated unique authors",
    )

    index = create_book_index(books)

    print("\nDictionary index:")
    print(index[1])

    book_id = 5

    print("\nSearch by ID:")
    print(index.get(book_id))

    record_operation(
        history,
        f"Search by ID: {book_id}",
    )

    search_result = search_book(
        books,
        "Harry",
    )

    print_books(
        "Search result: Harry",
        search_result,
    )

    record_operation(
        history,
        "Search by title or author",
    )

    filtered = filter_by_year(
        books,
        1900,
        1950,
    )

    print_books(
        "Books from 1900 to 1950",
        filtered,
    )

    record_operation(
        history,
        "Filtered books by year",
    )

    largest = find_largest_book(books)

    if largest:

        print("\nLargest book:")
        print(
            largest["title"],
            "-",
            largest["pages"],
            "pages",
        )

    average_pages = calculate_average_pages(
        books,
    )

    print(
        f"\nAverage number of pages: "
        f"{average_pages:.2f}"
    )

    sorted_books = sort_by_year(
        books,
    )

    print_books(
        "Books sorted by year",
        sorted_books,
    )

    grouped = group_books_by_author(
        books,
    )

    print("\nBooks grouped by author:")
    print("-" * 60)

    for author, author_books in grouped.items():

        print(
            f"{author}: "
            f"{len(author_books)} book(s)"
        )

    counter = count_books_by_author(
        books,
    )

    print("\nCounter books by author:")
    print(counter)

    author_books = get_books_by_author(
        books,
        "George Orwell",
    )

    print_books(
        "Books by George Orwell",
        author_books,
    )

    titles = [
        book["title"]
        for book in books
    ]

    print("\nList comprehension:")
    print(titles)

    years = {
        book["year"]
        for book in books
    }

    print("\nSet comprehension:")
    print(sorted(years))

    pages_by_title = {
        book["title"]: book["pages"]
        for book in books
    }

    print("\nDict comprehension:")

    for title, pages in pages_by_title.items():

        print(
            f"{title}: {pages} pages"
        )

    demo_average = calculate_average_values(
        100,
        200,
        300,
        400,
    )

    print(
        "\nAverage via *args:",
        demo_average,
    )

    new_book = create_record(
        id=13,
        title="Clean Code",
        author="Robert C. Martin",
        year=2008,
        pages=464,
    )

    print("\nCreated via **kwargs:")
    print(new_book)

    is_large_book = create_page_filter(
        400,
    )

    large_books = filter_items(
        books,
        is_large_book,
    )

    print_books(
        "Books with 400 or more pages",
        large_books,
    )

    minimum, maximum, average = (
        get_page_statistics(books)
    )

    print("\nPage statistics:")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", f"{average:.2f}")

    author_statistics = calculate_author_statistics(
        books,
    )

    print("\nAuthor statistics:")

    for author, statistics in author_statistics.items():

        print(
            f"{author}: "
            f"{statistics['count']} book(s), "
            f"average pages = "
            f"{statistics['average_pages']:.2f}"
        )

    sorted_by_pages = sort_items(
        books,
        key=lambda book: book["pages"],
        reverse=True,
    )

    print_books(
        "Universal sorting by pages",
        sorted_by_pages,
    )

    pipeline_result = process_pipeline(
        books,
        lambda items: filter_by_year(
            items,
            1900,
            2000,
        ),
        lambda items: sort_items(
            items,
            key=lambda book: book["pages"],
            reverse=True,
        ),
    )

    print_books(
        "Pipeline result",
        pipeline_result,
    )

    nested_groups = group_books_by_author_and_year(
        books,
    )

    print("\nNested grouping by author and year:")

    for author, years_data in nested_groups.items():

        print(f"\n{author}:")

        for year, year_books in years_data.items():

            print(
                f"  {year}: "
                f"{len(year_books)} book(s)"
            )

    print("\nOperation history:")

    for operation in history:

        print(
            f"- {operation}"
        )

    summary = {
        "total_books": len(books),
        "unique_authors": len(authors),
        "average_pages": round(
            average_pages,
            2,
        ),
        "largest_book": {
            "title": largest["title"],
            "pages": largest["pages"],
        }
        if largest
        else None,
        "page_statistics": {
            "minimum": minimum,
            "maximum": maximum,
            "average": round(
                average,
                2,
            ),
        },
        "books_by_author": dict(counter),
    }

    export_summary(
        summary,
    )

    print(
        "\nSummary exported to summary.json"
    )

    run_benchmark()


if __name__ == "__main__":
    main()