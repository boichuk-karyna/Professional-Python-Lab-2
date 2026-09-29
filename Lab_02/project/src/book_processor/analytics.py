from collections.abc import Callable

from book_processor.decorators import measure_time


@measure_time
def calculate_average_pages(
    books: list[dict],
) -> float:
    """Обчислення середньої кількості сторінок."""

    if not books:
        return 0.0

    return (
        sum(
            book["pages"]
            for book in books
        )
        / len(books)
    )


def find_book_by_title(
    books: list[dict],
    title: str,
) -> dict | None:
    """Пошук книги за назвою."""

    for book in books:
        if book["title"].lower() == title.lower():
            return book

    return None


def find_book_by_id(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Пошук книги за ID."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def find_largest_book(
    books: list[dict],
) -> dict | None:
    """Пошук найбільшої книги за кількістю сторінок."""

    if not books:
        return None

    return max(
        books,
        key=lambda book: book["pages"],
    )


def sort_books_by_year(
    books: list[dict],
    reverse: bool = False,
) -> list[dict]:
    """Сортування книг за роком видання."""

    return sorted(
        books,
        key=lambda book: book["year"],
        reverse=reverse,
    )


def calculate_average_values(
    *values: float,
) -> float:
    """Демонстрація *args."""

    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(
    **fields,
) -> dict:
    """Демонстрація **kwargs."""

    return dict(fields)


def create_year_filter(
    minimum_year: int,
) -> Callable[[dict], bool]:
    """Closure для фільтрації книг за роком."""

    def predicate(book: dict) -> bool:
        return book["year"] >= minimum_year

    return predicate


def filter_books(
    books: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Універсальна функція фільтрації."""

    return [
        book
        for book in books
        if predicate(book)
    ]
