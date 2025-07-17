import pandas as pd
import pytest
from Data_Aggregation.daily_leads_and_partners import daily_leads_and_partners
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with distinct and duplicates leads and partners
    (
        [
            ["2020-12-8", "toyota", 0, 1],
            ["2020-12-8", "toyota", 1, 0],
            ["2020-12-8", "toyota", 1, 2],
            ["2020-12-7", "toyota", 0, 2],
            ["2020-12-7", "toyota", 0, 1],
            ["2020-12-8", "honda", 1, 2],
            ["2020-12-8", "honda", 2, 1],
            ["2020-12-7", "honda", 0, 1],
            ["2020-12-7", "honda", 1, 2],
            ["2020-12-7", "honda", 2, 1]
        ],
        [
            ["2020-12-7", "honda", 3, 2],
            ["2020-12-7", "toyota", 1, 2],
            ["2020-12-8", "honda", 2, 2],
            ["2020-12-8", "toyota", 2, 3]
        ]
    ),
    # 2. Case with no entries
    (
        [],
        []
    ),
    # 3. Case with no duplicates
    (
        [
            ["2020-12-8", "toyota", 0, 1],
            ["2020-12-8", "toyota", 1, 2],
            ["2020-12-7", "toyota", 0, 2],
            ["2020-12-7", "toyota", 1, 1],
            ["2020-12-8", "honda", 1, 2],
            ["2020-12-8", "honda", 2, 1],
            ["2020-12-7", "honda", 0, 1],
            ["2020-12-7", "honda", 1, 2]
        ],
        [
            ["2020-12-7", "honda", 2, 2],
            ["2020-12-7", "toyota", 2, 2],
            ["2020-12-8", "honda", 2, 2],
            ["2020-12-8", "toyota", 2, 2]
        ]
    )
],
    ids=[
        "1. Basic case with distinct and duplicates leads and partners",
        "2. Case with no entries",
        "3. Case with no duplicates"
])
def test_daily_leads_and_partners(input_data: list[list[str | int]], expected_output: list[list[str | int]]) -> None:
    daily_sales: pd.DataFrame = pd.DataFrame(input_data, columns=["date_id", "make_name", "lead_id", "partner_id"])
    result: pd.DataFrame = daily_leads_and_partners(daily_sales).astype(
        {"date_id": "datetime64[ns]", "make_name": "object", "unique_leads": "Int64", "unique_partners": "Int64"})
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["date_id", "make_name", "unique_leads", "unique_partners"]).astype(
        {"date_id": "datetime64[ns]", "make_name": "object", "unique_leads": "Int64", "unique_partners": "Int64"})
    assert_frame_equal(result, expected)
