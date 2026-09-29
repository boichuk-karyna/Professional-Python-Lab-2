"""Processing functions for Variant 2 — Library Book Analysis."""

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
    """Create dictionary index by book ID."""

    return {
        book["id"]: book
        for book in books
    }


def create_title_index(
    books: list[dict],
) -> dict[str, dict]:
    """Create dictionary index by normalized title."""

    return {
        book["title"].strip().lower(): book
        for book in books
    }


def find_book_by_id(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Search a book by ID in a list. O(n)."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def find_book_by_index(
    index: dict[int, dict],
    book_id: int,
) -> dict | None:
    """Search a book by ID in dictionary index. O(1) average."""

    return index.get(book_id)


def find_book_by_title(
    books: list[dict],
    title: str,
) -> dict | None:
    """Search a book by title."""

    wanted = title.strip().lower()

    for book in books:
        if book["title"].strip().lower() == wanted:
            return book

    return None


def filter_by_author(
    books: list[dict],
    author: str,
) -> list[dict]:
    """Filter books by author."""

    wanted = author.strip().lower()

    return [
        book
        for book in books
        if book["author"].strip().lower() == wanted
    ]


def filter_by_year(
    books: list[dict],
    start_year: int,
    end_year: int | None = None,
) -> list[dict]:
    """Filter books by publication year."""

    if end_year is None:
        return [
            book
            for book in books
            if book["year"] == start_year
        ]

    if start_year > end_year:
        raise ValueError(
            "start_year must not be greater than end_year"
        )

    return [
        book
        for book in books
        if start_year <= book["year"] <= end_year
    ]


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Universal higher-order filtering function."""

    return [
        item
        for item in items
        if predicate(item)
    ]


def group_books_by_author(
    books: list[dict],
) -> dict[str, list[dict]]:
    """Group books by author using defaultdict."""

    grouped = defaultdict(list)

    for book in books:
        grouped[book["author"]].append(book)

    return dict(grouped)


def count_books_by_author(
    books: list[dict],
) -> Counter:
    """Count books by author using Counter."""

    return Counter(
        book["author"]
        for book in books
    )


def sort_books(
    books: list[dict],
    key: Callable[[dict], object] | None = None,
    reverse: bool = False,
) -> list[dict]:
    """Universal sorting function."""

    if key is None:
        key = lambda book: book["year"]

    return sorted(
        books,
        key=key,
        reverse=reverse,
    )
