"""1667. Fix Names in a Table
Tags: Easy, Database, Pandas

Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 
-Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
-Return the result table ordered by user_id.
-The result format is in the following example.

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+

Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+
"""

import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return users.assign(name=users["name"].str.capitalize()).sort_values("user_id")


if __name__ == "__main__":
    data: list[list[int | str]] = [
        [1, "aLice"],
        [2, "bOB"]
    ]
    users: pd.DataFrame = pd.DataFrame(data, columns=["user_id", "name"]).astype({"user_id": "Int64", "name": "object"})
    print(fix_names(users).to_string(index=False))
