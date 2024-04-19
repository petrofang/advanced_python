# (c) Giles Cooper 2024
"""
The file 'salesfig.csv' contains sales figures for five sales persons in INR.
    Use this file to create a DataFrame named Sales.

1.) Display the column labels of Sales.
2.) Display the last two rows of Sales.
3.) Display the first two columns of Sales.
4.) Add the following column to the Sales DataFrame.
    2018
    160000
    110000
    500000
    340000
    900000

5.) Display the sales made by all sales persons in the year 2017.
6.) Display the average sales made in 2017.
7.) Find the maximum sales made in 2017.   
    Display the saleperson who sold the maximum sales in 2017.
8.) Add data to Sales for salesman named 'Sumeet' where the sales made are
        [ 1962, 37800, 52000, 78438, 38852] 
    in the years 
        [2014, 2015, 2016, 2017 and 2018] 
    Display the updated Sales dataframe.
9.) Delete the data for the year 2014 from the DataFrame Sales. 
    Display the updated Sales dataframe.

10.) Delete the data for the sales man Kinshuk from the DataFrame Sales.
    Display the updated Sales dataframe.
"""
import pandas as pd
try:
  with open('salesfig.csv', 'r') as f:
    df = pd.read_csv(f)
except Exception as e: quit() #kthxbye

# lazy print statement function
def pr(df):print(f"{df}\n")

#1 
pr(df.columns[:])

#2 
pr(df.iloc[-2:])

#3
pr(df.iloc[:,:2])

#4
df[2018] = [160000, 110000, 500000, 340000, 900000]
# should we display it?
pr(df)

#5
pr(df[['name','2017']])
pr(f"max: {df['2017'].max()}")

#6
pr(f"avg: {df['2017'].mean()}")
