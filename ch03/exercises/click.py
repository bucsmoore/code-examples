import random

import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = pygame.display.get_window_size()


circles = []
num_circles = 3
offset = 10
diameter = (width/num_circles)-10
radius = diameter/2
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for circle in circles:
                if circle.collidepoint(event.pos):
                    print(num_circles)
                    num_circles -= 1

    # draw
    screen.fill("white")
    
    position = offset + radius
    circles = []
    if num_circles:
        for _ in range(num_circles):
            circle_obj = pygame.draw.circle(screen, "red", (position, height/2), radius)
            circles.append(circle_obj)
            position += diameter + offset

    pygame.display.flip()



