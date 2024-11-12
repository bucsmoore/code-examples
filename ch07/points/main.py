"""
file: main.py
"""

import pygame
from src import controller


def main():
    # initialize display and models
    pygame.init()
    display = pygame.display.set_mode()
    controller.mainloop(display)


main()
