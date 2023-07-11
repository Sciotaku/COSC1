# Author: Rahul Gupta
# Date: 2/24/2023
# Purpose: To visualize the cities on the world map based on decreasing population


from cs1lib import *
from city import City
from quicksort import *

# Constants for image and window sizes
IMG_WIDTH = 720
IMG_HEIGHT = 360
WIN_WIDTH = 720
WIN_HEIGHT = 360

n = 50  # Number of cities needed to visualize
no_cities = 1  # Number of cities to draw
rate = 5  # speed at which cities are drawn one after the other
img = load_image("world.png")  # Load the image


cities_list = []
data = open("world_cities.txt", "r")

for line in data:
    value = line.strip().split(',')  # Formate each lines based on given instructions.

    # Call the city class
    city = City(value[0], value[1], value[2], str(value[3]), str(value[4]), str(value[5]))
    cities_list.append(city)


# Comparison function to sort cities based on decreasing population.
def compare_population(city1, city2):
    return city2.population < city1.population


sorted_cities_pop = sort(cities_list, compare_population)
cities = sorted_cities_pop


# Helper function to calculate the number of cities to draw
def draw_city():
    global no_cities
    if no_cities <= n:
        no_cities = no_cities + 1


# Helper function that calls the draw method from the city class
def draw():
    for i in range(0, no_cities):
        city = cities[i]
        city.draw(IMG_WIDTH // 2, IMG_HEIGHT // 2)


# Main function
def visualize_cities():
    global no_cities

    # Draw the world map image.
    draw_image(img, 0, 0)

    # Call the draw function to draw the cities on the map
    draw()

    # Call the draw_city function to increase the number of cities to draw
    draw_city()


start_graphics(visualize_cities, framerate=rate, width=WIN_WIDTH, height=WIN_HEIGHT)
