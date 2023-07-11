class Lollipop:

    def __init__(self, color, size):
        self.lollipop_color = color  # set instance variable, self.lollipop_color equal to color
        self.lollipop_size = size  # set instance variable, self.lollipop_size equal to size
        self.material = "sugar"  # set instance variable, self.material equal to "sugar"

    def get_licks_left(self):
        return self.lollipop_size

    def lick(self, number_of_licks):

        if self.get_licks_left() - number_of_licks >= 0:   # if there is more lollipop than there are the number of
            # licks, lick the lollipop!
            self.lollipop_size = self.lollipop_size - number_of_licks
        else:  # if there are more licks than there is lollipop
            print("There is not enough lollipop to lick!")

    def __str__(self):
        return_string = "The lollipop is " + str(
            self.lollipop_color) + " in color, made of " + self.material + ", and has " + str(
            self.lollipop_size) + " licks left!"
        return return_string  # return a descriptive string of the lollipop
