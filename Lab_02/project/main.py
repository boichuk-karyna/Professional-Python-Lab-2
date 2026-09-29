"""Main program for Lab_02, Variant 2."""

from functools import reduce
from time import perf_counter

from data_processor.analytics import (
    aggregate_students,
    calculate_average_values,
    calculate_overall_average,
    compose,
    create_average_filter,
    create_record,
)

from data_processor.data import (
    ANALYSIS_CONFIG,
    students,
)

from data_processor.processors import (
    apply_group_bonus,
    count_by_group,
    create_student_index,
    filter_by_min_scores,
    filter_items,
    find_student_by_id,
    get_unique_groups,
    group_students,
    sort_students,
    top_n_students,
    transform_with_average,
)


def print_students(
    title: str,
    items: list[dict],
) -> None:
    """Print students in table form."""

    print(f"\n{title}")
    print("-" * 80)

    print(
        f"{'ID':<5}"
        f"{'Name':<25}"
        f"{'Group':<10}"
        f"{'Scores':<25}"
        f"{'Average':<10}"
    )

    print("-" * 80)

    for student in items:
        scores = ", ".join(
            str(score)
            for score in student["scores"]
        )

        print(
            f"{student['id']:<5}"
            f"{student['name']:<25}"
            f"{student['group']:<10}"
            f"{scores:<25}"
            f"{student['average']:<10.2f}"
        )


def run_benchmark() -> None:
    """Compare linear list search with dictionary search."""

    print("\n=== BENCHMARK ===")
    print("-" * 80)

    print(
        f"{'Records':<15}"
        f"{'List search':<20}"
        f"{'Dict search':<20}"
    )

    for size in (
        1_000,
        10_000,
        100_000,
    ):
        test_data = [
            {
                "id": i,
                "name": f"Student {i}",
                "group": f"PI-{i % 10}",
                "scores": [70, 80, 90],
                "average": 80.0,
            }
            for i in range(size)
        ]

        target_id = size - 1

        start = perf_counter()

        for student in test_data:
            if student["id"] == target_id:
                break

        list_time = (
            perf_counter()
            - start
        )

        index = {
            student["id"]: student
            for student in test_data
        }

        start = perf_counter()

        index.get(target_id)

        dict_time = (
            perf_counter()
            - start
        )

        print(
            f"{size:<15}"
            f"{list_time:<20.8f}"
            f"{dict_time:<20.8f}"
        )


def main() -> None:
    """Run the complete student analysis."""

    minimum_scores, top_n, bonus_group, bonus = (
        ANALYSIS_CONFIG
    )

    print(
        "=== LAB_02 — ВАРІАНТ 2 ==="
    )
    print(
        "Аналіз системи оцінювання студентів"
    )

    # Перевірка відсутності мутації.
    original_students = [
        {
            **student,
            "scores": list(student["scores"]),
        }
        for student in students
    ]

    # 1. Фільтрація за кількістю оцінок.
    filtered = filter_by_min_scores(
        students,
        minimum_scores,
    )

    # 2. Додавання середнього бала.
    with_average = transform_with_average(
        filtered
    )

    print_students(
        "Студенти з достатньою кількістю оцінок",
        with_average,
    )

    # 3. Closure для фільтрації.
    excellent_filter = create_average_filter(
        90
    )

    excellent = filter_items(
        with_average,
        excellent_filter,
    )

    print_students(
        "Студенти із середнім балом >= 90",
        excellent,
    )

    # 4. Додавання бонусу вибраній групі.
    with_bonus = apply_group_bonus(
        with_average,
        bonus_group,
        bonus,
    )

    print_students(
        f"Після бонусу +{bonus} "
        f"для групи {bonus_group}",
        with_bonus,
    )

    # 5. Сортування за двома ключами.
    ranking = sort_students(
        with_bonus
    )

    print_students(
        "Повний рейтинг",
        ranking,
    )

    # 6. Top-N.
    top_students = top_n_students(
        with_bonus,
        top_n,
    )

    print_students(
        f"Top-{top_n}",
        top_students,
    )

    # 7. Унікальні групи.
    groups = get_unique_groups(
        with_bonus
    )

    print(
        "\nУнікальні групи:",
        groups,
    )

    # 8. Групування.
    grouped = group_students(
        with_bonus
    )

    print("\nГрупування:")

    for group, members in grouped.items():
        print(
            f"{group}: "
            f"{len(members)} студентів"
        )

    # 9. Counter.
    group_counter = count_by_group(
        with_bonus
    )

    print(
        "\nCounter груп:",
        dict(group_counter),
    )

    # 10. Dict index.
    index = create_student_index(
        with_bonus
    )

    print(
        "\nDict-index, ID=3:",
        index.get(3),
    )

    # 11. Linear search.
    found = find_student_by_id(
        with_bonus,
        3,
    )

    print(
        "\nПошук студента ID=3:",
        found,
    )

    # 12. Reduce aggregation.
    statistics = aggregate_students(
        with_bonus
    )

    print("\n=== AGGREGATION ===")
    print(
        "count:",
        statistics["count"],
    )
    print(
        "sum_avg:",
        f"{statistics['sum_avg']:.2f}",
    )
    print(
        "group_avg:",
        {
            group: round(value, 2)
            for group, value
            in statistics["group_avg"].items()
        },
    )

    # 13. Загальний середній бал.
    overall = calculate_overall_average(
        with_bonus
    )

    print(
        "\nЗагальний середній бал:",
        f"{overall:.2f}",
    )

    # 14. *args.
    demo_average = calculate_average_values(
        80,
        85,
        90,
        95,
    )

    print(
        "\nAverage через *args:",
        demo_average,
    )

    # 15. **kwargs.
    new_student = create_record(
        id=99,
        name="Test Student",
        group="PI-99",
        scores=[90, 90, 90],
    )

    print(
        "\nЗапис через **kwargs:",
        new_student,
    )

    # 16. Composition / pipeline.
    pipeline = compose(
        lambda data: filter_by_min_scores(
            data,
            3,
        ),
        transform_with_average,
        lambda data: apply_group_bonus(
            data,
            bonus_group,
            bonus,
        ),
        sort_students,
    )

    pipeline_result = pipeline(
        students
    )

    print_students(
        "Результат function composition",
        pipeline_result,
    )

    # 17. Перевірка, що початкові дані не змінилися.
    assert students == original_students

    print(
        "\nПеревірка immutability: PASSED"
    )

    # 18. Benchmark.
    run_benchmark()


if __name__ == "__main__":
    main()
