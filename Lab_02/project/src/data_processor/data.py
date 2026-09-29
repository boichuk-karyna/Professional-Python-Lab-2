"""Data for Variant 2 — Library Book Analysis."""

books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "year": 1937,
        "pages": 310,
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "pages": 328,
    },
    {
        "id": 3,
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945,
        "pages": 112,
    },
    {
        "id": 4,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "year": 1997,
        "pages": 332,
    },
    {
        "id": 5,
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J. K. Rowling",
        "year": 1998,
        "pages": 352,
    },
    {
        "id": 6,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "pages": 432,
    },
    {
        "id": 7,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "pages": 281,
    },
    {
        "id": 8,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "pages": 180,
    },
    {
        "id": 9,
        "title": "The Catcher in the Rye",
        "author": "J. D. Salinger",
        "year": 1951,
        "pages": 234,
    },
    {
        "id": 10,
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "year": 1954,
        "pages": 1178,
    },
]

# Tuple — фіксовані розміри для benchmark.
BENCHMARK_SIZES = (1_000, 10_000, 100_000)
