"""176. Second Highest Salary
Tags: Medium, Database, Pandas

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 
-Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
-The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries: pd.DataFrame = employee.sort_values(by="salary", ascending=False).drop_duplicates("salary").reset_index(drop=True)
    if len(salaries) < 2:
        return pd.DataFrame([[None]], columns=["SecondHighestSalary"])
    return salaries.loc[[1], ["salary"]].rename(columns={"salary": "SecondHighestSalary"})


if __name__ == "__main__":
    data: list[list[int]] = [[1, 100], [2, 200], [3, 300]]
    employee: pd.DataFrame = pd.DataFrame(data, columns=["id", "salary"]).astype({"id": "int64", "salary": "int64"})
    print(second_highest_salary(employee).to_string(index=False))
