"""Decorators used in the project."""

from functools import wraps
from time import perf_counter
from typing import Any, Callable


def measure_time(func: Callable) -> Callable:
    """Measure execution time of a function."""

    @wraps(func)
    def wrapper(
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        start = perf_counter()

        result = func(
            *args,
            **kwargs,
        )

        elapsed = perf_counter() - start

        print(
            f"[TIMER] {func.__name__}: "
            f"{elapsed:.8f} s"
        )

        return result

    return wrapper
