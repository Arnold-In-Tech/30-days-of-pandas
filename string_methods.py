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


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # create column for bonus and populate with zeros
    employees['bonus'] = 0
    # substitute zeros with 100% salary for employees that meet condition
    employees.loc[(employees['employee_id']%2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    # sort by employee_id and return only emplyee id and bonus columns 
    return employees.sort_values(by='employee_id', ascending=True)[['employee_id','bonus']]


# Q 7

# Fix names in a table 

# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# Return the result table ordered by user_id.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+
# Output: 
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # loop through the df using lambda. Fix the names using .str.capitalize()
    users  = users.assign(name = lambda x: x['name'].str.capitalize())

    # return sorted df based on user_id values
    return users.sort_values(by='user_id', ascending=True)

# Alternative
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Apply the str.capitalize() function to fix the names
    users['name'] = users['name'].str.capitalize()
    
    # Sort the result table by user_id in ascending order
    result_df = users.sort_values(by='user_id', ascending=True)
    
    return result_df



# Q 7.

# Find users with valid e-mails

# Write a solution to find the users who have valid emails.

# A valid e-mail has a prefix name and a domain where:

# The prefix name is a string that may 
# contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
# The domain is '@leetcode.com'.
# Return the result table in any order.

# The result format is in the following example.

# Example 1:

# Input: 
# Users table:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+
# Output: 
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# +---------+-----------+-------------------------+
# Explanation: 
# The mail of user 2 does not have a domain.
# The mail of user 5 has the # sign which is not allowed.
# The mail of user 6 does not have the leetcode domain.
# The mail of user 7 starts with a period.


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    # Use the str.match() method with a regex pattern to find valid emails
    valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    
    return valid_emails_df


# === test code

# df = pd.read_csv('./test_data.csv', sep=',')
# print(valid_emails(df))


# =============================================================== #

# N/B
# ".apply()" iterates through each row and creates new col from old ones 

