from functools import reduce
from collections.abc import Callable


def calculate_average(
    scores: list[float],
) -> float:
    """Calculate average score without modifying scores."""

    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def filter_by_min_scores(
    students: list[dict],
    min_scores: int,
) -> list[dict]:
    """
    Return students having at least min_scores.

    The original data is not modified.
    """

    return [
        student.copy()
        for student in students
        if len(student.get("scores", [])) >= min_scores
    ]


def add_average_score(
    students: list[dict],
) -> list[dict]:
    """
    Add average field without modifying input students.
    """

    return [
        {
            **student,
            "average": calculate_average(
                student.get("scores", [])
            ),
        }
        for student in students
    ]


def add_group_bonus(
    students: list[dict],
    selected_group: str,
    bonus: float,
) -> list[dict]:
    """
    Add bonus only to students from selected_group.

    Does not mutate input.
    """

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
    Sort by two keys:

    1. average descending
    2. name ascending
    """

    return sorted(
        (
            student.copy()
            for student in students
        ),
        key=lambda student: (
            -student["average"],
            student["name"],
        ),
    )


def get_top_n(
    students: list[dict],
    n: int,
) -> list[dict]:
    """
    Return exactly the first N students
    from the required ranking.
    """

    if n <= 0:
        return []

    ranked = sort_students(students)

    return [
        student.copy()
        for student in ranked[:n]
    ]


def aggregate_students(
    students: list[dict],
) -> dict:
    """
    Aggregate using functools.reduce.

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
        average = float(student["average"])

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


def compose(
    *functions: Callable,
) -> Callable:
    """
    Real left-to-right function composition.

    compose(f, g, h)(value)
    means h(g(f(value))).
    """

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline


def filter_students(
    students: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """
    Universal higher-order filter.
    """

    return [
        student.copy()
        for student in students
        if predicate(student)
    ]


def create_min_scores_filter(
    minimum: int,
) -> Callable[[dict], bool]:
    """
    Closure remembering minimum number of scores.
    """

    def predicate(student: dict) -> bool:
        return len(
            student.get("scores", [])
        ) >= minimum

    return predicate


def calculate_average_values(
    *values: float,
) -> float:
    """Demonstrate *args."""

    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(
    **fields,
) -> dict:
    """Demonstrate **kwargs."""

    return dict(fields)


def process_students(
    students: list[dict],
    min_scores: int,
    selected_group: str,
    bonus: float,
    top_n: int,
) -> dict:
    """
    Complete Lab_02 pipeline.

    IMPORTANT:
    The pipeline itself uses compose().
    """

    pipeline = compose(
        lambda data: filter_by_min_scores(
            data,
            min_scores,
        ),
        add_average_score,
        lambda data: add_group_bonus(
            data,
            selected_group,
            bonus,
        ),
    )

    prepared = pipeline(students)

    ranked = sort_students(prepared)

    return {
        "students": ranked,
        "top_n": get_top_n(
            ranked,
            top_n,
        ),
        "aggregation": aggregate_students(
            ranked,
        ),
    }
