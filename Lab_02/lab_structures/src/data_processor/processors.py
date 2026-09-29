from collections import Counter, defaultdict
from collections.abc import Callable


# ---------------------------------------------------------
# 1. FILTERING
# ---------------------------------------------------------

def filter_by_min_scores(
    students: list[dict],
    min_scores: int,
) -> list[dict]:
    """
    Return students having at least min_scores.

    Pure transformation:
    original list is not modified.
    """

    return [
        student.copy()
        for student in students
        if len(student.get("scores", [])) >= min_scores
    ]


# ---------------------------------------------------------
# 2. AVERAGE CALCULATION
# ---------------------------------------------------------

def calculate_average(
    scores: list[float],
) -> float:
    """
    Calculate average score.
    """

    if not scores:
        return 0.0

    return sum(scores) / len(scores)


# ---------------------------------------------------------
# 3. ADD AVERAGE
# ---------------------------------------------------------

def add_average_score(
    students: list[dict],
) -> list[dict]:
    """
    Add average field to every student.

    Pure transformation.
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


# ---------------------------------------------------------
# 4. GROUP BONUS
# ---------------------------------------------------------

def add_group_bonus(
    students: list[dict],
    selected_group: str,
    bonus: float,
) -> list[dict]:
    """
    Add bonus to students from selected group.

    Original data is not modified.
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


# ---------------------------------------------------------
# 5. SORTING
# ---------------------------------------------------------

def sort_students(
    students: list[dict],
) -> list[dict]:
    """
    Sort by two keys:

    1. average - descending
    2. name - ascending
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


# ---------------------------------------------------------
# 6. TOP N
# ---------------------------------------------------------

def get_top_n(
    students: list[dict],
    n: int,
) -> list[dict]:
    """
    Return top N students.
    """

    if n <= 0:
        return []

    ranked = sort_students(students)

    return [
        student.copy()
        for student in ranked[:n]
    ]


# ---------------------------------------------------------
# 7. UNIVERSAL FILTER
# ---------------------------------------------------------

def filter_students(
    students: list[dict],
    predicate: Callable[[dict], bool],
) -> list[dict]:
    """
    Universal higher-order filter.

    Uses a predicate function.
    """

    return [
        student.copy()
        for student in students
        if predicate(student)
    ]


# ---------------------------------------------------------
# 8. CLOSURE
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# 9. GROUPING
# ---------------------------------------------------------

def group_students_by_group(
    students: list[dict],
) -> dict[str, list[dict]]:
    """
    Group students using defaultdict.
    """

    grouped = defaultdict(list)

    for student in students:
        grouped[
            student["group"]
        ].append(student.copy())

    return dict(grouped)


# ---------------------------------------------------------
# 10. COUNTER
# ---------------------------------------------------------

def count_students_by_group(
    students: list[dict],
) -> Counter:
    """
    Count students in every group.
    """

    return Counter(
        student["group"]
        for student in students
    )


# ---------------------------------------------------------
# 11. SET COMPREHENSION
# ---------------------------------------------------------

def get_unique_groups(
    students: list[dict],
) -> set[str]:
    """
    Return unique groups.
    """

    return {
        student["group"]
        for student in students
    }


# ---------------------------------------------------------
# 12. DICT COMPREHENSION
# ---------------------------------------------------------

def create_student_index(
    students: list[dict],
) -> dict[int, dict]:
    """
    Dictionary index by ID.

    Average lookup: O(1).
    """

    return {
        student["id"]: student
        for student in students
    }


# ---------------------------------------------------------
# 13. LINEAR SEARCH
# ---------------------------------------------------------

def find_student_by_id(
    students: list[dict],
    student_id: int,
) -> dict | None:
    """
    Linear O(n) search.
    """

    for student in students:
        if student["id"] == student_id:
            return student

    return None


# ---------------------------------------------------------
# 14. INDEX SEARCH
# ---------------------------------------------------------

def find_student_in_index(
    index: dict[int, dict],
    student_id: int,
) -> dict | None:
    """
    Average O(1) search.
    """

    return index.get(student_id)


# ---------------------------------------------------------
# 15. MAP EXAMPLE
# ---------------------------------------------------------

def get_student_names(
    students: list[dict],
) -> list[str]:
    """
    Demonstrate map().
    """

    return list(
        map(
            lambda student: student["name"],
            students,
        )
    )


# ---------------------------------------------------------
# 16. GENERATOR EXPRESSION
# ---------------------------------------------------------

def total_number_of_scores(
    students: list[dict],
) -> int:
    """
    Generator expression example.
    """

    return sum(
        len(student["scores"])
        for student in students
    )


# ---------------------------------------------------------
# 17. *ARGS
# ---------------------------------------------------------

def calculate_average_values(
    *values: float,
) -> float:
    """
    Demonstrate *args.
    """

    if not values:
        return 0.0

    return sum(values) / len(values)


# ---------------------------------------------------------
# 18. **KWARGS
# ---------------------------------------------------------

def create_record(
    **fields,
) -> dict:
    """
    Demonstrate **kwargs.
    """

    return dict(fields)


# ---------------------------------------------------------
# 19. TUPLE
# ---------------------------------------------------------

def get_score_statistics(
    students: list[dict],
) -> tuple[float, float, float]:
    """
    Return minimum, maximum and average score.

    Tuple is immutable.
    """

    all_scores = [
        score
        for student in students
        for score in student.get("scores", [])
    ]

    if not all_scores:
        return (0.0, 0.0, 0.0)

    return (
        min(all_scores),
        max(all_scores),
        sum(all_scores) / len(all_scores),
    )


# ---------------------------------------------------------
# 20. COMPOSE
# ---------------------------------------------------------

def compose(
    *functions: Callable,
) -> Callable:
    """
    Compose functions from left to right.

    compose(f, g, h)(x)
    -> h(g(f(x)))
    """

    def pipeline(value):
        result = value

        for function in functions:
            result = function(result)

        return result

    return pipeline


# ---------------------------------------------------------
# 21. PIPELINE
# ---------------------------------------------------------

def process_pipeline(
    students: list[dict],
    *operations: Callable[
        [list[dict]],
        list[dict],
    ],
) -> list[dict]:
    """
    Apply operations sequentially.
    """

    result = [
        student.copy()
        for student in students
    ]

    for operation in operations:
        result = operation(result)

    return result
