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
def pr(df : pd.DataFrame): 
    print(f"{df.to_string(index=False)}")

try: 
    with open(FILE, 'r') as f:
        df = pd.read_csv(f)
except Exception as e: quit() #  ¯\_(ツ)_/¯

# 1 
df = df.rename(columns={"Lastname":"LName","Firstname":"FName"})
# assuming the space in "Test 4" was a typo

# 2
print(f"\n{len(df)} records in database:")

# 3 
pr(df[['LName','FName','SSN']].sort_values('LName'))
print()

# 4
df_A_final = df[['LName', 'FName', 'Final']].loc[df['Final'] >= 90]
pr(df_A_final)
print(f"Students with 90+ on final: {len(df_A_final)/len(df)*100}%\n")

# 5
df_failures = df[['LName', 'FName', 'Grade']].loc[df.Grade == "F"]
print("Class failures:")
pr(df_failures)
print(f"Failures: {len(df_failures) / len(df) * 100}%\n")

# 6  # does 'final grade' mean the grade on the final? 
    # or the grade at the end of the course?
print('min/max grades on the final:')
pr(pd.concat([df[['LName', 'FName', 'Final']].loc[df.Final == min(df.Final)], 
              df[['LName', 'FName', 'Final']].loc[df.Final == max(df.Final)]]))
    # must be Final because it's numerical
    # with min|max(df.Grade), 'A' would be min and 'F' max!

# 7 
df_struggling4 = df.loc[df['Test4'] < 70]
print(f"\n{len(df_struggling4)} students struggled on Test 4.\n")

# 8
    # 'Test 5' meaning test 4?
df_failing4 = df_struggling4.loc[df_struggling4.Final < 70].loc[df_struggling4.Grade == 'F']
print('Failures who scored less than 70 on "Test 4":', end=" ")
print(len(df_failing4) / len(df_struggling4) *100 , "%", sep="")












# wait, how did George get a B with an average test score of 11? 
#   Must be on the football team