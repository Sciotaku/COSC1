# Filename: SA2.py
# Author Name: Rahul Gupta
# Date: 01/14/2023
# Course: COSC 1
# Purpose: SA3

# Problem 1
BRUTUS_RATE = 0.05
brutus_initial_sum = 1.00
time = 0
brutus_sum = 0
while time <= 2021:
    brutus_sum = brutus_initial_sum * (1 + BRUTUS_RATE)
    brutus_initial_sum = brutus_sum
    time = time + 1
print("The current wealth of Brutus is: ", brutus_sum)

# Function to calculate the compound interest
# def final_sum(initial_sum, rate, time):
#     final_value = 0
#     while time >= 0:
#         final_value = initial_sum * (1 + rate)
#         initial_sum = final_value
#         time = time - 1
#     print(final_value)
#
#
# # For Brutus
# final_sum(1.00, 0.05, 2021)
# # For Portia
# final_sum(100000.00, 0.04, 2021)
