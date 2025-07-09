import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from Statistics.count_salary_categories import count_salary_categories


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct income values
    (
        [
            [3, 108939],
            [2, 12747],
            [8, 87709],
            [6, 91796]
        ], [
            ["Low Salary", 1],
            ["Average Salary", 0],
            ["High Salary", 3]
        ]
    ),
    # 2. All incomes in the low salary category
    (
        [
            [1, 15000],
            [2, 18000],
            [3, 19999]
        ], [
            ["Low Salary", 3],
            ["Average Salary", 0],
            ["High Salary", 0]
        ]
    ),
    # 3. All incomes in the average salary category
    (
        [
            [1, 20000],
            [2, 30000],
            [3, 50000]
        ], [
            ["Low Salary", 0],
            ["Average Salary", 3],
            ["High Salary", 0]
        ]
    ),
    # 4. All incomes in the high salary category
    (
        [
            [1, 60000],
            [2, 70000],
            [3, 80000]
        ], [
            ["Low Salary", 0],
            ["Average Salary", 0],
            ["High Salary", 3]
        ]
    )
],
    ids=[
        "1. Basic case with distinct income values",
        "2. All incomes in the low salary category",
        "3. All incomes in the average salary category",
        "4. All incomes in the high salary category"
]
)
def test_count_salary_categories(input_data: list[list[int]], expected_output: list[list[str | int]]) -> None:
    accounts: pd.DataFrame = pd.DataFrame(input_data, columns=["account_id", "income"]).astype({"account_id": "Int64", "income": "Int64"})
    result: pd.DataFrame = count_salary_categories(accounts)
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["category", "accounts_count"]).astype({"category": "object", "accounts_count": "int64"})
    assert_frame_equal(result, expected)
