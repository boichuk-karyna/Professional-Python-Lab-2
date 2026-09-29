from time import perf_counter


def find_linear(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Linear O(n) search."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def benchmark(
    size: int,
    repetitions: int = 1000,
) -> tuple[float, float, float]:
    """
    Compare list, dict and set lookup.
    """

    books = [
        {
            "id": i,
            "title": f"Book {i}",
            "author": f"Author {i % 100}",
            "year": 2000 + i % 25,
            "pages": 100 + i % 500,
        }
        for i in range(size)
    ]

    index = {
        book["id"]: book
        for book in books
    }

    ids = {
        book["id"]
        for book in books
    }

    book_id = size - 1

    start = perf_counter()

    for _ in range(repetitions):
        find_linear(
            books,
            book_id,
        )

    list_time = perf_counter() - start

    start = perf_counter()

    for _ in range(repetitions):
        index.get(book_id)

    dict_time = perf_counter() - start

    start = perf_counter()

    for _ in range(repetitions):
        book_id in ids

    set_time = perf_counter() - start

    return (
        list_time,
        dict_time,
        set_time,
    )


def run_benchmark() -> None:
    """Run benchmark."""

    sizes = (
        1000,
        10000,
        100000,
    )

    print("\nBenchmark")
    print("-" * 75)

    print(
        f"{'Records':<15}"
        f"{'List O(n)':<20}"
        f"{'Dict O(1)':<20}"
        f"{'Set O(1)':<20}"
    )

    for size in sizes:

        (
            list_time,
            dict_time,
            set_time,
        ) = benchmark(size)

        print(
            f"{size:<15}"
            f"{list_time:<20.8f}"
            f"{dict_time:<20.8f}"
            f"{set_time:<20.8f}"
        )
