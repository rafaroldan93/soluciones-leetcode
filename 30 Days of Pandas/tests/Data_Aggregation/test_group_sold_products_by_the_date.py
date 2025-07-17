import pandas as pd
import pytest
from Data_Aggregation.group_sold_products_by_the_date import \
    categorize_products
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with multiple products sold on different dates
    (
        [
            ["2020-05-30", "Headphone"],
            ["2020-06-01", "Pencil"],
            ["2020-06-02", "Mask"],
            ["2020-05-30", "Basketball"],
            ["2020-06-01", "Bible"],
            ["2020-06-02", "Mask"],
            ["2020-05-30", "T-Shirt"]
        ],
        [
            ["2020-05-30", 3, "Basketball,Headphone,T-Shirt"],
            ["2020-06-01", 2, "Bible,Pencil"],
            ["2020-06-02", 1, "Mask"]
        ]
    ),
    # 2. Case with no products sold
    (
        [],
        []
    ),
    # 3. Case with all products sold on the same date
    (
        [
            ["2020-05-30", "Smartphone"],
            ["2020-05-30", "Tablet"],
            ["2020-05-30", "Smartwatch"]
        ],
        [
            ["2020-05-30", 3, "Smartphone,Smartwatch,Tablet"]
        ]
    ),
],
    ids=[
        "1. Basic case with multiple products sold on different dates",
        "2. Case with no products sold",
        "3. Case with all products sold on the same date"
]
)
def test_categorize_products(input_data: list[list[str]], expected_output: list[list[str]]) -> None:
    activities: pd.DataFrame = pd.DataFrame(input_data, columns=["sell_date", "product"])
    result: pd.DataFrame = categorize_products(activities).astype({"sell_date": "datetime64[ns]", "num_sold": "Int64", "products": "object"})
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["sell_date", "num_sold", "products"]).astype({
        "sell_date": "datetime64[ns]", "num_sold": "Int64", "products": "object"})
    assert_frame_equal(result, expected)
