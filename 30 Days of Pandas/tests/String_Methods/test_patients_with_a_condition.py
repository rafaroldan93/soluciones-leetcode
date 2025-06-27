import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from String_Methods.patients_with_a_condition import find_patients


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with patients having Type I Diabetes
    (
        [
            [1, 'Daniel', 'YFEV COUGH'],
            [2, 'Alice', ''],
            [3, 'Bob', 'DIAB100 MYOP'],
            [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201']
        ],
        [
            [3, 'Bob', 'DIAB100 MYOP'],
            [4, 'George', 'ACNE DIAB100']
        ]
    ),
    # 2. No patients with Type I Diabetes
    (
        [
            [1, 'Daniel', 'YFEV COUGH'],
            [2, 'Alice', ''],
            [5, 'Alain', 'DIAB201']
        ],
        []
    )
], ids=[
    "1. Basic case with patients having Type I Diabetes",
    "2. No patients with Type I Diabetes"
]
)
def test_find_patients(data: list[list[int | str]], expected_data: list[list[int | str]]) -> None:
    patients: pd.DataFrame = pd.DataFrame(data, columns=["patient_id", "patient_name", "conditions"]).astype({
        "patient_id": "int64", "patient_name": "object", "conditions": "object"})
    result: pd.DataFrame = find_patients(patients).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["patient_id", "patient_name", "conditions"]).astype({
        "patient_id": "int64", "patient_name": "object", "conditions": "object"})
    assert_frame_equal(result, expected, check_dtype=True)
