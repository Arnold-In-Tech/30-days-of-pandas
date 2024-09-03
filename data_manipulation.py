# Q 9.

# Nth Highest salary

# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
	nth_salary = employee.loc[employee['id'] == N, 'salary'].values[0] if (N <= len(employee.index) and employee['salary'].value_counts()[employee.loc[employee['id'] == N, 'salary'].values[0]] == 1) else None
	return pd.DataFrame([nth_salary ], columns=[f"getNthHighestSalary({N})"])


# Alternative
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    d=set()
    for i in employee["salary"]:
        d.add(i)
    c=list(set(d))
    c.sort()
    if(len(c)<N or len(c)==0 or N<=0 ):
        a=None
    else:
        a=c[-N]
    r="getNthHighestSalary"+"("+str(N)+")"
    t={r:[a]}
    o=pd.DataFrame(t)

    return o




# Q 10

# Second highest salary

# Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Drop any duplicate salary values to avoid counting duplicates as separate salary ranks
    unique_salaries = employee['salary'].drop_duplicates()

    # Sort the unique salaries in descending order and get the second highest salary
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None

    # If the second highest salary doesn't exist (e.g., there are fewer than two unique salaries), return None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    # Create a DataFrame with the second highest salary
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result_df


# Alternative

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salary = employee["salary"].drop_duplicates().sort_values(ascending=False)
    second_highest = distinct_salary.iloc[1] if len(distinct_salary) > 1 else None
    result = pd.DataFrame({"SecondHighestSalary": [second_highest]})
    return result


# === test code

# df = pd.read_csv('./test_data.csv', sep=',')
# print(nth_highest_salary(df, 2))


# =============================================================== #



# N/B 
# . drop_duplicates() will keep the first instance of a duplicate 
# row and remove any others.
