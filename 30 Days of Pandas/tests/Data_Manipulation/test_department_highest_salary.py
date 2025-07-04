import pandas as pd
import pytest
from Data_Manipulation.department_highest_salary import \
    department_highest_salary
from pandas.testing import assert_frame_equal


@pytest.mark.parametrize("employee_data, department_data, expected_data", [
    # 1. Basic case with distinct salaries
    (
        [
            [1, "Joe", 70000, 1],
            [2, "Jim", 90000, 1],
            [3, "Henry", 80000, 2],
            [4, "Sam", 60000, 2],
            [5, "Max", 90000, 1]
        ],
        [
            [1, "IT"],
            [2, "Sales"]
        ],
        [
            ["IT", "Jim", 90000],
            ["Sales", "Henry", 80000],
            ["IT", "Max", 90000]
        ]
    ),
    # 2. Case with all employees in one department
    (
        [
            [1, "Joe", 70000, 1],
            [2, "Jim", 90000, 1],
            [3, "Max", 90000, 1]
        ],
        [
            [1, "IT"]
        ],
        [
            ["IT", "Jim", 90000],
            ["IT", "Max", 90000]
        ]
    ),
    # 3. Case with no employees in a department
    (
        [
            [1, "Joe", 70000, 1],
            [2, "Jim", 90000, 1]
        ],
        [
            [1, "IT"],
            [2, "Sales"]
        ],
        [
            ["IT", "Jim", 90000]
        ]
    ),
    # 4. Case with multiple employees having the same highest salary in different departments
    (
        [
            [1, "Joe", 70000, 1],
            [2, "Jim", 90000, 1],
            [3, "Henry", 90000, 2],
            [4, "Sam", 60000, 2]
        ],
        [
            [1, "IT"],
            [2, "Sales"]
        ],
        [
            ["IT", "Jim", 90000],
            ["Sales", "Henry", 90000]
        ]
    ),
    # 5. Case with all employees having the same salary
    (
        [
            [1, "Joe", 70000, 1],
            [2, "Jim", 70000, 1],
            [3, "Henry", 70000, 2],
            [4, "Sam", 70000, 2]
        ],
        [
            [1, "IT"],
            [2, "Sales"]
        ],
        [
            ["IT", "Joe", 70000],
            ["IT", "Jim", 70000],
            ["Sales", "Henry", 70000],
            ["Sales", "Sam", 70000]
        ]
    )
],
    ids=[
    "1. Basic case with distinct salaries",
    "2. All employees in one department",
    "3. No employees in a department",
    "4. Multiple employees with same highest salary in different departments",
    "5. All employees with same salary"
]
)
def test_department_highest_salary(employee_data: list[list[int | str]], department_data: list[list[int | str]], expected_data: list[list[str | int]]) -> None:
    employee: pd.DataFrame = pd.DataFrame(employee_data, columns=["id", "name", "salary", "departmentId"]).astype({
        "id": "Int64",
        "name": "object",
        "salary": "Int64",
        "departmentId": "Int64"
    })
    department: pd.DataFrame = pd.DataFrame(department_data, columns=["id", "name"]).astype({"id": "Int64", "name": "object"})
    result: pd.DataFrame = department_highest_salary(employee, department)
    expected: pd.DataFrame = pd.DataFrame(expected_data, columns=["Department", "Employee", "Salary"]).astype({
        "Department": "object", "Employee": "object", "Salary": "Int64"})
    assert_frame_equal(result, expected)
