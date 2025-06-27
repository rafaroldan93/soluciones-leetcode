import pandas as pd
import pytest
from Data_Filtering.customers_who_never_order import find_customers
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("customers_data, orders_data, expected_data", [
    # 1. Basic case with customers who never ordered
    (
        [
            [1, "Joe"],
            [2, "Henry"],
            [3, "Sam"],
            [4, "Max"]
        ],
        [
            [1, 3],
            [2, 1]
        ],
        [
            ["Henry"],
            ["Max"]
        ]
    ),
    # 2. No customers who never ordered
    (
        [
            [1, "Joe"],
            [2, "Henry"],
            [3, "Sam"],
            [4, "Max"]
        ],
        [
            [1, 3],
            [2, 1],
            [3, 2],
            [4, 4]
        ],
        []
    )
],
    ids=[
    "1. Basic case with customers who never ordered",
        "2. No customers who never ordered"
]
)
def test_customers_who_never_order(customers_data: list[list[int | str]], orders_data: list[list[int]], expected_data: list[list[int]]) -> None:
    customers: pd.DataFrame = pd.DataFrame(customers_data, columns=["id", "name"]).astype({"id": "Int64", "name": "object"})
    orders: pd.DataFrame = pd.DataFrame(orders_data, columns=["id", "customerId"]).astype({"id": "Int64", "customerId": "Int64"})
    result: pd.DataFrame = find_customers(customers, orders).reset_index(drop=True)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["Customers"]).astype({"Customers": "object"})
    assert_frame_equal(result, expected, check_dtype=True)
