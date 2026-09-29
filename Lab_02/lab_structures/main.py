from src.data_processor.data import students
from src.data_processor.student_processor import (
    process_students,
)


def main() -> None:
    result = process_students(
        students=students,
        min_scores=2,
        selected_group="KN-21",
        bonus=5.0,
        top_n=3,
    )

    print("\nAll processed students:")
    print("-" * 60)

    for student in result["students"]:
        print(
            f'{student["id"]}: '
            f'{student["name"]} | '
            f'{student["group"]} | '
            f'average={student["average"]:.2f}'
        )

    print("\nTop-N:")
    print("-" * 60)

    for student in result["top_n"]:
        print(
            f'{student["name"]}: '
            f'{student["average"]:.2f}'
        )

    print("\nAggregation:")
    print("-" * 60)

    aggregation = result["aggregation"]

    print(f'count: {aggregation["count"]}')
    print(f'sum_avg: {aggregation["sum_avg"]:.2f}')

    print("group_avg:")

    for group, average in aggregation["group_avg"].items():
        print(f"  {group}: {average:.2f}")


if __name__ == "__main__":
    main()
