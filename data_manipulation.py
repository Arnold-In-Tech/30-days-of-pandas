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




# Q 11

# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+-------+--------+--------------+
# | id | name  | salary | departmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# Department table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | IT    |
# | 2  | Sales |
# +----+-------+
# Output: 
# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Jim      | 90000  |
# | Sales      | Henry    | 80000  |
# | IT         | Max      | 90000  |
# +------------+----------+--------+
# Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    # widen the maximum per group with transform, check equality against it to detect maximums and index with that mask
    employee_largest_df = employee.loc[employee["salary"].eq(employee.groupby("departmentId")["salary"].transform("max"))]

    # select specific columns and rename departmentId to id
    employee_largest_df = employee_largest_df[['name' ,'salary', 'departmentId']].rename(columns = {'departmentId':'id'})

    # merge df1 to department df. rename columns, and drop id column
    return pd.merge(employee_largest_df, department, on='id', how='inner').rename(columns = {'name_x':'Employee', 'name_y':'Department', 'salary': 'Salary'}).drop('id', axis=1)


# ref: https://stackoverflow.com/questions/75226607/get-all-the-rows-with-max-value-in-a-pandas-dataframe-column-in-python
# The transform() method allows you to execute a function for each value of the DataFrame.


# Alternative

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    df = employee.merge(department, left_on ='departmentId', right_on = 'id', how ='inner')

    df['max_salary'] = df.groupby('name_y') ['salary'].transform(max)

    return df[df.salary == df.max_salary]   [['name_y','name_x','max_salary']].rename(columns = {'name_y': 'Department', 'name_x':'Employee', 'max_salary': 'Salary'})
 





# === test code

# employee = pd.read_csv('./test_data.csv', sep=',')
# department = pd.read_csv('./department.csv', sep=',')

# print(department_highest_salary(employee, department))







# =============================================================== #

# N/B 
# . drop_duplicates() will keep the first instance of a duplicate 
# row and remove any others.

# Q 11. Using .apply to get multiple rows with the highets value
# Use groupby to group data by 'departmentId' and apply a lambda function to get employees with highest salary in each group
    # highest_salary_df = merged_df.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
