from functools import reduce
from collections.abc import Callable

from src.data_processor.decorators import measure_time


@measure_time
def calculate_average_pages(
    books: list[dict],
) -> float:
    """Calculate average pages."""

    if not books:
        return 0.0

    return sum(
        book["pages"]
        for book in books
    ) / len(books)


def aggregate_books(
    books: list[dict],
) -> dict:
    """
    Aggregate book statistics using reduce.
    """

    initial = {
        "count": 0,
        "sum_pages": 0,
        "author_sum": {},
        "author_count": {},
    }

    def reducer(
        accumulator: dict,
        book: dict,
    ) -> dict:

        author = book["author"]
        pages = book["pages"]

        accumulator["count"] += 1
        accumulator["sum_pages"] += pages

        accumulator["author_sum"][author] = (
            accumulator["author_sum"].get(
                author,
                0,
            )
            + pages
        )

        accumulator["author_count"][author] = (
            accumulator["author_count"].get(
                author,
                0,
            )
            + 1
        )

        return accumulator

    result = reduce(
        reducer,
        books,
        initial,
    )

    author_avg = {
        author: (
            result["author_sum"][author]
            / result["author_count"][author]
        )
        for author in result["author_sum"]
    }

    return {
        "count": result["count"],
        "sum_pages": result["sum_pages"],
        "author_avg": author_avg,
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


def build_processing_pipeline(
    minimum_year: int,
) -> Callable:
    """
    Build reusable pipeline.

    Closure remembers minimum_year.
    """

    def filter_by_year(
        books: list[dict],
    ) -> list[dict]:

        return [
            book.copy()
            for book in books
            if book["year"] >= minimum_year
        ]

    def sort_books(
        books: list[dict],
    ) -> list[dict]:

        return sorted(
            books,
            key=lambda book: (
                book["year"],
                book["title"],
            ),
        )

    return compose(
        filter_by_year,
        sort_books,
    )


def get_top_n(
    books: list[dict],
    n: int,
) -> list[dict]:
    """
    Return top N books by pages.
    """

    if n <= 0:
        return []

    sorted_books = sorted(
        books,
        key=lambda book: (
            -book["pages"],
            book["title"],
        ),
    )

    return [
        book.copy()
        for book in sorted_books[:n]
    ]


def calculate_summary(
    books: list[dict],
) -> dict:
    """Build complete summary."""

    aggregation = aggregate_books(books)

    return {
        "count": aggregation["count"],
        "sum_pages": aggregation["sum_pages"],
        "average_pages": (
            aggregation["sum_pages"]
            / aggregation["count"]
            if aggregation["count"]
            else 0.0
        ),
        "author_avg": aggregation["author_avg"],
    }
