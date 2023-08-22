# The below code fills the screen with 3 colors of your choosing.
# After each color, it waits 1000 milliseconds before continuing.
import pygame

pygame.init()
screen = pygame.display.set_mode()
color = [0, 234, 255]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [78, 132, 97]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [78, 1, 176]
screen.fill(color)
pygame.display.flip()
