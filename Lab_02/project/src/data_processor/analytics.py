from collections import deque
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
    """
    Create a closure that remembers year boundaries.
    """

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
    """Create a closure for filtering books by page count."""

    def predicate(book: dict) -> bool:
        return book["pages"] >= minimum_pages

    return predicate


def build_summary(
    books: list[dict],
    **options,
) -> dict:
    """Build summary using keyword configuration."""

    result = {
        "total_books": len(books),
        "total_pages": sum(
            book["pages"]
            for book in books
        ),
        "average_pages": calculate_average_pages(books),
    }

    if options.get("include_authors", False):
        result["authors"] = {
            book["author"]
            for book in books
        }

    if options.get("include_years", False):
        result["years"] = {
            book["year"]
            for book in books
        }

    return result


class OperationHistory:
    """Store recent operations using deque."""

    def __init__(
        self,
        max_length: int = 5,
    ) -> None:
        self.history = deque(
            maxlen=max_length
        )

    def add(
        self,
        operation: str,
    ) -> None:
        self.history.append(operation)

    def get_all(self) -> list[str]:
        return list(self.history)
