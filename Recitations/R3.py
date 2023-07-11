# Problem 1
#
# from cs1lib import *
# x = 200
# y = 200
# r = 20
# move_left = False
# move_right = False
# draw = True
#
#
# def release(key):
#     global move_left, move_right
#     if key == "l":
#         move_right = False
#     if key == "r":
#         move_left = False
#
#
# def keyword(key):
#     global x, y, move_left, move_right
#     if is_key_pressed("l"):
#         move_left = True
#     if is_key_pressed("r"):
#         move_right = True
#
#
# def drawing():
#     global x, y
#
#     if draw:
#         clear()
#         set_fill_color(1, 0, 0)
#         draw_circle(x, y, r)
#
#     if move_right:
#         x = x + 2
#     if move_left:
#         x = x - 2
#
#
# start_graphics(drawing, key_press=keyword, key_release=release)


# Problem 2
#
# def prod(n, m):
#     product = n * m
#     return product
#
#
# prod1 = prod(125, 1234)
# prod2 = prod(234, 679)
#
#
# def max_prod_num(n, m):
#     if n > m:
#         print("The first product is greater than the second")
#         return n
#     else:
#         print("The second product is greater than the first")
#     return m
#
#
# print(max_prod_num(prod1, prod2))


