"""Input data for Lab_02 — Student Analysis, Variant 2."""

students = [
    {
        "id": 1,
        "name": "Anna Koval",
        "group": "PI-21",
        "scores": [90, 92, 88, 95],
    },
    {
        "id": 2,
        "name": "Oleh Melnyk",
        "group": "PI-21",
        "scores": [75, 80, 82],
    },
    {
        "id": 3,
        "name": "Iryna Bondar",
        "group": "PI-22",
        "scores": [98, 95, 97, 100, 96],
    },
    {
        "id": 4,
        "name": "Andrii Shevchenko",
        "group": "PI-21",
        "scores": [85, 87, 90, 88],
    },
    {
        "id": 5,
        "name": "Maria Boyko",
        "group": "PI-22",
        "scores": [70, 78],
    },
    {
        "id": 6,
        "name": "Taras Novak",
        "group": "PI-23",
        "scores": [91, 89, 94, 90],
    },
    {
        "id": 7,
        "name": "Olena Tkachenko",
        "group": "PI-23",
        "scores": [82, 84, 86],
    },
    {
        "id": 8,
        "name": "Dmytro Kovalenko",
        "group": "PI-22",
        "scores": [93, 91, 89, 95],
    },
]


# Tuple — immutable configuration.
ANALYSIS_CONFIG = (
    3,       # minimum number of scores
    5,       # Top-N
    "PI-22", # group receiving bonus
    5.0,     # bonus
)
