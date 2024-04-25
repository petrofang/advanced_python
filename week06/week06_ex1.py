# Giles Cooper
"""Each row of the dataset in the file testgrades.csv file represents 
    one student in a course.

1.)  Read in the testgrades.csv file and change the column headings to:
“LName”   “FName”  “SSN”  “Test1” “Test2”  “Test3”  “Test 4”  “Final”  “Grade”

2.) Output the total number of students in the sample.

3.) Sort the data in the DataFrame by LName, 
    and display columns LName, FName and SNN.

4.) Find the students who have a final grade greater or equal to 90.  
    Display the LName, FName and Final columns for these students. 
    Output the % of students with a frade greater or equal to 90.

5.) Find out who failed (grade of F) and output their info.   
    Output the % of students who failed.

6.) Output info for the student who had the lowest final grade.
    Output info for the student who had the highest final grade.

7.) Create a new DataFrame containing only students with 
    a grade less than 70 on Test 4. How many students were there?

8.) Output the % of students who scored less and 70 on Test 5 
    and also had a failing grade.

9.) Create a separate DataFrame containing students who scored an A of any type.
    Create a separate DataFrame containing students who scored an B of any type.
    Create a separate DataFrame containing students who scored an C of any type.

10.) Display a pie chart which visualizes students with any type of A, 
    any type of B, any type of C, and others.
"""

import pandas as pd

FILE = "testgrades.csv"

# lazy print statement function
def pr(df):print(f"{df}\n")

try: 
    with open(FILE, 'r') as f:
        df = pd.read_csv(f)
except Exception as e: quit() #  ¯\_(ツ)_/¯

# 1 
df = df.rename(columns={"Lastname":"LName","Firstname":"FName"})

# 2
print(f"\n{len(df)} records in database:")

# 3 
pr(df[['LName','FName','SSN']].sort_values('LName'))

#4
df_A_final = df[['LName', 'FName', 'Final']].loc[df['Final'] >= 90]
print(df_A_final)
pr(f"Students with 90+ on final: {len(df_A_final)/len(df)*100}%")

#5
df_failures = df[['LName', 'FName', 'Grade']].loc[df.Grade == "F"]
print(df_failures)
pr(f"Failures: {len(df_failures) / len(df) * 100}%")

#6
pr(df)