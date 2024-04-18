# Giles Cooper
"""This exercise gives additional practice with DataFrames, 
including statistical methods.

1.) Create and output the following DataFrame
    Apples  Pears   Bananas
0   150     250     250
1   175     135     135
2   200     325     325
3   125     645     645     

2.) Update the row labels to:
        “Store 1”   “Store 2”   “Store 3”    “Store 4”         
    and print the updated DataFrame.

3.) Change the name of  the “bananas” column to “peaches”.   
    Output the updated DataFrame.

4.) Add data for an additional store to the dataframe, 
    and output the updated DataFrame.
        “Store 5”     245       350    725

5.) Double the inventory of Pears.  Output the updated dataframe.

6.) Output the minimum number of Apples at any store.

7.) Output the maximum quantity of fruit at any one store.

8.) Add a column named “Total” to the dataframe.  This column should 
    contain the average values of each row.  Output the updated dataframe.

9.) Add a final row labeled “Average” which contains the average 
    of each of the fruit.
    Output the updated dataframe.

10.)  Display only Store1 and Store 2 data.
"""

import pandas as pd

#1
df = pd.DataFrame({'Apples': [150, 175, 200, 125],
                   'Pears': [250, 135, 325, 645],
                   'Bananas': [250, 135, 325, 645]})

df.rename()