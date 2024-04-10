# Giles Cooper 2024
import numpy as np
import matplotlib.pyplot as plt

FILE = "languages.txt"
PHI = (1 + 5 ** 0.5) / 2

# parse and format FILE:
try: 
    with open(FILE) as file:
        languages = np.array([language.strip(('\'" ')) for language in file.readline().strip().split(",")])
        survey_says = np.array([int(data) for data in file.readline().strip().split(",")])
        # csv could probably do this cleaner, make a dictionary or something
except Exception as e:
    print(e)
    
# make a bar graph:
plt.bar(languages, survey_says, width=1/PHI, color="purple")
plt.title("Programming Language Popularity")
plt.xlabel("Language")
plt.ylabel(r"% Favorited")
plt.show()