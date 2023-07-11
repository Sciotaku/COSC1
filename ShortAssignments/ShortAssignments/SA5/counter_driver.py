# Author: Rahul Gupta
# Date: 02/12/2023
# Purpose: Create a driver for the counter class and check the methods

from ShortAssignments.SA5.counter import Counter

c1 = Counter(9, 0, 1)  # create a counter object
c2 = Counter(60, 0, 2)  # create another counter object

# use the methods defined in the counter object
print("Counter 1:", c1.get_value(), str(c1), c1.tick())
print("Counter 2:", c2.get_value(), str(c2), c2.tick())

for i in range(0, 5):
    print("Counter 1:", c1.get_value(), str(c1), c1.tick())
    print("Counter 2:", c2.get_value(), str(c2), c2.tick())
