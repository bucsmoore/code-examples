# print("Hello")  # procedure
# val = input("input something")  # functions return a value


# def myfunc():
#     x = 5  # variable created inside a function are dleted when the function ends
#     print("in function")
#     print("still in the function")
#     print(x) # the variable's scope


# myfunc()

# print(x) - invalid


## find max

# import random


# def findmax(numbers):
#     max = numbers[0]
#     for i in numbers:
#         if i > max:
#             max = i

#     print(max)


# nums = []
# new_num = int(input("add some numbers (0 to stop): "))
# while new_num:
#     nums.append(new_num)
#     new_num = int(input("add some numbers (0 to stop): "))

# findmax(nums)

# nums = [random.randint(1, 100) for _ in range(100)]
# findmax(nums)
# # do some more code
# findmax([4, 3, 7, 10, 999999])


# # default parameter values always go last
# def add(x, y=1):  # the variable names are parameters
#     return x + y


# print("Hello")  # positonal arguments
# range(start=1, stop=2, step=3)  # keyword arguments
# add(5, 6)  # values being passed are arguments
# add(x=5, y=6)  # prefer named/keyword parameters
# add(y=5, x=6)
# add(x=5)
# add(5)


# def my_min(x, y, z):  # , num):
#     result = x * factor
#     # factor *= 2

#     if result > y * factor:
#         result = y * factor
#     if result > z * factor:
#         result = z * factor
#     # if result > num * factor:
#     #     result = num * factor
#     # print(result)

#     return result


# factor = 5
# result = 0
# # f(x) = y
# # y = f(x)
# # num = int(input("enter a num: "))
# minnum = my_min(
#     1,
#     2,
#     3,
# )  # num)
# print("The min value is:", minnum)

# print("You guessed correct") if guess == "Red" else print("You guessed wrong")


# locally scoped variables includes parameters
# the placeholder for the value is the parameter
# def foo(x):  # x = a : happens automatically
#     # x limited to the scope of the function
#     x = input("guess: ")
#     print(x)


# a = 5
# foo(a)  # the value passed is the argument

# # def bar():

# Write a function to draw a regular polygon based on the function arguments.

# draw_eq_shape

# takes a turtle object, num_sides, and side_length as parameters. The function should use the turtle object to draw a shape according to the parameters.
# You should only use local variables inside your function
# After you define your function, add code that:

# creates a turtle
# changes the turtle object’s shape to ‘turtle’ and color to green
# Ask a user for num_sides and side_length values
# make sure you cast as the correct type
# call draw_eq_shape and pass your turtle, num_sides, and side_length as arguments


# import turtle


# def draw_eq_shape(turtle_object, num_sides, side_length):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle_object.forward(side_length)
#         turtle_object.right(angle)


# t = turtle.Turtle()
# s = turtle.Screen()
# sides = int(input("Enter the number of sides: "))
# length = int(input("Length of each side?: "))

# draw_eq_shape(t, sides, length)

# s.exitonclick()


# def vend(currency, button):
#     """
#     This function does stuff
#     return - str
#     args - current [int], button [str]
#     """
#     items = {
#         "A1": {"cost": 1, "item": "Hot Coffee"},
#         "A2": {"cost": 2, "item": "Hot Tea"},
#         "B1": {"cost": 5, "item": "Hot Chocolate"},
#     }

#     item_data = items[button]
#     if currency >= item_data["cost"]:
#         change = currency - item_data["cost"]
#         print("Your change is: ", change)
#         return item_data["item"]
#     else:
#         # print is not return
#         # print is a NOOP (No Operation)
#         print("Not enough money. Try again.")


# shows where your program starts


# def main():
#     """
#     main does not have a docstring
#     """
#     print(vend.__doc__)
# money = 5

# button = "A2"

# me = vend(money, button)
# print("I have a", me)

# money = 5
# button = "A2"

# me = vend(1, "B1")
# print("I have a", me)


# always at the end
# main()


# Managing Complexity

# 1000 lines code

# global Scope
x = 1
y = 1


# .. 500 lines later

x = "Hi"


# Variables should always be scoped (i.e. inside a function)
# - Constants: ALL CAPS (convention)
# Convention : where to start tracing
# def main():  # driver
#     x = 5
#     myfunction(x)
#     x = "hi"


# PI = 3.1475926
# RED = [255, 0, 0]


# def myfunction():
#     """
#     description
#     args
#     return
#     """
#     pass

# main()

# Programming Patterns
# - MVC
# - for loop
# - accumulator

# num = 0
# for i in range(10):
#     num = num + i
#     # num += i
# print(num)

# num = []
# for i in range(10):
#     num.append(num)
#     # num += i
# print(num)


# imports

# constants

# functions
# main should be in here somewhere

# call to main()


def removeVowels(somestr):
    vowels = "aeiou"
    vowels += vowels.upper()
    newstr = ""
    for ch in somestr:
        if ch not in vowels:
            newstr += ch
    return newstr


def main():
    mystr = "BInghamton"
    result = removeVowels(mystr)
    print(result)
    mystr = "Hoooooowdy!"
    result = removeVowels(mystr)
    print(result)


main()
