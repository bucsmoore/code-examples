"""
# main

#cases

# - snake_case:  underscores for spaces, all lowercase
# - camelCase: capital for spaces, starts lowercase lowercase
# - TitleCase: capital for spaces, starts capital

"""
# Skinability - how easy is it to change the visual interface

import random

import point
import pygame


def mainloop(display):
    points = []
    # mainloop
    while True:
        # eventloop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i, p in enumerate(points):
                    if p.rect.collidepoint(event.pos):
                        del points[i]
                        point_deleted = True
                if not point_deleted:
                    # t = turtle.Turtle()
                    # p = point.Point(*event.pos)
                    p = point.Point(event.pos[0], event.pos[1])
                    points.append(p)

        # draw updates
        display.fill("white")

        for p in points:
            pygame.draw.circle(display, p.color, p.rect.center, p.rect.h / 2)

        # show display
        pygame.display.flip()


def main():

    # initialize display and models
    pygame.init()
    display = pygame.display.set_mode()
    mainloop(display)


main()
