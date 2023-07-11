# Filename: SA2.py
# Author Name: Rahul Gupta
# Date: 01/14/2023
# Course: COSC 1
# Purpose: SA3

# Problem 2

BRUTUS_RATE = 0.05
PORTIA_RATE = 0.04
brutus_initial_sum = 1.00
portia_initial_sum = 100000.00
time = 0
brutus_sum = 0
portia_sum = 0
while time <= 2021:
    brutus_sum = brutus_initial_sum * (1 + BRUTUS_RATE)  # final sum of Brutus
    brutus_initial_sum = brutus_sum
    portia_sum = portia_initial_sum * (1 + PORTIA_RATE)  # Final sum of Portia
    portia_initial_sum = portia_sum
    time = time + 1
    if brutus_sum > portia_sum:
        print("Brutus's wealth at " + str(time) + " is " + str(brutus_sum))
        print("Portia's wealth at " + str(time) + " is " + str(portia_sum))
        print("The year when Brutus's wealth first exceeds Portia's wealth is:", time)
        break
