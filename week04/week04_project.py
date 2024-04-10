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
        to be cleaned (ie extra “ in data item.Empty column data should be
        replaced by 'none' (either on load or by working w/ array.     
        
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