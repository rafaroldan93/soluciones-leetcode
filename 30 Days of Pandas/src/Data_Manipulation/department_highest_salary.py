"""184. Department Highest Salary
Tags: Medium, Database, Pandas

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 
Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 
-Write a solution to find employees who have the highest salary in each of the departments.
-Return the result table in any order.
-The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
"""

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salaries: pd.Series = employee.groupby("departmentId")["salary"].agg("max")
    top_employees: pd.DataFrame = employee.merge(max_salaries, on=["departmentId", "salary"])
    merged: pd.DataFrame = top_employees.merge(department, left_on="departmentId", right_on="id", suffixes=("_Employee", "_Department"))
    return merged[["name_Department", "name_Employee", "salary"]].rename(columns={"name_Department": "Department", "name_Employee": "Employee", "salary": "Salary"})


if __name__ == "__main__":
    data_employee: list[list[int | str]] = [
        [1, "Joe", 70000, 1],
        [2, "Jim", 90000, 1],
        [3, "Henry", 80000, 2],
        [4, "Sam", 60000, 2],
        [5, "Max", 90000, 1]
    ]
    employee: pd.DataFrame = pd.DataFrame(data_employee, columns=["id", "name", "salary", "departmentId"]).astype({
        "id": "Int64", "name": "object", "salary": "Int64", "departmentId": "Int64"})
    data_department: list[list[int | str]] = [
        [1, "IT"],
        [2, "Sales"]
    ]
    department: pd.DataFrame = pd.DataFrame(data_department, columns=["id", "name"]).astype({"id": "Int64", "name": "object"})
    print(department_highest_salary(employee, department).to_string(index=False))
