"""1517. Find Users With Valid E-Mails
Tags: Easy, Database, Pandas

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains information of the users signed up in a website. Some e-mails are invalid.
 
-Write a solution to find the users who have valid emails.
-A valid e-mail has a prefix name and a domain where:
 ·The prefix name is a string that may contain letters (upper or lower case), digits, underscore "_", period ".", and/or dash "-". The prefix name must start with a letter.
 ·The domain is "@leetcode.com".
-Return the result table in any order.
-The result format is in the following example.

Example 1:

Input: 
Users table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+

Output: 
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+

Explanation: 
The mail of user 2 does not have a domain.
The mail of user 5 has the # sign which is not allowed.
The mail of user 6 does not have the leetcode domain.
The mail of user 7 starts with a period.
"""

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex: str = r"^^[a-zA-Z][\w\.\-]*@leetcode\.com$"
    return users.loc[users["mail"].str.match(regex)]


if __name__ == "__main__":
    data: list[list[int | str]] = [
        [1, "Winston", "winston@leetcode.com"],
        [2, "Jonathan", "jonathanisgreat"],
        [3, "Annabelle", "bella-@leetcode.com"],
        [4, "Sally", "sally.come@leetcode.com"],
        [5, "Marwan", "quarz#2020@leetcode.com"],
        [6, "David", "david69@gmail.com"],
        [7, "Shapiro", ".shapo@leetcode.com"]
    ]
    users: pd.DataFrame = pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype({"user_id": "int64", "name": "object", "mail": "object"})
    print(valid_emails(users).to_string(index=False))
