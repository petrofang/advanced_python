# Week 1 Ex. 1: File I/O and Exception Handling
# Giles Cooper
'''
For this exercise you are to write a Python program which:

1.) Allows the user to enter a positive int value, N.  
    If the user enters a negative value, they are to be reprompted until
    a positive value is provided. If an invalid value (non-digit) entered,
    the user is to be informed, and reprompted.

2.)  Ask the user for a name to be used for an output file

3.) Output N random numbers between 1 and 100 to the output file 

Be sure that your program file contains a comment at the top with your name,
contains well-named variables and is commented to indicate the tasks 
that are being completed. Output is also to be clearly formatted.
'''
from random import randrange
count = None
while not count:
    count = input("How many random numbers to generate?\n >>> ")

    try:
        count = int(count)    
        if count <= 0:
            print("I'm gonna need a number greater than 0...")
            count = None
        elif count > 100:
            print("That's too much for this demo; I'm just going to do 100.")
            count = 100
        else:
            print("Good job. ", end="")

    except ValueError:
        print("that's not a number.")
        count = None

print("What should we call the filename?")
filename = input(" >>> ")
# use a default filename if the user wants to play games:
if not filename: print(f"using default filename: {count}_random_numbers.txt")
filename = filename if filename else f"{count}_random_numbers.txt" 

# write so many numbers to file, line by line
with open(filename, 'w') as file:
    for i in range(0, count):
        random_number = randrange(1, 100)
        print(f"writing to {filename}: {random_number}.")
        file.write(f"{random_number}\n")






