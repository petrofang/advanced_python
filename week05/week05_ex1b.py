# Giles Cooper
"""8.) Create a Data Frame from the following dictionary:

data = { 'Course': [ 'Financial Accounting', 'Microeconomics', 
    'Programming Fundamentals',  'Statistics', 'Data Science'],  
    'No of Students': [150, 75, 200, 175, 125], 
    'Department': ['Accountancy', 'Economics', 'CIS', 'Math', 'Math' ]  }

9.) Display the DataFrame

10.) Display only the Course and Department columns

11.) Output the rows 0,3,4 from the Course and Department columns.

12.) Add code to count the number of rows and columns.

13.) Add a column labeled Professor, containing professor
    names 'Brown', 'Griffin', 'Sanchez', 'Chen', 'Pavone' 
    and display the updated DataFrame.

14.) Add a row containing the course 'Discrete Math', with 65 students,
    Math department and professor 'Hasson' and display the updated DataFrame.

15.) Add a column labeled Capacity, containing all 200's  
    and display the updated DataFrame.

16.) Change the column label “No of Students” to simply “Students”.

17.) Add a column labeled Avail, containing the space in all classrooms 
    and display the updated DataFrame.

18.) Using the DataFrame, output the average class size.

19.) Using the DataFrame, output the name of the class 
    with the largest available seats.

20.)  Delete all data for the course “Financial Accounting” 
    from the DataFrame. Display the updated DataFrame."""

import pandas as pd

#8 
data = { 'Course': [ 'Financial Accounting', 'Microeconomics', 
    'Programming Fundamentals', 'Statistics', 'Data Science'],  
    'No of Students': [150, 75, 200, 175, 125], 
    'Department': ['Accountancy', 'Economics', 'CIS', 'Math', 'Math' ]  }
data = pd.DataFrame(data)

#9
print(data)
print()

#10 
print(data.loc[:,['Course', 'Department']])
print()

#11
print(data.loc[[0,3,4],['Course', 'Department']])
print()

#12
print(f"rows: {len(data)}")
print(f"cols: {len(data.columns)}")

#13
data['Professor'] = ['Brown', 'Griffin', 'Sanchez', 'Chen', 'Pavone']
print(data)
print()

#14
data.loc[(len(data))] = {'Course':'Discrete Math', 
                         'No of Students':65, 
                         'Department':'Math', 
                         'Professor':'Hasson'}

#15
data['Capacity'] = 200
print(data)
print()

#16
data = data.rename(columns={"No of Students":"Students"})

#17
data['Avail'] = data['Capacity'] - data['Students']
print(data)
print()

#18
print(f"mean: {data['Students'].mean()}")
print()

#19
print(f"max availability: {data['Avail'].max()}")
print()

#20
data = data.drop(0, axis=0)
print(data)