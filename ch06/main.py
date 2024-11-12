# import json

# # JSON is a string format that is easily parsed by machines
# # store simple objects and lists

# person = {"name": "", "age": 0}

# persons = []
# for i in range(3):
#     person = {"name": "name" + str(i), "age": str(i)}
#     persons.append(person)

# print(type(persons), persons)

# # dumps takes python object (dictionary or list) and converts it to a json string
# persons_json_str = json.dumps(persons)
# print(type(persons_json_str), persons_json_str)

import random

import pygame

# Events
# GUI - anytime user interacts with the system, it creates an event
# - Events are handled by the OS
#   - mouse click, move
#   - keyboard event

pygame.init()
pygame.event.pump()

screen = pygame.display.set_mode((300, 400))

colors = ["purple", "blue", "green", "gold"]
random.shuffle(colors)

width, height = pygame.display.window_size()

hit_box_width = width / 2
hit_box_height = height / 2

hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "green": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "purple": pygame.Rect(0, 0, hit_box_width, hit_box_height),
}

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(500)
    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

msg = """
Your arrow keys correspond to the following colors:
  UP: gold
  DOWN: purple
  LEFT: green
  RIGHT: blue

  Click on the window, enter the sequence, then press <enter> in the console
"""

input(msg)  # use input to pause the program for the user
answer = []
# mainloop

while True:  # mainloop
    for event in pygame.event.get():
        if pygame.KEYDOWN == event.type:
            if event.key == pygame.K_UP:
                screen.fill("gold")
                answer.append("gold")
            elif event.key == pygame.K_RIGHT:
                screen.fill("blue")
                answer.append("blue")
            elif event.key == pygame.K_LEFT:
                screen.fill("green")
                answer.append("green")
            elif event.key == pygame.K_DOWN:
                screen.fill("purple")
                answer.append("purple")
            pygame.display.flip()
            pygame.time.wait(1000)

print("You Entered:", answer)
print("The correct pattern was", colors)

if answer == colors:
    print("Correct! You win.")
else:
    print("Were you even paying attention?")

pygame.quit()
