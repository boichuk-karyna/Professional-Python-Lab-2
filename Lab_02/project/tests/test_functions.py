from copy import deepcopy

from src.data_processor.data import students

from src.data_processor.processors import (
    calculate_average,
    calculate_average_values,
    create_min_scores_filter,
    create_record,
    create_student_index,
    filter_by_min_scores,
    filter_students,
    get_score_statistics,
    get_student_names,
    get_unique_groups,
    group_students_by_group,
    sort_students,
)

from src.data_processor.analytics import (
    aggregate_students,
    compose,
    process_students,
)


# ---------------------------------------------------------
# BASIC DATA STRUCTURES
# ---------------------------------------------------------

def test_students_is_list():
    assert isinstance(students, list)


def test_student_is_dict():
    assert isinstance(students[0], dict)


def test_required_student_fields():
    required = {
        "id",
        "name",
        "group",
        "scores",
    }

    for student in students:
        assert required.issubset(
            student.keys()
        )


# ---------------------------------------------------------
# AVERAGE
# ---------------------------------------------------------

def test_calculate_average():
    assert calculate_average(
        [80, 90, 100]
    ) == 90.0


def test_calculate_average_empty():
    assert calculate_average([]) == 0.0


# ---------------------------------------------------------
# FILTER
# ---------------------------------------------------------

def test_filter_by_min_scores():
    result = filter_by_min_scores(
        students,
        3,
    )

    assert len(result) == 5

    assert all(
        len(student["scores"]) >= 3
        for student in result
    )


# ---------------------------------------------------------
# UNIQUE GROUPS
# ---------------------------------------------------------

def test_unique_groups():
    groups = get_unique_groups(
        students
    )

    assert isinstance(groups, set)

    assert groups == {
        "KN-21",
        "KN-22",
        "KN-23",
    }


# ---------------------------------------------------------
# DICT INDEX
# ---------------------------------------------------------

def test_student_index():
    index = create_student_index(
        students
    )

    assert isinstance(index, dict)

    assert index[1]["name"] == (
        "Ivan Petrenko"
    )

    assert index[4]["name"] == (
        "Maria Shevchenko"
    )


# ---------------------------------------------------------
# GROUPING
# ---------------------------------------------------------

def test_grouping():
    grouped = group_students_by_group(
        students
    )

    assert "KN-21" in grouped
    assert "KN-22" in grouped
    assert "KN-23" in grouped

    assert len(grouped["KN-21"]) == 3
    assert len(grouped["KN-22"]) == 3
    assert len(grouped["KN-23"]) == 2


# ---------------------------------------------------------
# CLOSURE
# ---------------------------------------------------------

def test_closure():
    predicate = create_min_scores_filter(
        3
    )

    result = filter_students(
        students,
        predicate,
    )

    assert all(
        len(student["scores"]) >= 3
        for student in result
    )


# ---------------------------------------------------------
# MAP
# ---------------------------------------------------------

def test_map():
    names = get_student_names(
        students
    )

    assert names[0] == (
        "Ivan Petrenko"
    )

    assert len(names) == len(students)


# ---------------------------------------------------------
# TUPLE
# ---------------------------------------------------------

def test_tuple_statistics():
    result = get_score_statistics(
        students
    )

    assert isinstance(
        result,
        tuple,
    )

    assert len(result) == 3

    minimum, maximum, average = result

    assert minimum == 70
    assert maximum == 97
    assert average > 0


# ---------------------------------------------------------
# SORTING
# ---------------------------------------------------------

def test_sort_by_two_keys():
    data = [
        {
            "id": 1,
            "name": "Zed",
            "group": "A",
            "scores": [90],
            "average": 90,
        },
        {
            "id": 2,
            "name": "Anna",
            "group": "A",
            "scores": [90],
            "average": 90,
        },
        {
            "id": 3,
            "name": "Bob",
            "group": "A",
            "scores": [80],
            "average": 80,
        },
    ]

    result = sort_students(data)

    assert result[0]["name"] == "Anna"
    assert result[1]["name"] == "Zed"
    assert result[2]["name"] == "Bob"


# ---------------------------------------------------------
# TOP N
# ---------------------------------------------------------

def test_top_n():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    top = result["top_n"]

    assert len(top) == 3

    averages = [
        student["average"]
        for student in top
    ]

    assert averages == sorted(
        averages,
        reverse=True,
    )


def test_top_n_zero():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=0,
    )

    assert result["top_n"] == []


# ---------------------------------------------------------
# BONUS
# ---------------------------------------------------------

def test_group_bonus():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=10,
    )

    kn21 = [
        student
        for student in result["students"]
        if student["group"] == "KN-21"
    ]

    assert all(
        student["average"] > 0
        for student in kn21
    )


# ---------------------------------------------------------
# REDUCE
# ---------------------------------------------------------

def test_reduce_aggregation_keys():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    aggregation = result[
        "aggregation"
    ]

    assert set(
        aggregation.keys()
    ) == {
        "count",
        "sum_avg",
        "group_avg",
    }


def test_reduce_count():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    aggregation = result[
        "aggregation"
    ]

    assert aggregation["count"] == 7


def test_reduce_group_avg():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    group_avg = result[
        "aggregation"
    ]["group_avg"]

    assert isinstance(
        group_avg,
        dict,
    )

    assert "KN-21" in group_avg


# ---------------------------------------------------------
# COMPOSE
# ---------------------------------------------------------

def test_compose():
    pipeline = compose(
        lambda data: filter_by_min_scores(
            data,
            2,
        ),
        lambda data: data[:3],
    )

    result = pipeline(students)

    assert len(result) == 3

    assert all(
        len(student["scores"]) >= 2
        for student in result
    )


# ---------------------------------------------------------
# *ARGS
# ---------------------------------------------------------

def test_args():
    result = calculate_average_values(
        10,
        20,
        30,
    )

    assert result == 20.0


# ---------------------------------------------------------
# **KWARGS
# ---------------------------------------------------------

def test_kwargs():
    result = create_record(
        id=10,
        name="Test",
        group="KN-99",
        scores=[100],
    )

    assert result == {
        "id": 10,
        "name": "Test",
        "group": "KN-99",
        "scores": [100],
    }


# ---------------------------------------------------------
# NO MUTATION
# ---------------------------------------------------------

def test_no_mutation():
    original = deepcopy(
        students
    )

    process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    assert students == original
