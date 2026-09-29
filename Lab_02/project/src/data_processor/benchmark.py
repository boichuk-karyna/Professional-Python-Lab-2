"""Benchmark for list and dictionary search."""

from time import perf_counter

from data_processor.data import BENCHMARK_SIZES


def find_linear(
    books: list[dict],
    book_id: int,
) -> dict | None:
    """Linear search in list. Complexity O(n)."""

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def benchmark(
    size: int,
) -> tuple[float, float]:
    """Compare list search and dict search."""

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

    target_id = size - 1

    index = {
        book["id"]: book
        for book in books
    }

    start = perf_counter()

    find_linear(
        books,
        target_id,
    )

    list_time = perf_counter() - start

    start = perf_counter()

    index.get(target_id)

    dict_time = perf_counter() - start

    return list_time, dict_time


def run_benchmark() -> None:
    """Run benchmark for 1000, 10000 and 100000 records."""

    print("\n=== BENCHMARK ===")
    print("-" * 75)

    print(
        f"{'Records':<15}"
        f"{'List search O(n)':<25}"
        f"{'Dict search O(1)':<25}"
    )

    for size in BENCHMARK_SIZES:
        list_time, dict_time = benchmark(size)

        print(
            f"{size:<15}"
            f"{list_time:<25.8f}"
            f"{dict_time:<25.8f}"
        )
