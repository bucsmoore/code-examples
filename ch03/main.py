# money = int(input("Please enter money: "))
# cost  = 2.15
# if money >= cost:
#     print("Here's change:", money-cost)
# else:
#     print("More money needed")

# x = int(input("Enter a number:"))
# if x:
#     print(x)
# print("done with x")

# if x > -1:
#     print(x)
# print("done with x > -1")

# cost = 2.15
# amt = 10

# if amt >= cost:
#     if amt >= 10:
#         print("Only denominations 5 or less")
#     else:
#         print("Change:", amt-cost)
# else:
#     print("more money")

# if amt >= 10:
#         print("Only denominations 5 or less")
# elif amt >= cost:
#     print("Change:", amt-cost)
# elif amt >= 1:
#     print("Cheapskate")
# else:
#     print("more money")

# x = 20

# if x >= 5:
#     print("a")
# elif x >= 10:
#     print("b")
# else:
#     print("c")


# x = 20

# if x >= 10: #most exclusive condition
#     print("b")
# elif x >= 5:
#     print("a")
# else:
#     print("c")


## Fizzbuzz

# - Take user input as an integer
# - For multiples of 3, print "Fizz"
# - For multiples of 5, print "Buzz"
# - For multiples of 3 and 5, print "FizzBuzz"

# num = int(input("Num?: "))

# for i in range(num + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")


# Events

import random

import pygame

pygame.init()
screen = pygame.display.set_mode()

colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

print(colors)

msg = """use your arrow keys:
    UP: red
    DOWN: green
    LEFT: blue
    RIGHT: yellow

    press any key when ready
"""


for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(500)

input(msg)

user_guess = []
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            user_guess.append("red")
        elif event.key == pygame.K_DOWN:
            user_guess.append("green")
        elif event.key == pygame.K_LEFT:
            user_guess.append("blue")
        elif event.key == pygame.K_RIGHT:
            user_guess.append("yellow")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos)
print(user_guess, colors)
if user_guess == colors:
    print("You won")
else:
    print("Pay attention, do better!")

pygame.quit()
