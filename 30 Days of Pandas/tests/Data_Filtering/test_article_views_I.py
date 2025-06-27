import pandas as pd
import pytest
from Data_Filtering.article_views_I import article_views
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with multiple views
    (
        [
            [1, 3, 5, "2019-08-01"],
            [1, 3, 6, "2019-08-02"],
            [2, 7, 7, "2019-08-01"],
            [2, 7, 6, "2019-08-02"],
            [4, 7, 1, "2019-07-22"],
            [3, 4, 4, "2019-07-21"],
            [3, 4, 4, "2019-07-21"]
        ],
        [
            [4],
            [7]
        ]
    ),
    # 2. No views
    (
        [
            [1, 3, 5, "2019-08-01"],
            [2, 7, 6, "2019-08-02"],
        ],
        []
    )
],
    ids=[
    "1. Basic case with multiple views",
    "2. No views"
])
def test_article_views(data: list[int | str], expected_data: list[int]) -> None:
    views: pd.DataFrame = pd.DataFrame(data, columns=["article_id", "author_id", "viewer_id", "view_date"]).astype(
        {"article_id": "Int64", "author_id": "Int64", "viewer_id": "Int64", "view_date": "datetime64[ns]"})
    result: pd.DataFrame = article_views(views).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["id"]).astype({"id": "Int64"})
    assert_frame_equal(result, expected, check_dtype=True)
