# Author: Rahul Gupta
# Date: 2/19/2022
# Purpose: System class for lab 2


class System:
    def __init__(self, body_list):
        self.body_list = body_list  # Defining instance variable

    # Method to call the draw method in body class
    def draw(self, cx, cy, pixels_per_meter):
        for planet in self.body_list:
            planet.draw(cx, cy, pixels_per_meter)

    # Method to compute acceleration of the body
    def compute_acceleration(self, n):
        ax = 0
        ay = 0
        for i in range(len(self.body_list)):
            if i != n:
                # calculate the x distance between the Earth and the moon
                dx = self.body_list[i].x - self.body_list[n].x

                # calculate the y distance between the Earth and the moon
                dy = self.body_list[i].y - self.body_list[n].y

                # calculate the total distance between the Earth and the moon
                total_dist = (dx ** 2 + dy ** 2) ** (1 / 2)

                # Calculate the acceleration due to gravity
                a = 6.67 * 10 ** (-11) * self.body_list[i].mass / total_dist ** 2

                # Calculate the x-component of acceleration
                ax = ax + a * dx / total_dist

                # Calculate the x-component of acceleration
                ay = ay + a * dy / total_dist

        return ax, ay

    # Method to call the update_position and update_velocity in body class.
    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)

        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(ax, ay, timestep)
