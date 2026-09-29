from copy import deepcopy

from src.data_processor.analytics import (
    aggregate_books,
    compose,
    get_top_n,
)
from src.data_processor.data import books
from src.data_processor.processors import (
    calculate_average_pages,
    calculate_average_values,
    count_books_by_author,
    create_book_index,
    create_record,
    create_year_filter,
    filter_books,
    filter_by_year,
    find_book_by_id,
    find_book_by_title,
    find_largest_book,
    get_page_statistics,
    get_unique_authors,
    group_books_by_author,
    sort_by_pages,
    sort_by_year,
)


def test_get_unique_authors():
    result = get_unique_authors(books)

    assert isinstance(result, set)
    assert "Mark Lutz" in result
    assert "Robert Martin" in result


def test_create_book_index():
    index = create_book_index(books)

    assert isinstance(index, dict)
    assert index[1]["title"] == "Python Basics"
    assert index[4]["title"] == "Fluent Python"


def test_find_book_by_id():
    result = find_book_by_id(
        books,
        3,
    )

    assert result is not None
    assert result["title"] == "Effective Python"


def test_find_book_by_title():
    result = find_book_by_title(
        books,
        "Clean Code",
    )

    assert result is not None
    assert result["id"] == 2


def test_find_book_not_found():
    assert find_book_by_id(
        books,
        999,
    ) is None


def test_filter_by_year():
    result = filter_by_year(
        books,
        2019,
    )

    assert all(
        book["year"] >= 2019
        for book in result
    )


def test_filter_closure():
    predicate = create_year_filter(
        2020,
    )

    result = filter_books(
        books,
        predicate,
    )

    assert all(
        book["year"] >= 2020
        for book in result
    )


def test_calculate_average_pages():
    result = calculate_average_pages(
        books,
    )

    expected = (
        sum(
            book["pages"]
            for book in books
        )
        / len(books)
    )

    assert result == expected


def test_calculate_average_pages_empty():
    assert calculate_average_pages([]) == 0.0


def test_find_largest_book():
    result = find_largest_book(
        books,
    )

    assert result is not None
    assert result["title"] == "Learning Python"
    assert result["pages"] == 1648


def test_sort_by_year():
    result = sort_by_year(
        books,
    )

    years = [
        book["year"]
        for book in result
    ]

    assert years == sorted(years)


def test_sort_by_pages():
    result = sort_by_pages(
        books,
    )

    pages = [
        book["pages"]
        for book in result
    ]

    assert pages == sorted(
        pages,
        reverse=True,
    )


def test_top_n():
    result = get_top_n(
        books,
        3,
    )

    assert len(result) == 3

    pages = [
        book["pages"]
        for book in result
    ]

    assert pages == sorted(
        pages,
        reverse=True,
    )


def test_top_n_zero():
    assert get_top_n(
        books,
        0,
    ) == []


def test_top_n_negative():
    assert get_top_n(
        books,
        -1,
    ) == []


def test_group_books_by_author():
    result = group_books_by_author(
        books,
    )

    assert "Mark Lutz" in result
    assert len(result["Mark Lutz"]) == 2


def test_count_books_by_author():
    result = count_books_by_author(
        books,
    )

    assert result["Mark Lutz"] == 2


def test_aggregate_books():
    result = aggregate_books(
        books,
    )

    assert result["count"] == len(books)

    expected_sum = sum(
        book["pages"]
        for book in books
    )

    assert result["sum_pages"] == expected_sum

    assert "author_avg" in result

    assert isinstance(
        result["author_avg"],
        dict,
    )


def test_page_statistics_tuple():
    result = get_page_statistics(
        books,
    )

    assert isinstance(
        result,
        tuple,
    )

    assert result[0] == 274
    assert result[1] == 1648


def test_args():
    result = calculate_average_values(
        10,
        20,
        30,
    )

    assert result == 20.0


def test_kwargs():
    result = create_record(
        id=1,
        title="Test",
        pages=100,
    )

    assert result == {
        "id": 1,
        "title": "Test",
        "pages": 100,
    }


def test_compose():
    pipeline = compose(
        lambda items: filter_by_year(
            items,
            2019,
        ),
        lambda items: sort_by_pages(
            items,
            reverse=True,
        ),
    )

    result = pipeline(books)

    assert all(
        book["year"] >= 2019
        for book in result
    )

    pages = [
        book["pages"]
        for book in result
    ]

    assert pages == sorted(
        pages,
        reverse=True,
    )


def test_no_mutation():
    original = deepcopy(books)

    result = filter_by_year(
        books,
        2019,
    )

    result.append(
        {
            "id": 999,
            "title": "Temporary",
            "author": "Test",
            "year": 2026,
            "pages": 1,
        }
    )

    assert books == original


def test_top_n_no_mutation():
    original = deepcopy(books)

    get_top_n(
        books,
        3,
    )

    assert books == original
