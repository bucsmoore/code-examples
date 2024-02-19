import random

import pygame


def add_color(color1, color2, color3, **kwargs):
    pass

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()
font_size = 72
font = pygame.font.SysFont(None, font_size)
colors = []
for _ in range(10000):
    color = [random.randint(0,255) for _ in range(3)]
    colors.append(color)
add_color(*colors)


    
random.shuffle(colors)
for color in colors:  # color = colors.next()
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(500)

    # add black screen between each color to make them more distinct
    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(250)

user_guess = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and len(user_guess) < 4:
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
            # ADD: use the spacebar to give the user another chance to guess
                
    msgs = []
    if len(user_guess) >= 4:
        msgs.append(f"You Entered: {user_guess}.")
        msgs.append(f"The correct pattern was: {colors}.")
        if user_guess == colors:
            msgs.append(" -- Correct! You win. [close the window to end the program]")
        else:
            msgs.append(" -- Were you even paying attention?")
    else:
        msgs.append("Your arrow keys correspond to the following colors:")
        msgs.append("UP: red")
        msgs.append("DOWN: purple")
        msgs.append("LEFT: green")
        msgs.append("RIGHT: blue")
        msgs.append("Click on the window, enter the sequence, then press <enter> in the console")

    x_coor = 10
    y_coor = x_coor
    for msg in msgs:
        text = font.render(msg, True, "white")
        screen.blit(text, [x_coor, y_coor])
        y_coor += font_size * 2
    pygame.display.flip()



