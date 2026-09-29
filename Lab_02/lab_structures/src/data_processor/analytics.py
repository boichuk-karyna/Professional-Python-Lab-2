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


def calculate_author_statistics(
    books: list[dict],
) -> dict[str, dict[str, float]]:
    result = {}

    authors = {
        book["author"]
        for book in books
    }

    for author in authors:
        author_books = [
            book
            for book in books
            if book["author"] == author
        ]

        result[author] = {
            "count": len(author_books),
            "average_pages": sum(
                book["pages"]
                for book in author_books
            ) / len(author_books),
        }

    return result


def process_pipeline(
    books: list[dict],
    *operations: Callable[[list[dict]], list[dict]],
) -> list[dict]:
    result = books

    for operation in operations:
        result = operation(result)

    return result