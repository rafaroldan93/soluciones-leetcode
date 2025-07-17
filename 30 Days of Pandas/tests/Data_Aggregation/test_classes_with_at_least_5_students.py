import pandas as pd
import pytest
from Data_Aggregation.classes_with_at_least_5_students import find_classes
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with classes having at least 5 students
    (
        [
            ["A", "Math"],
            ["B", "English"],
            ["C", "Math"],
            ["D", "Biology"],
            ["E", "Math"],
            ["F", "Computer"],
            ["G", "Math"],
            ["H", "Math"],
            ["I", "Math"]
        ],
        [
            ["Math"]
        ]
    ),
    # 2. Case with no classes having at least 5 students
    (
        [
            ["A", "English"],
            ["B", "Biology"],
            ["C", "Computer"]
        ],
        []
    ),
    # 3. Case with multiple classes, some with and some without enough students
    (
        [
            ["A", "Math"],
            ["B", "Math"],
            ["C", "Math"],
            ["D", "Math"],
            ["E", "Math"],
            ["F", "Biology"],
            ["G", "Biology"],
            ["H", "Biology"],
            ["I", "Biology"],
            ["J", "Biology"],
            ["K", "Biology"],
            ["L", "Computer"]
        ],
        [
            ["Biology"],
            ["Math"]
        ]
    ),
],
    ids=[
        "1. Basic case with classes having at least 5 students",
        "2. Case with no classes having at least 5 students",
        "3. Case with multiple classes, some with and some without enough students"
]
)
def test_find_classes(input_data: list[list[str]], expected_output: list[list[str]]) -> None:
    courses: pd.DataFrame = pd.DataFrame(input_data, columns=["student", "class"])
    result: pd.DataFrame = find_classes(courses).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["class"])
    assert_frame_equal(result, expected)
