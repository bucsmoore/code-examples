# import math
# import random
# import turtle

# pi = "raspberry"
# # modulename.attribute
# print(math.pi)
# # input("This will not save anywhere")
# # abs(-5)
# print(random.randint(1, 1000000))

# pen = turtle.Turtle()  # complex type
# window = turtle.Screen()
# num = 1  # primitive type

# # use the turtle's interface
# pen.shape("turtle")
# pen.color("purple")
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)
# pen.forward(50)
# pen.right(90)

# pen.up()

# pen.forward(100)

# pen.down()
# pen.forward(100)

# # this always has to be the last line executed
# window.exitonclick()


# this is a list for colors

# color = input("Enter 3 colors: ")
# mycolor.append(color)
# print(mycolor)
# color = input(": ")
# mycolor.append(color)
# print(mycolor)
# color = input(": ")
# mycolor.append(color)
# print(mycolor)

# # for
# mycolor = ["red", "green", "blue"]
# for hf in mycolor:  # hf = "blue"
#     print(hf)
#     print("One more")
# print("done")

# looping is also called iteration
for i in [1, 2, 3, 4]:
    print(i)
    i = i * 10
    print(i)

# 2 uses for `for`

## 1. Iterating through a list
# mylist = [9, 5, "hi"]
# for i in mylist:
#     print(i)

## 2.
# ### when you arent using the iterating variable, use _
# for _ in [0] * 100000:
#     print("sunday")


## Range

# # with one argument
# # start: 0 - default
# # stop: 3
# # step: 1 - default
# print(list(range(3)))
# print(range(3))

# # with one argument
# # start: 3
# # stop: 20
# # step: 1 - default
# print(list(range(3, 20)))
# print(range(3, 20))

# # with one argument
# # start: 3
# # stop: 20
# # step: 3
# print(list(range(3, 20, 3)))
# print(range(3, 20, 3))

# items = [0] * 10
# item_len = len(items)
# print(list(range(item_len)))

# print(list(range(100)))
# print(list(range(50, 101)))
# print(list(range(2, 101, 2)))
# print(list(range(100, 0, -1)))
# print(list(range(10, -16, -5)))

# for _ in range(5):
#     print("sunday")


import turtle  # 1.  import the modules

wn = turtle.Screen()  # 2.  Create a screen
wn.bgcolor("green")
donatello = turtle.Turtle()  # 3.  Create two turtles

donatello.shape("turtle")
colors = ["red", "purple", "yellow", "blue"]

for color in colors:
    donatello.color(color)
    for i in range(4):
        donatello.left(90)
        donatello.forward(50)
    donatello.up()
    donatello.forward(100)
    donatello.down()
wn.exitonclick()
