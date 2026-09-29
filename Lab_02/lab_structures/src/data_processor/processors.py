from collections import Counter, defaultdict


def get_unique_authors(
    books: list[dict],
) -> set[str]:
    """Отримання множини унікальних авторів."""

    return {
        book["author"]
        for book in books
    }


def create_book_index(
    books: list[dict],
) -> dict[int, dict]:
    """Створення dict-індексу за ID книги."""

    return {
        book["id"]: book
        for book in books
    }


def filter_by_author(
    books: list[dict],
    author: str,
) -> list[dict]:
    """Фільтрація книг за автором."""

    return [
        book
        for book in books
        if book["author"] == author
    ]


def filter_by_year(
    books: list[dict],
    year: int,
) -> list[dict]:
    """Фільтрація книг за роком видання."""

    return [
        book
        for book in books
        if book["year"] >= year
    ]


def group_books_by_author(
    books: list[dict],
) -> dict[str, list[dict]]:
    """Групування книг за авторами."""

    result = defaultdict(list)

    for book in books:
        result[book["author"]].append(book)

    return dict(result)


def count_books_by_author(
    books: list[dict],
) -> Counter:
    """Підрахунок кількості книг кожного автора."""

    return Counter(
        book["author"]
        for book in books
    )
