import random

import pygame

pygame.init()
pygame.event.pump()

screen = pygame.display.set_mode()

width, height = pygame.display.get_window_size()  # returns as tuple, (w, h)
hit_box_width = width / 2
hit_box_height = height / 2

## 0,0 is the top left corner
hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "green": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "purple": pygame.Rect(0, 0, hit_box_width, hit_box_height),
}
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright
# Define main colors
main_colors = {
    "red": (200, 0, 0),
    "green": (0, 200, 0),
    "blue": (0, 0, 200),
    "purple": (200, 0, 200),
}
# Define highlight colors
highlight_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (255, 0, 255),
}
# Create Font Object
font = pygame.font.Font(None, 24)
running = True
result = []  # a list for the user's sequence guesses
turns = 0  # keep track of the number of turns
order = []  # create a shuffle-able list of colors
msg = ["Press spacebar to play the game...(q to quit)"]

while running:  # mainloop - 1 frame
    # 1. event loop
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                order = list(hitboxes.keys())
                random.shuffle(order)
                turns = len(order)
                result = []
                for color in order:
                    # pygame.draw.rect(screen_obj, highlight_colors[color], hitboxes[color])
                    pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1000)
            elif event.key.lower() == pygame.K_q:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if order:
                turns = turns - 1
                if hitboxes["red"].collidepoint(event.pos):
                    result.append("red")
                elif hitboxes["purple"].collidepoint(event.pos):
                    result.append("purple")
                elif hitboxes["green"].collidepoint(event.pos):
                    result.append("green")
                elif hitboxes["blue"].collidepoint(event.pos):
                    result.append("blue")

    if order and len(result) == len(order):
        msg = ["You entered: " + str(result), "the correct pattern was: " + str(order)]
        if result == order:
            msg.append("Yay! You won.")
            order = []
        else:
            msg.append("Um, no.")
        msg.append("Press spacebar to play again.")
    elif turns:
        msg = ["Your turn"]

    screen.fill("black")

    for c, hb in hitboxes.items():
        pygame.draw.rect(screen, main_colors[c], hb)

    if result:
        pygame.draw.rect(screen, highlight_colors[result[-1]], hitboxes[result[-1]])

    ypos = 60
    for m in msg:
        text = font.render(m, True, "white")
        screen.blit(text, (20, ypos))
        ypos += 60

    pygame.display.flip()
