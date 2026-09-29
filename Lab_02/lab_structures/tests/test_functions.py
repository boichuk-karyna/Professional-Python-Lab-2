from copy import deepcopy

from src.data_processor.analytics import (
    aggregate_books,
    calculate_average_pages,
    calculate_average_values,
    calculate_page_statistics,
    compose,
    create_page_filter,
    create_record,
)

from src.data_processor.data import books

from src.data_processor.processors import (
    count_books_by_author,
    create_book_index,
    filter_by_pages,
    filter_by_year,
    find_book_by_id,
    find_book_by_title,
    find_largest_book,
    get_unique_authors,
    group_books_by_author,
    sort_by_pages,
    sort_by_year,
)


def test_data_is_list():
    assert isinstance(books, list)


def test_book_is_dict():
    assert isinstance(books[0], dict)


def test_book_contains_required_fields():
    required = {
        "id",
        "title",
        "author",
        "year",
        "pages",
    }

    assert required.issubset(books[0])


def test_unique_authors():
    result = get_unique_authors(books)

    assert isinstance(result, set)

    assert "Robert Martin" in result
    assert "Andrew Hunt" in result


def test_create_book_index():
    result = create_book_index(books)

    assert isinstance(result, dict)
    assert result[1]["title"] == "Clean Code"
    assert result[5]["title"] == "Fluent Python"


def test_find_book_by_id():
    result = find_book_by_id(
        books,
        5,
    )

    assert result is not None
    assert result["title"] == "Fluent Python"


def test_find_book_by_id_missing():
    assert find_book_by_id(
        books,
        999,
    ) is None


def test_find_book_by_title():
    result = find_book_by_title(
        books,
        "Clean Code",
    )

    assert result is not None
    assert result["id"] == 1


def test_filter_by_year():
    result = filter_by_year(
        books,
        2015,
    )

    assert all(
        book["year"] >= 2015
        for book in result
    )


def test_filter_by_pages():
    result = filter_by_pages(
        books,
        500,
    )

    assert all(
        book["pages"] >= 500
        for book in result
    )


def test_group_books_by_author():
    result = group_books_by_author(
        books
    )

    assert isinstance(result, dict)

    assert len(
        result["Robert Martin"]
    ) == 2


def test_counter():
    result = count_books_by_author(
        books
    )

    assert result["Robert Martin"] == 2
    assert result["Andrew Hunt"] == 1


def test_sort_by_year():
    result = sort_by_year(
        books
    )

    years = [
        book["year"]
        for book in result
    ]

    assert years == sorted(years)


def test_sort_by_pages():
    result = sort_by_pages(
        books
    )

    pages = [
        book["pages"]
        for book in result
    ]

    assert pages == sorted(
        pages,
        reverse=True,
    )


def test_find_largest_book():
    result = find_largest_book(
        books
    )

    assert result is not None
    assert result["title"] == "Learning Python"
    assert result["pages"] == 1648


def test_average_pages():
    result = calculate_average_pages(
        books
    )

    expected = sum(
        book["pages"]
        for book in books
    ) / len(books)

    assert result == expected


def test_average_values_args():
    assert calculate_average_values(
        10,
        20,
        30,
    ) == 20.0


def test_average_values_empty():
    assert calculate_average_values() == 0.0


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


def test_closure():
    is_large = create_page_filter(
        500
    )

    result = [
        book
        for book in books
        if is_large(book)
    ]

    assert all(
        book["pages"] >= 500
        for book in result
    )


def test_page_statistics():
    minimum, maximum, average = (
        calculate_page_statistics(
            books
        )
    )

    assert minimum == 352
    assert maximum == 1648

    expected = sum(
        book["pages"]
        for book in books
    ) / len(books)

    assert average == expected


def test_aggregate():
    result = aggregate_books(
        books
    )

    assert result["count"] == len(books)

    assert result["sum_pages"] == sum(
        book["pages"]
        for book in books
    )

    assert result["average_pages"] == (
        result["sum_pages"]
        / result["count"]
    )

    assert (
        result["author_stats"]
        ["Robert Martin"]
        ["count"]
        == 2
    )


def test_aggregate_empty():
    result = aggregate_books([])

    assert result["count"] == 0
    assert result["sum_pages"] == 0
    assert result["average_pages"] == 0.0
    assert result["author_stats"] == {}


def test_compose():
    pipeline = compose(
        lambda data: filter_by_year(
            data,
            2010,
        ),
        sort_by_pages,
    )

    result = pipeline(books)

    assert all(
        book["year"] >= 2010
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

    get_unique_authors(books)
    create_book_index(books)
    filter_by_year(books, 2010)
    filter_by_pages(books, 500)
    group_books_by_author(books)
    count_books_by_author(books)
    sort_by_year(books)
    sort_by_pages(books)
    find_largest_book(books)
    calculate_average_pages(books)
    aggregate_books(books)

    assert books == original
