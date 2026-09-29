"""Pure processing functions for student data."""

from collections import Counter, defaultdict
from collections.abc import Callable


def filter_by_min_scores(
    students: list[dict],
    minimum_scores: int,
) -> list[dict]:
    """
    Return students having enough scores.

    Original data is not modified.
    """
    return [
        student
        for student in students
        if len(student["scores"]) >= minimum_scores
    ]


def calculate_average(
    student: dict,
) -> float:
    """Calculate average score of one student."""

    scores = student["scores"]

    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def add_average(
    student: dict,
) -> dict:
    """
    Create a new student record with average.

    Original dictionary is not mutated.
    """
    return {
        **student,
        "average": calculate_average(student),
    }


def transform_with_average(
    students: list[dict],
) -> list[dict]:
    """Add average to every student using map."""

    return list(
        map(
            add_average,
            students,
        )
    )


def add_group_bonus(
    student: dict,
    selected_group: str,
    bonus: float,
) -> dict:
    """
    Create a new record with group bonus.

    Original data remains unchanged.
    """
    new_average = student["average"]

    if student["group"] == selected_group:
        new_average += bonus

    return {
        **student,
        "average": new_average,
    }


def apply_group_bonus(
    students: list[dict],
    selected_group: str,
    bonus: float,
) -> list[dict]:
    """Apply bonus to the selected group without mutation."""

    return [
        add_group_bonus(
            student,
            selected_group,
            bonus,
        )
        for student in students
    ]


def sort_students(
    students: list[dict],
) -> list[dict]:
    """
    Sort students by two keys.

    First: average descending.
    Second: name ascending.
    """
    return sorted(
        students,
        key=lambda student: (
            -student["average"],
            student["name"],
        ),
    )


def top_n_students(
    students: list[dict],
    n: int,
) -> list[dict]:
    """Return Top-N students."""

    if n <= 0:
        return []

    return sort_students(students)[:n]


def create_student_index(
    students: list[dict],
) -> dict[int, dict]:
    """Create dictionary index by student ID."""

    return {
        student["id"]: student
        for student in students
    }


def find_student_by_id(
    students: list[dict],
    student_id: int,
) -> dict | None:
    """Linear search by ID."""

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def group_students(
    students: list[dict],
) -> dict[str, list[dict]]:
    """Group students by group."""

    grouped = defaultdict(list)

    for student in students:
        grouped[student["group"]].append(student)

    return dict(grouped)


def get_unique_groups(
    students: list[dict],
) -> set[str]:
    """Return unique groups using set comprehension."""

    return {
        student["group"]
        for student in students
    }


def count_by_group(
    students: list[dict],
) -> Counter:
    """Count students in every group."""

    return Counter(
        student["group"]
        for student in students
    )


def filter_items(
    items: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """Universal higher-order filtering function."""

    return list(
        filter(
            predicate,
            items,
        )
    )


def map_items(
    items: list[dict],
    transform: Callable[[dict], dict],
) -> list[dict]:
    """Universal higher-order mapping function."""

    return list(
        map(
            transform,
            items,
        )
    )
