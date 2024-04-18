# Giles Cooper
"""This exercise give you experience using Pandas Series 
    and DataFrame objects. Complete the following:

1.)  Create the following Series  
    Vowels, having 5 elements with index labels 
    'a', 'e', 'i', 'o' and 'u' and all the five values set to zero.

2.)  Set all the values of Vowels to 10 and display the Series.

3.)  Divide all values of Vowels by 2 and display the Series.

4.)  Create another series Vowels1 having 5 elements with index labels 
    'a', 'e', 'i', 'o' and 'u' having values [2,5,6,3,8] respectively.

5.) Add Vowels and Vowels1 and assign the result to Vowels3.  Display Vowels3.

6.) Subtract Vowels from Vowels1, and display the result.

7.) Alter the labels of Vowels1 to ['A', 'E', 'I', 'O', 'U'].  Display Vowels1.
"""


import pandas as pd

vowel_list = ['a', 'e', 'i', 'o', 'u'] # sorry, 'y' -- not today
vowels = pd.Series(0, vowel_list) 

vowels += 10
print("\nvowels += 10")
print(vowels)

vowels = vowels / 2
print("\nvowels = vowels / 2")
print(vowels)

vowels1 = pd.Series([2,5,6,3,8], vowels.index)
print("\nvowels1 = pd.Series([2,5,6,3,8], vowels.index)")
print(vowels1)

vowels3 = vowels + vowels1
print("\nvowels3 = vowels + vowels1")
print(vowels3)


print("\nvowels1-vowels")
print(vowels1-vowels)

print("\nvowels1.index = [v.upper() for v in vowel_list]")
vowels1.index = [v.upper() for v in vowel_list]
print(vowels1)