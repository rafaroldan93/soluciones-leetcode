import pandas as pd
import pytest
from Data_Manipulation.delete_duplicate_emails import delete_duplicate_emails
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct emails
    (
        [
            [1, "john@example.com"],
            [2, "bob@example.com"],
            [3, "john@example.com"]
        ], [
            [1, "john@example.com"],
            [2, "bob@example.com"]
        ]
    ),
    # 2. Case with all emails the same
    (
        [
            [1, "john@example.com"],
            [2, "john@example.com"],
            [3, "john@example.com"]
        ], [
            [1, "john@example.com"]
        ]
    ),
    # 3. Distinct emails but ids unordered
    (
        [
            [3, "john@example.com"],
            [1, "john@example.com"],
            [2, "john@example.com"]
        ], [
            [1, "john@example.com"]
        ]
    )
],
    ids=[
        "1. Basic case with distinct emails",
        "2. Case with all emails the same",
        "3. Distinct emails but ids unordered"
]
)
def test_delete_duplicate_emails(input_data: list[list[int | str]], expected_output: list[list[int | str]]) -> None:
    person: pd.DataFrame = pd.DataFrame(input_data, columns=["id", "email"]).astype({"id": "int64", "email": "object"})
    delete_duplicate_emails(person)
    person.reset_index(drop=True, inplace=True)
    assert_frame_equal(person, pd.DataFrame(expected_output, columns=["id", "email"]).astype({"id": "int64", "email": "object"}))
