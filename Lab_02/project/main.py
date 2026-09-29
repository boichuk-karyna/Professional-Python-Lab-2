from src.data_processor.data import students
from src.data_processor.analytics import process_students


def main():
    result = process_students(
        students,
        min_scores=2,
        selected_group="KN-21",
        bonus=2.0,
        top_n=3,
    )

    print("Students:")

    for student in result["students"]:
        print(
            student["id"],
            student["name"],
            student["group"],
            student["average"],
        )

    print("\nTop students:")

    for student in result["top_n"]:
        print(
            student["name"],
            student["average"],
        )

    print("\nAggregation:")
    print(result["aggregation"])


if __name__ == "__main__":
    main()
