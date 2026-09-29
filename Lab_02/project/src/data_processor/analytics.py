"""Analytical functions for Variant 2 — Library Book Analysis."""

from collections.abc import Callable

from data_processor.decorators import measure_time


@measure_time
def calculate_average_pages(
    books: list[dict],
) -> float:
    """Calculate average number of pages."""

    if not books:
        return 0.0

    return sum(
        book["pages"]
        for book in books
    ) / len(books)


def find_largest_book(
    books: list[dict],
) -> dict | None:
    """Find the book with the largest number of pages."""

    if not books:
        return None

    return max(
        books,
        key=lambda book: book["pages"],
    )


def sort_by_year(
    books: list[dict],
    reverse: bool = False,
) -> list[dict]:
    """Sort books by publication year."""

    return sorted(
        books,
        key=lambda book: book["year"],
        reverse=reverse,
    )


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


def create_year_filter(
    minimum_year: int,
    maximum_year: int | None = None,
) -> Callable[[dict], bool]:
    """Create a closure for filtering by publication year."""

    def predicate(book: dict) -> bool:
        if maximum_year is None:
            return book["year"] >= minimum_year

        return (
            minimum_year
            <= book["year"]
            <= maximum_year
        )

    return predicate


def create_page_filter(
    minimum_pages: int,
) -> Callable[[dict], bool]:
    """Create a closure for filtering by minimum pages."""

    def predicate(book: dict) -> bool:
        return book["pages"] >= minimum_pages

    return predicate


def aggregate_books(
    books: list[dict],
) -> dict:
    """Calculate aggregate statistics."""

    if not books:
        return {
            "count": 0,
            "total_pages": 0,
            "average_pages": 0.0,
            "min_year": None,
            "max_year": None,
        }

    total_pages = sum(
        book["pages"]
        for book in books
    )

    return {
        "count": len(books),
        "total_pages": total_pages,
        "average_pages": total_pages / len(books),
        "min_year": min(
            book["year"]
            for book in books
        ),
        "max_year": max(
            book["year"]
            for book in books
        ),
    }


def build_summary(
    books: list[dict],
    **options,
) -> dict:
    """Build summary using keyword options."""

    summary = aggregate_books(books)

    if options.get("include_authors", False):
        summary["authors"] = {
            book["author"]
            for book in books
        }

    if options.get("include_years", False):
        summary["years"] = {
            book["year"]
            for book in books
        }

    return summary


def process_books(
    books: list[dict],
    predicate: Callable[[dict], bool] | None = None,
) -> list[dict]:
    """Process books using an optional predicate."""

    if predicate is None:
        return list(books)

    return [
        book
        for book in books
        if predicate(book)
    ]
