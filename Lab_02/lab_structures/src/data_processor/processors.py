from collections import Counter, defaultdict
from collections.abc import Callable


def get_unique_authors(
    books: list[dict],
) -> set[str]:
    """Return unique authors using set comprehension."""

    return {
        book["author"]
        for book in books
    }


def create_book_index(
    books: list[dict],
) -> dict[int, dict]:
    """Create O(1) average lookup index by ID."""

    return {
        book["id"]: book
        for book in books
    }


def create_title_index(
    books: list[dict],
) -> dict[str, dict]:
    """Create dictionary index by title."""

    return {
        book["title"]: book
        for book in books
    }


def find_book_by_id(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Linear search by ID."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def find_book_by_title(
    books: list[dict],
    title: str,
) -> dict | None:
    """Linear search by title."""

    for book in books:
        if book["title"] == title:
            return book

    return None


def find_book_in_index(
    index: dict[int, dict],
    book_id: int,
) -> dict | None:
    """Average O(1) lookup in dictionary."""

    return index.get(book_id)


def filter_by_year(
    books: list[dict],
    minimum_year: int,
) -> list[dict]:
    """Filter books by publication year."""

    return [
        book.copy()
        for book in books
        if book["year"] >= minimum_year
    ]


def create_year_filter(
    minimum_year: int,
) -> Callable[[dict], bool]:
    """
    Closure that remembers minimum_year.
    """

    def predicate(book: dict) -> bool:
        return book["year"] >= minimum_year

    return predicate


def filter_books(
    books: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Universal higher-order filtering function."""

    return [
        book.copy()
        for book in books
        if predicate(book)
    ]


def group_books_by_author(
    books: list[dict],
) -> dict[str, list[dict]]:
    """Group books using defaultdict."""

    grouped = defaultdict(list)

    for book in books:
        grouped[book["author"]].append(book.copy())

    return dict(grouped)


def count_books_by_author(
    books: list[dict],
) -> Counter:
    """Count books for every author."""

    return Counter(
        book["author"]
        for book in books
    )


def sort_by_year(
    books: list[dict],
    reverse: bool = False,
) -> list[dict]:
    """Sort books by publication year."""

    return sorted(
        (book.copy() for book in books),
        key=lambda book: (
            book["year"],
            book["title"],
        ),
        reverse=reverse,
    )


def sort_by_pages(
    books: list[dict],
    reverse: bool = True,
) -> list[dict]:
    """Sort books by page count."""

    return sorted(
        (book.copy() for book in books),
        key=lambda book: (
            -book["pages"],
            book["title"],
        ),
    ) if reverse else sorted(
        (book.copy() for book in books),
        key=lambda book: (
            book["pages"],
            book["title"],
        ),
    )


def find_largest_book(
    books: list[dict],
) -> dict | None:
    """Find book with the largest number of pages."""

    if not books:
        return None

    return max(
        books,
        key=lambda book: book["pages"],
    )


def calculate_average_pages(
    books: list[dict],
) -> float:
    """Calculate average page count."""

    if not books:
        return 0.0

    total_pages = sum(
        book["pages"]
        for book in books
    )

    return total_pages / len(books)


def calculate_average_values(
    *values: float,
) -> float:
    """Calculate average using *args."""

    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(
    **fields,
) -> dict:
    """Create a dictionary using **kwargs."""

    return dict(fields)


def get_page_statistics(
    books: list[dict],
) -> tuple[int, int, float]:
    """
    Return min pages, max pages and average pages.

    Tuple is used as an immutable result structure.
    """

    if not books:
        return (0, 0, 0.0)

    pages = [
        book["pages"]
        for book in books
    ]

    return (
        min(pages),
        max(pages),
        sum(pages) / len(pages),
    )


def process_pipeline(
    items: list[dict],
    *operations: Callable[[list[dict]], list[dict]],
) -> list[dict]:
    """
    Apply operations from left to right.

    This is a reusable function-composition pipeline.
    """

    result = [
        item.copy()
        for item in items
    ]

    for operation in operations:
        result = operation(result)

    return result
