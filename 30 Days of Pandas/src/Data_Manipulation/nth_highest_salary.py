"""177. Nth Highest Salary
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
 
-Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.
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
n = 2

Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2

Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
"""
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee.sort_values(by="salary", ascending=False).drop_duplicates("salary").reset_index(drop=True)
    if N > len(salaries) or N < 1:
        return pd.DataFrame([[None]], columns=[f"getNthHighestSalary({N})"])
    return salaries.loc[[N - 1], ["salary"]].rename(columns={"salary": f"getNthHighestSalary({N})"})


if __name__ == "__main__":
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=["id", "salary"]).astype({"id": "Int64", "salary": "Int64"})
    print(nth_highest_salary(employee, 2).to_string(index=False))
