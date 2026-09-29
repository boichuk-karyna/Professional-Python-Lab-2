"""Analytical functions for Lab_02."""

from functools import reduce

from data_processor.decorators import measure_time


@measure_time
def aggregate_students(
    students: list[dict],
) -> dict:
    """
    Aggregate student statistics using reduce.

    Returns:
        count
        sum_avg
        group_avg
    """

    initial = {
        "count": 0,
        "sum_avg": 0.0,
        "group_totals": {},
    }

    def reducer(
        accumulator: dict,
        student: dict,
    ) -> dict:
        group = student["group"]
        average = student["average"]

        new_group_totals = {
            **accumulator["group_totals"],
        }

        current = new_group_totals.get(
            group,
            [0, 0.0],
        )

        new_group_totals[group] = [
            current[0] + 1,
            current[1] + average,
        ]

        return {
            "count": accumulator["count"] + 1,
            "sum_avg": accumulator["sum_avg"] + average,
            "group_totals": new_group_totals,
        }

    result = reduce(
        reducer,
        students,
        initial,
    )

    group_avg = {
        group: total / count
        for group, (count, total)
        in result["group_totals"].items()
    }

    return {
        "count": result["count"],
        "sum_avg": result["sum_avg"],
        "group_avg": group_avg,
    }


def calculate_overall_average(
    students: list[dict],
) -> float:
    """Calculate overall average."""

    if not students:
        return 0.0

    return sum(
        student["average"]
        for student in students
    ) / len(students)


def create_average_filter(
    minimum_average: float,
):
    """
    Create closure for average filtering.

    The returned function remembers minimum_average.
    """

    def predicate(student: dict) -> bool:
        return (
            student["average"]
            >= minimum_average
        )

    return predicate


def calculate_average_values(
    *values: float,
) -> float:
    """Calculate average using *args."""

    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(
    **fields,
) -> dict:
    """Create dictionary using **kwargs."""

    return dict(fields)


def compose(
    *functions,
):
    """
    Compose functions from left to right.

    This is a higher-order function.
    """

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline
