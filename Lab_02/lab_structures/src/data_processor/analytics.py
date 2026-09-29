from functools import reduce
from collections.abc import Callable

from src.data_processor.decorators import measure_time


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
    """Create dictionary using **kwargs."""

    return dict(fields)


def create_page_filter(
    minimum_pages: int,
) -> Callable[[dict], bool]:
    """
    Closure that remembers minimum_pages.
    """

    def predicate(book: dict) -> bool:
        return book["pages"] >= minimum_pages

    return predicate


def calculate_page_statistics(
    books: list[dict],
) -> tuple[int, int, float]:
    """
    Return minimum pages, maximum pages
    and average pages.
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


def aggregate_books(
    books: list[dict],
) -> dict:
    """
    Aggregate book statistics using reduce.

    Returns:
        count
        sum_pages
        average_pages
        author_stats
    """

    initial = {
        "count": 0,
        "sum_pages": 0,
        "author_count": {},
        "author_pages": {},
    }

    def reducer(
        accumulator: dict,
        book: dict,
    ) -> dict:

        author = book["author"]
        pages = book["pages"]

        accumulator["count"] += 1
        accumulator["sum_pages"] += pages

        accumulator["author_count"][author] = (
            accumulator["author_count"].get(author, 0)
            + 1
        )

        accumulator["author_pages"][author] = (
            accumulator["author_pages"].get(author, 0)
            + pages
        )

        return accumulator

    result = reduce(
        reducer,
        books,
        initial,
    )

    average_pages = (
        result["sum_pages"] / result["count"]
        if result["count"]
        else 0.0
    )

    author_stats = {
        author: {
            "count": result["author_count"][author],
            "average_pages": (
                result["author_pages"][author]
                / result["author_count"][author]
            ),
        }
        for author in result["author_count"]
    }

    return {
        "count": result["count"],
        "sum_pages": result["sum_pages"],
        "average_pages": average_pages,
        "author_stats": author_stats,
    }


def compose(
    *functions: Callable,
) -> Callable:
    """
    Compose functions from left to right.
    """

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline
