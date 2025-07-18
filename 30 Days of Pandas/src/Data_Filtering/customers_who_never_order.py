"""183. Customers Who Never Order
Tags: Easy, Database, Pandas

Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 
Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 
-Write a solution to find all customers who never order anything.
-Return the result table in any order.
-The result format is in the following example.

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""

import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers.loc[(~customers["id"].isin(orders["customerId"])), ["name"]].rename(columns={"name": "Customers"})


if __name__ == "__main__":
    data_customers: list[list[int | str]] = [
        [1, "Joe"],
        [2, "Henry"],
        [3, "Sam"],
        [4, "Max"]
    ]
    customers: pd.DataFrame = pd.DataFrame(data_customers, columns=["id", "name"]).astype({"id": "Int64", "name": "object"})
    data_orders: list[list[int]] = [
        [1, 3],
        [2, 1]
    ]
    orders: pd.DataFrame = pd.DataFrame(data_orders, columns=["id", "customerId"]).astype({"id": "Int64", "customerId": "Int64"})

    print(find_customers(customers, orders).to_string(index=False))
