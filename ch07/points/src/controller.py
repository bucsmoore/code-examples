import random

import pygame
from src import point


def mainloop(display):
    points = []
    # mainloop
    running = True
    while running:
        # eventloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i, p in enumerate(points):
                    if p.rect.collidepoint(event.pos):
                        del points[i]
                        point_deleted = True
                if not point_deleted:
                    p = point.Point(event.pos[0], event.pos[1])
                    points.append(p)

        # draw updates
        display.fill("white")
        print(points)
        for p in points:
            pygame.draw.circle(display, p.color, p.rect.center, p.rect.h / 2)

        # show display
        pygame.display.flip()
