from copy import deepcopy

from src.data_processor.data import students
from src.data_processor.student_processor import (
    add_average_score,
    add_group_bonus,
    aggregate_students,
    calculate_average,
    compose,
    filter_by_min_scores,
    get_top_n,
    process_students,
    sort_students,
)


def test_calculate_average():
    assert calculate_average([90, 80, 100]) == 90.0


def test_calculate_average_empty():
    assert calculate_average([]) == 0.0


def test_filter_by_min_scores():
    result = filter_by_min_scores(
        students,
        min_scores=2,
    )

    assert len(result) == 7

    assert all(
        len(student["scores"]) >= 2
        for student in result
    )


def test_filter_does_not_mutate_input():
    original = deepcopy(students)

    filter_by_min_scores(
        students,
        min_scores=2,
    )

    assert students == original


def test_add_average_score():
    result = add_average_score(students)

    assert result[0]["average"] == 90.0
    assert result[1]["average"] == 90.0
    assert result[2]["average"] == 77.5


def test_add_average_does_not_mutate_input():
    original = deepcopy(students)

    add_average_score(students)

    assert students == original


def test_add_group_bonus():
    prepared = add_average_score(students)

    result = add_group_bonus(
        prepared,
        selected_group="KN-21",
        bonus=5.0,
    )

    assert result[0]["average"] == 95.0
    assert result[1]["average"] == 90.0
    assert result[2]["average"] == 82.5
    assert result[5]["average"] == 96.33333333333333


def test_add_group_bonus_does_not_mutate_input():
    prepared = add_average_score(students)
    original = deepcopy(prepared)

    add_group_bonus(
        prepared,
        selected_group="KN-21",
        bonus=5.0,
    )

    assert prepared == original


def test_sort_students():
    prepared = add_average_score(students)

    result = sort_students(prepared)

    assert result[0]["name"] == "Maria Shevchenko"
    assert result[0]["average"] == 95.0

    averages = [
        student["average"]
        for student in result
    ]

    assert averages == sorted(
        averages,
        reverse=True,
    )


def test_sort_students_uses_name_as_second_key():
    data = [
        {
            "id": 1,
            "name": "Zoe",
            "group": "A",
            "scores": [90],
            "average": 90.0,
        },
        {
            "id": 2,
            "name": "Anna",
            "group": "A",
            "scores": [90],
            "average": 90.0,
        },
    ]

    result = sort_students(data)

    assert result[0]["name"] == "Anna"
    assert result[1]["name"] == "Zoe"


def test_top_n():
    prepared = add_average_score(students)

    result = get_top_n(
        prepared,
        n=3,
    )

    assert len(result) == 3

    assert result[0]["name"] == "Maria Shevchenko"
    assert result[1]["name"] == "Sofia Tkachenko"
    assert result[2]["name"] == "Ivan Petrenko"


def test_top_n_after_bonus():
    prepared = add_average_score(students)

    prepared = add_group_bonus(
        prepared,
        selected_group="KN-21",
        bonus=5.0,
    )

    result = get_top_n(
        prepared,
        n=3,
    )

    assert len(result) == 3

    assert result[0]["name"] == "Sofia Tkachenko"
    assert result[1]["name"] == "Ivan Petrenko"
    assert result[2]["name"] == "Maria Shevchenko"


def test_top_n_zero():
    prepared = add_average_score(students)

    assert get_top_n(prepared, 0) == []


def test_aggregate_students():
    prepared = add_average_score(students)

    result = aggregate_students(prepared)

    assert result["count"] == 8

    assert result["sum_avg"] == (
        90.0
        + 90.0
        + 77.5
        + 95.0
        + 70.0
        + (91 + 89 + 94) / 3
        + (82 + 84 + 80) / 3
        + 95.0
    )

    assert set(result["group_avg"]) == {
        "KN-21",
        "KN-22",
        "KN-23",
    }


def test_aggregate_group_average():
    prepared = add_average_score(students)

    result = aggregate_students(prepared)

    assert result["group_avg"]["KN-21"] == (
        90.0 + 77.5 + (91 + 89 + 94) / 3
    ) / 3

    assert result["group_avg"]["KN-22"] == (
        90.0 + 95.0 + 95.0
    ) / 3

    assert result["group_avg"]["KN-23"] == (
        70.0 + (82 + 84 + 80) / 3
    ) / 2


def test_aggregate_empty():
    result = aggregate_students([])

    assert result == {
        "count": 0,
        "sum_avg": 0.0,
        "group_avg": {},
    }


def test_compose():
    pipeline = compose(
        lambda x: x + 1,
        lambda x: x * 2,
        lambda x: x - 3,
    )

    assert pipeline(5) == 9


def test_process_students():
    original = deepcopy(students)

    result = process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=5.0,
        top_n=3,
    )

    assert len(result["students"]) == 7
    assert len(result["top_n"]) == 3

    assert result["aggregation"]["count"] == 7

    assert result["top_n"] == result["students"][:3]

    assert students == original


def test_process_students_has_bonus():
    result = process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=5.0,
        top_n=7,
    )

    by_name = {
        student["name"]: student
        for student in result["students"]
    }

    assert by_name["Ivan Petrenko"]["average"] == 95.0

    assert by_name["Sofia Tkachenko"]["average"] == (
        (91 + 89 + 94) / 3 + 5
    )

    assert by_name["Andrii Melnyk"]["average"] == 77.5
