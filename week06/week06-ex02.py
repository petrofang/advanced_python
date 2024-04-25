# Giles Cooper 2024
"""For this project you will be using a dataset from the Titanic disaster 
    to analyze and view a number of characteristics of the tragedy. 
    The dataset is a subset of full Titanic statistic.

1.) Store the dataset from the file titanic.txt into a dataframe.

2.) Display the first and last 10 lines of the data on the screen.   
    Place the code which does this in a function (accepting DataFrame 
    parameter) so it can be called easily.

3.) Change column names to “Name”, “Survival”, “Sex”, “Age” and “Class”.  
    Display the first and last 10 lines of the data on the screen.

4.) Remove all rows from the data which have NaN for age. Display the first
    and last 10 lines of the data on the screen.

5.) Create a dataFrame with survivors only.  Display the first and last 
    10 lines of  the data on the screen.  Output the number of survivors.

6.) Pandas has many built in visualization capabilities, implemented 
    using matplotlib.  The hist() method will create a histogram for 
    any numerical columns in a dataframe (dataframe.hist())
    Use this method to draw a histogram of the ages in survivors DataFrame.

7.) Display the first and last 10 lines of the dataset - names and age of ONLY  
    Hint:  It may help to create a new dataset with results

8.) Determine and display the names and ages of survivors under the age of 25.
    Output the number of survivors under 25.

9.) Output the names of survivors in 1st class. Output the names of survivors
    in the 2nd class.  Output the names of the survivors in 3rd class.   
    Output the number of survivors in each class.

10.) Draw a bar chart of numbers in 1st, 2nd and 3rd class.
"""

import pandas as pd
import matplotlib.pyplot as plt

FILE = 'TitanicSurvival.csv'

# 1.
try:
    with open(FILE, 'r') as f:
        df = pd.read_csv(f)
except Exception as e: 
    print(e)
    quit()
 
# 2.
def display(df : pd.DataFrame) -> None: 
    print()
    print(pd.concat([df.iloc[0:10], df.iloc[-10:]]))
display(df)

# 3.
df.rename(columns={'rownames':'Name',
                   'survived':'Survival',
                   'sex':'Sex',
                   'age':'Age',
                   'passengerClass':'Class'}, inplace=True)
display(df)

# 4.
n = len(df)
df.dropna(inplace=True) # assuming age is the only NaN value in a row
df.reset_index(inplace=True, drop=True)
display(df)
print(f"    {n - len(df)} souls lost to insufficient data. Rest in Peace.")

# 5.
df_survivors = df.loc[df.Survival == 'yes']
df_survivors.reset_index(inplace=True, drop=True)
display(df_survivors)
print(f"    The Titanic disaster had {len(df_survivors)} survivors.")

# 6.
plt.hist(df_survivors.Age, bins=80)
plt.title("Titanic Survivor Age Distribution")
plt.show()

# 7. "the dataset - names and age of ONLY " [...] the survivors?
df_names = df_survivors[['Name', 'Age']]
display(df_names)

# 8.
display(df_names.loc[df_names.Age < 25].reset_index(drop=True))
u25_count = len(df_names.loc[df_names.Age < 25])
print(f"There were {u25_count} Titanic survivors under the age of 25.\n")

# 9.
class_1 = df_survivors.loc[df_survivors.Class.str.contains('1')]
class_2 = df_survivors.loc[df_survivors.Class.str.contains('2')]
class_3 = df_survivors.loc[df_survivors.Class.str.contains('3')]

print(f"    There were {len(class_1)} first-class survivors:")
for survivor in list(class_1.Name):
    print(survivor, end="; ")
print('\n')
   
print(f"    There were {len(class_2)} second-class survivors:")
for survivor in list(class_2.Name):
    print(survivor, end="; ")
print('\n')
   
print(f"    There were {len(class_3)} third-class survivors:")
for survivor in list(class_3.Name):
    print(survivor, end="; ")
print('\n')

# 10 
plt.bar(['first', 'second', 'third'], 
        [len(class_1),len(class_2),len(class_3)], 
        color='navy',
        width=.618)
plt.ylabel("Number of Survivors")
plt.xlabel("Passenger Class")
plt.title(label="Titanic Survivors by Class")
plt.show()   

