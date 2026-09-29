from collections import Counter, defaultdict
from collections.abc import Callable


def get_unique_authors(
    books: list[dict],
) -> set[str]:
    """Return a set of unique authors."""

    return {
        book["author"]
        for book in books
    }


def create_book_index(
    books: list[dict],
) -> dict[int, dict]:
    """Create O(1)-average lookup index by book ID."""

    return {
        book["id"]: book
        for book in books
    }


def create_title_index(
    books: list[dict],
) -> dict[str, dict]:
    """Create lookup index by title."""

    return {
        book["title"].lower(): book
        for book in books
    }


def find_book_by_id(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Linear search for a book by ID."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def find_book_by_title(
    books: list[dict],
    title: str,
) -> dict | None:
    """Linear search for a book by title."""

    normalized_title = title.strip().lower()

    for book in books:
        if book["title"].lower() == normalized_title:
            return book

    return None


def filter_by_year(
    books: list[dict],
    start_year: int,
    end_year: int,
) -> list[dict]:
    """Filter books by publication year."""

    return [
        book
        for book in books
        if start_year <= book["year"] <= end_year
    ]


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Generic higher-order filtering function."""

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
    """Count books written by each author."""

    return Counter(
        book["author"]
        for book in books
    )


def sort_books(
    books: list[dict],
    key: Callable[[dict], object],
    reverse: bool = False,
) -> list[dict]:
    """Universal sorting function."""

    return sorted(
        books,
        key=key,
        reverse=reverse,
    )
