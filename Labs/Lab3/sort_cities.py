# Author: Rahul Gupta
# Date: 2/24/2023
# Purpose: Reads in the city information, sort it according to the three criteria, and writes out the
# results to the three files (cities_alpha.txt, cities_population.txt, and cities_latitude.txt)

from quicksort import sort
from city import City

# Read data from file and create list of City objects
cities = []
data = open("world_cities.txt", "r")

for line in data:
    value = line.strip().split(',')  # Formate each lines based on given instructions.

    # Call the city class
    city = City(value[0], value[1], value[2], str(value[3]), str(value[4]), str(value[5]))
    cities.append(city)


# Comparison function to sort cities alphabetically by name
def compare_alph(city1, city2):
    name1 = city1.name.lower()  # convert to lowercase for comparison
    name2 = city2.name.lower()
    if name1 <= name2:
        return True
    else:
        return False


sorted_cities_alph = sort(cities, compare_alph)

# Write sorted lists to new files based on Alphabetical Order
new_file1 = open("cities_alpha.txt", "w")
for city in sorted_cities_alph:
    new_file1.write(str(city) + "\n")


# Comparison function to sort cities based on decreasing population.
def compare_population(city1, city2):
    return city2.population <= city1.population


sorted_cities_pop = sort(cities, compare_population)

# Write sorted lists to new files based on population
new_file2 = open("cities_population.txt", "w")
for city in sorted_cities_pop:
    new_file2.write(str(city) + "\n")


# Comparison function to sort cities based on latitude from south to north.
def compare_latitude(city1, city2):
    if city1.latitude <= city2.latitude:
        return True
    else:
        return False


sorted_cities_lat = sort(cities, compare_latitude)

# Write sorted lists to new files based on latitude
new_file3 = open("cities_latitude.txt", "w")
for city in sorted_cities_lat:
    new_file3.write(str(city) + "\n")

# Close all the files
data.close()
new_file1.close()
new_file2.close()
new_file3.close()

