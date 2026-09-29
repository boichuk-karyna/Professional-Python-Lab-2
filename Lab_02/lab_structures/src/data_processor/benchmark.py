from time import perf_counter


def find_linear(
    books: list[dict],
    book_id: int,
) -> dict | None:

    for book in books:
        if book["id"] == book_id:
            return book

    return None


def benchmark(
    size: int,
) -> tuple[float, float, float]:

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

    book_index = {
        book["id"]: book
        for book in books
    }

    book_ids = {
        book["id"]
        for book in books
    }

    start = perf_counter()

    find_linear(
        books,
        target_id,
    )

    list_time = perf_counter() - start

    start = perf_counter()

    book_index.get(
        target_id
    )

    dict_time = perf_counter() - start

    start = perf_counter()

    target_id in book_ids

    set_time = perf_counter() - start

    return (
        list_time,
        dict_time,
        set_time,
    )


def run_benchmark() -> None:

    sizes = [
        1_000,
        10_000,
        100_000,
    ]

    print()
    print("BENCHMARK")
    print("-" * 80)

    print(
        f"{'Records':<15}"
        f"{'List O(n)':<20}"
        f"{'Dict O(1)':<20}"
        f"{'Set O(1)':<20}"
    )

    for size in sizes:

        list_time, dict_time, set_time = (
            benchmark(size)
        )

        print(
            f"{size:<15}"
            f"{list_time:<20.8f}"
            f"{dict_time:<20.8f}"
            f"{set_time:<20.8f}"
        )


if __name__ == "__main__":
    run_benchmark()
