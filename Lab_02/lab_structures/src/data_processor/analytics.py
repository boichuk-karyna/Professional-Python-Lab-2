from functools import reduce
from collections.abc import Callable

from src.data_processor.decorators import measure_time


# ---------------------------------------------------------
# REDUCE AGGREGATION
# ---------------------------------------------------------

def aggregate_students(
    students: list[dict],
) -> dict:
    """
    Aggregate students using reduce.

    Result contains exactly:

    count
    sum_avg
    group_avg
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
        average = float(
            student["average"]
        )

        accumulator["count"] += 1

        accumulator["sum_avg"] += average

        accumulator["group_sum"][group] = (
            accumulator["group_sum"].get(
                group,
                0.0,
            )
            + average
        )

        accumulator["group_count"][group] = (
            accumulator["group_count"].get(
                group,
                0,
            )
            + 1
        )

        return accumulator

    result = reduce(
        reducer,
        students,
        initial,
    )

    group_avg = {
        group: (
            result["group_sum"][group]
            / result["group_count"][group]
        )
        for group in result["group_sum"]
    }

    return {
        "count": result["count"],
        "sum_avg": result["sum_avg"],
        "group_avg": group_avg,
    }


# ---------------------------------------------------------
# COMPLETE PIPELINE
# ---------------------------------------------------------

def process_students(
    students: list[dict],
    min_scores: int,
    selected_group: str,
    bonus: float,
    top_n: int,
) -> dict:
    """
    Complete Lab_02 processing pipeline.
    """

    def filter_operation(
        data: list[dict],
    ) -> list[dict]:
        return [
            student.copy()
            for student in data
            if len(
                student.get("scores", [])
            ) >= min_scores
        ]

    def average_operation(
        data: list[dict],
    ) -> list[dict]:
        return [
            {
                **student,
                "average": (
                    sum(student["scores"])
                    / len(student["scores"])
                    if student["scores"]
                    else 0.0
                ),
            }
            for student in data
        ]

    def bonus_operation(
        data: list[dict],
    ) -> list[dict]:
        return [
            {
                **student,
                "average": (
                    student["average"] + bonus
                    if student["group"]
                    == selected_group
                    else student["average"]
                ),
            }
            for student in data
        ]

    pipeline = compose(
        filter_operation,
        average_operation,
        bonus_operation,
    )

    prepared = pipeline(students)

    ranked = sorted(
        prepared,
        key=lambda student: (
            -student["average"],
            student["name"],
        ),
    )

    return {
        "students": ranked,
        "top_n": [
            student.copy()
            for student in ranked[:top_n]
        ],
        "aggregation": aggregate_students(
            ranked
        ),
    }


# ---------------------------------------------------------
# COMPOSE
# ---------------------------------------------------------

def compose(
    *functions: Callable,
) -> Callable:
    """
    Function composition.
    """

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline


# ---------------------------------------------------------
# DECORATED AVERAGE
# ---------------------------------------------------------

@measure_time
def calculate_average_for_students(
    students: list[dict],
) -> float:
    """
    Calculate overall average.

    Decorated with measure_time.
    """

    if not students:
        return 0.0

    return sum(
        student["average"]
        for student in students
    ) / len(students)
