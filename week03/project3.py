# Giles Cooper
"""For this exercise we will use a subset of this data set having 30 rows.  
The first line of the file contains the headers:    
    Sepal Length, 
    Sepal Width, 
    Petal Length, 
    Petal Width, 
    Iris (type) 
    and a species number (1,2 or 3).    

This line is followed by 10 rows for each of the three species.   
You can download this file for your use on the class website,  iris.txt.

Using this data set, perform the following:

    01. Use the data in the file Iris.txt in a 2-D array called 'iris'.
    02. Display the data stored in 'iris'.
    03. Drop column whose index = 4 from the array iris (we do not need the 
        text for the Iris name, the species number is enough.
    04. Create a 1-D array header having elements "sepal length", 
        "sepal width", "petal length", "petal width", "Species No" 
        in that order. These headers will be needed for future tables.
    05. Display the updated data, formatted in a tabular form (see below).
    06. Display the shape, dimensions and size of iris.
    07. Split iris into three 2-D arrays, each array for a different species. 
        Call them iris1, iris2, iris3.
    08. Output the three arrays iris1, iris2, iris3. Be sure your output is 
        organized as shown in sample output file
    09. Find the max, min, mean and standard deviation for the columns of the 
        array iris and store the results in the arrays iris_max, iris_min, 
        iris_avg, iris_std, iris_var respectively. The results must be 
        rounded to not more than two decimal places. 
        Display as shown in sample output file.
    10. Find the max, min, mean and standard deviation for the columns of the
        array iris1 and store the results in the arrays iris1_max, iris1_min,
        iris1_avg, iris1_std, iris1_var respectively. The results must be
        rounded to not more than two decimal places. 
        Display as shown in sample output file.
    11. Find the max, min, mean and standard deviation for the columns of the
        array iris2 and store the results in the arrays iris2_max, iris2_min,
        iris2_avg, iris2_std, iris2_var respectively. The results must be 
        rounded to not more than two decimal places. 
        Display as shown in sample output file.
    12. Find the max, min, mean and standard deviation for the columns of the 
        array iris3 and store the results in the arrays iris3_max, iris3_min, 
        iris3_avg, iris3_std, iris3_var respectively. The results must be 
        rounded to not more than two decimal places.
        Display as shown in output file.
    13. Check the minimum value for sepal length, sepal width, 
        petal length and petal width of the three species 
        in comparison to the minimum value of sepal length, sepal width, 
        petal length and petal width for the data set as a whole 
        and create the table below indicating by “1” 
        if the species value is greater than the dataset value 
        and “0” otherwise.
    14. COMPUTED RESULTS should be printed in a tablular format as shown
        in the output file. F-strings will help you out here.
"""
import numpy as np

FILE = "iris.txt" # note: check interpreter path
HEADERS = np.array(["sepal length", "sepal width", "petal length", 
                    "petal width", "species #"])

# helper function to display data in tabular format
def display_iris(iris, title=None):
    if title: print(f"\nArray for {title}:")
    for header in HEADERS:
        print(f"{header[:9]}", end="  ")
    print()
    for i in range(len(iris)):
        for j in range(len(iris[i])):
            print("   ", end ="")
            print(f"{iris[i][j]:.02f}", end="    ")
        print()

#helper function to display stats
def display_stats(source_array:dict, species:str=None):
    if species: print(f"\n{species} Statistics:")
    for header in HEADERS[:4]:
        print(f"    {header[:9]}", end="")
    print()
    for key in source_array.keys():
      if key != 'ndarray':  
        print(f"{key.upper()}:",end="")
        for i in range(len(source_array[key])):
            print("     ", end ="")
            print(f"{source_array[key][i]:.02f}", end="    ")
        print()

# find the max values of array columns and return 1d array of values
def array_max(source_array):
    max_array = np.zeros(len(source_array[0,:]))
    for i in range(len(source_array[0,:])):
        max_array[i] = np.max(source_array[:,i])
    return max_array

# find min values of array
def array_min(source_array):
    array = np.zeros(len(source_array[0,:]))
    for i in range(len(source_array[0,:])):
        array[i] = np.min(source_array[:,i])
    return array

# find mean averages of array 
def array_avg(source_array):
    array = np.zeros(len(source_array[0,:]))
    for i in range(len(source_array[0,:])):
        array[i] = np.average(source_array[:,i])
    return array

# standard deviation
def array_std(source_array):
    array = np.zeros(len(source_array[0,:]))
    for i in range(len(source_array[0,:])):
        array[i] = np.std(source_array[:,i])
    return array

# get data from file and format as needed
try: iris = np.genfromtxt(FILE, skip_header=1, delimiter=',')
except Exception as e:
    print(e)
    quit() 
print(iris)
iris = np.concatenate((iris[:,0:4], iris[:,5:]), axis=1)
display_iris(iris, "cleaned data")

print(f"\niris array dimensions: {iris.ndim}, ",
      f"shape: {iris.shape}, size: {iris.size}")

# get data for each species..
# this splitting does not allow for a larger data set, 
# we assume there are 10 of each species.
# maybe classify by if iris[:,-1] == 1|2|3|else ?

# let's just do these as dictionaries, so the whole kit-n-kaboodle
# can be passed to the display_stats function
irises = {}
iris1 = {}
iris2 = {}
iris3 = {}

# set the array for each species as a dictionary value
irises['ndarray'] = iris[:,:4]
iris1['ndarray'] = iris[:10,:4]
iris2['ndarray'] = iris[10:20,:4]
iris3['ndarray'] = iris[20:,:4]

#display the arrays
display_iris(iris1['ndarray'], "Species 1")
display_iris(iris2['ndarray'], "Species 2")
display_iris(iris3['ndarray'], "Species 3")

#calculate the stats for each species (and full dataset)
irises['max'] = array_max(irises['ndarray'])
irises['min'] = array_min(irises['ndarray'])
irises['avg'] = array_avg(irises['ndarray'])
irises['std'] = array_std(irises['ndarray'])

# risking some points on this but I just think it's better structure
iris1['max'] = array_max(iris1['ndarray'])
iris1['min'] = array_min(iris1['ndarray'])
iris1['avg'] = array_avg(iris1['ndarray'])
iris1['std'] = array_std(iris1['ndarray'])

iris2['max'] = array_max(iris2['ndarray'])
iris2['min'] = array_min(iris2['ndarray'])
iris2['avg'] = array_avg(iris2['ndarray'])
iris2['std'] = array_std(iris2['ndarray'])

iris3['max'] = array_max(iris3['ndarray'])
iris3['min'] = array_min(iris3['ndarray'])
iris3['avg'] = array_avg(iris3['ndarray'])
iris3['std'] = array_std(iris3['ndarray'])

# display statistics 
display_stats(irises, "Full Data Set")
display_stats(iris1, "Iris-setosa")
display_stats(iris2, "Iris-versicolor")
display_stats(iris3, "Iris-virginica")

# put all minimum-size data into a dictionary with ndarray values:
min_data = {}
min_data[0] = irises['min'] 
min_data[1] = iris1['min']  
min_data[2] = iris2['min']  
min_data[3] = iris3['min'] 

print("\ncompare minimums data values per species vs dataset")
print("    (0 indicates lowest minimum in dataset)")
print("          ", end="")
for header in HEADERS[:4]:print(f"  {header[:9]} ", end="")
print()

# this seems pretty succinct but is there a better way?
for key,array in min_data.items():
    if key != 0:
        print(f"species #{key}", end ="       ")
        for index in range(len(array)):
            if array[index] > min_data[0][index]:
                print(1, end="           ")
            else:
                print(0, end="           ")
        print()

