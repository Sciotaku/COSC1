# Author: Rahul Gupta
# Date: 02/12/2023
# Purpose: Create a counter class that countdowns to 0 and wraps to limit - 1

class Counter:
    def __init__(self, limit, initial_value=0, min_digits=1):
        self.limit = limit
        self.min_digits = min_digits

        if 0 <= initial_value < limit:  # check if the initial value if within limit
            self.value = initial_value
        else:
            print("Error: The initial value must be between 0 and", self.limit)
            self.value = limit - 1  # wrap the value to limit - 1

    def get_value(self):
        return self.value  # return value as an integer

    def __str__(self):  # return value as a string
        str_value = str(self.value)  # convert the value to a string
        req = self.min_digits - len(str_value)  # calculate the no. of digits in the given value
        if len(str_value) < self.min_digits:  # check if the no. of value is at least min_digit
            str_value = '0' * req + str_value  # append O's to reach min_digit
        return str_value

    def tick(self):  # countdowns the value
        if self.value <= 0:  # check if the value is reaching negative
            self.value = self.limit - 1  # wrap the value to limit - 1
            return True
        else:
            self.value = self.value - 1  # decrement the value by 1
            return False




