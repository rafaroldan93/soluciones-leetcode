import pandas as pd
import pytest
from Data_Manipulation.rank_scores import order_scores
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with distinct scores
    (
        [
            [1, 3.5],
            [2, 3.65],
            [3, 4.0],
            [4, 3.85],
            [5, 4.0],
            [6, 3.65]
        ],
        [
            [4.0, 1],
            [4.0, 1],
            [3.85, 2],
            [3.65, 3],
            [3.65, 3],
            [3.5, 4]
        ]
    ),
    # 2. Case with all scores the same
    (
        [
            [1, 3.5],
            [2, 3.5],
            [3, 3.5]
        ],
        [
            [3.5, 1],
            [3.5, 1],
            [3.5, 1]
        ]
    ),
    # 3. Case with descending scores
    (
        [
            [1, 4.0],
            [2, 3.8],
            [3, 3.6]
        ],
        [
            [4.0, 1],
            [3.8, 2],
            [3.6, 3]
        ]
    ),
    # 4. Case with ascending scores
    (
        [
            [1, 3.0],
            [2, 3.2],
            [3, 3.4]
        ],
        [
            [3.4, 1],
            [3.2, 2],
            [3.0, 3]
        ]
    ),
    # 5. Case with mixed scores and ties
    (
        [
            [1, 3.5],
            [2, 3.65],
            [3, 4.0],
            [4, 3.85],
            [5, 4.0],
            [6, 3.65],
            [7, 3.5]
        ],
        [
            [4.0, 1],
            [4.0, 1],
            [3.85, 2],
            [3.65, 3],
            [3.65, 3],
            [3.5, 4],
            [3.5, 4]
        ]
    )
],
    ids=[
    "1. Basic case with distinct scores",
    "2. All scores the same",
    "3. Descending scores",
    "4. Ascending scores",
    "5. Mixed scores with ties"
]
)
def test_order_scores(data: list[list[int | float]], expected_data: list[list[float | int]]) -> None:
    scores: pd.DataFrame = pd.DataFrame(data, columns=["id", "score"])
    result: pd.DataFrame = order_scores(scores).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["score", "rank"])
    assert_frame_equal(result, expected)
