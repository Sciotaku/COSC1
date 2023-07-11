#Author: Vasanta
#Date: 03/03/2023
#Purpose: demo deque

from collections import deque

d = deque()

d.append(10)
d.append(5)
d.append(25)
d.append(23)

x = d.popleft()
print(x)
