# Giles Cooper 2024
"""The file USPopulation.txt contains the midyear population of the 
    United States, in thousands, during the years 1950 through 1990.  
    The first line of the file contains the population for 1950, 
    the second for 1951 and so forth. 

Write a program which reads the populations from the file and calculates
    the following:

The program should output:

The average annual change in population during that time period
The year with the greatest increase in population during that time period
The year with the smallest increase in population during that time period
The program should provide a line plot of annual changes in populations
    from 1950 - 1990. Be sure that your plot contains a title, x and y labels,
    some color and an attractive marker.
Your program should use only ndarrays for storage of populations, years
    and population changes.
Be sure your code well commented.

Hint:  You may want to develop the program incrementally, verifying array 
    contents and calculations with output (or the variable window) after each 
    task is completed.

Output:
    Average change is 2443.88
    Largest increase in population 3185 in year 1955
    Smallest increase in population 1881 in year 1967
"""
import numpy as np
import matplotlib.pyplot as plt

# load up the file
FILE = "USPopulation.txt"
try: population = np.genfromtxt(FILE, delimiter='\n')
except Exception as e: 
    print(e)
    quit()   

year=np.arange(1950,1991)

# find average yearly population change:
change = int(np.sum(max(population)-min(population))/(len(population)-1)*1000)
print(f"The average US population growth per year between 1950 and 1990 was",
      f"{change:,}.")

# find the change from year-to-year. NaN the first year,
#     because it had no prior year to compare
change=[]
for i in range(len(population)):
    if i==0:change.append(np.nan)
    else:change.append(population[i]-population[i-1])
change = np.array(change)

print(f"The greatest growth was in {year[np.where(change == np.nanmax(change))[0]][0]}",
      f"with an increase of approximately {int(np.nanmax(change)*1000):,}.")
print(f"The least growth was in {year[np.where(change == np.nanmin(change))[0]][0]}",
      f"with an increase of approximately {int(np.nanmin(change)*1000):,}.")

fig = plt.figure()
# plt.xkcd() # love xkcd.com .. most of my procrastination time is spent there
# I like the graphical effect this function gives but unfortunately it causes
# the console to spam because the fonts aren't loaded on my debian system so
# I'll just comment it out
plt.plot(year, change/1000, color='blue', linewidth=1, marker="D")
plt.title("US Population Growth")
plt.xlabel("Year")
plt.ylabel("Millions")
plt.show()