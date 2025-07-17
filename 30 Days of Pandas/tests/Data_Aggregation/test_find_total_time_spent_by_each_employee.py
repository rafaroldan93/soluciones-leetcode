import pandas as pd
import pytest
from Data_Aggregation.find_total_time_spent_by_each_employee import total_time
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct in_time and out_time
    (
        [
            [1, "2020-11-28", 4, 32],
            [1, "2020-11-28", 55, 200],
            [1, "2020-12-03", 1, 42],
            [2, "2020-11-28", 3, 33],
            [2, "2020-12-09", 47, 74]
        ],
        [
            ["2020-11-28", 1, 173],
            ["2020-11-28", 2, 30],
            ["2020-12-03", 1, 41],
            ["2020-12-09", 2, 27]
        ]
    ),
    # 2. Case with multiple entries on the same day
    (
        [
            [1, "2020-11-28", 10, 20],
            [1, "2020-11-28", 30, 50],
            [2, "2020-11-28", 5, 15],
            [2, "2020-11-28", 25, 35]
        ],
        [
            ["2020-11-28", 1, 30],
            ["2020-11-28", 2, 20]
        ]
    ),
    # 3. Case with no entries
    (
        [],
        []
    )
],
    ids=[
        "1. Basic case with distinct in_time and out_time",
        "2. Case with multiple entries on the same day",
        "3. Case with no entries"
]
)
def test_total_time(input_data: list[list[int | str]], expected_output: list[list[str | int]]) -> None:
    employees: pd.DataFrame = pd.DataFrame(input_data, columns=["emp_id", "event_day", "in_time", "out_time"])
    result: pd.DataFrame = total_time(employees)
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["day", "emp_id", "total_time"])
    assert_frame_equal(result, expected)
