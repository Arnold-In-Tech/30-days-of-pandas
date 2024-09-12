# Q 15

# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# Output: 
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
# Explanation: 
# Low Salary: Account 2.
# Average Salary: No accounts.
# High Salary: Accounts 3, 6, and 8.

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal_count = accounts[accounts['income']<20000].shape[0]
    av_sal_count = accounts[(accounts['income']>=20000)&(accounts['income']<=50000)].shape[0]
    high_sal_count = accounts[accounts['income']>50000].shape[0]
    result = pd.DataFrame({
        'category':['High Salary','Low Salary','Average Salary'],
        'accounts_count':[high_sal_count, low_sal_count, av_sal_count]
        })
    return result


# === test code

# accounts = pd.read_csv('./test_data.csv', sep=',')
# print(count_salary_categories(accounts))
