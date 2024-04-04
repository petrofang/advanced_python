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