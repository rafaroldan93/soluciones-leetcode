import pandas as pd
import pytest
from Data_Manipulation.second_highest_salary import second_highest_salary
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with distinct salaries
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        [[200]]
    ),
    # 2. Case with duplicate salaries
    (
        [
            [1, 100],
            [2, 100],
            [3, 200]
        ],
        [[100]]
    ),
    # 3. Case with only one salary
    (
        [
            [1, 100]
        ],
        [[None]]
    ),
    # 4. Case with no salaries
    (
        [],
        [[None]]
    ),
    # 5. Case with multiple salaries but no second highest
    (
        [
            [1, 100],
            [2, 100],
            [3, 100]
        ],
        [[None]]
    )
],
    ids=[
    "1. Basic case with distinct salaries",
    "2. Case with duplicate salaries",
    "3. Case with only one salary",
    "4. Case with no salaries",
    "5. Case with multiple salaries but no second highest"
]
)
def test_second_highest_salary(data: list[list[int]], expected_data: list[list[int]] | list[list[None]]):
    employee: pd.DataFrame = pd.DataFrame(data, columns=["id", "salary"]).astype({"id": "int64", "salary": "int64"})
    result: pd.DataFrame = second_highest_salary(employee).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["SecondHighestSalary"])
    assert_frame_equal(result, expected, check_dtype=False)
