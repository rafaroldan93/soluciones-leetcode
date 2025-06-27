import pandas as pd
import pytest
from Data_Filtering.big_countries import big_countries
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, expected_data", [
    (
        # 1. Basic case with multiple big countries
        [
            ["Afghanistan", "Asia", 652230, 25500100, 20343000000],
            ["Albania", "Europe", 28748, 2831741, 12960000000],
            ["Algeria", "Africa", 2381741, 37100000, 188681000000],
            ["Andorra", "Europe", 468, 78115, 3712000000],
            ["Angola", "Africa", 1246700, 20609294, 100990000000]
        ],
        [
            ["Afghanistan", 25500100, 652230],
            ["Algeria", 37100000, 2381741]
        ]
    ),
    (
        # 2. No big countries
        [
            ["Andorra", "Europe", 468, 78115, 3712000000],
            ["Angola", "Africa", 1246700, 20609294, 100990000000]
        ],
        []
    )
],
    ids=[
    "1. Basic case with multiple big countries",
        "2. No big countries"
]
)
def test_big_countries(data: list[list[str | int]], expected_data: list[list[str | int]]) -> None:
    world: pd.DataFrame = pd.DataFrame(data, columns=["name", "continent", "area", "population", "gdp"]).astype(
        {"name": "object", "continent": "object", "area": "Int64", "population": "Int64", "gdp": "Int64"})
    result: pd.DataFrame = big_countries(world).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["name", "population", "area"]).astype(
        {"name": "object", "population": "Int64", "area": "Int64"})
    assert_frame_equal(result, expected, check_dtype=True)
