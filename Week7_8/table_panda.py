'''
This program performs different data manipulation using Pandaa and analyzes by filtering, transforming, 
duplicate removal.
It answers the following:
a. Select only the Name and Salary columns.
b. Filters out all employees in the IT department
c. Selects employees who are older than 30.
d. Find average salary of employees in each department.
e. Counts the number of employees in each department.
f. Adds a new column Bonus which is 10% of each employees salary.
g. Replaces all occurrences of HR in the Department column with Human Resources
h. Finds employee with the longest tenure (based on JoinDate).
i. Create a new column SalaryCategory where salaries above 75,000 are categorized as High and Low
j. Checks if there are any duplicate EmployeeIDs and remove them if found.
k. Calculates the median Age of all employees.

'''
import pandas as pd

df = pd.read_csv("tabledf.csv")

print("The data inside the file is:\n",df)
print()
#Query to select only the Name and Salary Columns.
print("The Name and Salary Columns only:")
print(df[['Name','Salary']])
print()

#Filter out all employees who are in IT department
print("The table after filtering out the employees from IT department:")
print(df[df['Department'] != 'IT'])
print()

#Employees who are older than 30
print("The employees who are older than 30:")
print(df[df['Age'] > 30])
print()

#fins the average salary of employees in each department.
print("The average salarys of employees in each department are:")
print(df.groupby('Department')['Salary'].mean())
print()

#Count the number of employees in each department
print("This counts the number of employees in each of the department: ")
print(df['Department'].value_counts())
print()

#Creates a new column "Bonus" where bonus is 10% of each department
print("The table after the addition of column 'Bonus' is:")
df['Bonus'] = 0.10 * df['Salary']
print(df)
print()

#Replaces the HR with Human Resources
print("The table after replacing HR with Human Resources is:")
df['Department'] = df['Department'].replace('HR','Human Resources')
print(df)
print()

#shows employee who have spent most years based on joindate
print("The table showing the employee who have spent most years is:")
print(df[df['JoinDate'] == df['JoinDate'].min()])
print()

#Adds a SalaryCategory column where Salary > 75000 is categorized as "High" and the rest as "Low"
print("The table after adding the column SalaryCategory is:") 
df['SalaryCategory'] = df['Salary'].apply(lambda x: 'High' if x > 75000 else 'Low')
print(df)
print()

#removes the employee if the ID's are duplicate.
print("After removing employee having duplicate IDs is:")
df = df.drop_duplicates(subset='EmployeeID')
print(df)
print()

#calculates the median Age of all employees
age_med = df['Age'].median()
print("Median Age:",age_med)