#Problem 1:

def help_atm(w_amt):
    g_amt = w_amt

    if (g_amt >= 20):
        print(g_amt//20, 20)
        g_amt = g_amt % 20

    if (g_amt >= 5):
        print(g_amt//5, 5)
        g_amt = g_amt % 5

    if (g_amt >= 1):
        print(g_amt, 1)

help_atm(38)
print("--------")
help_atm(30)
print("--------")
help_atm(8)
print("--------")
help_atm(47)


#Problem 2:

def is_leap(year):
    if year%400 == 0:
        print(True)
    elif year%100 == 0:
        print(False)
    elif year%4 == 0:
        print(True)
    else:
        print(False)

is_leap(2100)
is_leap(2000)
is_leap(2008)
is_leap(2019)