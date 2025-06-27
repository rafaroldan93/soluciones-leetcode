import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from String_Methods.fix_names_in_a_table import fix_names


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with multiple names
    (
        [
            [1, "aLice"],
            [2, "bOB"]
        ],
        [
            [1, "Alice"],
            [2, "Bob"]
        ]
    ),
    # 2. No names to fix
    (
        [
            [1, "Charlie"],
            [2, "Rafael"]
        ],
        [
            [1, "Charlie"],
            [2, "Rafael"]
        ]
    )],
    ids=[
        "1. Basic case with multiple names",
        "2. No names to fix"
]
)
def test_fix_names(data: list[list[int | str]], expected_data: list[list[int | str]]) -> None:
    users: pd.DataFrame = pd.DataFrame(data, columns=["user_id", "name"]).astype(
        {"user_id": "Int64", "name": "object"})
    users: pd.DataFrame = pd.DataFrame(data, columns=["user_id", "name"]).astype(
        {"user_id": "Int64", "name": "object"})
    result: pd.DataFrame = fix_names(users).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["user_id", "name"]).astype(
        {"user_id": "Int64", "name": "object"})
    assert_frame_equal(result, expected, check_dtype=True)
