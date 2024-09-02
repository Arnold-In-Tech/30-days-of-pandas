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



# === test code

# df = pd.read_csv('./test_data.csv', sep=',')
# print(nth_highest_salary(df, 2))