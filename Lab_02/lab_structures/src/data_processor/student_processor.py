"""
Compatibility module for Lab_02.

The actual individual variant is Variant 2:
book data processing.
"""

from src.data_processor.analytics import (
    aggregate_books,
    compose,
    get_top_n,
)
from src.data_processor.processors import (
    calculate_average_pages,
    create_book_index,
    create_title_index,
    create_year_filter,
    count_books_by_author,
    create_record,
    filter_books,
    filter_by_year,
    find_book_by_id,
    find_book_by_title,
    find_book_in_index,
    find_largest_book,
    get_page_statistics,
    get_unique_authors,
    group_books_by_author,
    sort_by_pages,
    sort_by_year,
)


def process_books(
    books: list[dict],
    minimum_year: int,
    top_n: int,
) -> dict:
    """
    Complete Lab_02 processing pipeline.

    The original input is never modified.
    """

    filtered = filter_by_year(
        books,
        minimum_year,
    )

    sorted_books = sort_by_pages(
        filtered,
        reverse=True,
    )

    top_books = get_top_n(
        filtered,
        top_n,
    )

    return {
        "books": sorted_books,
        "top_n": top_books,
        "aggregation": aggregate_books(filtered),
        "authors": get_unique_authors(filtered),
        "grouped": group_books_by_author(filtered),
    }
