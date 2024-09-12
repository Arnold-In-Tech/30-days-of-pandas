
# ============================ Data Filtering ============================== #

# 1) 
# Big Countries
# A country is big if:

#     it has an area of at least three million (i.e., 3000000 km2), or
#     it has a population of at least twenty-five million (i.e., 25000000).

# Write a solution to find the name, population, and area of the big countries.

# Return the result table in any order.

# Input

# | name        | continent | area    | population | gdp          |
# | ----------- | --------- | ------- | ---------- | ------------ |
# | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
# | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
# | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
# | Andorra     | Europe    | 468     | 78115      | 3712000000   |
# | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |

# Output
# | name        | population | area    |
# | ----------- | ---------- | ------- |
# | Afghanistan | 25500100   | 652230  |
# | Algeria     | 37100000   | 2381741 |

import pandas as pd 

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]



# 2)
# Recylable and low fat products
# Write a solution to find the ids of products that are both low fat and recyclable.

# Return the result table in any order.

# The result format is in the following example.

# Input: 
# Products table:
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+
# Output: 
# +-------------+
# | product_id  |
# +-------------+
# | 1           |
# | 3           |
# +-------------+
# Explanation: Only products 1 and 3 are both low fat and recyclable.

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df[['product_id']]
    



# 3. 
# Customers Who Never Order

# Table: Customers

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.

 

# Table: Orders

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

 

# Write a solution to find all customers who never order anything.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# Output: 
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+



def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # Select the customers whose 'id' is not present in the orders DataFrame's 'customerId' column.
    df = customers[~customers['id'].isin(orders['customerId'])]     # tilde(~) sign works as a NOT(!) operator

    # Build a DataFrame that only contains the 'name' column and rename it as 'Customers'.
    df = df[['name']].rename(columns={'name': 'Customers'})

    return df


# 4 
# Article views

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+
# Output: 
# +------+
# | id   |
# +------+
# | 4    |
# | 7    |
# +------+

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df1 = views[(views.author_id == views.viewer_id)]   # df where author_id == viewer_id
    df2 = df1.rename(columns={"author_id": "id"})       # rename author_id to id
    df3 = df2[['id']].drop_duplicates()                 # drop rows with duplicate author ids
    df4 = df3.sort_values(by=['id'])                    # sort ids 
    return df4



# Q 13

# Delete duplicate emails

# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

# For Pandas users, please note that you are supposed to modify Person in place.

# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Person table:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Output: 
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+
# Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

# Modify person inplace

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the rows based on id (Ascending order)
    person.sort_values(by='id',ascending=True,inplace=True)

    # Drop duplicate rows based on the 'email' column, keeping the first occurrence
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    

# Q 14
    
# Rearrange products

# Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Products table:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+
# Output: 
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+
# Explanation: 
# Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
# Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()    






# =========================================================================================== #

# N/B
# Note
    # loc gets rows (and/or columns) with particular LABELS.
    # iloc gets rows (and/or columns) at integer/index locations.

# Examples:
# >>> s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2]) 
# 49    a
# 48    b
# 47    c
# 0     d
# 1     e
# 2     f

# >>> s.loc[0]    # value at index label 0
# 'd'

# >>> s.iloc[0]   # value at index location 0
# 'a'

# >>> s.loc[0:1]  # rows at index labels between 0 and 1 (inclusive)
# 0    d
# 1    e

# >>> s.iloc[0:1] # rows at index location between 0 and 1 (exclusive)
# 49    a

# =========================================================================================== #


