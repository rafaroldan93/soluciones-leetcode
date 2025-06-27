import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from String_Methods.invalid_tweets import invalid_tweets


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with valid and invalid tweets
    (
        [
            [1, "Let us Code"],
            [2, "More than fifteen chars are here!"]
        ],
        [
            [2]
        ]
    ),
    # 2. All tweets are valid
    (
        [
            [1, "Short tweet"],
            [2, "Exactly 15 char"]
        ],
        []
    )
],
    ids=[
        "1. Basic case with valid and invalid tweets",
        "2. All tweets are valid"
]
)
def test_invalid_tweets(data: list[list[int | str]], expected_data: list[list[int]]) -> None:
    tweets: pd.DataFrame = pd.DataFrame(data, columns=["tweet_id", "content"]).astype({"tweet_id": "Int64", "content": "object"})
    result: pd.DataFrame = invalid_tweets(tweets).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["tweet_id"]).astype({"tweet_id": "Int64"})
    assert_frame_equal(result, expected, check_dtype=True)
