from Other.lollipop import Lollipop  # import Lollipop class from lollipop.py file

lollipop1 = Lollipop("green", 50)  # instantiate an object of class Lollipop, with values "green" and 50
lollipop2 = Lollipop("red", 10)

print(lollipop1)  # print lollipop1, i.e. test __str__ method
print(lollipop2)  # print lollipop2, i.e. test __str__ method

print(lollipop1.lollipop_color)  # print instance variable lollipop1.color
print(lollipop2.lollipop_color)

lollipop1.lick(40)  # lick the lollipop 40 times, test .lick() method
print(lollipop1.get_licks_left())  # test .get_licks_left() method
lollipop1.lick(20)  # attempt to "break" .lick() method

