from functools import reduce

from .processors import (
    calculate_average,
    sort_students,
)


def aggregate_students(students):
    def reducer(accumulator, student):
        group = student["group"]
        average = student["average"]

        accumulator["count"] += 1
        accumulator["sum_avg"] += average

        if group not in accumulator["group_avg"]:
            accumulator["group_avg"][group] = []

        accumulator["group_avg"][group].append(average)

        return accumulator

    initial = {
        "count": 0,
        "sum_avg": 0.0,
        "group_avg": {},
    }

    result = reduce(
        reducer,
        students,
        initial,
    )

    result["group_avg"] = {
        group: sum(values) / len(values)
        for group, values in result["group_avg"].items()
    }

    return result


def compose(*functions):
    def pipeline(data):
        result = data

        for function in functions:
            result = function(result)

        return result

    return pipeline


def process_students(
    students,
    min_scores=2,
    selected_group=None,
    bonus=0.0,
    top_n=3,
):
    # Не змінюємо оригінальні дані
    processed = []

    for student in students:
        if len(student["scores"]) < min_scores:
            continue

        item = student.copy()
        item["scores"] = list(student["scores"])

        item["average"] = calculate_average(
            item["scores"]
        )

        if (
            selected_group is not None
            and item["group"] == selected_group
        ):
            item["average"] += bonus

        processed.append(item)

    sorted_students = sort_students(processed)

    if top_n > 0:
        top = sorted_students[:top_n]
    else:
        top = []

    aggregation = aggregate_students(
        processed
    )

    return {
        "students": processed,
        "top_n": top,
        "aggregation": aggregation,
    }
