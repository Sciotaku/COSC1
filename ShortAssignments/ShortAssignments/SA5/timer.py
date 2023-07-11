# Author: Rahul Gupta
# Date: 02/12/2023
# Purpose: Create a timer class that countdowns a time to 00:00:00

from ShortAssignments.SA5.counter import Counter  # import the counter object


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self):  # returns the time as a string
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self):  # countdown the time
        if self.seconds.tick():  # check seconds whether to wrap or not
            if self.minutes.tick():  # check minutes whether to wrap or not
                self.hours.tick()  # decrease or wrap the hours

    def is_zero(self):  # check if the entered time is 00:00:00
        if self.hours.get_value() == 0 and self.minutes.get_value() == 0 and self.seconds.get_value() == 0:
            return True
        return False



