"""1148. Article Views I
Tags: Easy, Database, Pandas

Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 
-Write a solution to find all the authors that viewed at least one of their own articles.
-Return the result table sorted by id in ascending order.
-The result format is in the following example.

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[(views["author_id"] == views["viewer_id"]), ["author_id"]].drop_duplicates().rename(columns={"author_id": "id"}).sort_values(by="id")


if __name__ == "__main__":
    data: list[list[int | str]] = [
        [1, 3, 5, "2019-08-01"],
        [1, 3, 6, "2019-08-02"],
        [2, 7, 7, "2019-08-01"],
        [2, 7, 6, "2019-08-02"],
        [4, 7, 1, "2019-07-22"],
        [3, 4, 4, "2019-07-21"],
        [3, 4, 4, "2019-07-21"]
    ]
    views: pd.DataFrame = pd.DataFrame(data, columns=["article_id", "author_id", "viewer_id", "view_date"]).astype(
        {"article_id": "Int64", "author_id": "Int64", "viewer_id": "Int64", "view_date": "datetime64[ns]"})

    print(article_views(views).to_string(index=False))
