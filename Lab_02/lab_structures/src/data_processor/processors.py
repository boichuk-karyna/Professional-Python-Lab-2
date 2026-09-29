from collections import Counter, defaultdict


def get_unique_authors(books: list[dict]) -> set[str]:
    return {
        book["author"]
        for book in books
    }


def create_book_index(books: list[dict]) -> dict[int, dict]:
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