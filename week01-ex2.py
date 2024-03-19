# Week 1 Ex 2
# Giles Cooper
"""
The purpose of this exercise is to give you some practice using the csv module
    of Python.  This module provides a convenient way to work with csv file, 
    particularly when the data is to be stored as a dictionary.

You are to use the file “presidential.csv” for input to your program.  If you 
    take a look at the contents of this file, you will see that the file 
    contains a number of rows -- each with a president's name, start date, 
    end date and party affiliation.  The first row of the file, as is common 
    with many csv files, contains the column titles.

The program is to:

Open the file using method provided by the csv module, 
    storing the contents to a dictionary

Open a text file which will contain your output

Using your dictionary of stored data, output the names of all Democratic 
    presidents that did not serve full terms to your output file
    (start and end dates of 1/20 can help identify these presidents)

Using your dictionary of stored data, output the names of all Republican 
    presidents that did not serve full terms to your output file           
    (start and end dates of 1/20 can help identify these presidents)

Be sure that your program file contains a comment at the top with your name, 
    contains well-named variables and is commented to indicate the tasks that 
    are being completed. Output is also to be clearly formatted.
"""

import csv
short_term_dems=[]
short_term_reps=[]

# find short-term presidents and sort by party.
with open('presidential.csv', 'r') as presidents:
    president_list = csv.DictReader(presidents)
    for president in president_list: 
        short_term=False       
        if not president["start"].startswith("1/20"): short_term=True
        if not president["end"].startswith("1/20"): short_term=True
        if short_term: 
            if president["party"] == "Democratic": 
                short_term_dems.append(president["name"])
            elif president["party"] == "Republican": 
                short_term_reps.append(president["name"])

with open('partial_term_presidents.txt', 'w') as part:
    part.write("Democratic Presidents:\n")
    for president in short_term_dems:
            part.write(f'{president} served an incomplete term.\n')  
    part.write("\nRepublican Presidents:\n")
    for president in short_term_reps:
            part.write(f'{president} served an incomplete term.\n')
