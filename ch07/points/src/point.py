import random

import pygame


class Point:
    # method
    def __init__(self, x=0, y=0, color=None):
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 20, 20)
        self.color = color or (
            random.randrange(256),
            random.randrange(256),
            random.randrange(256),
        )
        # NEVER RETURN FROM __INIT__
