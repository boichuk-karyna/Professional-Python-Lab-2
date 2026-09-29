from src.data_processor.data import students

from src.data_processor.processors import (
    calculate_average_values,
    count_students_by_group,
    create_record,
    create_student_index,
    create_min_scores_filter,
    filter_students,
    get_score_statistics,
    get_student_names,
    get_unique_groups,
    group_students_by_group,
    total_number_of_scores,
)

from src.data_processor.analytics import (
    calculate_average_for_students,
    process_students,
)


def print_students(
    title: str,
    items: list[dict],
) -> None:

    print()
    print(title)
    print("-" * 80)

    for student in items:

        average = student.get(
            "average",
            0.0,
        )

        print(
            f"{student['id']:2} | "
            f"{student['name']:<22} | "
            f"{student['group']:<6} | "
            f"scores={student['scores']} | "
            f"average={average:.2f}"
        )


def main() -> None:

    print_students(
        "ALL STUDENTS",
        students,
    )

    # -----------------------------------------------------
    # SET
    # -----------------------------------------------------

    groups = get_unique_groups(
        students
    )

    print(
        "\nUnique groups:",
        groups,
    )

    # -----------------------------------------------------
    # DICT INDEX
    # -----------------------------------------------------

    index = create_student_index(
        students
    )

    print(
        "\nSearch by dictionary index:",
        index.get(4),
    )

    # -----------------------------------------------------
    # LINEAR SEARCH
    # -----------------------------------------------------

    from src.data_processor.processors import (
        find_student_by_id,
    )

    print(
        "\nLinear search:",
        find_student_by_id(
            students,
            3,
        ),
    )

    # -----------------------------------------------------
    # CLOSURE
    # -----------------------------------------------------

    predicate = create_min_scores_filter(
        3
    )

    students_with_three_scores = filter_students(
        students,
        predicate,
    )

    print_students(
        "STUDENTS WITH AT LEAST 3 SCORES",
        students_with_three_scores,
    )

    # -----------------------------------------------------
    # MAP
    # -----------------------------------------------------

    names = get_student_names(
        students
    )

    print(
        "\nNames via map:",
        names,
    )

    # -----------------------------------------------------
    # GENERATOR
    # -----------------------------------------------------

    scores_count = total_number_of_scores(
        students
    )

    print(
        "\nTotal number of scores:",
        scores_count,
    )

    # -----------------------------------------------------
    # TUPLE
    # -----------------------------------------------------

    statistics = get_score_statistics(
        students
    )

    print(
        "\nScore statistics tuple:",
        statistics,
    )

    # -----------------------------------------------------
    # COUNTER
    # -----------------------------------------------------

    counter = count_students_by_group(
        students
    )

    print(
        "\nStudents by group:",
        counter,
    )

    # -----------------------------------------------------
    # FULL PIPELINE
    # -----------------------------------------------------

    result = process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    print_students(
        "PROCESSED AND SORTED STUDENTS",
        result["students"],
    )

    print_students(
        "TOP 3",
        result["top_n"],
    )

    # -----------------------------------------------------
    # REDUCE
    # -----------------------------------------------------

    print(
        "\nREDUCE AGGREGATION:"
    )

    print(
        "count:",
        result["aggregation"]["count"],
    )

    print(
        "sum_avg:",
        result["aggregation"]["sum_avg"],
    )

    print(
        "group_avg:",
        result["aggregation"]["group_avg"],
    )

    # -----------------------------------------------------
    # DECORATOR
    # -----------------------------------------------------

    average = calculate_average_for_students(
        result["students"]
    )

    print(
        "\nAverage:",
        average,
    )

    # -----------------------------------------------------
    # *ARGS
    # -----------------------------------------------------

    demo_average = calculate_average_values(
        80,
        90,
        100,
    )

    print(
        "\nAverage via *args:",
        demo_average,
    )

    # -----------------------------------------------------
    # **KWARGS
    # -----------------------------------------------------

    record = create_record(
        id=100,
        name="Test Student",
        group="KN-99",
        scores=[90, 95],
    )

    print(
        "\nRecord via **kwargs:",
        record,
    )

    # -----------------------------------------------------
    # GROUPING
    # -----------------------------------------------------

    grouped = group_students_by_group(
        students
    )

    print(
        "\nGrouped students:"
    )

    for group, members in grouped.items():
        print(
            group,
            "->",
            len(members),
        )


if __name__ == "__main__":
    main()
