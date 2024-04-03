import numpy as np

def check_int(n:str, can_be_negative=True) -> int:
    # a little helper function for integer validation
    # data may be negative, matrix dimensions may not
    try: 
        n = int(n)
        if n < 1 and not can_be_negative: raise IndexError
        return n
    except Exception as e:
            # crafting the error message:
            positive = " positive" if not can_be_negative else "n"
            return check_int(input(f"It must be a{positive} integer; try again: > "), can_be_negative)
        
while True:
    print("we are going to create two matrices and multiply them.")

    # X is the "width" also meaning the number of columns
    # Y is the "height" meaning the number of rows.
    # so really we're asking for the number of columns first, then rows
    # that was messing me up for a while. it's kind of counterintuitive
    print("    please provide the X dimension of the first matrix: ")
    x_1 = check_int(input(), False)
    print("    and the Y dimension:")
    y_1 = check_int(input(), False)


    print("now for the second matrix, \n    what is the X dimension?")
    x_2 = check_int(input(), False)
    print("    and the Y dimension:")
    y_2 = check_int(input(), False)

    if not x_1 == y_2:
        print("These matrices are not multiplicable.")
    else: break

list1=[]
list2=[]

# get data points from user. fake the index "+1" for
# user-friendliness (or "first" would be "zeroth")
print(f"okay the first matrix is {x_1} by {y_1}.")
for y in range(y_1):
    print(f"Matrix #1, row {y+1}:")
    row = []
    for x in range(x_1):
        print(f"input integer value for column #{x+1}: ")
        row.append(check_int(input()))
    list1.append(row)

print(f"Now, let's enter the data for Matrix 2.")
print(f"dimensions are {x_2} by {y_2}")
for y in range(y_2):
    print(f"Matrix #2, row #{y+1}:")
    row = []
    for x in range(x_2):
        print(f"input integer value for column #{x+1}: ")
        row.append(check_int(input()))
    list2.append(row)

# lists for debug:
# list1 = [[1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 0]]
# list2 = [[1, 2, 3],
#          [0, 1, 2],
#          [3, 0, 1],
#          [2, 3, 0],
#          [1, 2, 3]]

# initialize the ndarrays
matrix_a = np.array(list1)
matrix_b = np.array(list2)
# these lines help with the non-user generated debug lists:
# y_1, x_1 = matrix_a.shape
# y_2, x_2 = matrix_b.shape
matrix_c = np.zeros((y_1, x_2), np.int64)
matrix_z = np.matmul(matrix_a, matrix_b)

for x in range(y_1):
    for y in range(x_2):
        # for each square on the new matrix:
        matrix_c[x,y] += np.sum(matrix_a[x] * matrix_b[:,y])

# verify the resultant matrix:
matrix_z = np.matmul(matrix_a, matrix_b)
print(matrix_a)
print("*")
print(matrix_b)
print("=")
print(matrix_c)
if (matrix_c == matrix_z).all():
    print("np.matmul() affirms this matrix multiplication.")
else:
    print("hmm, something is wrong here.")