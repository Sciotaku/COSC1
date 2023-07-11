# Author: Rahul Gupta
# Date: 2/24/2023
# Purpose: City class for Lab 3


from cs1lib import *
from random import uniform, randint


class City:
    def __init__(self, country_code, city_name, region, population, latitude, longitude):

        # Defining Instance Variables
        self.country_code = str(country_code)
        self.name = str(city_name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def draw(self, cx, cy):
        px = int((self.longitude + 180) / cx * 720)  # Equation to scale the longitude to the size of the image
        py = int((90 - self.latitude) / cy * 360)  # Equation to scale the latitude to the size of the image
        set_fill_color(uniform(0, 1), uniform(0, 1), uniform(0, 1))
        draw_circle(px, py, 5)

    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
