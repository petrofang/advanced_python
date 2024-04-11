# Giles Cooper 2024
"""For this program you will be examining physical characteristics of the 
major characters from the StarWars trilogy contained in the file starwars.csv

Your program is to:

    Open the file starwars.csv, reading data into an ndarray.
        You only need name, hair_color, eye_color and gender columns
        Any row that would cause a raised exception (ie too many columns) 
            should be omitted.  
        The many parameters of the genfromtxt method can help here.

    Output array as read, so that you know what you are working with.

    View your data and see if there is any other data that needs 
        to be cleaned (ie extra “ in data item. Empty column data should 
        be replaced by 'none' (either on load or by working w/ array.     
        
    Output array data as a formatted table.
 
    Output 6 tables, indicating specifics on characters which have blue eyes,
        brown eyes, black eyes, yellow eyes, orange eyes and Other colors.
        (View sample output).
 
    Draw a pie chart indicating the blue,brown,black, yellow, orange 
        and other eye categories.
 
    Draw a bar chart which shows genders of Masculine, Feminine and Others.
 
    Finally, draw a bar chart which describes the blue-eyed characters 
        that are blond, brunette (brown) and black haired.
 
    Be sure that each of your plots contains a title, pie sections labeled and
        quantities noted, and bar charts with horizontal and vertical labeling.
 """
import csv 
import numpy as np
import matplotlib.pyplot as plt

FILE = "starwars.csv"

def table(data:np.ndarray):
    """ Print data array in tabular format """
    for i in range(len(data)):
        for j in range(len(data[i])):    
            print(f"{data[i][j]:<24}", end = "")
        print()
    print()

def get_eye_color(data:np.ndarray, color : str='') -> np.ndarray:
    """ returns an array filtered to only the eye color specified. """
    # trim headers:
    data = data[1:]

    #filter for eye color:
    if color: data = data[data[:,2]==color]
    data = data[:,(0,1,3)]

   # insert new headers
    data = np.insert(data, 0, np.array([f"{color.upper()} EYES", "Hair Color", "Gender"]), axis=0)
    return(data)

#   get hair color
def get_hair_color(data, color): return data[data[:,1]==color]


try: # to get the data from the file:
    # the "incorrect lengths" are not incorrect; they are being parsed wrong.
    # we can avoid errors caused by commas-within-quotes if we let
    # csv module handle the initial file parsing. from there it's
    # trivial to convert to list then ndarray. 
    with open(FILE) as f: data = np.array(list(csv.reader(f)))
except Exception as e: print(e)

print("Raw Data:")
print(data)

# pare down dataset and fill empty strings:
data = data[:,(0,3,5,8)]
for index,array in enumerate(data):
    for schmindex,datum in enumerate(array):
        if not datum: data[index,schmindex] = "none"
print("Parsed data:")
table(data)

#print table for each eye color
blues = get_eye_color(data,'blue')
browns = get_eye_color(data,'brown')
blacks = get_eye_color(data,'black')
yellows = get_eye_color(data,'yellow')
oranges = get_eye_color(data, 'orange')
# okay... but how do I do "others" now??

others = []
for row in data[1:].tolist():
    if row[2] not in ['blue', 'brown', 'black', 'yellow', 'orange']:
        others.append(row)

others = np.array(others)

table(blues)
table(browns)
table(blacks)
table(yellows)
table(oranges)
print("OTHER COLOR EYES        HAIR                    EYE COLOR")
table(others[:,:-1]) 

# there's got to be a better way to plot this 
listed_already = np.concatenate((browns[1:], blues[1:], blacks[1:], yellows[1:], oranges[1:]))
labels = ['blue', 'brown', 'black', 'yellow', 'orange', 'other']
plt.pie([len(blues)-1, len(browns)-1, len(blacks)-1, len(yellows)-1, len(oranges)-1, len(data)- len(listed_already)], labels=labels, colors=('blue', 'brown', 'darkgrey', 'yellow', 'orange', 'green'), autopct="%1.0f")
plt.title("Eye Colors")
plt.show()

#determine gender counts and plot them
dudes, dudettes, etceteras = 0,0,0
for datum in data:
    if datum[3] == "masculine": dudes += 1
    elif datum[3] == "feminine": dudettes += 1
    else: etceteras += 1

plt.bar(["masculine", 'feminine', 'other'],[dudes, dudettes, etceteras])
plt.ylabel('Number of Characters')
plt.xlabel('Gender Representation')
plt.title("Star Wars - Bechdel")
plt.show()

#determine hair color and plot counts:
blonds=get_hair_color(blues, 'blond')
brunes=get_hair_color(blues, 'brown')
blacks=get_hair_color(blues, 'black')

plt.bar(['blonds', 'brunes', 'black-haired folks'], [len(blonds), len(brunes), len(blacks)], color='cyan', width=.618)
plt.ylabel('Number of Characters')
plt.title("Hair color of blue-eyes")
plt.show()
