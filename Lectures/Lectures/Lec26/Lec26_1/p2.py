#Author: Vasanta
#Date: 03/03/2023
#Purpose: Demo deque

from collections import deque

d = deque()

d.append(10)
d.append(20)
d.append(5)
d.append(12)

x = d.popleft()
print(x)
