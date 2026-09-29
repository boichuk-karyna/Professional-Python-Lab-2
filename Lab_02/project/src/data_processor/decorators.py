"""Decorators used in the project."""

from functools import wraps
from time import perf_counter


def measure_time(func):
    """Decorator for measuring function execution time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        result = func(
            *args,
            **kwargs,
        )

        elapsed = perf_counter() - start

        print(
            f"[BENCHMARK] "
            f"Функція '{func.__name__}' "
            f"виконалась за {elapsed:.8f} с"
        )

        return result

    return wrapper
