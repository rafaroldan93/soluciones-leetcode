import pandas as pd
import pytest
from Data_Manipulation.rearrange_products_table import rearrange_products_table
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with all products available in all stores
    (
        [
            [0, 95, 100, 105],
            [1, 70, None, 80]
        ], [
            [0, "store1", 95],
            [1, "store1", 70],
            [0, "store2", 100],
            [0, "store3", 105],
            [1, "store3", 80]
        ]
    ),
    # 2. Case with some products not available in some stores
    (
        [
            [2, None, 200, None],
            [3, 150, None, 180]
        ], [
            [3, "store1", 150],
            [2, "store2", 200],
            [3, "store3", 180]
        ]
    ),
    # 3. Case with all products not available in all stores
    (
        [
            [4, None, None, None],
            [5, None, None, None]
        ], []
    )
],
    ids=[
        "1. Basic case with all products available in all stores",
        "2. Case with some products not available in some stores",
        "3. Case with all products not available in all stores"
]
)
def test_rearrange_products_table(input_data: list[list[int | None]], expected_output: list[list[int | str]]) -> None:
    products: pd.DataFrame = pd.DataFrame(input_data, columns=["product_id", "store1", "store2", "store3"]).astype(
        {"product_id": "Int64", "store1": "Int64", "store2": "Int64", "store3": "Int64"})
    result: pd.DataFrame = rearrange_products_table(products).reset_index(drop=True)
    expected_df: pd.DataFrame = pd.DataFrame(expected_output, columns=["product_id", "store", "price"]).astype(
        {"product_id": "Int64", "store": "object", "price": "Int64"})
    assert_frame_equal(result, expected_df)
