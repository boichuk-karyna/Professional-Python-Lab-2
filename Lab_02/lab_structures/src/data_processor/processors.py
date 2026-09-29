from collections import Counter, defaultdict


def get_unique_authors(books: list[dict]) -> set[str]:
    """Set comprehension: отримання унікальних авторів."""

    return {
        book["author"]
        for book in books
    }


def create_book_index(books: list[dict]) -> dict[int, dict]:
    """Dict comprehension: створення індексу книг за ID."""

    return {
        book["id"]: book
        for book in books
    }


def filter_by_author(
    books: list[dict],
    author: str,
) -> list[dict]:
    """List comprehension: фільтрація книг за автором."""

    return [
        book
        for book in books
        if book["author"] == author
    ]


def filter_by_year(
    books: list[dict],
    min_year: int,
) -> list[dict]:
    """Фільтрація книг, виданих починаючи з певного року."""

    return [
        book
        for book in books
        if book["year"] >= min_year
    ]


def group_books_by_author(
    books: list[dict],
) -> dict[str, list[dict]]:
    """Групування книг за авторами через defaultdict."""

    result = defaultdict(list)

    for book in books:
        result[book["author"]].append(book)

    return dict(result)


def count_books_by_author(
    books: list[dict],
) -> Counter:
    """Counter для підрахунку кількості книг кожного автора."""

    return Counter(
        book["author"]
        for book in books
    )
