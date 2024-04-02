# Week 3 - Exercise #1

import numpy as np
import numpy.random as rng

# 1.26.4
print(f"\nNumPy version: {np.version.version}\n")

array = np.zeros(10, np.int_)
print(f"{array}\n")

array[4:7] = 5
print(f"{array}\n")

array=np.array([i for i in range(10,100)])
print(f"{array}\n")

array = np.array([rng.randint(10,100) for _ in range(10)])
print(f"{array}\n")

array = np.array([[0,1,2],
                  [3,4,5],
                  [5,6,7]])
print(f"{array}\n")

array = np.array([1,2,0,0,4,0])
print("Find the non-zero values:")
text_array=f" {[f'{i:<2}' for i in array]}"
print(f"{text_array}")
print(f"{array != 0}\n")

print(f"{np.eye(3)}\n")

array = np.zeros((5,5), np.int8)
print(array)
array[0:5,0] = 5
array[4:5] = 5
print(array)
print()

array = np.zeros((8,8), np.int8)
# I had trouble with this one and did not find the answer on my own
# I get the nested slicing I guess, but I need more practice
array[1::2, ::2] = 1  
array[::2, 1::2] = 1
print(array)
print()

array = np.array([rng.random() for _ in range(25)])
print(array)
array = np.sort(array)
print(array)