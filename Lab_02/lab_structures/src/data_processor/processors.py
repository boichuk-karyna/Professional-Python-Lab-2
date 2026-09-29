from collections import Counter, defaultdict
from collections.abc import Callable


def get_unique_authors(
    books: list[dict],
) -> set[str]:
    """Return unique book authors."""

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
    """Create dictionary index by book title."""

    return {
        book["title"]: book
        for book in books
    }


def find_book_by_id(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Find book by ID."""

    index = create_book_index(books)

    return index.get(book_id)


def find_book_by_title(
    books: list[dict],
    title: str,
) -> dict | None:
    """Find book by title."""

    index = create_title_index(books)

    return index.get(title)


def filter_by_year(
    books: list[dict],
    minimum_year: int,
) -> list[dict]:
    """Return books published from minimum_year."""

    return list(
        filter(
            lambda book: book["year"] >= minimum_year,
            books,
        )
    )


def filter_by_pages(
    books: list[dict],
    minimum_pages: int,
) -> list[dict]:
    """Return books with enough pages."""

    return [
        book
        for book in books
        if book["pages"] >= minimum_pages
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


def sort_by_year(
    books: list[dict],
    reverse: bool = False,
) -> list[dict]:
    """Sort books by publication year."""

    return sorted(
        books,
        key=lambda book: (
            book["year"],
            book["title"],
        ),
        reverse=reverse,
    )


def sort_by_pages(
    books: list[dict],
    reverse: bool = True,
) -> list[dict]:
    """Sort books by number of pages."""

    return sorted(
        books,
        key=lambda book: (
            book["pages"],
            book["title"],
        ),
        reverse=reverse,
    )


def find_largest_book(
    books: list[dict],
) -> dict | None:
    """Find book with maximum number of pages."""

    if not books:
        return None

    return max(
        books,
        key=lambda book: book["pages"],
    )


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Universal filtering function."""

    return [
        item
        for item in items
        if predicate(item)
    ]


def sort_items(
    items: list[dict],
    key: Callable,
    reverse: bool = False,
) -> list[dict]:
    """Universal sorting function."""

    return sorted(
        items,
        key=key,
        reverse=reverse,
    )
