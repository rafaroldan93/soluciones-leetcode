"""1757. Recyclable and Low Fat Products
Tags: Easy, Database, Pandas

Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ("Y", "N") where "Y" means this product is low fat and "N" means it is not.
recyclable is an ENUM (category) of types ("Y", "N") where "Y" means this product is recyclable and "N" means it is not.
 
-Write a solution to find the ids of products that are both low fat and recyclable.
-Return the result table in any order.
-The result format is in the following example.

Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+

Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+

Explanation: Only products 1 and 3 are both low fat and recyclable.
"""

import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y"), ["product_id"]]


if __name__ == "__main__":
    data: list[list[str]] = [
        ["0", "Y", "N"],
        ["1", "Y", "Y"],
        ["2", "N", "Y"],
        ["3", "Y", "Y"],
        ["4", "N", "N"]
    ]
    products: pd.DataFrame = pd.DataFrame(data, columns=["product_id", "low_fats", "recyclable"]).astype(
        {"product_id": "int64", "low_fats": "category", "recyclable": "category"})

    print(find_products(products).to_string(index=False))
