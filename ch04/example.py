import random

import pygame

pygame.init()
screen = pygame.display.set_mode()
font_size = 72
font = pygame.font.SysFont(None, font_size)
colors = ["red", "purple", "green", "blue"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(500)

user_guesses = []

while True: # true != True

    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("red")
                user_guesses.append("red")
            elif event.key == pygame.K_DOWN:
                screen.fill("purple")
                user_guesses.append("purple")
            elif event.key == pygame.K_LEFT:
                screen.fill("green")
                user_guesses.append("green")
            elif event.key == pygame.K_RIGHT:
                screen.fill("blue")
                user_guesses.append("blue")
        # if event.type == pygame.event.MOUSEBUTTONDOWNEVENT:
            #event.key # ERROR, no key for mouse event


    # Update data based on state
    print(user_guesses)
    msgs = []
    if len(user_guesses) >= 4:
        msgs.append("You guess "+ str(user_guesses)) 
        msgs.append("The actual pattern "+ str(colors))

        if user_guesses != colors:
            msgs.append("Try paying attention next time.")
        else:
            msgs.append("Your were correct. Nice Job.")

    # Update screen
    x_coor = 15
    y_coor = x_coor
    for msg in msgs:
        text = font.render(msg, True, "white")
        screen.blit(text, [x_coor, y_coor])
        y_coor += font_size * 2 

    # display       
    pygame.display.flip()




