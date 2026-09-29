from collections import defaultdict


def calculate_average(scores):
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def calculate_average_values(*values):
    if not values:
        return 0.0

    return sum(values) / len(values)


def filter_by_min_scores(students, min_scores):
    return [
        student
        for student in students
        if len(student["scores"]) >= min_scores
    ]


def get_unique_groups(students):
    return {
        student["group"]
        for student in students
    }


def create_student_index(students):
    return {
        student["id"]: student
        for student in students
    }


def group_students_by_group(students):
    result = defaultdict(list)

    for student in students:
        result[student["group"]].append(student)

    return dict(result)


def create_min_scores_filter(min_scores):
    def predicate(student):
        return len(student["scores"]) >= min_scores

    return predicate


def filter_students(students, predicate):
    return [
        student
        for student in students
        if predicate(student)
    ]


def get_student_names(students):
    return [
        student["name"]
        for student in students
    ]


def get_score_statistics(students):
    all_scores = [
        score
        for student in students
        for score in student["scores"]
    ]

    if not all_scores:
        return (0, 0, 0.0)

    minimum = min(all_scores)
    maximum = max(all_scores)
    average = sum(all_scores) / len(all_scores)

    return minimum, maximum, average


def sort_students(students):
    return sorted(
        students,
        key=lambda student: (
            -student["average"],
            student["name"],
        ),
    )


def create_record(**kwargs):
    return dict(kwargs)
