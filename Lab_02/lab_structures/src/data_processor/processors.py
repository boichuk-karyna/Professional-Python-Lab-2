from functools import reduce
from collections.abc import Callable


def calculate_average(scores: list[float]) -> float:
    """Calculate average score without mutating input."""
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def filter_by_min_scores(
    students: list[dict],
    min_scores: int,
) -> list[dict]:
    """Keep students with enough scores."""
    return [
        student.copy()
        for student in students
        if len(student["scores"]) >= min_scores
    ]


def add_average_score(
    students: list[dict],
) -> list[dict]:
    """Add average score to every student."""
    return [
        {
            **student,
            "average": calculate_average(student["scores"]),
        }
        for student in students
    ]


def add_group_bonus(
    students: list[dict],
    selected_group: str,
    bonus: float,
) -> list[dict]:
    """Add bonus to students from selected group."""
    return [
        {
            **student,
            "average": (
                student["average"] + bonus
                if student["group"] == selected_group
                else student["average"]
            ),
        }
        for student in students
    ]


def sort_students(
    students: list[dict],
) -> list[dict]:
    """
    Sort students by:
    1. average descending
    2. name ascending
    """
    return sorted(
        students,
        key=lambda student: (
            -student["average"],
            student["name"],
        ),
    )


def get_top_n(
    students: list[dict],
    n: int,
) -> list[dict]:
    """Return Top-N students."""
    return sort_students(students)[:n]


def aggregate_students(
    students: list[dict],
) -> dict:
    """
    Aggregate students using reduce.

    Returns:
        count: number of students
        sum_avg: sum of average scores
        group_avg: average score by group
    """

    initial = {
        "count": 0,
        "sum_avg": 0.0,
        "group_sum": {},
        "group_count": {},
    }

    def reducer(
        accumulator: dict,
        student: dict,
    ) -> dict:
        group = student["group"]
        average = student["average"]

        accumulator["count"] += 1
        accumulator["sum_avg"] += average

        accumulator["group_sum"][group] = (
            accumulator["group_sum"].get(group, 0.0)
            + average
        )

        accumulator["group_count"][group] = (
            accumulator["group_count"].get(group, 0)
            + 1
        )

        return accumulator

    result = reduce(
        reducer,
        students,
        initial,
    )

    group_avg = {
        group: result["group_sum"][group]
        / result["group_count"][group]
        for group in result["group_sum"]
    }

    return {
        "count": result["count"],
        "sum_avg": result["sum_avg"],
        "group_avg": group_avg,
    }


def compose(
    *functions: Callable,
) -> Callable:
    """Compose functions from left to right."""

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline


def process_students(
    students: list[dict],
    min_scores: int,
    selected_group: str,
    bonus: float,
    top_n: int,
) -> dict:
    """Complete Lab_02 processing pipeline."""

    filtered = filter_by_min_scores(
        students,
        min_scores,
    )

    with_average = add_average_score(
        filtered,
    )

    with_bonus = add_group_bonus(
        with_average,
        selected_group,
        bonus,
    )

    sorted_students = sort_students(
        with_bonus,
    )

    top_students = get_top_n(
        sorted_students,
        top_n,
    )

    aggregation = aggregate_students(
        sorted_students,
    )

    return {
        "students": sorted_students,
        "top_n": top_students,
        "aggregation": aggregation,
    }
