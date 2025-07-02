import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from String_Methods.find_users_with_valid_e_mail import valid_emails


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with multiple valid emails
    (
        [
            [1, "Winston", "winston@leetcode.com"],
            [2, "Jonathan", "jonathanisgreat"],
            [3, "Annabelle", "bella-@leetcode.com"],
            [4, "Sally", "sally.come@leetcode.com"],
            [5, "Marwan", "quarz#2020@leetcode.com"],
            [6, "David", "david69@gmail.com"],
            [7, "Shapiro", ".shapo@leetcode.com"]
        ],
        [
            [1, "Winston", "winston@leetcode.com"],
            [3, "Annabelle", "bella-@leetcode.com"],
            [4, "Sally", "sally.come@leetcode.com"]
        ]
    ),
    # 2. No valid emails
    (
        [
            [1, "Alice", "alice#gmail.com"],
            [2, "Bob", "bob@.com"],
            [3, "Charlie", "33charlie@leetcode"],
            [4, "Diana", "-diana@leetcode..com"],
            [5, "Eve", ".eve@leetcode.com"],
            [6, "Frank", "_frank@leetcode,com"],
            [7, "Grace", " grace@leetcode@com"],
            [8, "Hank", "$hank@leetcode..com"]
        ],
        []
    )
],
    ids=[
        "1. Basic case with multiple valid emails",
        "2. No valid emails"
]
)
def test_valid_emails(data: list[list[int | str]], expected_data: list[list[int | str]]) -> None:
    users: pd.DataFrame = pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype(
        {"user_id": "Int64", "name": "object", "mail": "object"})
    result: pd.DataFrame = valid_emails(users).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["user_id", "name", "mail"]).astype(
        {"user_id": "Int64", "name": "object", "mail": "object"})
    assert_frame_equal(result, expected, check_dtype=True)
