import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from String_Methods.calculate_special_bonus import calculate_special_bonus


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with multiple bonus calculations
    (
        [
            [2, "Meir", 3000],
            [3, "Michael", 3800],
            [7, "Addilyn", 7400],
            [8, "Juan", 6100],
            [9, "Kannon", 7700]
        ],
        [
            [2, 0],
            [3, 0],
            [7, 7400],
            [8, 0],
            [9, 7700]
        ]
    ),
    # 2. No bonus calculations
    (
        [
            [2, "Meir", 3000],
            [3, "Michael", 3800],
            [6, "Addilyn", 7400],
            [8, "Juan", 6100],
            [10, "M.Kannon", 7700]
        ],
        [
            [2, 0],
            [3, 0],
            [6, 0],
            [8, 0],
            [10, 0]
        ]
    )
],
    ids=[
        "1. Basic case with multiple bonus calculations",
        "2. No bonus calculations"
]
)
def test_calculate_special_bonus(data: list[list[int | str]], expected_data: list[list[int | str]]) -> None:
    employees: pd.DataFrame = pd.DataFrame(data, columns=["employee_id", "name", "salary"]).astype({"employee_id": "int64", "name": "object", "salary": "int64"})
    result: pd.DataFrame = calculate_special_bonus(employees)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["employee_id", "bonus"]).astype({"employee_id": "int64", "bonus": "int64"})
    assert_frame_equal(result, expected, check_dtype=True)
