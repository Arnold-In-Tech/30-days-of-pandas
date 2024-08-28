# Q.5
# Write a solution to find the IDs of the invalid tweets. 
# The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

# Return the result table in any order.

# The result format is in the following example.

# Input: 
# Tweets table:
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+
# Output: 
# +----------+
# | tweet_id |
# +----------+
# | 2        |
# +----------+

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # filter rows where length of content is > 15
    invalid_df = tweets[tweets['content'].str.len() > 15]
    # Alternative using lambda
    ## invalid_df = tweets[tweets['content'].apply(lambda x: True if len(x)> 15 else False)]

    # obtain only tweet_id of the invalids df
    output_df = invalid_df[['tweet_id']]        # the double brackets ensures a dataframe of the selected collumn is returned
    return output_df


# Q 6

# Calculate special bonus

# Write a solution to calculate the bonus of each employee. 
# The bonus of an employee is 100% of their salary 
# if the ID of the employee is an odd number and 
# the employee's name does not start with the character 'M'. 
# The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output: 
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+


import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # create column for bonus and populate with zeros
    employees['bonus'] = 0
    # substitute zeros with 100% salary for employees that meet condition
    employees.loc[(employees['employee_id']%2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    # sort by employee_id and return only emplyee id and bonus columns 
    return employees.sort_values(by='employee_id', ascending=True)[['employee_id','bonus']]


# === test code

# employees = pd.read_csv('./test_data.csv', sep=',')
# print(calculate_special_bonus(employees))