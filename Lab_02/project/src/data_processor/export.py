import json


def export_summary(
    summary: dict,
    filename: str = "summary.json",
) -> None:

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            summary,
            file,
            ensure_ascii=False,
            indent=4,
        )