from time import perf_counter


def find_linear(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book

    return None


def benchmark(size):
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

    book_id = size - 1

    index = {
        book["id"]: book
        for book in books
    }

    start = perf_counter()

    find_linear(
        books,
        book_id,
    )

    list_time = perf_counter() - start

    start = perf_counter()

    index.get(book_id)

    dict_time = perf_counter() - start

    return list_time, dict_time


def run_benchmark():
    sizes = [
        1000,
        10000,
        100000,
    ]

    print("\nBenchmark")
    print("-" * 60)
    print(
        f"{'Records':<15}"
        f"{'List search':<20}"
        f"{'Dict search':<20}"
    )

    for size in sizes:
        list_time, dict_time = benchmark(size)

        print(
            f"{size:<15}"
            f"{list_time:<20.8f}"
            f"{dict_time:<20.8f}"
        )