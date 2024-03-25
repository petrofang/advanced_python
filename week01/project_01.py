"""
The file UN.csv contains the names and some details of each country that 
    belongs to the UN.  Each line of the input file contains the record
    of one country -- each record contains 4 items separated by a comma 
    as the delimiter. The items in each record are in this order:

        country
        continent
        population in millions
        area in square miles

The goal of your program is to use this input file to create an output file
    containing only the country and the population.  The output file should 
    be ordered by total population (descending order).

Be sure that your program file contains a comment at the top with your name, 
    contains well-named variables and is commented to indicate the tasks that
    are being completed.

Output is also to be clearly formatted  (see sample output file provided)
"""
import csv

# load countries from csv and convert to a list of tuples (name, population)
country_populations = []
try:
    with open('UN.csv', 'r') as united_nations:
        countries = csv.DictReader(
            united_nations, ['country','continent','population','area'])
        for country in countries:
            # need to "float" the population, because it's a string:
            country_populations.append((country['country'], float(country['population'])))
except FileNotFoundError as e:
    print(e)

else:
    try:
        # sort country_populations by population:
        country_populations.sort(key=lambda a: a[1], reverse=True)

        # write to file:
        with open('populations.txt', 'w') as file:
            file.write(f"Population{'Country':>40}\n")
            for country, population in country_populations:
                file.write(f"{population: 8.2f}M {country:>40}\n")      
    # lazy, but here it is:  
    except Exception as e:
        print(e)