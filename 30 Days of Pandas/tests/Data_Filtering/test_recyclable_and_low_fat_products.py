import pandas as pd
import pytest
from Data_Filtering.recyclable_and_low_fat_products import find_products
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("data, expected_data", [
    # 1. Basic case with low fat and recyclable products
    (
        [
            ["0", "Y", "N"],
            ["1", "Y", "Y"],
            ["2", "N", "Y"],
            ["3", "Y", "Y"],
            ["4", "N", "N"]
        ],
        [[1],
         [3]
         ]
    ),
    # 2. No low fat and recyclable products
    (
        [
            ["0", "Y", "N"],
            ["1", "N", "N"],
            ["2", "N", "Y"],
            ["3", "N", "N"],
            ["4", "N", "N"]
        ],
        []
    )
],
    ids=[
    "1. Basic case with low fat and recyclable products",
    "2. No low fat and recyclable products"
]
)
def test_find_products(data: list[list[str]], expected_data: list[list[int]]) -> None:
    products: pd.DataFrame = pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
        {"product_id": "int64", "low_fats": "category", "recyclable": "category"})
    result: pd.DataFrame = find_products(products).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["product_id"]).astype({"product_id": "int64"})
    assert_frame_equal(result, expected, check_dtype=True)
