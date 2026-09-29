from collections.abc import Callable

from src.data_processor.decorators import measure_time


@measure_time
def calculate_average_pages(
    books: list[dict],
) -> float:
    if not books:
        return 0.0

    return sum(
        book["pages"]
        for book in books
    ) / len(books)


def find_largest_book(
    books: list[dict],
) -> dict | None:
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
    return sorted(
        books,
        key=lambda book: book["year"],
        reverse=reverse,
    )


def calculate_average_values(
    *values: float,
) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(
    **fields,
) -> dict:
    return dict(fields)


def create_page_filter(
    minimum_pages: int,
) -> Callable[[dict], bool]:

    def predicate(book: dict) -> bool:
        return book["pages"] >= minimum_pages

    return predicate


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:

    return [
        item
        for item in items
        if predicate(item)
    ]


def get_page_statistics(
    books: list[dict],
) -> tuple[int, int, float]:

    if not books:
        return 0, 0, 0.0

    pages = [
        book["pages"]
        for book in books
    ]

    return (
        min(pages),
        max(pages),
        sum(pages) / len(pages),
    )