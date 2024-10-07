# import turtle

# data[n]

# mystr = "Hello"
# # mystr[3] = "j"
# mystr + "Goodbye"
# mylist = list(mystr)
# mylist.append("Goodbye")
# myotherlist = mylist + list("Goodbye")
# print(mystr, mylist, myotherlist)

# slicing
# new_str = mystr[2:4]
# print(new_str)
# new_str = mystr[2:]
# print(new_str)
# new_str = mystr[:4]
# print(new_str)
# myturtle = turtle.Turtle()
# myturtle.speed(0) #makes turtle go faster
# screen = turtle.Screen()
# width = screen.window_width()
# height = screen.window_height()

# xcoor, ycoor = myturtle.pos()

# horizontal_valid = abs(xcoor) < width/2
# vertical_valid = abs(ycoor) < height/2

# mynums = [1, 2, 3, 4, 5, 6]
# # mystr[3] = "j"
# mystr + "Goodbye"
# mylist = list(mystr)
# mylist.append("Goodbye")
# myotherlist = mylist + list("Goodbye")
# print(mystr, mylist, myotherlist)

# slicing
# new_str = mynums[2:4]
# print(new_str)
# new_str = mynums[2:]
# print(new_str)
# new_str = mynums[:4]
# print(new_str)
# new_str = mynums[:]
# print(new_str)
# new_str = mynums[2:4] + mynums[-2:]
# print(new_str)
# mynums[2:3] = [5]
# print(mynums)

# for value in mynums:  # i = mynums[0]
#     value = 0
# print(value)
# print(mynums)

# for idx, value in enumerate(mynums):
#     mynums[idx] = 0 * value
# print(mynums)


# for i in [1, 2, 3, 4]:
#     print(i)

# for i in range(10):
#     print(i)

# num = int(input("Please enter a number"))
# var = 1000
# for i in range(var):
#     if 1 <= i <= 100:
#         num = int(input("Please enter a number between 1 and 100: "))

# 1 <= i <= 100

# num = int(input("Please enter a number"))
# while num < 1 or num > 100:
#     num = int(input("Please enter a number between 1 and 100: "))

# for i in range(10):
#     print(i)

# i = 0
# while i < 10:  # infinite loop
#     print(i)
#     i = i + 1  # i += 1


# import random

# code = random.randrange(1000)
# for i in range(1000):
#     if i == code:
#         print("broken")
#         break

# code = random.randrange(1000)
# i = 0
# while i != code and i < 1000:
#     if i == code:
#         print("broken")

# n = 10
# answer = 1
# while n > 0:
#     answer = answer + n
#     n = n - 1
# print(answer)


# mytup = (1, 2, 3)
# print(mytup)
# print(mytup[0])
# mytup[0] = 5

# mytup = (5,) * 4  # tuples of 1 need a comma
# print(mytup)


# import turtle

# screen = turtle.Screen()
# screen.setworldcoordinates(-1, -1, 1, 1)
# t = turtle.Turtle()
# t.speed(0)
# t.circle(1, steps=360)
# t.up()
# t.goto(-1, 0)
# t.down()
# t.goto(1, 0)
# t.up()
# t.goto(0, -1)
# t.down()
# t.goto(0, 1)

import random

num = random.randint(1, 1000)
high = 1000
guess = 0
num_guesses = 0
while guess != num:
    guess = int(input("Guess a number between 1 and 1000: "))
    if guess < num:
        print("Your guess is too low")
    if guess > num:
        print("Your guess is too high")
    num_guesses += 1

print(num, "is correct! It only took you", num_guesses, "guesses to get it.")


#################################################################################

# contacts = [["Aang", "657-6789"], ["Sokka", "568-9970"], ["Katara", "645-7897"]]
# name = input("Who's number do you want? ")
# for contact in contacts:
#     if contact[0] == name:
#         print(contact[1])
