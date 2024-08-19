import pygame

pygame.init()
screen = pygame.display.set_mode()
# [red, green, blue]
color = [80, 200, 150]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [0, 255, 0]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [255, 0, 255]
screen.fill(color)
pygame.display.flip()
