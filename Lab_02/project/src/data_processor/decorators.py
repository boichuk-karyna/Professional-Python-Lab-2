from functools import wraps
from time import perf_counter
from typing import Callable, Any


def measure_time(func: Callable) -> Callable:
    """Measure execution time of a function."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()

        result = func(*args, **kwargs)

        elapsed = perf_counter() - start

        print(
            f"[TIMER] {func.__name__}: "
            f"{elapsed:.8f} s"
        )

        return result

    return wrapper


def repeat(count: int):
    """Parameterized decorator that repeats a function."""

    if count <= 0:
        raise ValueError("count must be greater than zero")

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None

            for _ in range(count):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator
