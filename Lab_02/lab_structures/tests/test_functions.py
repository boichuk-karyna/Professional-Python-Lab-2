from src.data_processor.analytics import (
    calculate_average_values,
)

from src.data_processor.processors import (
    get_unique_authors,
)

from src.data_processor.data import books


def test_average():
    result = calculate_average_values(
        10,
        20,
        30,
    )

    assert result == 20


def test_unique_authors():
    authors = get_unique_authors(books)

    assert "George Orwell" in authors