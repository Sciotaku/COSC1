# Author: Rahul Gupta
# Date: 02/12/2023
# Purpose: Create a timer for the counter class and check the methods

from ShortAssignments.SA5.timer import Timer

timer = Timer(1, 30, 0)  # create a timer object
print(timer)  # print the timer value

while not timer.is_zero():  # prints all the timer value till it reaches 00:00:00
    timer.tick()
    print(timer)
