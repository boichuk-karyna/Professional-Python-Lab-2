from collections import Counter, defaultdict, deque
from collections.abc import Callable


def get_unique_authors(
    books: list[dict],
) -> set[str]:
    return {
        book["author"]
        for book in books
    }


def create_book_index(
    books: list[dict],
) -> dict[int, dict]:
    return {
        book["id"]: book
        for book in books
    }


def filter_by_year(
    books: list[dict],
    start_year: int,
    end_year: int,
) -> list[dict]:
    return [
        book
        for book in books
        if start_year <= book["year"] <= end_year
    ]


def search_book(
    books: list[dict],
    query: str,
) -> list[dict]:
    query = query.lower()

    return [
        book
        for book in books
        if query in book["title"].lower()
        or query in book["author"].lower()
    ]


def group_books_by_author(
    books: list[dict],
) -> dict[str, list[dict]]:
    result = defaultdict(list)

    for book in books:
        result[book["author"]].append(book)

    return dict(result)


def count_books_by_author(
    books: list[dict],
) -> Counter:
    return Counter(
        book["author"]
        for book in books
    )


def get_books_by_author(
    books: list[dict],
    author: str,
) -> list[dict]:
    return [
        book
        for book in books
        if book["author"] == author
    ]


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    return [
        item
        for item in items
        if predicate(item)
    ]


def sort_items(
    items: list[dict],
    key: Callable[[dict], object],
    reverse: bool = False,
) -> list[dict]:
    return sorted(
        items,
        key=key,
        reverse=reverse,
    )


def group_books_by_author_and_year(
    books: list[dict],
) -> dict[str, dict[int, list[dict]]]:
    result = defaultdict(lambda: defaultdict(list))

    for book in books:
        result[book["author"]][book["year"]].append(book)

    return {
        author: dict(years)
        for author, years in result.items()
    }


def create_operation_history(
    max_size: int = 10,
) -> deque[str]:
    return deque(maxlen=max_size)


def record_operation(
    history: deque[str],
    operation: str,
) -> None:
    history.append(operation)