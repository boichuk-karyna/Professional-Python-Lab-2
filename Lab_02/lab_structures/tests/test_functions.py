from copy import deepcopy

from src.data_processor.student_processor import (
    add_average_score,
    add_group_bonus,
    aggregate_students,
    calculate_average,
    filter_by_min_scores,
    get_top_n,
    process_students,
    sort_students,
)
from src.data_processor.data import students


def test_calculate_average():
    assert calculate_average([90, 80, 100]) == 90.0


def test_calculate_average_empty():
    assert calculate_average([]) == 0.0


def test_filter_by_min_scores():
    result = filter_by_min_scores(
        students,
        min_scores=2,
    )

    assert all(
        len(student["scores"]) >= 2
        for student in result
    )


def test_add_average_score():
    result = add_average_score(students)

    assert result[0]["average"] == 90.0
    assert result[1]["average"] == 90.0


def test_add_group_bonus():
    prepared = add_average_score(students)

    result = add_group_bonus(
        prepared,
        selected_group="KN-21",
        bonus=5.0,
    )

    assert result[0]["average"] == 95.0
    assert result[1]["average"] == 90.0


def test_sort_students():
    prepared = add_average_score(students)

    result = sort_students(prepared)

    averages = [
        student["average"]
        for student in result
    ]

    assert averages == sorted(
        averages,
        reverse=True,
    )


def test_top_n():
    prepared = add_average_score(students)

    result = get_top_n(
        prepared,
        n=3,
    )

    assert len(result) == 3

    averages = [
        student["average"]
        for student in result
    ]

    assert averages == sorted(
        averages,
        reverse=True,
    )


def test_aggregate_students():
    prepared = add_average_score(students)

    result = aggregate_students(prepared)

    assert result["count"] == len(students)

    assert "sum_avg" in result
    assert "group_avg" in result

    assert set(result["group_avg"]) == {
        "KN-21",
        "KN-22",
        "KN-23",
    }


def test_no_mutation():
    original = deepcopy(students)

    process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=5.0,
        top_n=3,
    )

    assert students == original


def test_process_students():
    result = process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=5.0,
        top_n=3,
    )

    assert len(result["top_n"]) == 3
    assert result["aggregation"]["count"] == 7
