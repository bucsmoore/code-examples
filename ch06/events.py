import random

import pygame

pygame.init()
pygame.event.pump()
screen = pygame.display.set_mode(300, 400)
colors = ["red", "purple", "green", "blue"]
random.shuffle(colors)
for color in colors:  # color = colors.next()
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(500)

    # add black screen between each color to make them more distinct
    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)
msg = """
Your arrow keys correspond to the following colors:
  UP: red
  DOWN: purple
  LEFT: green
  RIGHT: blue

  Click on the window, enter the sequence, then press <enter> in the console
"""

input(msg)  # use input to pause the program for the user
user_guess = []
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            screen.fill("red")
            user_guess.append("red")
        elif event.key == pygame.K_DOWN:
            screen.fill("purple")
            user_guess.append("purple")
        elif event.key == pygame.K_LEFT:
            screen.fill("green")
            user_guess.append("green")
        elif event.key == pygame.K_RIGHT:
            screen.fill("blue")
            user_guess.append("blue")
        pygame.display.flip()
        pygame.time.wait(1000)
print("You Entered:", user_guess)
print("The correct pattern was", colors)

if user_guess == colors:
    print("Correct! You win.")
else:
    print("Were you even paying attention?")

pygame.quit()
