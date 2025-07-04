import pandas as pd
import pytest
from Data_Manipulation.nth_highest_salary import nth_highest_salary
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, n, expected_data", [
    # 1. Basic case with distinct salaries
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        2,
        [[200]]
    ),
    # 2. Case with duplicate salaries
    (
        [
            [1, 100],
            [2, 100],
            [3, 200]
        ],
        2,
        [[100]]
    ),
    # 3. Case with n equal to the number of distinct salaries
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        3,
        [[100]]
    ),
    # 4. Case with n greater than the number of distinct salaries
    (
        [
            [1, 100],
            [2, 200]
        ],
        3,
        [[None]]
    ),
    # 5. Case with n equal to 1 (highest salary)
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        1,
        [[300]]
    ),
    # 6. Case with n equal to 0
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        0,
        [[None]]
    ),
    # 7. Case with n negative
    (
        [
            [1, 100],
            [2, 200],
            [3, 300]
        ],
        -1,
        [[None]]
    )
],
    ids=[
        "1. Basic case with distinct salaries",
        "2. Case with less than n distinct salaries",
        "3. Case with n equal to the number of distinct salaries",
        "4. Case with n greater than the number of distinct salaries",
        "5. Case with n equal to 1 (highest salary)",
        "6. Case with n equal to 0 (invalid case)",
        "7. Case with n negative (invalid case)"
]
)
def test_nth_highest_salary(data: list[list[int]], n: int, expected_data: list[list[int]] | list[list[None]]) -> None:
    employee: pd.DataFrame = pd.DataFrame(data, columns=["id", "salary"]).astype({"id": "int64", "salary": "int64"})
    result: pd.DataFrame = nth_highest_salary(employee, n).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=[f"getNthHighestSalary({n})"])
    assert_frame_equal(result, expected, check_dtype=True)
