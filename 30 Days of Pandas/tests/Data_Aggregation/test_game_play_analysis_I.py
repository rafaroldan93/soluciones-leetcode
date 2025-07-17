import pandas as pd
import pytest
from Data_Aggregation.game_play_analysis_I import game_analysis
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct player_id and event_date
    (
        [
            [1, 2, "2016-03-01", 5],
            [1, 2, "2016-05-02", 6],
            [2, 3, "2017-06-25", 1],
            [3, 1, "2016-03-02", 0],
            [3, 4, "2018-07-03", 5]
        ],
        [
            [1, "2016-03-01"],
            [2, "2017-06-25"],
            [3, "2016-03-02"]
        ]
    ),
    # 2. Only one player with multiple devices
    (
        [
            [1, 2, "2016-03-01", 5],
            [1, 3, "2016-05-02", 6],
            [1, 4, "2016-06-01", 2]
        ],
        [
            [1, "2016-03-01"]
        ]
    ),
    # 3. No entries in the activity table
    (
        [],
        []
    )
],
    ids=[
        "1. Basic case with distinct player_id and event_date",
        "2. Only one player with multiple devices",
        "3. No entries in the activity table"
])
def test_game_analysis(input_data: list[list[int | str]], expected_output: list[list[int | str]]) -> None:
    activity: pd.DataFrame = pd.DataFrame(input_data, columns=["player_id", "device_id", "event_date", "games_played"])
    result: pd.DataFrame = game_analysis(activity)
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["player_id", "first_login"])
    assert_frame_equal(result, expected)
