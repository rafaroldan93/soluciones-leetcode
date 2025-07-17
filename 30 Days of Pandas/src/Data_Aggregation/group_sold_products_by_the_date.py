"""1484. Group Sold Products By The Date
Tags: Easy, Database, Pandas

Table Activities:
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.

-Write a solution to find for each date the number of different products sold and their names.
-The sold products names for each date should be sorted lexicographically.
-Return the result table ordered by sell_date.
-The result format is in the following example.

Example 1:

Input: 
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+

Output: 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+

Explanation: 
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.
"""


import pandas as pd
from pandas.core.groupby.generic import SeriesGroupBy


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    products_by_date: SeriesGroupBy = activities.drop_duplicates().groupby("sell_date")["product"]
    products_by_date_lexicographically: pd.DataFrame = products_by_date.apply(lambda x: ",".join(sorted(x))).reset_index()
    num_sold_by_date: pd.Series[int] = products_by_date.count()
    return pd.merge(num_sold_by_date, products_by_date_lexicographically, on="sell_date").sort_values("sell_date").rename(columns={"product_x": "num_sold", "product_y": "products"}).reset_index(drop=True)


if __name__ == "__main__":
    data: list[list[str]] = [
        ["2020-05-30", "Headphone"],
        ["2020-06-01", "Pencil"],
        ["2020-06-02", "Mask"],
        ["2020-05-30", "Basketball"],
        ["2020-06-01", "Bible"],
        ["2020-06-02", "Mask"],
        ["2020-05-30", "T-Shirt"]
    ]
    activities: pd.DataFrame = pd.DataFrame(data, columns=["sell_date", "product"]).astype({"sell_date": "datetime64[ns]", "product": "object"})
    print(categorize_products(activities).to_string(index=False))
