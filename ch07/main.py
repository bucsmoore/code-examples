# # top level class: object
# class Animal:  # blueprint for data
#     # #dunder
#     aid = 0
#     def __init__(self, name, type="dog"):
#         # instance variable
#         self.name = name
#         self.type = type
#         self.id = id(self)
#         self.arrived_date = time.strftime("%d/%m/%Y")  # string formatted time
#     def calcid(self):
#         Animal.aid += 1
#         key = self.type[0].upper()
#         return f"{key}-{Animal.aid}"
# my_animal = Animal("zelda")
# my_animal2 = Animal(
#     "sansa",
#     "cat",
# )
# print(
#     my_animal.name,
#     my_animal.type,
#     my_animal.id,
#     my_animal.arrived_date,
# )
# print(
#     my_animal2.name,
#     my_animal2.type,
#     my_animal2.id,
#     my_animal2.arrived_date,
# )
# import json
# import random
# import string


# def generate_random_string(length):
#     letters = string.ascii_letters
#     return "".join(random.choice(letters) for _ in range(length))


# name = "A"
# people = {}
# for _ in range(1000):
#     length = random.randint(5, 20)
#     key = generate_random_string(length)
#     people[key] = random.randint(1, 10)

# print(people)
# fptr = open("people.json", "w")
# json.dump(people, fptr)


# MVC
# Model- Data
# View - Display - pygame
# Controller - Logic

import pygame

BUTTON_SIZE = 25
NUM_BUTTONS = 10


# model
class LED:
    def __init__(self):
        self.on = False
        self.color = (10, 10, 10)
        self.rect = pygame.Rect(0, 0, BUTTON_SIZE, BUTTON_SIZE)


# Driver - Controller
def main():
    # initialize display and models
    pygame.init()
    display = pygame.display.set_mode()
    machine_rect = pygame.Rect(
        0, 0, BUTTON_SIZE * NUM_BUTTONS * 2 + BUTTON_SIZE, BUTTON_SIZE * 3
    )
    machine_rect.center = (display.get_width() / 2, display.get_height() / 2)
    running = True
    leds = []
    for i in range(NUM_BUTTONS):
        led = LED()
        led.rect.x = machine_rect.x + BUTTON_SIZE + (BUTTON_SIZE * 2 * len(leds))
        led.rect.y = machine_rect.y + BUTTON_SIZE
        leds.append(led)

    # mainloop
    while running:
        # eventloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for led in leds:
                    if led.rect.collidepoint(event.pos):
                        if led.on:
                            led.on = False
                            led.color = (190, 0, 0)
                        else:
                            led.on = True
                            led.color = (0, 255, 0)

        # Redraw
        pygame.draw.rect(display, "grey", machine_rect)
        for led in leds:
            pygame.draw.circle(display, led.color, led.rect.center, BUTTON_SIZE / 2)
        # display updates
        pygame.display.flip()


main()
