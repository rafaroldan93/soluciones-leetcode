import pandas as pd
import pytest
from Data_Aggregation.customer_placing_the_largest_number_of_orders import \
    largest_orders
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("input_data, expected_output", [
    # 1. Basic case with one customer having the most orders
    (
        [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 3]
        ],
        [
            [3]
        ]
    ),
    # 2. Case with multiple customers having the most orders
    (
        [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 3],
            [5, 2]
        ],
        [
            [2],
            [3]
        ]
    ),
    # 3. Case with no orders
    (
        [],
        []
    ),
],
    ids=[
        "1. Basic case with one customer having the most orders",
        "2. Case with multiple customers having the most orders",
        "3. Case with no orders"
]
)
def test_largest_orders(input_data: list[list[int]], expected_output: list[list[int]]) -> None:
    orders: pd.DataFrame = pd.DataFrame(input_data, columns=["order_number", "customer_number"])
    result: pd.DataFrame = largest_orders(orders).astype({"customer_number": "Int64"})
    expected: pd.DataFrame = pd.DataFrame(expected_output, columns=["customer_number"]).astype({"customer_number": "Int64"})
    assert_frame_equal(result, expected)
