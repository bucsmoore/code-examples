# print(True)
# print(False)

# print(True > False)

# print(bool("Hello"))
# print(bool(1))
# print(bool(-1))

# # emptiness to be false
# print(bool(0))
# print(bool(""))
# print(bool([]))

# x = 10
# y = 100000
# print(x < y)
# print(x > y)
# print(x <= y)
# print(x >= y)
# print(x == y)  # equality ==
# print(x != y)

# print(x and y)  # both must be true, result is true
# print(x or y)  # one must be true, result is true
# print(not x)

# print("h" in "hello")
# print("hello" in "hello")
# print("" in "hello")

# print("" is "hello")
# print("" == "hello")

# var = "hello"
# var2 = "hello"
# print(var is var2)

# var = list("hello")
# var2 = list("hello")
# print(var is var2)


# print("Hello" > "Goodbye")
# print(ord("H"), ord("G"))

# print("apple" < "Apple")
# print(chr(97))

# x = 7

# print(x < 16 and x > 2)
# print(2 < x <= 16)

# print(not x < 6)


# print(x > 5 or x == "ABC" and x == 9)

# import turtle

# don = turtle.Turtle()
# don.color("purple")
# screen = turtle.Screen()

# # do stuff

# screen.exitonclick()

# import turtle

# sides = int(input("Num sides?"))
# length = int(input("length?"))

# bill = turtle.Turtle()
# bill.shape("turtle")
# bill.color("orange")

# for _ in range(sides):
#     bill.forward(length)
#     bill.right(360 / sides)

# screen = turtle.Screen()
# screen.exitonclick()

# money = 1
# cost = 78
# if money >= cost:
#     print("Change:", money - cost)
# else:
#     print("not enough money")

# if (money - cost) > 2:
#     print("Not enough change, sorry. I'm keeping it.")
#     if money-cost < 3:
#         print("don't worry about it")
# print("continue")

# money = float(input("Give me money: "))
# cost = 5
# if money >= cost:
#     if money > 10:
#         print("Not enough change")
#     else:
#         print(money - cost)
# else:
#     print("please insert more money")

# money = float(input("Give me money: "))
# cost = 5
# if money > 10:
#     print("Not enough change")
# elif money > 7:
#     print("something")
# elif money >= cost:
#     print(money - cost)
# else:
#     print("please insert more money")

# num = int(input("Enter a num: "))
# for i in range(0, num + 1):
#     if not (i % 3) and not (i % 5):
#         print("fizzbuzz")
#     elif not (i % 5):
#         print("buzz")
#     elif not (i % 3):
#         print("fizz")


import random

randnum = random.randrange(1, 11)
print(randnum)

guess = -1

for i in range(3):
    if guess != randnum:
        guess = int(input("Enter your guess: "))
        if guess < randnum:
            print("Too low")
        elif guess > randnum:
            print("Too high")
        else:
            print("Correct, the number was:", randnum)
            break
