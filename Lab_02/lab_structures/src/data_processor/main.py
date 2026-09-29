from src.data_processor.analytics import (

    calculate_average_pages,
    calculate_average_values,
    create_page_filter,
    create_record,
    find_largest_book,
    filter_items,
    get_page_statistics,
    sort_by_year,
)

from src.data_processor.benchmark import run_benchmark

from src.data_processor.data import books

from src.data_processor.processors import (
    count_books_by_author,
    create_book_index,
    get_books_by_author,
    get_unique_authors,
    group_books_by_author,
    search_book,
    filter_by_year,
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
            f"{book['title'][:40]:42} "
            f"{book['author'][:25]:27} "
            f"{book['year']:4} "
            f"{book['pages']:4}"
        )


def main() -> None:

    print_books(
        "All books",
        books,
    )

    # LIST
    print("\nLIST:")
    print(type(books))
    print(f"Number of books: {len(books)}")

    # TUPLE
    first_book_info = (
        books[0]["title"],
        books[0]["year"],
        books[0]["pages"],
    )

    print("\nTUPLE:")
    print(first_book_info)

    # SET
    authors = get_unique_authors(books)

    print("\nUnique authors:")
    for author in sorted(authors):
        print(author)

    # DICT
    index = create_book_index(books)

    print("\nDictionary index:")
    print(index[1])

    # SEARCH BY ID
    book_id = 5

    print("\nSearch by ID:")

    found_by_id = index.get(book_id)

    print(found_by_id)

    # SEARCH BY TITLE OR AUTHOR
    search_result = search_book(
        books,
        "Harry",
    )

    print_books(
        "Search result: Harry",
        search_result,
    )

    # FILTER BY YEAR
    filtered = filter_by_year(
        books,
        1900,
        1950,
    )

    print_books(
        "Books from 1900 to 1950",
        filtered,
    )

    # FIND LARGEST BOOK
    largest = find_largest_book(books)

    if largest:
        print("\nLargest book:")
        print(
            largest["title"],
            "-",
            largest["pages"],
            "pages",
        )

    # AVERAGE
    average_pages = calculate_average_pages(
        books
    )

    print(
        f"\nAverage number of pages: "
        f"{average_pages:.2f}"
    )

    # SORTING
    sorted_books = sort_by_year(
        books
    )

    print_books(
        "Books sorted by year",
        sorted_books,
    )

    # GROUPING
    grouped = group_books_by_author(
        books
    )

    print("\nBooks grouped by author:")
    print("-" * 50)

    for author, author_books in grouped.items():
        print(
            f"{author}: "
            f"{len(author_books)} book(s)"
        )

    # COUNTER
    counter = count_books_by_author(
        books
    )

    print("\nCounter books by author:")
    print(counter)

    # GET BOOKS BY AUTHOR
    author_books = get_books_by_author(
        books,
        "George Orwell",
    )

    print_books(
        "Books by George Orwell",
        author_books,
    )

    # LIST COMPREHENSION
    titles = [
        book["title"]
        for book in books
    ]

    print("\nList comprehension:")
    print(titles)

    # SET COMPREHENSION
    years = {
        book["year"]
        for book in books
    }

    print("\nSet comprehension:")
    print(sorted(years))

    # DICT COMPREHENSION
    pages_by_title = {
        book["title"]: book["pages"]
        for book in books
    }

    print("\nDict comprehension:")
    for title, pages in pages_by_title.items():
        print(
            f"{title}: {pages} pages"
        )

    # *ARGS
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

    # **KWARGS
    new_book = create_record(
        id=13,
        title="Clean Code",
        author="Robert C. Martin",
        year=2008,
        pages=464,
    )

    print("\nCreated via **kwargs:")
    print(new_book)

    # CLOSURE
    is_large_book = create_page_filter(
        400
    )

    large_books = filter_items(
        books,
        is_large_book,
    )

    print_books(
        "Books with 400 or more pages",
        large_books,
    )

    # TUPLE AGGREGATION
    minimum, maximum, average = (
        get_page_statistics(books)
    )

    print("\nPage statistics:")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", f"{average:.2f}")

    # BENCHMARK
    run_benchmark()


if __name__ == "__main__":
    main()