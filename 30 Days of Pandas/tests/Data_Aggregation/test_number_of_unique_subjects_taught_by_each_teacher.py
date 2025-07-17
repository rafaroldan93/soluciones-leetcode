import pandas as pd
import pytest
from Data_Aggregation.number_of_unique_subjects_taught_by_each_teacher import \
    count_unique_subjects
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct teacher_id and subject_id
    (
        [
            [1, 2, 3],
            [1, 2, 4],
            [1, 3, 3],
            [2, 1, 1],
            [2, 2, 1],
            [2, 3, 1],
            [2, 4, 1]
        ],
        [
            [1, 2],
            [2, 4]
        ]
    ),
    # 2. Case with distinct teacher_id but unique subject_id
    (
        [
            [1, 2, 3],
            [1, 2, 4],
            [2, 1, 1],
            [2, 1, 2],
            [2, 1, 3],
            [2, 1, 4]
        ],
        [
            [1, 1],
            [2, 1]
        ]
    ),
    # 3. Case with no subjects
    (
        [],
        []
    )
],
    ids=[
        "1. Basic case with distinct teacher_id and subject_id",
        "2. Case with distinct teacher_id but unique subject_id",
        "3. Case with no subjects"
]
)
def test_count_unique_subjects(input_data: list[list[int]], expected_output: list[list[int]]) -> None:
    teacher: pd.DataFrame = pd.DataFrame(input_data, columns=["teacher_id", "subject_id", "dept_id"])
    result: pd.DataFrame = count_unique_subjects(teacher).astype({"teacher_id": "Int64", "cnt": "Int64"})
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["teacher_id", "cnt"]).astype({"teacher_id": "Int64", "cnt": "Int64"})
    assert_frame_equal(result, expected)
