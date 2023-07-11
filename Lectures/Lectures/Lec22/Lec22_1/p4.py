#Author: Vasanta
#Date: 02/22/2023
#Purpose: Towers of Hanoi

def toh(n, source, dest, spare):
    if n == 1:
        print("Move ring", n, "from", source, "to", dest)
        return

    toh(n-1, source, spare, dest)
    print("Move ring", n, "from", source, "to", dest)
    toh(n-1, spare, dest, source)

toh(3, "A", "B", "C")